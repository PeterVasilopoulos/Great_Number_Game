from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)
app.secret_key = "something cool"

@app.route('/')
def num_game():
    if 'random' not in session:
        session['random'] = random.randint(1,100)
        session['status'] = False

    return render_template("num_game.html")

@app.route('/guess', methods=["POST"])
def guess():
    session['guess'] = request.form['guess']
    if session['guess'] == session['random']:
        session['status'] = True
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    session['status'] = False
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)