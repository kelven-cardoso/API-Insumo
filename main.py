from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/insumos', methods=['GET'])
def insumos():
    return


if __name__ == "__main__":  
    app.run(debug=True)


    