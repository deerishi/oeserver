from flask import Flask, send_file, request
from flask_restful import Resource, Api
import os


class ListBundles(Resource):
    def get(self):
        clientId = request.args.get('clientId')

        basedir = os.path.join(os.path.realpath(
            os.path.dirname(__file__))) + f"\\{clientId}\\bundles"
        result = []
        try:
            for root, dirs, files in os.walk(basedir):
                print(f"file is ", files)
                for file in files:
                    if file.endswith(".wbn"):
                        result.append(file)
                        print(os.path.join(root, file))
            print('basedir is ', basedir)
            basedir = os.path.join(os.path.realpath(
                os.path.dirname(__file__))) + f"\\bundles"
            for root, dirs, files in os.walk(basedir):
                print(f"file is ", files)
                for file in files:
                    if file.endswith(".wbn"):
                        result.append(file)
                        print(os.path.join(root, file))

            print('basedir is ', basedir)
            return {"bundles": result}
        except Exception as e:
            print('Exception is ',e)
            return "Unable to list bundles",500
