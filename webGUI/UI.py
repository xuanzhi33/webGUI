class UI:
    def __init__(self, tagName="div", innerHtml="", attrs={}):
        self.tagName = tagName
        self.innerHtml = innerHtml
        self.attrs = attrs
        self.children = []
    def renderToHTML(self):
        attrsHTML = ""
        for attr in self.attrs:
            attrsHTML += ' ' + attr + '="' + self.attrs[attr] + '"'
        return '<' + self.tagName + attrsHTML + '>' + self.innerHtml + '</' + self.tagName + '>'
    def addChild(self, child):
        self.children.append(child)
    def getText(self):
        return self.innerHtml
    def getAttr(self, attr):
        return self.attrs[attr]

class Para(UI):
    def __init__(self, text):
        super().__init__("p", text)

class Button(UI):
    def __init__(self, text, onclick):
        super().__init__("button", text, {"onclick": onclick})

