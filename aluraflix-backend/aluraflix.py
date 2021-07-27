from flask import Flask
from flask_restful import Resource, Api, reqparse
import database

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('titulo', help='aqui vai um titulo')
parser.add_argument('descricao')
parser.add_argument('url')


class VideosLista(Resource):
    def get(self):
        return database.get_video(), 200
    
    def post(self):
        args = parser.parse_args()
        titulo = args['titulo']
        descricao = args['descricao']
        url = args['url']
        if len(titulo) > 50:
            return "Titulo maior que o permitido. Diminua para 50 caracteres.", 413
        if len(descricao) > 500:
            return "Descricao maior que valor permitido. Diminua para 500 caracteres.", 413
        if len(url) > 100:
            return "URL maior que o valor permitido. Diminua para 100 caracteres.", 413
        if not isinstance(titulo,str) or not isinstance(descricao,str) or not isinstance(url,str):
            return "Necessário que valores sejam todos em texto", 413
        return database.inserir_video(titulo,descricao,url), 201

class Video(Resource):
    def get(self, id):
        video = database.get_video_by_id(id)
        if video:
            return video, 200
        else:
            return "Sinto muito. Não encontramos esse video =c", 404


api.add_resource(VideosLista, '/videos')
api.add_resource(Video, '/videos/<id>')

if __name__ == '__main__':
    app.run(debug=True)