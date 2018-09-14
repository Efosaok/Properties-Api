from flask import Flask, jsonify
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return { 'message': 'welcome to the beginning of nothingness' }

if __name__ == '__main__':
    app.run(debug=True)
