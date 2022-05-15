from config import Config
from app import app, db
from app.models import User, Post, followers
from app import cli


@app.shell_context_processor
def make_shell_context():
    return {'app': app, 'db': db, 'User': User, 'Post': Post, 'followers': followers, 'config': Config}