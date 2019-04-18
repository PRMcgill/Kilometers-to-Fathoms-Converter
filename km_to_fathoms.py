from flask import Flask

app = Flask(__name__)

@app.route('/')
def initial_page():
    return 'Kilometer to Fathoms Convert'

@app.route('/km/<int:km>')
def km_to_fathoms(km):
    fathoms = km * 546.807
    return f"{km} kilometers converts to {fathoms} fathoms."

@app.route('/fathoms/<int:fathoms>')
def fathoms_to_km(fathoms):
    km = fathoms / 546.807
    return f"{fathoms} fathoms converts to {km} kilometers."


if __name__=="__main__":
    app.run()