from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px
import bovid


app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def index():
    df = bovid.df
    fig = px.bar(df, x='Date', y='Cases')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html', graphJSON = graphJSON)