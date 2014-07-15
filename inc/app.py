#!/usr/bin/python

import cgi

form = cgi.FieldStorage()
contactName = form['contactName'].value
print "%s " % contactName
