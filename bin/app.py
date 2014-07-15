#!/usr/bin/python

import cgi

def isLeap(year):
   if year % 400 == 0:
       return 1
   elif year % 100 == 0:
       return 0
   elif year % 4 == 0:
       return 1
   else:
       return 0

reshtml = """Content-Type: text/html\n
<html>
 <head><title>Leap Year</title></head>

 <body>
  <h1>Is it a leap year?</h1>
  <p>%s</p>
 </body>
</html>"""

form = cgi.FieldStorage()
contactName = form['contactName'].value
message = "%s " % contactName
print reshtml % message
