from flask import Flask, render_template
from db import fetch_mysql, fetch_fbref_mysql
from plots import iris_scatterplot
import plotly
import json

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template("home.html")


@app.route('/about')
def about():  # put application's code here
    return render_template("about.html")


@app.route('/data')
def data():
    iris_scatter = json.dumps(iris_scatterplot, cls=plotly.utils.PlotlyJSONEncoder)
    iris_data = fetch_mysql("SELECT * FROM iris")
    return render_template("data_test.html", iris_data=iris_data, iris_scatter=iris_scatter)


@app.route('/football')
def football():
    football_data = fetch_fbref_mysql("SELECT * FROM player_data")
    return render_template("football.html", football_data=football_data)


if __name__ == '__main__':
    app.run(debug=True)
