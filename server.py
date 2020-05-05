import json
import os

from flask import Flask, render_template

from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    @app.route('/')
    @app.route('/data')
    def index():
        db_session.global_init("db/blogs.sqlite")
        session = db_session.create_session()
        if os.access('info.json', os.R_OK):
            with open('info.json') as f:
                file = f.read()
                resp = json.loads(file)
                print(resp)
                user = User(name=resp['name'],
                            address=resp['address'],
                            email=resp['email'],
                            cookies=resp['cookies'],
                            count=resp['count'],
                            comment=resp['comment'])
                session.add(user)
                session.commit()
                session.add(user)
                session.commit()
                session.add(user)
                session.commit()
                session.add(user)
                session.commit()
            os.remove('info.json')
        user = session.query(User)
        return render_template("index.html", user=user)


if __name__ == '__main__':
    main()
    app.run(port=8080, host='127.0.0.1')
