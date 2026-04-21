import dash
from dash import html, dcc, Input, Output

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("Weather Forecast App"),

    html.P("Enter weather conditions to get a prediction."),

    html.Label("Temperature"),
    dcc.Input(id="temp", type="number"),

    html.Label("Humidity"),
    dcc.Input(id="humidity", type="number"),

    html.Label("Wind Speed"),
    dcc.Input(id="wind", type="number"),

    html.Br(), html.Br(),

    html.Button("Predict", id="btn"),

    html.H2(id="output")
])


@app.callback(
    Output("output", "children"),
    Input("btn", "n_clicks"),
    Input("temp", "value"),
    Input("humidity", "value"),
    Input("wind", "value"),
)
def update_output(n, temp, humidity, wind):
    if n is None:
        return ""

    # TEMP FAKE OUTPUT (until model is ready)
    return f"Prediction will appear here (Temp={temp}, Humidity={humidity}, Wind={wind})"


if __name__ == "__main__":
    app.run(debug=True)