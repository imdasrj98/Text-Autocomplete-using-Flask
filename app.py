from flask import Flask, Response, render_template, request
import json
from wtforms import TextField, Form

app = Flask(__name__, template_folder='template')

class SearchForm(Form):
    autocomp = TextField('Insert Footballer', id='city_autocomplete')


@app.route('/_autocomplete', methods=['GET', 'POST'])
def autocomplete():
    cities = ["Lionel Messi",
          "Cristiano Ronaldo",
          "Ronaldo Nazario",
          "Ronaldinho Gaucho",
          "Sergio Ramos",
          "Sergio Busquets",
          "Sergio Aguero",
          "Diego Costa",
          "Diego Godin"]
    print(cities)
    return Response(json.dumps(cities), mimetype='application/json')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm(request.form)
    return render_template("search.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
