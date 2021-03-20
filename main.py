from flask import Flask, render_template, request, url_for, flash, redirect
import json
app = Flask(__name__)
app.config['SECRET_KEY'] = 'asasas'
jsonFilePath = "data\Food_Table.json"

def get_info(name):
    with open(jsonFilePath) as jsonFile:
        results = []
        data = json.load(jsonFile)
        for i in range(0,len(data)-1):
            for item, value in data[str(i)].items():
                if item == 'Display_Name':
                    if name in value.lower():
                        results.append(data[str(i)]['Display_Name']+' '+data[str(i)]['Portion_Display_Name'])
                        break
        return(results)

@app.route('/', methods=('GET', 'POST'))
def index():
    results = []
    if request.method == 'POST':
        name = request.form['name']
        if not name:
            flash('Name is required!')
        else:
            results = get_info(name)
            if results == []: flash('No matches were found!')
    return render_template('index.html', results = results)

if __name__ == '__main__':
    app.run()