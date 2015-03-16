#!/usr/bin/env python

from HTMLParser import HTMLParser
import urllib2
from sys import argv

class DataParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.count_table = 0
		self.in_th = False
     		self.in_td = False
		self.headers = []
		self.data = []	

	def handle_starttag(self, tag, attrs):
		if tag == 'table':
			self.count_table+=1
		if tag == 'th':
			self.in_th = True
		if tag == 'td':
			self.in_td = True 
     
	def handle_data(self, data):
		if self.in_th and self.count_table == 1:
			self.headers.append(data)
		if self.in_td and self.count_table == 1:
			self.data.append(data)
   			
	def handle_endtag(self, tag):
		self.in_th = False
		self.in_td = False
			
html = urllib2.urlopen('http://localhost/server-status').read()
#.decode('utf-8')

parser = DataParser()
parser.feed(html)

try:
        script, SS_nr, SS_max = argv

        def SS_stat(arg):
                SS_index = parser.headers.index('SS')
                SS_values= parser.data[SS_index::len(parser.headers)]

                max_reached = 0

                for item in SS_values:
                        if int(item) > int(SS_max):
                                max_reached+=1

                if  max_reached >= int(SS_nr):
                        print 1, SS_values
                else:
                        print 0, SS_values
except ValueError:
        print 'Suppli params: number of procs AND time'
