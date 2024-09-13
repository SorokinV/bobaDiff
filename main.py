import difflib
import requests
import html

def file(fn):
    r = requests.get(fn)
    return r

from html.parser import HTMLParser
class HTMLParser(HTMLParser):
    nn = 0
    ll = []
    def handle_starttag(self, tag, attrs):
        if tag=='html':
            self.nn = 0
        elif tag == 'body':
            self.nn = 1
        else: self.nn += 1
        self.ll.append(str(self.nn)+' '+tag)
        if tag=='head' or tag=='body' or tag=='html':
            print('bb',tag,self.nn)
            print(attrs)

    def handle_endtag(self, tag):
        #print("Encountered an end tag :", tag)
        if tag=='head' or tag=='body' or tag=='html':
            print('ee',tag,self.nn)
        self.nn -= 1

    #def handle_data(self, data):
    #    print("Encountered some data  :", data)

def refine (rn):
    ll = []
    nn = 0
    rcontent = str(rn)
    parser = HTMLParser()
    parser.feed(rcontent)
    parser.close()
    print(parser.nn)
    print(parser.ll)
    return parser.ll

def main():
    print('привет')
    r1 = file('https://github.com/NelliSm/Sprint_5/pulls')
    print(f'\n{len(r1.text)}')
    nlist = refine(r1.content.replace(b'\n',b''))
    print(len(nlist))
    #r1content = r1.content.replace(b'\n',b'')
    #print(r1content)
    #print('Досвидос')
    return()

main()
