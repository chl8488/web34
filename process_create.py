#!C:\Users\User\AppData\Local\Programs\Python\Python39\python.exe
#-*- coding: utf-8 -*-
import sys
import codecs
import cgi,os
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form=cgi.FieldStorage()
title=form.getvalue('title')
description=form.getvalue('description')

open_file=open('data/'+title,'w')
open_file.write(description)
open_file.close()

print("Location: index.py?id="+title)#html 폼에 제목과 내용을 쓰고 제출하면
#index.py?id=title 로 이동하게한다
print()
