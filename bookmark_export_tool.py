import sys
import os
from bs4 import BeautifulSoup

def parse_html_bookmarks(html_file):
    with open(html_file, "r") as file:
        # Parse HTML file
        soup = BeautifulSoup(file, "html.parser")
        
        # Find all bookmark links
        bookmark_links = soup.find_all("a")
        
        # Extract URLs and titles
        bookmarks = [(link.get("href"), link.text) for link in bookmark_links]
        
        return bookmarks

def export_bookmarks(html_file, output_file):
    # Parse HTML bookmarks
    bookmarks = parse_html_bookmarks(html_file)
    
    # Write bookmarks to a text file
    with open(output_file + ".txt", "w") as text_file:
        for url, title in bookmarks:
            text_file.write(f"{title}: {url}\n")
    
    print("Text file exported successfully to", output_file + ".txt")

    # Write bookmarks to a Markdown file
    with open(output_file + ".md", "w") as md_file:
        md_file.write("# Bookmarks\n\n")
        for url, title in bookmarks:
            md_file.write(f"- [{title}]({url})\n")

    print("Markdown file exported successfully to", output_file + ".md")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python export_edge_bookmarks.py <input_html_file> <output_file>")
        sys.exit(1)

    html_file = sys.argv[1]
    output_file = sys.argv[2]

    export_bookmarks(html_file, output_file)

# Below it the bash command to excute the program
# python3 bookmark_export_tool.py input_html_file output_file

