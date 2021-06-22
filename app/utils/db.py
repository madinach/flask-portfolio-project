import psycopg2
from app.constants.tables import CREATE_TABLE
from urllib.parse import urlparse




def connect_db():
    try:
        connect_url = "postgres://euglgvrfsyazyn:174971399e35e43d7a71bbbf08e46d2dd498152b78f14845e4312625f9934fc7@ec2-54-197-100-79.compute-1.amazonaws.com:5432/df2o4f3djt73vl"
        result = urlparse(connect_url)
        user = result.username
        password = result.password
        database = result.path[1:]
        host = result.hostname
        db=psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password)
        print('Connected to postgresql 🐘')
        cur = db.cursor()
        cur.execute(CREATE_TABLE)
        cur.execute("SELECT NOW()")
        db.commit()
        return db
    except (Exception, psycopg2.DatabaseError) as error:
        print("error:")
        print(error)
  

def create_project(title,description,url,cover):
         query = "INSERT INTO projects (title,description,url,cover) VALUES('{}','{}','{}','{}') RETURNING *".format(title, description, url,cover)
         db = connect_db()
         cursor = db.cursor()
         cursor.execute(query)
         db.commit()
         
def get_projects():
         query = "SELECT * from projects"
         db = connect_db()
         cursor = db.cursor()
         cursor.execute(query)
         return cursor.fetchall()

         
