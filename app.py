from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot', methods=('POST','GET'))
def chatbot():
    req = request.get_json(force=True)
    print('----------')
    print(req)
    # return jsonify(fulfillmentText = '챗봇 접속 성공') # 글자만 전송
    return jsonify(fulfillment_messages = [
        {
            "payload" : {
                "richContent" : [
                    [
                        # 이미지, 카드 ....
                        {
                            "type" : "image" ,
                            "rawUrl" : "https://blog.kakaocdn.net/dn/q6mpg/btqSLGVwFZr/EX4SXiSdyLMrIlJNaZ2AJ0/img.jpg",
                         },
                        {
                            "type": "info",
                            "title": "피자 메뉴",
                            "subtitle": "피자 메뉴판",
                            "actionLink": "http://file3.instiz.net/data/file3/2018/10/29/9/9/a/99a03fa549e4153476f51c13861854f3.gif"
                        },
                        {
                            "type": "description",
                            "title": "피자 설명판",
                            "text": [
                                "어쩌라고",
                                "그냥먹어",
                                "안녕"
                            ]
                        },
                        {
                            "type": "button",
                            "icon": {
                                "type": "logout",
                                "color": "#FF9800"
                            },
                            "text": "누르지마라",
                            "link": "https://playentry.org/uploads/thumb/6052/6052dc5c6a6a320152e1e6cb.png",
                            "event": {
                                "name": "",
                                "languageCode": "",
                                "parameters": {}
                            }
                        },
                        {
                            "type": "accordion",
                            "title": "감자 사진",
                            "subtitle": "진짜 감자 사진",
                            "image": {
                                "src": {
                                    "rawUrl": "https://cdn.mindgil.com/news/photo/202007/69482_3679_1449.jpg"
                                }
                            },
                            "text": "감자 맞다니깐"
                        },
                        {
                            "type": "chips",
                            "options": [
                                {
                                    "text": "강아지",
                                    "image": {
                                        "src": {
                                            "rawUrl": "http://image.dongascience.com/Photo/2020/03/5bddba7b6574b95d37b6079c199d7101.jpg"
                                        }
                                    },
                                    "link": "https://example.com"
                                },
                                {
                                    "text": "고양이",
                                    "image": {
                                        "src": {
                                            "rawUrl": "https://cdn.imweb.me/upload/S201712205a3a0910b89f5/d95b7faed6d64.jpg"
                                        }
                                    },
                                    "link": "https://example.com"
                                }
                            ]
                        }
                    ]
                ]
            }
        }
    ])


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
