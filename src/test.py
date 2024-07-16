import unittest

from markdown_to_html import markdown_to_html_node

from block_parser import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list,
    block_type_paragraph,
)

from inline_parser import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
    text_node_to_html_node,
)

class TestHTMLGenerator(unittest.TestCase):

    def test(self):
        # print("TASNTOHESNATOHEASN")
        text = """

### See **you** *space* taco!

```
codelyodely
odely
```

>This
>*Are*
>**Quota!!!!**

* things
* ![taco](httpx://ttt.taco.meat/barkdust.png)
* *list*

- **other**
- *list*
- [tako](httpx://ttt.tako.meat/headfoot.png)
- **things**

1. One
2. Two
3. Three
4. Five

    This to a *paragpaph* of **stuff** and things
on multiple lines.

"""
        html = """<div><h3>See <b>you</b> <i>space</i> taco!</h3><code>
codelyodely
odely
</code><blockquote>This
<i>Are</i>
<b>Quota!!!!</b>
</blockquote><ul><li>things</li><li><img src="httpx://ttt.taco.meat/barkdust.png" alt="taco"></img></li><li><i>list</i></li></ul><ul><li><b>other</b></li><li><i>list</i></li><li><a href="httpx://ttt.tako.meat/headfoot.png">tako</a></li><li><b>things</b></li></ul><ol><li>One</li><li>Two</li><li>Three</li><li>Five</li></ol><p>This to a <i>paragpaph</i> of <b>stuff</b> and things
on multiple lines.</p></div>"""
        html_node = markdown_to_html_node(text)
        self.assertEqual(html_node.to_html(), html)


# def main():
#     markdown = """
#
# ### See **you** *space* taco!
#
# ```
# codelyodely
# odely
# ```
#
# >This
# >*Are*
# >**Quota!!!!**
#
# * things
# * ![taco](httpx://ttt.taco.meat/barkdust.png)
# * *list*
#
# - **other**
# - *list*
# - [tako](httpx://ttt.tako.meat/headfoot.png)
# - **things**
#
# 1. One
# 2. Two
# 3. Three
# 4. Five
#
#     This to a *paragpaph* of **stuff** and things
# on multiple lines.
#
# """
#     node = markdown_to_html_node(markdown)
#     print(f"Node: {node}")
#     print(f"{node.to_html()}")
#
# main()
