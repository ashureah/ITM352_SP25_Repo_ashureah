from flask import Flask, render_template

app = Flask(__name__)
your_name = "Ashureah"

@app.route('/')
def home():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)