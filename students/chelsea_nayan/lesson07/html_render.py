# Lesson07: HTML Renderer
"""
HTML Renderer: rendering HTML via classes
"""

class Element(object): # The intializer signature
    tag = 'html'
    indent = '  '

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        self.attributes = kwargs

    # Add another string to the content
    def append(self, new_content):
        return self.contents.append(new_content)

    def _open_tag(self):
        open_tag = [f'<{self.tag}']
        for key, value in self.attributes.items():
            open_tag.append(f' {key}="{value}"')
        open_tag.append('>')
        open_tag = ''.join(open_tag)
        return open_tag

    def _close_tag(self):
        close_tag = f'</{self.tag}>'
        return close_tag

    # Render the tag and the strings in the content
    # Takes a file-like object, call its write() method, write the html for a tag
    def render(self, out_file, curr_ind=''):
        out_file.write(curr_ind + self._open_tag() + '\n')

        for content in self.contents:
            try:
                content.render(out_file, curr_ind + self.indent)
            except AttributeError:
                out_file.write(curr_ind + self.indent + content +'\n')

        out_file.write(curr_ind + self._close_tag() + '\n')

class Body(Element):
    tag = 'body'

class Html(Element):
    tag = 'html'

    # overrides previous render()
    def render(self, out_file, curr_ind=''):
        out_file.write(curr_ind + '<DOCTYPE html>\n')
        super().render(out_file, curr_ind)

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class Ul(Element):
    tag = 'ul'

class Li(Element):
    tag = 'li'

# Render tag on one line, overrrides the render method
class OneLineTag(Element):
    def render(self, out_file, curr_ind = ''):
        out_file.write(curr_ind + self._open_tag())
        out_file.write(self.contents[0])
        out_file.write(self._close_tag())
        out_file.write('\n')

    # Ensure no content will be appended
    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = 'title'

class A(OneLineTag):
    tag = 'a'
    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content,**kwargs)

class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        self.tag = (f'h{level}')
        super().__init__(content,**kwargs)

class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError('SelfClosingTag cannot contain content')
        super().__init__(content=content, **kwargs)

    def render(self, out_file, curr_ind=''):
        out_file.write(curr_ind + f'{self._open_tag()}\n')

    # Ensure no content will be appended
    def append(self, *args, **kwargs):
        raise TypeError('Cannot append to SelfClosingTag')

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class Meta(SelfClosingTag):
    tag = 'meta'
