from typing import Union
from fastapi import FastAPI
from CarregarDB import carregarDB
mydb = carregarDB()
app = FastAPI()


@app.get("/")
def read_root():
    data_cursor = mydb.cursor()
    data_cursor.execute('SELECT DISTINCT Data FROM custo_produt;')
    arquivo = data_cursor.fetchall()
    return arquivo

