from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def index():
    return render_template('index.html')