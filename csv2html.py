from flask import Flask, render_template, Response


app = Flask(__name__)
@app.route("/")

@app.route("/csv")
def print_csv():

    import pandas as pd

    df = pd.read_csv("seoul_weather.csv")
    dataframe = df.to_html()

    return render_template("csv2html.html", dataframe=dataframe)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



