from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Role,Book
from  flask_migrate import Migrate, MigrateCommand

app = create_app('development')

manager = Manager(app,db)
migrate = Migrate(app,db)

manager.add_command('server',Server)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Role = Role,Book = Book)

if __name__ == '__main__':
    manager.run()
