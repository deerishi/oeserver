from flask_restful import Resource
from flask import Flask, request, send_from_directory

import os




class GetBundles(Resource):
    def get(self):
        
        file_name=request.args.get('file')
        clientId=request.args.get('clientId')
        file_name1 = os.path.join(os.path.realpath(os.path.dirname(__file__))) + f"\\bundles\\{clientId}\\{file_name}"
        file_name2= os.path.join(os.path.realpath(os.path.dirname(__file__))) + f"\\bundles\\{file_name}"

        baseDir1 = os.path.join(os.path.realpath(os.path.dirname(__file__))) + f"\\bundles\\{clientId}"
        baseDir2= os.path.join(os.path.realpath(os.path.dirname(__file__))) + "\\bundles"

        print('file_name1 is ',file_name1,' and file_name2 = ',file_name2,' and file_name is ',file_name)
        
        if os.path.isfile(file_name1):
            return send_from_directory(baseDir1, file_name, as_attachment=True)
        if os.path.isfile(file_name2):
            return send_from_directory(baseDir2, file_name, as_attachment=True)
        else:
            return "FileNotFound",404
  



