from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px
import plotly.graph_objects as go
import bovid


app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def index():

    df = bovid.df
    df['MA7'] = df.Cases.rolling(7).mean()
    fig = px.bar(df, x='Date', y='Cases', template='plotly_dark')
    fig.add_traces(go.Scatter(x= df.Date, y=df.MA7, mode = 'lines', name = '7 Day Average'))
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html', graphJSON = graphJSON)