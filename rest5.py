from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

#inisiasi
app = Flask(__name__)
api = Api(app)
CORS(app)

identitas={}

class KResource(Resource):
    def get(self):
        return identitas
    def post(self):
        name = request.form["name"]
        keterangan = request.form["keterangan"]
        identitas["Toto"] = name
        identitas["Gem"] = keterangan
        response = ({"msg":"berhasil di post"})
        return response
    
api.add_resource(KResource, "/api",methods =["GET","POST"])
if __name__ == '__main__':
    app.run(debug=True,port=5005)
    