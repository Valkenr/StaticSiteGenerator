from copy_static import copy_dir
from generate_page import generate_page_recursive

def main():
    copy_dir("static", "public")
    # generate_page("content/index.md", "template.html", "public")
    generate_page_recursive("content", "template.html", "public")

main()

