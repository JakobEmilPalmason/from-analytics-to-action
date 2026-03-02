"""Convert lecture PDF slides to Markdown with images extracted and placed inline."""

import hashlib
import sys
from pathlib import Path

import pymupdf  # PyMuPDF

MIN_IMAGE_DIM = 50  # skip images where both dimensions are below this


def _save_image(doc, xref: int, dest_path: Path) -> None:
    """Extract and save an image from the PDF, handling alpha masks."""
    img_info = doc.extract_image(xref)
    image_bytes = img_info["image"]
    ext = img_info["ext"]

    # If it's a JPEG with no mask, save the original bytes directly
    smask = img_info.get("smask", 0)
    if smask == 0 and ext in ("jpeg", "jpg"):
        dest_path = dest_path.with_suffix(".jpg")
        dest_path.write_bytes(image_bytes)
        return dest_path

    # Otherwise use Pixmap for PNG output (handles colorspace conversion + alpha)
    pix = pymupdf.Pixmap(image_bytes)

    # Convert CMYK to RGB
    if pix.n - pix.alpha > 3:
        pix = pymupdf.Pixmap(pymupdf.csRGB, pix)

    if smask > 0:
        mask_info = doc.extract_image(smask)
        mask_pix = pymupdf.Pixmap(mask_info["image"])
        # Create RGBA pixmap
        if pix.alpha == 0:
            pix = pymupdf.Pixmap(pix, 1)  # add alpha channel
        pix.set_alpha(mask_pix.samples)

    dest_path = dest_path.with_suffix(".png")
    pix.save(str(dest_path))
    return dest_path


def lecture_pdf_to_markdown(pdf_path: Path, images_dir: Path) -> str:
    """Convert a lecture PDF to markdown with images placed inline."""
    doc = pymupdf.open(pdf_path)
    images_dir.mkdir(parents=True, exist_ok=True)

    seen_hashes = {}  # md5 -> relative image path
    sections = []

    for page_num, page in enumerate(doc, 1):
        blocks = page.get_text("dict")["blocks"]
        # Sort by vertical position (top to bottom), then horizontal (left to right)
        blocks.sort(key=lambda b: (b["bbox"][1], b["bbox"][0]))

        page_parts = []
        img_counter = 0

        for block in blocks:
            if block["type"] == 0:  # text block
                lines = []
                for line in block["lines"]:
                    line_text = "".join(span["text"] for span in line["spans"])
                    lines.append(line_text)
                text = "\n".join(lines).strip()
                if text:
                    page_parts.append(text)

            elif block["type"] == 1:  # image block
                w = block.get("width", 0)
                h = block.get("height", 0)
                if w < MIN_IMAGE_DIM and h < MIN_IMAGE_DIM:
                    continue

                # Get the xref for this image from the page
                image_bytes = block.get("image")
                if not image_bytes:
                    continue

                img_hash = hashlib.md5(image_bytes).hexdigest()[:12]

                if img_hash in seen_hashes:
                    rel_path = seen_hashes[img_hash]
                else:
                    # Find xref by matching image bytes through page images
                    xref = _find_image_xref(doc, page, image_bytes)
                    if xref is None:
                        continue

                    img_counter += 1
                    base_name = f"slide{page_num:02d}_img{img_counter:02d}"
                    dest_path = images_dir / base_name
                    try:
                        saved_path = _save_image(doc, xref, dest_path)
                        rel_path = f"images/{saved_path.name}"
                        seen_hashes[img_hash] = rel_path
                    except Exception as e:
                        print(f"    WARNING: Could not save image on slide {page_num}: {e}")
                        continue

                page_parts.append(f"![]({rel_path})")

        header = f"<!-- Slide {page_num} -->"
        if page_parts:
            sections.append(header + "\n\n" + "\n\n".join(page_parts))
        else:
            sections.append(header)

    doc.close()
    return "\n\n---\n\n".join(sections)


def _find_image_xref(doc, page, image_bytes: bytes) -> int | None:
    """Find the xref of an image on a page by matching content."""
    img_hash = hashlib.md5(image_bytes).hexdigest()
    for img in page.get_images(full=True):
        xref = img[0]
        try:
            extracted = doc.extract_image(xref)
            if hashlib.md5(extracted["image"]).hexdigest() == img_hash:
                return xref
        except Exception:
            continue
    return None


def convert_all_lectures(base_dir: Path, overwrite: bool = False):
    """Find all lecture PDFs and convert each to markdown with images."""
    pdf_files = sorted(
        p for p in base_dir.rglob("*.pdf")
        if "lectures" in p.parts
    )

    if not pdf_files:
        print("No lecture PDF files found.")
        return

    print(f"Found {len(pdf_files)} lecture PDF files.\n")

    for pdf_path in pdf_files:
        md_path = pdf_path.with_suffix(".md")
        images_dir = pdf_path.parent / "images"

        if md_path.exists() and not overwrite:
            print(f"  SKIP (exists): {md_path.relative_to(base_dir)}")
            continue

        print(f"  Converting: {pdf_path.relative_to(base_dir)}")
        try:
            markdown_text = lecture_pdf_to_markdown(pdf_path, images_dir)
            md_path.write_text(markdown_text, encoding="utf-8")
            print(f"       -> {md_path.relative_to(base_dir)}")
        except Exception as e:
            print(f"  ERROR: {e}")

    print("\nDone.")


if __name__ == "__main__":
    repo_root = Path(__file__).resolve().parent.parent
    overwrite = "--overwrite" in sys.argv
    convert_all_lectures(repo_root, overwrite=overwrite)
