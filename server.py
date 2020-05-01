from flask import Flask, render_template
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.sqlite")
    db_session.create_session()
    user = User()
    user.name = 'Афанасий Петрович'
    user.address = 'Москва'
    user.email = 'email@email.ru'
    session = db_session.create_session()
    session.add(user)
    user = session.query(User).first()
    print(user.name)
    session.commit()
    app.run()
    session = db_session.create_session()
    user = User()
    user.name = 'Афанасий Петрович'
    user.address = 'Москва'
    user.email = 'email@email.ru'
    session = db_session.create_session()
    session.add(user)
    user = session.query(User).first()
    session.commit()
    print(user.name)


if __name__ == '__main__':
    main()
