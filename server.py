from pytube import YouTube
from pytube import Playlist
from flask import Flask, render_template , request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/youtube')
def video():
    url = request.args.get('url')
    if url:
        yt = YouTube(url)
        video={
            "info":{
                "title": yt.title,
                "thumbnail": yt.thumbnail_url,
                "video": yt.embed_url
            },
            "sources": []
        }
        videos = yt.streams.filter(progressive=True)
        for v in videos:
            video['sources'].append({
                "url":v.url,
                "size":v.filesize,
                "resolution":v.resolution
            })
        return video


if __name__ == "__main__":
    app.run(debug=True)

