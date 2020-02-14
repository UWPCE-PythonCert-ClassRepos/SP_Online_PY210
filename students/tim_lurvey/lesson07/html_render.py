#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    def __init__(self, content: str = "") -> None:
        self.indent = False
        self.tags = ["<html>", "</html>"]
        self.delimiter = "\n"
        self._content = []
        self.append(content)

    def append(self, additional_content: str) -> None:
        if additional_content:
            self._content.append(additional_content)

    def render(self, out_file, ind: str = "") -> None:
        """recursively build all the elements and format as strings for file printing"""
        out_file.write(self.print_strings(getattr(self, 'initial_strings', []) + \
                                          self.get_strings(indent=ind)))

    def add_keyval_to_tag(self, n:int, key:str, value:str= ""):
        """add the string 'key="value"' to the nth tag"""
        i = self.tags[n].index(">")
        val = ""
        if value:
            val += f'="{value}"'
        self.tags[n] = self.tags[n][:i] + f'{key}{val}' + self.tags[n][i:]

    def set_leading_tag_key(self, key:str, val: str = ""):
        """If key is requested, apply the keyed string and add to TAGS list"""
        if val:
            self.add_keyval_to_tag(n=0, key=f' {key}', value=val)

    def wrap_tags(self, strings_list: list) -> list:
        """add object tags in the appropriate positions"""
        if self.tags[0]:
            strings_list.insert(0, self.tags[0])
        if self.tags[-1]:
            strings_list.append(self.tags[-1])
        return strings_list

    def get_strings(self, indent: str = "") -> list:
        """Convert contents into a string, recursively"""
        lines = []   # create container for string chunks
        # get indent
        ind = ""
        if indent:
            ind = indent
        for item in self._content:
            # add if string
            if isinstance(item, str):
                lines.append(ind + item)
            # convert to string if supported by object
            elif hasattr(item, "get_strings"):
                lines.extend(item.get_strings(indent=indent))
            # error if not string capable
            else:
                raise TypeError("Bad type, {}, Cannot get string.".format(type(item)))
        # wrap with object tags
        self.wrap_tags(strings_list=lines)
        # join with delimiters and tabs for pretty printing
        return [ind+l for l in lines]

    def print_strings(self, lines: list, delimiter: str = "\n" ):
        """join all the lines with the delimiter"""
        return delimiter.join(lines)


class Html(Element):
    """HTML element, responsible for doc's initial line and formatting tags"""
    def __init__(self, content: str = ""):
        # set instance variables
        self.initial_strings = ["<!DOCTYPE html>"]
        # call parent initializer
        super().__init__(content=content)
        # update instance variables
        self.tags = ["<html>", "</html>"]


class Body(Element):
    """Body element. Only accepts content"""
    def __init__(self, content: str = ""):
        # call parent initializer
        super().__init__(content=content)
        # update instance variables
        self.indent = True
        self.tags = ["<body>", "</body>"]


class P(Element):
    """Paragraph element. Accepts content and style"""
    def __init__(self, content: str = "", style: str = ""):
        # call parent initializer
        super().__init__(content=content)
        # update instance variables
        self.indent = True
        self.tags = ["<p>", "</p>"]
        self.set_leading_tag_key("style", style)



class Head(Element):
    """Head element. Only accepts content"""
    def __init__(self, content: str = ""):
        # call parent initializer
        super().__init__(content=content)
        # update instance variables
        self.indent = True
        self.tags = ["<head>", "</head>"]


class Title(Head):
    """Title element. Only accepts content"""
    def __init__(self, content: str = ""):
        # call parent initializer
        super().__init__(content=content)
        # update instance variables
        self.indent = True
        self.tags = ["<title>", "</title>"]


class Hr(Element):
    """Hr element. Only accepts content"""
    def __init__(self, content: str = ""):
        # call parent initializer
        super().__init__(content=content)
        # update instance variables
        self.indent = True
        self.tags = ["", "<hr />"]


class H(Element):
    """Heading element. Accepts content, heading number"""
    def __init__(self, num: int = 1, content: str = ""):
        # call parent initializer
        super().__init__(content=content)
        # update instance variables
        self.indent = True
        self.tags = ["<h>", "</h>"]
        self.set_tags_num(num=num)

    def set_tags_num(self, num):
        for i in range(len(self.tags)):
            self.add_keyval_to_tag(i, key=num)


class A(Title):
    """Hyperlink element. Accepts content, url"""
    def __init__(self, url:str = "", content: str = ""):
        # call parent initializer
        super().__init__(content=content)
        # update instance variables
        self.indent = True
        self.tags = ["<a>", "</a>"]
        self.delimiter = ""
        self.set_leading_tag_key("href",val=url)


class Ul(Element):
    """List header element. Accepts content, id, style"""
    def __init__(self, content: str = "", id: str = "", style: str = ""):
        # call parent initializer
        super().__init__(content=content)
        # update instance variables
        self.indent = True
        self.tags = ["<ul>", "</ul>"]
        self.set_leading_tag_key("style",val=style)
        self.set_leading_tag_key("id",val=id)


class Li(Ul):
    """List item element. Accepts content, style"""
    def __init__(self, content: str = "", style: str = ""):
        # call parent initializer
        super().__init__(content=content, style=style)
        # update instance variables
        self.tags = ["<li>", "</li>"]
        self.set_leading_tag_key("style",val=style)


class Meta(Element):
    """Meta element. Accepts content, charset"""
    def __init__(self, content: str = "", charset: str = ""):
        # call parent initializer
        super().__init__(content=content)
        # update instance variables
        self.indent = True
        self.tags = ['<meta charset="{}" />'.format(charset),'']
