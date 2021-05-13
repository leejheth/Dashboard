import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# data = pd.read_csv("avocado.csv")
# data = data.query("type == 'conventional' and region == 'Albany'")
# data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
# data.sort_values("Date", inplace=True)

# data = pd.DataFrame({'name': ['bob 2012', 'Ava 2013', 'Aby 007', 'XYZ 8', 'GRZ x7', 'Boo VIII', 'Joy 2020'],
#                    'Date': ['2020-02-01', '2020-05-01', '2020-06-30', '2020-04-15', '2020-01-04', '2020-03-21', '2020-07-08'],
#                    'colour': ['pink', 'teal', 'velvet', 'pink', 'green', 'teal', 'pink'],
#                    'AveragePrice': [1, 2, 3, 4, 5, 6, 7],
#                    'Total Volume': [100, 200, 300, 400, 500, 600, 700],
#                    'unit': ['cm', 'inch', 'cm', 'cm', 'inch', 'cm', 'cm']})

Date = [1, 2, 3, 4, 5, 6]
Price = [10,20,30,40,50,70]
Volume = [100,200,300,400,800,900]

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Dashboard example",),
        html.P(
            children="An example dashboard to try out functions."
        ),
        html.P(
            children="This is the next line"
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": Date,
                        "y": Price,
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Graph 1"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        # "x": data["Date"],
                        # "y": data["Total Volume"],
                        "x": Date,
                        "y": Volume,
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Graph 2"},
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)