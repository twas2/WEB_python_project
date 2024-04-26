import os
from flask import Flask, render_template, request, redirect, url_for
from utils import generate_math_problem
import random
app = Flask(__name__)
seed = random.randint(1, 1000000)
number_of_problems = 5
problems = generate_math_problem(number_of_problems, seed=seed)  # Assuming there are 5 problems
total_problems = len(problems)
current_problem_index = 0


@app.route('/')
def index():
    global number_of_problems, seed

    return render_template('index.html')


@app.route('/test', methods=['GET', 'POST'])
def test():
    global current_problem_index
    if request.method == 'GET':
        current_problem = problems[current_problem_index]
        counter = current_problem_index + 1
        return render_template('test.html', problem=current_problem, counter=counter, total=total_problems)

    elif request.method == 'POST':
        user_answer = request.form['answer']
        correct_answer = eval(problems[current_problem_index])
        wrong_answer = False

        if user_answer != str(correct_answer):
            wrong_answer = True
        else:
            current_problem_index += 1
            if current_problem_index == total_problems:
                return redirect(url_for('submit'))  # Redirect to final page
            return redirect(url_for('test'))  # Redirect to next problem

    return redirect(url_for('test'))  # Redirect to final page if all problems are solved


@app.route('/submit')
def submit():
    return render_template('final.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        seed = request.form['seed']
        return redirect(url_for('index'))
    return render_template('register.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)