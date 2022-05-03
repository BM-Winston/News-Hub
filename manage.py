from app import app, create_app
from flask_script import Manager,Server


app = create_app('development')

if __name__ == '__main__':
    app.run()
