import json

quiz_data = [
    {
        "question": "How many planets are in our solar system?",
        "options": ["10", "12", "8", "9"],
        "correct": ["8"]
    },
    {
        "question": "Which of these planets have rings? Select all that apply. ",
        "options": ["Jupiter", "Mars", "Venus", "Neptune", "Uranus"],
        "correct": ["Jupiter", "Neptune", "Uranus"]
    },
    {
        "question": "Which planet in our solar system has the fastest winds?",
        "options": ["Neptune", "Jupiter", "Saturn", "Mars"],
        "correct": ["Neptune"]
    },
    {
        "question": "Which of the following planets has the hottest surface temperature in the solar system?",
        "options": ["Mercury", "Venus", "Mars", "Jupiter"],
        "correct": ["Venus"]
    },
    {
        "question": "Which of the planets have the strongest magnetic field?",
        "options": ["Earth", "Saturn", "Jupiter", "Uranus"],
        "correct": ["Jupiter"]
    },
    {
        "question": "Which of these planets rotate in the opposite direction of most planets? Select all that apply.",
        "options": ["Venus", "Uranus", "Earth", "Neptune"],
        "correct": ["Venus", "Uranus"]
    }
]

# Save to a file
with open("quiz_questions.json", "w") as json_file:
    json.dump(quiz_data, json_file, indent=4)

print("JSON file created successfully!")
