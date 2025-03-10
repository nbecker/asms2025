import os
import PyPDF2

# Folder containing your PDFs
PDF_FOLDER = "papers"
OUTPUT_HTML = "index.html"

def get_pdf_title(filepath):
    """Return the PDF title from metadata if available; otherwise use filename."""
    try:
        with open(filepath, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            info = reader.metadata
            pdf_title = info.get('/Title')  # Title from PDF metadata
            if pdf_title:
                return pdf_title.strip()
    except Exception:
        pass
    # Fall back to filename without extension
    return os.path.splitext(os.path.basename(filepath))[0]

def generate_index(pdf_folder, output_html):
    # Get list of PDF files in the folder
    pdf_files = [f for f in os.listdir(pdf_folder) if f.lower().endswith('.pdf')]
    pdf_files.sort()

    links_html = []
    for pdf_file in pdf_files:
        # Title can be from metadata or fallback
        title = get_pdf_title(os.path.join(pdf_folder, pdf_file))
        # Link to the PDF file
        link_html = f'<li><a href="{pdf_file}" target="_blank">{title}</a></li>'
        links_html.append(link_html)

    # Build the main HTML page
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Conference Papers Index</title>
</head>
<body>
    <h1>Conference Papers</h1>
    <ul>
        {'\n'.join(links_html)}
    </ul>
</body>
</html>
"""

    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html_content)

if __name__ == "__main__":
    generate_index(PDF_FOLDER, OUTPUT_HTML)
    print(f"Created {OUTPUT_HTML} with links to all PDFs in {PDF_FOLDER}")
