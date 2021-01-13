#!C:\Users\User\AppData\Local\Programs\Python\Python39\python.exe
#-*- coding: utf-8 -*-
import sys
import codecs
import cgi
import os
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form=cgi.FieldStorage()
pageID=form.getvalue('title')


os.remove('data/'+pageID)

print("Location: index.py")
print()
