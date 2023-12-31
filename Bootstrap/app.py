from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def base():
    context = {
        'title': 'Сайт-визитка'
    }
    return render_template("base.html", **context)


if __name__ == '__main__':
    app.run(debug=True)
