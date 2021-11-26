class Images(object):
    def __init__(self, url='', date='', desc=''):
        self.url = url
        self.date = date
        self.desc = desc

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


    def tostring(self):
        smallurl = self.url + '&pid=hp&w=384&h=216&rs=1&c=4'
        return '![]({}){} [download]({})'.format(smallurl, self.date, self.url)

    def formatmarkdown(self):
        return '{} | [{}]({})'.format(self.date, self.desc, self.url)

    def tolarge(self):
        smallurl = self.url + '&w=1000'
        return '![]({})Today: [{}]({})'.format(smallurl, self.desc, self.url)
