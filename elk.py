from app import cli, create_app, db
from app.auth.models.user import User

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}