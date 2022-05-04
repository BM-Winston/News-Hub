from app import app, create_app
from flask_script import Manager,Server


app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

@manager.command
def test():
    '''
    Run the unittest
    '''
    import unnittest
    test = unittest.Testloader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    app.run()
