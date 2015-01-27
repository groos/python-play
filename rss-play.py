import feedparser

f = feedparser.parse('http://www.reddit.com/r/minecraft/.rss')

print f.feed.title

print '''
Notch has invited you over for a party at his new Beverly Hills Mansion.
See below for details :D
'''

print f.feed.subtitle

for entrie in f.entries:
    print '>>' + entrie.title + '\n  ' + entrie.description
    print '>>' + entrie.link + '\n~~~~~~~~~~~~~~~~~~~~~~~~~~\n'

