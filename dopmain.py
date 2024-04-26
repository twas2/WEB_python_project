from flask import Flask, render_template, request, redirect, url_for
from utils import generate_math_problem

app = Flask(__name__)


problems = generate_math_problem(5, seed=42)  # Assuming there are 5 problems
total_problems = len(problems)
current_problem_index = 0
total_time = 0  # Added variable to keep track of total time

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    global current_problem_index, total_time

    if request.method == 'GET':
        current_problem = problems[current_problem_index]
        counter = current_problem_index + 1
        return render_template('test.html', problem=current_problem, counter=counter, total=total_problems,
                               total_time=total_time)

    elif request.method == 'POST':
        user_answer = request.form['answer']
        correct_answer = eval(problems[current_problem_index])
        wrong_answer = False

        if user_answer != str(correct_answer):
            wrong_answer = True
        else:
            current_problem_index += 1
            if current_problem_index == total_problems:
                total_time += float(request.form['totalTime'])  # Add the elapsed time from the form
                username = request.form['username']  # Get the username from the form
                increment_tests_completed(username)  # Increment tests completed for the user
                return redirect(url_for('submit'))  # Redirect to final page
            return redirect(url_for('test'))  # Redirect to next problem

    return redirect(url_for('test'))  # Redirect to final page if all problems are solved


@app.route('/submit')
def submit():
    return render_template('final.html', total_time=total_time)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        seed = request.form['seed']
        return redirect(url_for('index'))
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
