import Flask
from Flask import render_template

app = Flask(__name__)

@route
def jobs():
    return render_template("index.html")