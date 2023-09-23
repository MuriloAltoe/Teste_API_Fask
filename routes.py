from flask import Flask, jsonify, request
from Database.connection import Cursor


app = Flask(__name__)

@app.route('/api/cliente', methods=['GET', 'POST'])
def apiCliente():
    try:
        cursor = Cursor()
        cursor.Conectar()

        if request.method == "GET":
            cursor.conn.cursor().execute("SELECT * FROM cliente")
            rows = cursor.conn.cursor().fetchall()

            lista = []

            return(lista)

            # for row in rows:
            #     lista.append(row)

            return jsonify({
                "data": rows
            })

            # except:
            #     return jsonify({"data":"get"})

        elif request.method == "POST":
            # cursor.conn.cursor().execute("""
            #     DROP TABLE IF EXISTS cliente;

            #     CREATE TABLE cliente (
            #         id INT PRIMARY KEY,
            #         nome VARCHAR(255),
            #         email VARCHAR(255)
            #     );
            # """)
            
            cursor.conn.commit()

            return jsonify({"oi":"post"})     

    except:
        # return {"erro":"erro"}
        ...
    finally:
        cursor.Fechar()
if __name__ == '__main__':
    app.run(debug=True)
