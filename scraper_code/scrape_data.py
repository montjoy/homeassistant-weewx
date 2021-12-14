#!/usr/bin/python3

path = 'weewx.html'
wee_file = open(path,'r')
wee_data = wee_file.read()


# print(wee_data)

#from html.parser import HTMLParser

#class MyHTMLParser(HTMLParser):
#    def handle_starttag(self, tag, attrs):
#        print("Encountered a start tag:", tag)

#    def handle_endtag(self, tag):
#        print("Encountered an end tag :", tag)

#    def handle_data(self, data):
#        print("Encountered some data  :", data)

#parser = MyHTMLParser()
#parser.feed(wee_data)

# from html.parser import HTMLParser
# from html.entities import name2codepoint

# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print("Start tag:", tag)
#         for attr in attrs:
#             print("     attr:", attr)

#     def handle_endtag(self, tag):
#         print("End tag  :", tag)

#     def handle_data(self, data):
#         print("Data     :", data)

#     def handle_comment(self, data):
#         print("Comment  :", data)

#     def handle_entityref(self, name):
#         c = chr(name2codepoint[name])
#         print("Named ent:", c)

#     def handle_charref(self, name):
#         if name.startswith('x'):
#             c = chr(int(name[1:], 16))
#         else:
#             c = chr(int(name))
#         print("Num ent  :", c)

#     def handle_decl(self, data):
#         print("Decl     :", data)

# parser = MyHTMLParser()
# parser.feed(wee_data)
from lxml import etree
from io import StringIO, BytesIO

import requests
import lxml.html

html = requests.get('http://local-weewx:8099')
doc = lxml.html.fromstring(html.content)

# broken_html=wee_data
# parser = etree.HTMLParser()
# tree   = etree.parse(StringIO(broken_html), parser)
# result = etree.tostring(tree.getroot(), pretty_print=True, method="html")
# print(result)

labels = doc.xpath('//div[@id="current_widget"]/div[@class="widget_contents"]/table/tbody/tr/td[@class="label"]/text()')

# outside_temp = tree.xpath('//div[@class="widget_contents"]/table/tbody/tr/td[@class="label"][text() = "Outside Temperature"]/../td[@class="data"]/text()')
# dew_point = tree.xpath('//div[@class="widget_contents"]/table/tbody/tr/td[@class="label"][text() = "Dew Point"]/../td[@class="data"]/text()')

# print(labels)
# print(outside_temp)
# print(dew_point)

weatherdata = {}

for label in labels:
    fixedlabel = label.lower().replace(' ', '_')
    # print(fixedlabel)
    # prep_xpath = '//div/[@id="current_widget"]/div[@class="widget_contents"]/table/tbody/tr/td[@class="label"][text() = $var]/../td[@class="data"]/text()', var=label
    # print(prep_xpath)
    reading = doc.xpath('//div/[@id="current_widget"]/div[@class="widget_contents"]/table/tbody/tr/td[@class="label"][text() = $var]/../td[@class="data"]/text()', var=label)
    # weatherdata[fixedlabel] = reading

print(weatherdata)
