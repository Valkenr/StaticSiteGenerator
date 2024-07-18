import os
import shutil

from extract_markdown import (
    extract_title,
    file_to_text,
)

from markdown_to_html import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} with {template_path}")
    markdown = file_to_text(from_path)
    title = extract_title(markdown)
    # print(f"Title: {title}\nText: {markdown}")
    html_nodes = markdown_to_html_node(markdown)
    html = html_nodes.to_html()
    # print(f"HTML: {html}")
    template_text = file_to_text(template_path)
    template = template_text.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    # temp_1 = template_text.split("{{ Title }}")
    # temp_2 = temp_1[1].split("{{ Content }}")
    # template = temp_1[0] + title + temp_2[0] + html + temp_2[1]
    # print(f"Template: {template}")
    print(f"Attempting to create {dest_path.replace(".md", ".html")}")
    temp_file = open(dest_path.replace(".md", ".html"), 'w')
    print("Attempting to write file")
    temp_file.write(template)
    temp_file.close()

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    print(f"|{dir_path_content}|{template_path}|{dest_dir_path}|")
    dir_list = os.listdir(dir_path_content)
    print(f"Contents: {dir_list}")
    for obj in dir_list:
        if os.path.isfile(os.path.join(dir_path_content, obj)):
            print(f"Copying {obj}")
            if not os.path.exists(dest_dir_path):
                print(f"Making {dest_dir_path}")
                os.mkdir(dest_dir_path)
            generate_page(os.path.join(dir_path_content, obj), template_path, os.path.join(dest_dir_path, obj))
        else:
            print(f"At {obj}")
            print(f"Joining {os.path.join(dir_path_content, obj)}")
            if not os.path.exists(dest_dir_path):
                os.mkdir(dest_dir_path)
            generate_page_recursive(os.path.join(dir_path_content, obj), template_path, os.path.join(dest_dir_path, obj))

            # if os.path.isfile(os.path.join(source, node)):
            #     # print(f"Copying {node}")
            #     if not os.path.exists(target):
            #         # print(f"Making {target}")
            #         os.mkdir(target)
            #     shutil.copy(os.path.join(source, node), os.path.join(target, node))
            # else:
            #     # print(f"At {node}")
            #     # print(f"Joining {os.path.join(source, node)}")
            #     if not os.path.exists(target):
            #         # print(f"Making {target}")
            #         os.mkdir(target)
