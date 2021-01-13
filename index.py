#!C:\Users\User\AppData\Local\Programs\Python\Python39\python.exe
#-*- coding: utf-8 -*-
print("content-type:text/html\r\n")
import sys
import codecs
import cgi
import os, view
import html_sanitizer

# stdout의 인코딩을 UTF-8로 강제 변환한다
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

#data디렉토리 안에 있는 파일 리스트를 웹화면에서 자동으로 추가,삭제(data디렉토리에서
#파일을 생성하면 리스트에 자동으로추가)
sanitizer=html_sanitizer.Sanitizer()
form=cgi.FieldStorage()
if 'id' in form:# form에 'id'가 있다면
    title=pageId=form.getvalue('id')# URL쿼리스트링을 가져오는방법
    title=sanitizer.sanitize(title)
    description=open('data/'+pageId, encoding='UTF-8').read()#data 파일 안에있는 pageId를 읽기용으로불러와라
    description=sanitizer.sanitize(description)#본문의 내용에 <>태그 같은것을 없애줌
    update_link= '<a href="update.py?id={}"> 수정</a>'.format(pageId)#pageId 의값이 {}가 된다.
    delete_action='''
    <form action='listdelete.py' method='post'>
        <p><input type="hidden" name='title' value={title}></p>
        <p><input type='submit' name='del'value='삭제'></p>
    </form>'''.format(title=pageId)
else:
    title=pageId='Welcome'
    description='Hello web'
    update_link=''
    delete_action=''
print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {Str}
  </ol>
  <a href="create.py">추가</a>
  {upli}
  {dela}
  <h2>{title}</h2>
  <p>{desc}
  </p>

</body>
</html>
'''.format(title=title, desc=description, Str=view.getList(), upli=update_link,
dela=delete_action))
