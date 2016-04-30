from flask import Flask,jsonify
import db.medidas as m
import os

app = Flask(__name__)

@app.route("/all")
def get_all():
    medidas=[]
    for medida in m.get_all():
        medidas.append({"time":medida[0],"temperatura":medida[1],"humedad relativa":medida[2],"humedad en tierra":medida[3],"luz":medida[4],"distancia":medida[5]})
    return jsonify({"medidas":medidas})

if __name__ == "__main__":
    if not os.path.isfile("./db/example.db"):
        m.medidas().init_db()
    app.run(debug=True)
