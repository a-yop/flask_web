from flask import Flask , render_template
from data import Articles

app = Flask(__name__)
app.debug = True
#True 해놓으면 재실행해줌 / 개발이 끝나면 꼭 없애야해!!!파일 다 보임, 해킹위험

@app.route('/',methods=['GET','POST'])
def hello_world():
    articles = Articles()
    return render_template('index.html', articles = articles) #템플릿/abc에 있으면 ('abc/index.html')
#데코?
# 키값 = value

if __name__ == '__main__':
    app.run()

#1,2,8,9 네줄로 서버를 만들어
#app.run이 제일 먼저 실행 된다.
