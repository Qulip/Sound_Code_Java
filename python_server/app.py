from flask import Flask
from function.execute import *
from flask_restx import Resource, Api



app = Flask(__name__)
api = Api(app)

# @app.route('/test/<string:name>')
# def test():
#     return execute(name)

@api.route('/test/<string:name>')
class Hello(Resource):
    def get(self, name):  # 멤버 함수의 파라미터로 name 설정
        return execute(name)




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

