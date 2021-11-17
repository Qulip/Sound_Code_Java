# -*- coding: utf8 -*-


from flask import Flask
from function.authenticate import *
from flask_restx import Resource, Api


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
api = Api(app)

# @app.route('/test/<string:name>')
# def test():
#     return execute(name)

@api.route('/authenticate/<string:name>')
class Hello(Resource):
    def get(self, name):  # 멤버 함수의 파라미터로 name 설정
        return secondary_authenticate(name)

@api.route('/getKey')
class Hello2(Resource):
    def get(self):
        return show_key_index()



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
