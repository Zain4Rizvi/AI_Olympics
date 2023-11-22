from flask import Blueprint, redirect, render_template, request, flash, jsonify, url_for
import json
import string

from .creator import generate_song, generate_album_cover
import random

# courseText
# quizQuestions
# response
# summary
# images

prompt = "default"
topics = ""

# usually easier to keep the name the same as the file
views = Blueprint('views', __name__)

# homepage


@views.route('/', methods=['GET', 'POST'])
# @login_required
def home():
    return render_template("query.html")


@views.route('/query', methods=['GET', 'POST'])
def query():
    return render_template('query.html', prompt="", courseParagraphs="", courseImages="")


@views.route('/generate-response', methods=['POST'])
def generate_response():
    global topics
    prompt = json.loads(request.data)
    promptGenre = prompt['genre']
    promptTopic = prompt['topic']
    # print(promptText)
    print(promptGenre)
    print(promptTopic)

    topics += f", {promptGenre}"

    response = generate_song(promptGenre, promptTopic)
    return jsonify({"lyrics": response['lyrics'], "title": response['title']})


@views.route('/generate-cover', methods=['POST'])
def generate_cover():
    cover_url = generate_album_cover(topics)
    print(cover_url)
    return jsonify({"image_url": cover_url})
