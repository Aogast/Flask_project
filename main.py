import json
import os

from flask import Flask, url_for, request, render_template, redirect
from pickle import loads, dumps

from data import db_session
from data.users import User


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/instr')
def instr():
    return render_template('Инструкция.html')


@app.route('/table')
def tab():
    return render_template('ordertable.html', user='x')


@app.route('/ord', methods=['POST', 'GET'])
def order():
    if request.method == 'POST':
        n = {'name': request.form['name'],
             'adress': request.form['adress'],
             'telefon': request.form['telnum'],
             'email': request.form['email'],
             'amount': request.form['cooknumber'],
             'surgeter': request.form['surgeter'],
             'cv': request.form['CVV'],
             'kindofcook': request.form['kindof'],
             'comment': request.form['comment'],
             'time': request.form['time']}
        b = dumps(n)
        print(n)
        return redirect(url_for('tab'))
    else:
        return render_template('makeorder.html')


@app.route('/instruction')
def instr():
    return render_template('Инструкция.html')


@app.route('/data')
def js_info():
    db_session.global_init("db/blogs.sqlite")
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
    return render_template('index.html', user=user)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
