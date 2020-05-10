import flask


app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def handle_request():
    return "Successful Connection"

app.run(host="0.0.0.0", port=5000, debug=True)

