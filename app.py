from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL, MySQLdb
import MySQLdb.cursors
import re    
import random

app = Flask(__name__)

# app.secret_key = 'xyz123abc'
# app.config['MYSQL_HOST']='localhost'
# app.config['MYSQL_USER']='root'
# app.config['MYSQL_PASSWORD']='root123$'
# app.config['MYSQL_DB']='donate'

# mysql = MySQL(app)

# global score

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input', methods=['GET', 'POST'])
def input():
    
    # T_score = f"your score: {score}"
    you_chose = ""
    message = ""
    computer_chose = ""
    # score = 0
    if request.method == 'POST' and request.form['choice']:
        
        computer_answer = random.choice(["rock","paper","scissors"])
        computer_chose = f"Computer chose: {computer_answer}"
        you_chose = f"You chose: {request.form['choice']}"
        if request.form['choice'] == computer_answer:
            message = "It's a tie!"
        elif request.form['choice'] == 'rock' and computer_answer == "scissors":
            message = "You win!"
            # score +=1
        elif request.form['choice'] == 'paper' and computer_answer == 'rock':
            message = "You win!"
            # score +=1
        elif request.form['choice'] == 'scissors' and computer_answer == 'paper':
            message = "You win!"
            # score +=1
        else:
            message = "You lose!" 
        # print(score)
    # T_score = f"your score: {score}"     
    return render_template('index.html', message=message, computer_chose=computer_chose, you_chose=you_chose)


if __name__ == "__main__":
    app.run(debug=True, port=8000)