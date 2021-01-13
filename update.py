#!C:\Users\User\AppData\Local\Programs\Python\Python39\python.exe
#-*- coding: utf-8 -*-
import sys
import codecs
import cgi
import os, view
# stdout의 인코딩을 UTF-8로 강제 변환한다
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("content-type:text/html\r\n")

# ?뒤쪽은 쿼리스트링이라고 불린다.
form=cgi.FieldStorage()
if 'id' in form:# form에 'id'가 있다면
    pageId=form.getvalue('id')# URL쿼리스트링을 가져오는방법
    description=open('data/'+pageId, encoding='UTF-8').read()#data 파일 안에있는 pageId를 읽기용으로
                                          #불러와라
else:
    pageId='Welcome'
    description='Hello web'
#form method='GET' 방식은 보통 쿼리 문자열(query string)에 포함되어 전송되므로,
#길이의 제한이 있습니다. 따라서 보안상 취약점이 존재하므로, 중요한 데이터는 POST 방식을
#사용하여 요청하는 것이 좋습니다.
#HTML,CSS.. 등의 파일의 내용이 바뀌어야되므로 pageId를 hidden으로 따로전송한다.
#따로 전송하지않으면 파일이 수정되는게 아니라 추가가되버림
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
  <a href="create.py">수정</a>
  <h2>{title}</h2>
<form action='process_update.py' method='post'>
  <p><input type='hidden' name=pageId value="{form_defult_title}">
  <p><input type="text" name='title' placeholder='제목' value={form_defult_title}></p>
  <p><textarea rows='4' cols='30' name='description'>{form_defult_description}</textarea></p>
  <p><input type='submit' value='수정'></p>
</form>
</body>
</html>
'''.format(title=pageId, desc=description, Str=view.getList(), form_defult_title=pageId,
form_defult_description=description))
