
def e_content(content=None):
    content = "<html>\n" + content + "\n</html>"
    return content
def e_append(new_content, content):
    new_content = content.replace("<html>", "")
    new_content = new_content.replace("</html>", "")
    new_content = "<html>" + new_content + "</html>"
    return new_content
        
content = e_content("this is a string")
new_content = e_append("and another string", content)
print(new_content)
