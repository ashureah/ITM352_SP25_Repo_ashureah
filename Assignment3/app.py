from flask import Flask, render_template, request, redirect, url_for, session
import json
import random
import time

app = Flask(__name__)
app.secret_key = "supersecretkey"

def load_questions(filename):
    with open(filename, 'r') as file:
        return json.load(file)

questions = load_questions("quiz_questions.json")

@app.route('/')
def index():
    session.clear()
    session['questions'] = random.sample(questions, len(questions))
    session['current'] = 0
    session['score'] = 0
    session['start_time'] = time.time()
    return render_template('index.html')

@app.route('/question', methods=['GET', 'POST'])
def question():
    current = session.get('current', 0)
    if request.method == 'POST':
        selected = request.form.getlist('answer')
        correct = set(session['questions'][current - 1]['correct'])
        selected_values = set(selected)

        response_time = time.time() - session['response_start']
        if selected_values == correct:
            if response_time < 5:
                session['score'] += 2
            else:
                session['score'] += 1

    if current >= len(session['questions']):
        return redirect(url_for('result'))

    q = session['questions'][current]
    session['current'] += 1
    session['response_start'] = time.time()

    return render_template('question.html', q=q, num=current + 1, total=len(session['questions']))

@app.route('/result')
def result():
    total_time = time.time() - session.get('start_time', time.time())
    score = session.get('score', 0)
    max_score = len(session.get('questions', [])) * 2
    return render_template('result.html', score=score, total_time=total_time, max_score=max_score)

if __name__ == '__main__':
    app.run(debug=True)