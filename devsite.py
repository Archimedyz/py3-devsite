from app import app, db
from app.models import User, Post

# TODO: make model imports generic to
# avoid having to always edit this function
@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Post': Post
    }

