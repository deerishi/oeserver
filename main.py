from flask_restful import Resource, Api
from listBundles import ListBundles
from getBundles import GetBundles
from generateBundle import GenerateBundle
from flask import Flask


app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}




api.add_resource(HelloWorld, '/hello-world')
api.add_resource(GetBundles, '/get-bundle/')
api.add_resource(ListBundles, '/list-bundles')
api.add_resource(GenerateBundle, '/generate-bundle')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=False)
