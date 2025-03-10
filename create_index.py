import os

def generate_index_for_subdir(folder_path, html_title):
    """
    Scans `folder_path` for all .pdf files,
    creates an index.html in that folder using filenames as the link text.
    """

    # List all PDFs in the folder
    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    pdf_files.sort()

    # Build <li> links
    links_html = []
    for pdf_file in pdf_files:
        # Just use the filename (without extension) as the visible text
        link_text = os.path.splitext(pdf_file)[0]
        link_html = f'<li><a href="{pdf_file}" target="_blank">{link_text}</a></li>'
        links_html.append(link_html)

    # Construct the overall HTML
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{html_title}</title>
</head>
<body>
    <h1>{html_title}</h1>
    <ul>
        {'\n'.join(links_html)}
    </ul>
    <!-- Optional link back to parent directory -->
    <p><a href="../">Back to main index</a></p>
</body>
</html>
"""

    # Write index.html inside the folder
    output_path = os.path.join(folder_path, "index.html")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Created {output_path}")

if __name__ == "__main__":
    # Adjust as needed
    #generate_index_for_subdir("papers", "List of Papers")
    generate_index_for_subdir("presentations", "List of Presentations")
