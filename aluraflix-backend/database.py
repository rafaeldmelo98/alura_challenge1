import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="user1",
        password="senha123",
        host="127.0.0.1",
        port=3306,
        database="alurachallenge1"
    )

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)


cur = conn.cursor()
   
def get_video():
    try:
        # Get Cursor
        lista_videos = []
        cur.execute(
            "SELECT *  FROM videos")
        # Print Result-set
        for (id, titulo, descricao, url) in cur:
            print(f"id: {id}, titulo: {titulo}, descricao: {descricao}, url: {url}")
            video = {'id':id, 'titulo':titulo,'descricao':descricao,'url':url}
            lista_videos.append(video)
        conn.close()
        return lista_videos
    except mariadb.Error as e: 
        conn.close()
        return {'mensagem':f"Error: {e}"}


def get_video_by_id(id_recebido):   
    try:
        cur.execute(
            f"SELECT *  FROM videos WHERE id = '{str(id_recebido)}'")
        video = {}
        for (id, titulo, descricao, url) in cur:
            print(f"id: {id}, titulo: {titulo}, descricao: {descricao}, url: {url}")
            video = {'id':id, 'titulo':titulo,'descricao':descricao,'url':url}
        conn.close()
        return video
    except mariadb.Error as e: 
        conn.close()
        return {'mensagem':f"Error: {e}"}

def inserir_video(titulo, descricao, url):
    try: 
        cur.execute(f"INSERT INTO videos (titulo,descricao,url) VALUES ('{str(titulo)}',\
        '{str(descricao)}','{str(url)}')") 
        return {'mensagem':'Filme cadastrado com sucesso!'}
    except mariadb.Error as e: 
        conn.close()
        return {'mensagem':f"Error: {e}"}

conn.commit()

