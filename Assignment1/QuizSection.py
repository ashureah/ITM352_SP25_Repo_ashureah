import json
import random
import time

def load_questions(filename):
    """Load questions from a JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)

def ask_question(question_data):
    """Ask a multiple-choice quiz question and return if the answer is correct and the response time."""
    question = question_data["question"]
    options = question_data["options"]
    correct_answers = set(question_data["correct"])
    
    random.shuffle(options)
    
    print("\n" + question)
    labels = [chr(97 + i) for i in range(len(options))]
    option_map = {labels[i]: options[i] for i in range(len(options))}
    
    for label, option in option_map.items():
        print(f"{label}) {option}")
    
    start_time = time.time()
    while True:
        user_answer = input("Your answer (comma-separated if multiple): ").strip().lower()
        user_choices = {option_map[ans] for ans in user_answer.replace(" ", "").split(",") if ans in option_map}
        
        if user_choices == correct_answers:
            end_time = time.time()
            response_time = end_time - start_time
            print("Correct!\n")
            return True, response_time
        else:
            print("Incorrect. Try again.")

def run_quiz(filename):
    """Run the quiz, shuffle questions, and track score and time."""
    questions = load_questions(filename)
    random.shuffle(questions)
    
    score = 0
    total_time = 0
    
    for question_data in questions:
        correct, response_time = ask_question(question_data)
        total_time += response_time
        if correct:
            if response_time < 5:
                score += 2
                print("Bonus point for answering quickly!")
            else:
                score += 1
    
    print(f"Quiz finished! Your score: {score}/{len(questions) * 2}")
    print(f"Total time taken: {total_time:.2f} seconds")
    save_score(score, total_time)

def save_score(score, total_time, filename="scores.txt"):
    """Save the quiz score to a file."""
    with open(filename, "a") as file:
        file.write(f"Score: {score}, Time: {total_time:.2f} seconds\n")
    print("Your score has been saved.")

if __name__ == "__main__":
    run_quiz("quiz_questions.json")
