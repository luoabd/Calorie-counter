from flask import Flask, render_template, request, url_for, flash, redirect
import json
app = Flask(__name__)
app.config['SECRET_KEY'] = 'b9m6z7Vv39WTc2'

jsonFilePath = "data\Food_Table.json"

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        name = request.form['name']
    return render_template('index.html')

if __name__ == '__main__':
    app.run()