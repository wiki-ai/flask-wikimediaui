from flask import Flask, render_template

from flask_wikimediaui import build_static_blueprint

app = Flask(__name__)


@app.route('/')
def root():
    # This template uses assets from WikimediaUI
    return render_template("index.html")

# Adds static assets for wikimedia-ui to path
app.register_blueprint(build_static_blueprint("wikimediaui", __name__))

if __name__ == "__main__":
    app.run(port=8080, debug=True)
