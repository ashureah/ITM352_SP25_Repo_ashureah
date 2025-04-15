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
        post_link = meme['postLink']

        return render_template_string("""
            <h1>{{ title }}</h1>
            <a href="{{ post_link }}" target="_blank">
                <img src="{{ image_url }}" alt="Wholesome Meme" width="600">
            </a>
        """, title=title, image_url=image_url, post_link=post_link)
    else:
        return "Failed to retrieve meme", 500

if __name__ == '__main__':
    app.run(debug=True)
