from pytube import YouTube
from pytube import Playlist
from flask import Flask, render_template , request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hello EORLD????"

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
        videos = yt.streams.filter(progressive=True).order_by('resolution').desc()
        for v in videos:
            video['sources'].append({
                "url":v.url,
                "size":v.filesize_mb,
                "resolution":v.resolution,
                "type":v.mime_type,
                "bool":v.includes_audio_track
            })
        return video


if __name__ == "__main__":
    app.run(debug=True)

