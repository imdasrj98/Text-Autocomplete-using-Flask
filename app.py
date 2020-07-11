from flask import Flask, Response, render_template, request
import json
from wtforms import TextField, Form
from flask_restful import Resource, Api

app = Flask(__name__, template_folder='template')
api=Api(app)

class SearchForm(Form):
    autocomp = TextField('Insert Footballer', id='footballer_autocomplete')

footballer = ["Lionel Messi",
      "Cristiano Ronaldo",
      "Ronaldo Nazario",
      "Ronaldinho Gaucho",
      "Sergio Ramos",
      "Sergio Busquets",
      "Sergio Aguero",
      "Diego Costa",
      "Diego Godin"]

@app.route('/_autocomplete', methods=['GET', 'POST'])
def autocomplete():
    print(footballer)
    return Response(json.dumps(footballer), mimetype='application/json')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm(request.form)
    return render_template("search.html", form=form)

class Football(Resource):
    def get(self):
        return Response(json.dumps(footballer), mimetype='application/json')

api.add_resource(Football, '/names')

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
