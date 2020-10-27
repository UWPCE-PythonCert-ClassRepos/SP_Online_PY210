#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

# This is the framework for the base class

#===========
# Step 1
#===========
class Element(object):

    tag = "html"
    attributes = {}
#===========
# Step 9 - indentation
#===========    
    indent = "  "
    # indent = ""

    def __init__(self, content=None, **kwargs): # Step 4: adding kwargs for attributes
        # pass
        if content:
            self.contents = [content]
        else:
            self.contents = []
        # print("contents is:", self.contents)
        if kwargs:
            self.attributes = kwargs

    def append(self, new_content):
        # pass
        # self.contents.append(self.indent)
        self.contents.append(new_content)

# Step 9 - adding indentation
    def render(self, out_file, cur_ind=""):
        # out_file.write("just something as a place holder...")
        # ind = self.indent + cur_ind
        ind = cur_ind
#===========
# Step 4 - updated for attributes rendering
#===========
        # nind = self.indent + cur_ind
        # open_tag = [cur_ind + "<{}".format(self.tag)] # Step 9 - adding indent
        open_tag = [ind + "<{}".format(self.tag)] # Step 9 - adding indent
        attrstr = ''
        for key, value in self.attributes.items():
            attrstr += " " + key + "=" + '"'+ value + '"'
        # print(attrstr)
        open_tag.append(attrstr)
        # open_tag.append(">\n" + nind)
        open_tag.append(">\n")
        out_file.write("".join(open_tag))
        # Step4: refactoring for Step4: adding attributes
        # out_file.write("<{} {}>\n".format(self.tag, " ".join(self.attributes)) ) 
        
        
        for content in self.contents:
            try:
                out_file.write(ind+self.indent) # default indentation for content
                content.render(out_file)
            except AttributeError:                
                out_file.write(content)
            
            # out_file.write("\n"+cur_ind)
            out_file.write("\n" )
        
        out_file.write(ind + "</{}>\n".format(self.tag))

#===========
# Step 2
#===========
class Html(Element):
    # indent = "  "
#===========
# Step 7 - update html
#===========
    def render(self, out_file, cur_ind=""):
        # cur_ind = self.indent + cur_ind
        # open_tag = [cur_ind + "<{}".format(self.tag)]
        ind = cur_ind
        out_file.write(ind + '<!DOCTYPE html>\n')
        # out_file.write('<!DOCTYPE html>\n')
        super().render(out_file, cur_ind=ind)
        
        
        # open_tag = ["<{}".format(self.tag)]
        # attrstr = ''
        # for key, value in self.attributes.items():
            # attrstr += " " + key + "=" + '"'+ value + '"'
        
        # open_tag.append(attrstr)
        # open_tag.append(">\n")
        # out_file.write("".join(open_tag))
        
        # for content in self.contents:
            # try:
                # content.render(out_file)
            # except AttributeError:
                # out_file.write(content)        
            # out_file.write("\n")
        
        # out_file.write("</{}>\n".format(self.tag))
        
        

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

#===========
# Step 3
#===========
class Head(Element):
    tag = 'head'    
    
    
# kept append method, but made sure it's on one line
class OneLineTag(Element):
    # def __init__(self, content=None, tag = ''):
        # self.tag = tag # need to overwrite at init
    # def __init__(self, content=None, **kwargs):        
        # if content:
            # self.contents = [content]
        # else:
            # self.contents = []
        # if kwargs:
            # self.attributes = kwargs
    def render(self, out_file, cur_ind=""): # get rid of '\n'
        # out_file.write("just something as a place holder...")
        # out_file.write("<{}>".format(self.tag))
        ind = cur_ind
#===========
# Step 4 - updated for attributes rendering
#===========
        open_tag = [ind + "<{}".format(self.tag)]
        attrstr = ''
        for key, value in self.attributes.items():
            attrstr += " " + key + "=" + '"'+ value + '"'
        # print(attrstr)
        open_tag.append(attrstr)
        # open_tag.append(">\n")
        open_tag.append(">")
        out_file.write("".join(open_tag))
        
        
        for content in self.contents:
            try:
                # out_file.write(ind+self.indent) # default indentation for content
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            
            # out_file.write("\n")
        
        out_file.write("</{}>\n".format(self.tag))
        
class Title(OneLineTag):
    tag = 'title'  
            

#===========
# Step 5
#===========

class SelfClosingTag(Element):
    # def __init__(self, content=None, tag = 'hr', **kwargs):
        # self.tag = tag # need to overwrite at init
        # self.contents = []
    def __init__(self, content=None, **kwargs):        
        if kwargs:
            self.attributes = kwargs
            
    def render(self, out_file, cur_ind=""):
        # out_file.write("just something as a place holder...")
        ind = cur_ind    
        #===========
        # Step 4 - updated for attributes rendering
        #===========
        open_tag = [ind + "<{}".format(self.tag)]
        attrstr = ''
        for key, value in self.attributes.items():
            attrstr += " " + key + "=" + '"'+ str(value) + '"'
        # print(attrstr)
        open_tag.append(attrstr)
        open_tag.append(" ")  #  content is just a whitespace
        out_file.write("".join(open_tag))
        out_file.write("/>\n") # closing slash
    
    def append(self, *args): # do nothing
        raise TypeError("You can not add content to a SelfClosingTag")  

# Only need signatured for the specific tags        
class Hr(SelfClosingTag):
    tag = 'hr'
    
class Br(SelfClosingTag):
    tag = 'br'

#===========
# Step 6
#===========    

class A(OneLineTag):
    tag = 'a'
    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

#===========
# Step 7
#===========    
class H(OneLineTag): 
    # tag = 'h'
    def __init__(self, level, content=None, **kwargs):
        if level in range(1,7):
            self.tag = 'h'+str(level)
        else:
            self.tag = 'h1'
        super().__init__(content, **kwargs)
        
        
#===========
# Step 8
#===========           
class Meta(SelfClosingTag):          
    tag='meta'
    
class Ul(Element):
    tag = 'ul'        
                
class Li(OneLineTag): 
    tag = 'li'
                


#===========
# Step 8
#===========                           
                