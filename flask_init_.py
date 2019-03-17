# coding：utf-8
from flask import Flask, jsonify, render_template
import get_movie
import get_music

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>hello,world</h1>"


@app.route('/music/<music_name>')
def music(music_name):
    music_json = get_music.get_music(music_name)
    return jsonify(music_json)


@app.route('/movie/<movie_name>')
def movie(movie_name):
    movie_json = get_movie.get_movie(movie_name)
    return jsonify(movie_json)


if __name__ == '__main__':
    app.run(debug=True)
