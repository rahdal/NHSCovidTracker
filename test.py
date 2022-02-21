import plotly.express as px
import bovid

df = bovid.df
fig = px.bar(df, x='Date', y='Cases')
fig.show()