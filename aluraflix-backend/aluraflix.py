from flask import Flask
from flask_restful import Resource, Api, reqparse
import database

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('titulo', help='titulo do video')
parser.add_argument('descricao', help='descrição do conteúdo do titulo')
parser.add_argument('url', help='endereço de onde está o video')


class VideosLista(Resource):
    def get(self):
        return database.get_video(), 200
    
    def post(self):
        args = parser.parse_args()
        titulo = args['titulo']
        descricao = args['descricao']
        url = args['url']
        if titulo is None:
            return {'message':'Informar titulo é necessário!'}, 400
        if descricao is None:
            return {'message':'Informar descrição é necessária!'}, 400
        if url is None:
            return {'message':'Informar URL é necessária!'}, 400

        if len(titulo) > 50:
            return {'message':'Titulo maior que o permitido. Diminua para 50 caracteres.'},400

        if len(descricao) > 500:
            return {'message':'Descricao maior que valor permitido. Diminua para 500 caracteres.'}, 400

        if len(url) > 100:
            return {'message':'URL maior que o valor permitido. Diminua para 100 caracteres.'}, 400

        if not isinstance(titulo,str) or not isinstance(descricao,str) or not isinstance(url,str):
            return {'message':'Necessário que valores sejam todos em texto'}, 400

        return database.inserir_video(titulo,descricao,url), 201

class Video(Resource):
    def get(self, id):
        video = database.get_video_by_id(id)
        if video:
            return video, 200
        else:
            return "Sinto muito. Não encontramos esse video =c", 404

    def put(self, id):
        args = parser.parse_args()
        titulo = args['titulo']
        descricao = args['descricao']
        url = args['url']
        if titulo is None:
            return {'message':'Informar titulo é necessário!'}, 400
        
        if descricao is None:
            return {'message':'Informar descrição é necessário!'}, 400
        
        if url is None:
            return {'message':'Informar URL é necessário!'}, 400
        
        if len(titulo) > 50:
            return {'message':'Titulo maior que o permitido. Diminua para 50 caracteres.'},400

        if len(descricao) > 500:
            return {'message':'Descricao maior que valor permitido. Diminua para 500 caracteres.'}, 400

        if len(url) > 100:
            return {'message':'URL maior que o valor permitido. Diminua para 100 caracteres.'}, 400

        if not isinstance(titulo,str) or not isinstance(descricao,str) or not isinstance(url,str):
            return {'message':'Necessário que valores sejam todos em texto'}, 400

        return database.atualizar_video(id,titulo,descricao,url), 200

    def delete(self, id):
        video = database.deletar_video(id)
        if video['deletado']:
            return video, 404
        return video, 200


api.add_resource(VideosLista, '/videos')
api.add_resource(Video, '/videos/<id>')

if __name__ == '__main__':
    app.run(debug=True)