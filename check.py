import urllib
import re


def check():
    file1 = urllib.urlopen('http://www.cmu.edu/oie/newsandevents/orientation.html')
    part1 = re.search('<h1>International Graduate Student Orientation Programs<\/h1>\n<p>(.*)<\/p>', file1.read())
    part2 = re.search('<a href=.*<\/a>',part1.group(0))
    part3 = re.search('Registration link to come',part1.group(0))
#    print part1.group()
#    try:
#       print part2.group()
#  except:

#     print part3.group()
    if part2:
        return 1
    elif part3:
        return -1
    else:
        return 0

if __name__ == '__main__':
    a = check()
    if a == 1:
        print 'http://www.cmu.edu/oie/newsandevents/orientation.html'
    elif a == -1:
        print 'Not yet'
    else:
        print 'Unexpected'
