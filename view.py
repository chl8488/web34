import os, html_sanitizer
def getList():#data디렉토리 안에 있는 파일 리스트를 웹화면에서 자동으로 추가,삭제(data디렉토리에서
#파일을 생성하면 리스트에 자동으로추가)
    sanitizer=html_sanitizer.Sanitizer()
    files=os.listdir('data')# listdir= data라는 디렉토리에 있는 파일목록을 리스트에 담아서 받아내주는 함수
    listStr=''
    for item in files:
        item=sanitizer.sanitize(item)
        listStr=listStr+'<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
    return listStr# ?뒤쪽은 쿼리스트링이라고 불린다
