from flask import Flask

app = Flask(__name__)
your_name = "Ashureah"

@app.route('/')
def welcome():
    return f"Welcome to {your_name}’s web site!"

if __name__ == '__main__':
    app.run(debug=True)
