#!C:\Users\User\AppData\Local\Programs\Python\Python39\python.exe
#-*- coding: utf-8 -*-
import sys
import codecs
import cgi, os
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form=cgi.FieldStorage()
pageId=form.getvalue('pageId')
title=form.getvalue('title')
description=form.getvalue('description')
#rename('경로/'+현재파일이름, 변경할이름)

open_file=open('data/'+pageId,'w')#기존의 id를 수정해야하기 때문에 title이아닌 pageId를쓴다
open_file.write(description)
open_file.close()

os.rename('data/'+pageId,'data/'+title)

print("Location: index.py?id="+title)#html 폼에 제목과 내용을 쓰고 제출하면
#index.py?id=title 로 이동하게한다
print()
