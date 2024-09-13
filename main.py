import difflib
import requests
import html
import hashlib

def file(fn):
    r = requests.get(fn)
    return r

from html.parser import HTMLParser
class HTMLParser(HTMLParser):
    nn = 0
    ll = []
    au = []
    mc = hashlib.sha256()
    cc = ('class', 'name', 'id')

    def handle_starttag(self, tag, attrs):
        if tag=='html':
            self.nn = 0
        elif tag == 'body':
            self.nn = 1
        else: self.nn += 1

        mc = hashlib.md5()
        mc.update(str(self.nn).encode())
        mc.update(tag.encode())

        for attr, value in attrs:
            if attr in self.cc:
                mc.update(value.encode())

        self.ll.append([self.nn, tag, mc.hexdigest()])
        if tag=='head' or tag=='body' or tag=='html':
            print('bb',tag,self.nn)
            print(attrs)
        nu = [attr[0] for attr in attrs if attr[0] not in self.au]
        self.au.extend(nu)

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
    print(len(parser.au),parser.au)
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
