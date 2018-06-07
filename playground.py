from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')

def default():
    return render_template('play.html', color = 'cornflowerblue')

@app.route('/play/<num>')

def play(num):
    return render_template('play.html', times = int(num), color = 'cornflowerblue')

@app.route('/play/<num>/<color>')

def play_with_color(num, color):
    return render_template('play.html', times = int(num), color = color)

app.run(debug=True)