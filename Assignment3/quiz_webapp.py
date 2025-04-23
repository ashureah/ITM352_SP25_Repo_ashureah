from flask import Flask, render_template, request, redirect, url_for, session, make_response
import json
import os

app = Flask(__name__)
app.secret_key = 'secret_key_here'



def load_questions(filename='quiz_questions.json'):
    with open(filename, 'r') as file:
        return json.load(file)

questions = load_questions()


@app.route('/')
def home():
    username = request.cookies.get('username')
    score_history = session.get('score_history', [])

    if username:
        return render_template('index2.html', username=username, score_history=score_history)
    else:
        return render_template('enter_name.html')

@app.route('/save_name', methods=['POST'])
def save_name():
    username = request.form.get('username')
    resp = make_response(redirect(url_for('home')))
    resp.set_cookie('username', username)
    session['score_history'] = []
    return resp


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    import random

    if 'score' not in session or 'question_index' not in session:
        session['score'] = 0
        session['question_index'] = 0
        session['missed_questions'] = []

        
        shuffled = load_questions()
        random.shuffle(shuffled)
        session['questions'] = shuffled

    index = session['question_index']
    questions = session.get('questions', load_questions())

    if index >= len(questions):
        return redirect(url_for('result'))

    if request.method == 'POST':
        selected = request.form.getlist('answer')
        current_q = questions[index]
        correct_answers = set(current_q['correct'])
        user_answers = set(selected)

        explanation = f"Correct answer(s): {', '.join(correct_answers)}"

        if user_answers == correct_answers:
            session['score'] += 1
            result = "Correct!"
        else:
            result = "Incorrect. " + explanation
            session['missed_questions'].append({
                'question': current_q['question'],
                'your_answer': list(user_answers),
                'correct': list(correct_answers),
                'explanation': explanation
            })

        session['question_index'] += 1
        return render_template('question_result.html', result=result, explanation=explanation)

    q = questions[index]
    options = q['options'].copy()
    random.shuffle(options)

    progress = int((index) / len(questions) * 100)
    return render_template('quiz.html', question=q['question'], options=options, progress=progress)


@app.route('/result')
def result():
    score = session.get('score', 0)
    total = len(questions)
    username = request.cookies.get('username')
    score_history = session.get('score_history', [])
    score_history.append(score)
    session['score_history'] = score_history
    missed = session.get('missed_questions', [])

    return render_template('result2.html', score=score, total=total, username=username, missed=missed)

@app.route('/restart')
def restart():
    session.pop('score', None)
    session.pop('question_index', None)
    session.pop('missed_questions', None)
    return redirect(url_for('quiz'))

if __name__ == '__main__':
    app.run(debug=True)
