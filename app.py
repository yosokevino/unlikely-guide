from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/toaster_ovens')
def toaster_ovens():
    return render_template("toaster_ovens.html")

if __name__ == '__main__':
    app.run()