from app import create_app
from app.models import db
from flask_script import Manager, Server
from flask_script.commands import ShowUrls, Clean
from flask_migrate import Migrate, MigrateCommand

app = create_app('prod')
migrate = Migrate(app, db)
manger = Manager(app)
manger.add_command('server', Server)
manger.add_command('db', MigrateCommand)
manger.add_command('show', ShowUrls)
manger.add_command('clean', Clean)


@manger.shell
def make_shell_context():
    return dict(
        app=app,
        db=db,
    )


@manger.command
def test():
    import unittest

    tests = unittest.TestLoader().discover('tests')

    # with open('UnittestTextReport.txt', 'a') as f:
    #     unittest.TextTestRunner(stream=f, verbosity=2).run(tests)

    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manger.run()
