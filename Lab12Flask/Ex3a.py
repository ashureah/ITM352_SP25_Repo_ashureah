from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def get_meme():
    url = "https://meme-api.com/gimme/wholesomememes"
    response = requests.get(url)

    if response.status_code == 200:
        meme = response.json()
        title = meme['title']
        image_url = meme['url']
        subreddit = meme['subreddit']

        return render_template_string("""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="refresh" content="10">
                <title>Wholesome Meme</title>
                <style>
                    body { text-align: center; font-family: Arial, sans-serif; }
                    img { max-width: 80%; height: auto; border-radius: 10px; }
                    h1 { margin-bottom: 10px; }
                    p { color: gray; }
                </style>
            </head>
            <body>
                <h1>{{ title }}</h1>
                <img src="{{ image_url }}" alt="Wholesome Meme">
                <p>Source: r/{{ subreddit }}</p>
            </body>
            </html>
        """, title=title, image_url=image_url, subreddit=subreddit)
    else:
        return "Failed to load meme", 500

if __name__ == '__main__':
    app.run(debug=True)
