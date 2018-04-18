from flask import Flask, render_template, request, session
import random
from flask.ext.session import Session

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route("/")
def main():
    return render_template('index.html')


@app.route("/showGame")
def show_game():

    randNum = random.randint(0, 100)
    session['randNum'] = randNum
    print randNum
    session['count'] = 0
    
    return render_template("game.html")

@app.route("/result")
def check_guess():
    
    guess = int(request.args.get("guess"))
    name = request.form.get('inputName')

    randNum = session['randNum']
  
    if session['count'] < 10:

        if guess == randNum:
            return render_template("result.html", name=name, response='! You Won.',count=session['count'])

        else:
            session['count'] += 1
            if guess > randNum:
                return render_template("result.html",response='Too high. Try again!',count=session['count'])
            elif guess < randNum:
                return render_template("result.html",response='Too low. Try again!',count=session['count'])
        
    else:
        return render_template("result.html",name=name,response='You lose.')


if __name__ == "__main__":
	app.debug = True
	app.run()
