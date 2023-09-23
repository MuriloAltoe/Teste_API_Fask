import psycopg2

class Cursor():
    def __init__(self) -> None:
       self.conn = None

    def Conectar(self):
        self.conn = psycopg2.connect(
            dbname="postgres",
            user="user",
            password="admin",
            host="localhost"
        )
        
        
    def Fechar(self):
        self.conn.close()
        