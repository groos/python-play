import feedparser
from HTMLParser import HTMLParser


'''
TODO: expand myhtmlparser class to create a list from a table.

see: https://github.com/schmijos/html-table-parser-python3/blob/master/html_table_parser/parser.py
'''

class myHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print 'Start tag: ', tag
        for attr in attrs:
            print '    attr:', attr
    

f = feedparser.parse('http://www.reddit.com/r/minecraft/.rss')

print f.feed.title

print 'Basic RSS parser written in Python'


print f.feed.subtitle + '\n'

descriptions = []
x = 1

for entry in f.entries:
    #print '>>' + entry.title + '\n'
    #print '>>' + entry.link + '\n~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
    descriptions.append(entry.description)

testhtml = '<head></head>'

parser = HTMLParser()
parser.feed(descriptions[x])

print descriptions[x] + '\n'
print parser.handle_starttag(parser, 'a', )
