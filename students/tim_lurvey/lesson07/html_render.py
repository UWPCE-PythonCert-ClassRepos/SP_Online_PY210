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

    def render(self, out_file, indent: bool = False) -> None:
        out_file.write(self.print_strings(self.get_strings(indent=indent)))

    def add_keyval_to_tag(self, n:int, key:str, value:str= ""):
        """add the string 'key="value"' to the nth tag"""
        i = self.tags[n].index(">")
        val = ""
        if value:
            val += f'="{value}"'
        self.tags[n] = self.tags[n][:i] + f'{key}{val}' + self.tags[n][i:]

    def set_tags(self,strings_list: list) -> list:
        """add object tags in the appropriate positions"""
        if self.tags[0]:
            strings_list.insert(0, self.tags[0])
        if self.tags[-1]:
            strings_list.append(self.tags[-1])
        return strings_list

    def get_strings(self, indent: bool = False) -> list:
        """Convert contents into a string, recursively"""
        lines = []   # create container for string chunks
        # get indent
        ind = ""
        if indent:
            ind = "\t"
        for item in self._content:
            # add if string
            if isinstance(item, str):
                lines.append(ind + item)
            # convert to string if supported by object
            elif hasattr(item, "get_strings"):
                lines.extend(item.get_strings(indent=item.indent))
            # error if not string capable
            else:
                raise TypeError("Bad type, {}, Cannot get string.".format(type(item)))
        # wrap with object tags
        self.set_tags(strings_list=lines)
        # join with delimiters and tabs for pretty printing
        return [ind+l for l in lines]

    def print_strings(self, lines: list, delimiter: str = "\n" ):
        return delimiter.join(lines)


class Html(Element):

    def __init__(self, content: str = ""):
        super().__init__(content=content)
        self.tags = ["<html>", "</html>"]


class Body(Html):

    def __init__(self, content: str = ""):
        super().__init__(content=content)
        self.indent = True
        self.tags = ["<body>", "</body>"]


class P(Html):

    def __init__(self, content: str = "", style: str = ""):
        super().__init__(content=content)
        self.indent = True
        self.tags = ["<p>", "</p>"]
        self.set_tags_style(style)

    def set_tags_style(self, style: str = ""):
        """If style is requested, apply the style string and add to TAGS list

        Note: This logic could live in the constructor (initializer).  Through
        experience, we don't allow it in my team.  We had some 'issues' with some
        persons putting everything under the __init__ and made a group policy
        against any logic defined in the initialization method."""
        if style:
            self.add_keyval_to_tag(n=0, key=' style', value=style)


class Head(Html):

    def __init__(self, content: str = ""):
        super().__init__(content=content)
        self.indent = True
        self.tags = ["<head>", "</head>"]


class Title(Head):

    def __init__(self, content: str = ""):
        super().__init__(content=content)
        self.indent = True
        self.tags = ["<title>", "</title>"]


class Hr(Html):

    def __init__(self, content: str = ""):
        super().__init__(content=content)
        self.indent = True
        self.tags = ["", "<hr />"]


class H(Html):

    def __init__(self, num: int = 1, content: str = ""):
        super().__init__(content=content)
        self.indent = True
        self.tags = ["<h>", "</h>"]
        self.set_tags_num(num=num)

    def set_tags_num(self, num):
        for i in range(len(self.tags)):
            self.add_keyval_to_tag(i, num)


class A(Title):

    def __init__(self, url:str = "", content: str = ""):
        super().__init__(content=content)
        self.indent = True
        self.tags = ["<a>", "</a>"]
        self.delimiter = ""
        self.add_keyval_to_tag(n=0, key=' href', value=url)


class Ul(Html):
    """List header"""
    def __init__(self, content: str = "", id: str = "", style: str = ""):
        super().__init__(content=content)
        self.indent = True
        self.tags = ["<ul>", "</ul>"]
        if id:
            self.add_keyval_to_tag(n=0, key=' id', value=id)
        if style:
            self.add_keyval_to_tag(n=0, key=' style', value=style)


class Li(Ul):
    """List item"""
    def __init__(self, content: str = "", style: str = ""):
        super().__init__(content=content)
        self.tags = ["<li>", "</li>"]


class Meta(Html):
    """Meta element creator"""
    def __init__(self, content: str = "", charset: str = ""):
        super().__init__(content=content)
        self.indent = True
        self.tags = ['<meta charset="{}" />'.format(charset),'']
