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
    aappend = False

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

        if tag == 'body':
            self.aappend = True

        if self.aappend:
            self.ll.append([self.nn, tag, mc.hexdigest()])

        '''
        if tag=='head' or tag=='body' or tag=='html':
            print('bb',tag,self.nn)
            print(attrs)
        '''
        '''    
        nu = [attr[0] for attr in attrs if attr[0] not in self.au]
        self.au.extend(nu)
        '''

    def handle_endtag(self, tag):
        """
        if tag=='head' or tag=='body' or tag=='html':
            print('ee',tag,self.nn)
        """
        self.nn -= 1

    #def handle_data(self, data):
    #    print("Encountered some data  :", data)

def refine (rn):
    rcontent = str(rn)

    parser = HTMLParser()
    parser.feed(rcontent)
    parser.close()

    #print(parser.nn)
    #print(parser.ll)
    #print(len(parser.au),parser.au)
    return parser.ll


def to2files():

    a1 = '12.txt'
    a2 = '23.txt'

    """
    print('привет')
    """
    r1 = file('https://github.com/NelliSm/Sprint_5/pulls')
    nlist1 = refine(r1.content.replace(b'\n',b''))
    r2 = file('https://github.com/SorokinV/bobaDiff/pulls')
    nlist2 = refine(r2.content.replace(b'\n',b''))

    f1 = open(a1, 'wt')
    ffff = [f1.write(f'{str(rr[0])} {rr[1]} {rr[2]})') for rr in r1]
    f1.close()
    f2 = open(a2, 'wt')
    ffff = [f2.write(f'{str(rr[0])} {rr[1]} {rr[2]})') for rr in r2]
    f2.close()

    """
    for i in range(30):
        print(nlist1[i])
        print(nlist2[i])
    print('Досвидос')
    return()
    """

    return a1, a2

__version__ = 1, 7, 0

import sys
import difflib

def fail(msg):
    out = sys.stderr.write
    out(msg + "\n\n")
    out(__doc__)
    return 0

# open a file & return the file object; gripe and return 0 if it
# couldn't be opened
def fopen(fname):
    try:
        return open(fname)
    except IOError as detail:
        return fail("couldn't open " + fname + ": " + str(detail))

# open two files & spray the diff to stdout; return false iff a problem
def fcompare(f1name, f2name):
    f1 = fopen(f1name)
    f2 = fopen(f2name)
    if not f1 or not f2:
        return 0

    a = f1.readlines(); f1.close()
    b = f2.readlines(); f2.close()
    for line in difflib.ndiff(a, b):
        print(line, end=' ')

    return 1

# crack args (sys.argv[1:] is normal) & compare;
# return false iff a problem

def main(args):
    import getopt
    try:
        opts, args = getopt.getopt(args, "qr:")
    except getopt.error as detail:
        return fail(str(detail))
    noisy = 1
    qseen = rseen = 0
    for opt, val in opts:
        if opt == "-q":
            qseen = 1
            noisy = 0
        elif opt == "-r":
            rseen = 1
            whichfile = val
    if qseen and rseen:
        return fail("can't specify both -q and -r")
    if rseen:
        if args:
            return fail("no args allowed with -r option")
        if whichfile in ("1", "2"):
            restore(whichfile)
            return 1
        return fail("-r value must be 1 or 2")
    '''
    if len(args) != 2:
        return fail("need 2 filename args")
    f1name, f2name = args
    '''

    f1name, f2name = to2files()
    if noisy:
        print('-:', f1name)
        print('+:', f2name)
    return fcompare(f1name, f2name)

# read ndiff output from stdin, and print file1 (which=='1') or
# file2 (which=='2') to stdout

def restore(which):
    restored = difflib.restore(sys.stdin.readlines(), which)
    sys.stdout.writelines(restored)

if __name__ == '__main__':
    main(sys.argv[1:])