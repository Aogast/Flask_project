import json
import os

from flask import Flask, url_for, request, render_template, redirect

from data import db_session
from data.users import User


app = Flask(__name__)
db_session.global_init("db/blogs.sqlite")


@app.route('/')
def index():
    '''main page'''
    return render_template('main.html')


@app.route('/instr')
def instr():
    '''instruction for using'''
    return render_template('Инструкция.html')


@app.route('/table')
def tab():
    '''page with a table of orders'''
    return render_template('ordertable.html', user=js_info())


@app.route('/ord', methods=['POST', 'GET'])
def order():
    '''function, which makes orders and creates json'''
    if request.method == 'POST':
        filejs = {'name': request.form['name'],
             'address': request.form['address'],
             'telefon': request.form['telnum'],
             'email': request.form['email'],
             'amount': request.form['cooknumber'],
             'surgeter': request.form['surgeter'],
             'cv': request.form['CVV'],
             'kindofcook': request.form['kindof'],
             'comment': request.form['comment'],
             'time': request.form['time']}
        with open('info.json', 'w') as f:
            f.write(json.dumps(filejs))
        return redirect(url_for('tab'))
    else:
        return render_template('makeorder.html')


def js_info():
    '''function, which creates database'''
    session = db_session.create_session()
    if os.access('info.json', os.R_OK):
        with open('info.json') as f:
            file = f.read()
            resp = json.loads(file)
            user = User(name=resp['name'],
                        telefon=resp['telefon'],
                        address=resp['address'],
                        email=resp['email'],
                        kindofcook=resp['kindofcook'],
                        amount=resp['amount'],
                        comment=resp['comment'],
                        time=resp['time'],
                        cv=resp['cv'],
                        surgeter=resp['surgeter'])
            session.add(user)
            session.commit()
            os.remove('info.json')
    user = session.query(User)
    return user


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
