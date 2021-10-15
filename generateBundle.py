from flask_restful import Resource
from flask import Flask, request, send_from_directory
import os


class GenerateBundle(Resource):
    def post(self):
        content = request.json
        print('Json content is ', content)
        try:
            url_list = content.get("urlList", "")
            primaryURL = content.get("primaryUrl", "")
            manifestUrl = content.get("manifestUrl", "")
            bundle_name = content.get("bundleName", "")
            clientId = request.args.get("clientId", "")

            print(
                f"url_list = {url_list}, primaryUrl= {primaryURL}, manifest_url = {manifestUrl} clientId ={clientId}")

            basedir = os.path.join(os.path.realpath(os.path.dirname(
                __file__))) + f"\\generate_bundles\\{clientId}"
            if not os.path.exists(basedir):
                os.makedirs(basedir)
            urlPath = f"{basedir}\\urls_{bundle_name}.txt"
            with open(urlPath, "w") as myfile:
                myfile.write(f"# Url list for {primaryURL}\n")
                for url in url_list:
                    myfile.write(url+"\n")

            basedirBundle = os.path.join(os.path.realpath(
                os.path.dirname(__file__))) + f"\\bundles\\{clientId}"
            if not os.path.exists(basedirBundle):
                os.makedirs(basedirBundle)

            bundle_file = f"{basedirBundle}\\{bundle_name}"

            print("\n\n\n\nGenerating Bundle for file ",bundle_file)
            output=os.system(
                f"gen-bundle -URLList {basedir}\\urls_{bundle_name}.txt -primaryURL {primaryURL}  -o {bundle_file}")
            
            if output!=0:
                raise Exception("Unable to Bundle")

            print("\n\n\nBundle generation complete Generating Bundle for file ",bundle_file)
            if os.path.isfile(bundle_file):
                print("\n\n\Returning  file ",bundle_file)

                return send_from_directory(basedirBundle, bundle_name, as_attachment=True)
            else:
                print("\n\n\n not Returning  file ",bundle_file)
                return "File Not Found",404
        except Exception as e:
            print('\n\n exception is ',e)
            return "Unable to bundle the website", 400
