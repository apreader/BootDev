from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue

        parts = node.text.split(delimiter)

        if len(parts) % 2 == 0:
            raise ValueError("unmatched delimiter")
        
        for i in range(len(parts)):
            part = parts[i]
            if part == "":
                continue
            if i % 2 == 0:
                new_list.append(TextNode(part, TextType.TEXT))
            
            else:
                new_list.append(TextNode(part, text_type))
    return new_list

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):

def split_nodes_link(old_nodes):
