from flask_script import Manager, Shell, Server
from blog import app, db
from blog.models import User

# app = app('development')
app = app
manager = Manager(app)

manager.add_command('server', Server)



@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User)

if __name__ == '__main__':
    manager.run()