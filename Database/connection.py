import psycopg2

class Cursor():
    self.cursor

    def Conectar(self):
        conn = psycopg2.connect(
            dbname="nome_do_banco_de_dados",
            user="seu_usuario",
            password="sua_senha",
            host="localhost"
        )
        self.cursor = conn.cursor()
        pass

    def Executar(self, scriptsql):
        self.cursor.execute(scriptsql)
        pass

    def Fechar(self):
        self.cursor.close()
        pass