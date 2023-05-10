from flask import Flask, render_template
from CarregarDB import carregarDB
mydb = carregarDB()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    
    data_cursor = mydb.cursor()
    data_cursor.execute('SELECT DISTINCT Data FROM custo_produt;')
    arquivo = data_cursor.fetchall()
    
    return arquivo


if __name__ == "__main__":  
    app.run(debug=True)

    # servidor do heroku

    