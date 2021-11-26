class Images(object):
    def __init__(self, url='', date='', desc=''):
        self.data = {'url': url, 'date': date, 'desc': desc}

    def url(self) -> str:
        return self.data.get('url')

    def date(self) -> str:
        return self.data.get('date')

    def desc(self) -> str:
        return self.data.get('desc')

    def tostring(self):
        smallurl = self.url() + '&pid=hp&w=384&h=216&rs=1&c=4'
        return '![]({}){} [download]({})'.format(smallurl, self.date(), self.url())

    def formatmarkdown(self):
        return '{} | [{}]({})'.format(self.date(), self.desc(), self.url())

    def tolarge(self):
        smallurl = self.url() + '&w=1000'
        return '![]({})Today: [{}]({})'.format(smallurl, self.desc(), self.url())
