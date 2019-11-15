from flask import Flask
from flask import render_template

app = Flask(__name__)

db = [('Post 1', 'Ivan', 'Content 1'), ('Post 2', 'Gosho', 'Content 2')]


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/posts')
def list_posts():
    return render_template('posts.html', posts=db)


@app.route('/posts/<int:id>')
def get_post(id):
    post = db[id]
    return render_template('posts.html', posts=post)
