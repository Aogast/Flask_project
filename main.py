from flask import Flask, url_for, request, render_template, redirect
from pickle import loads, dumps
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
                'surname': request.form['surname'],
                'adress': request.form['adress'],
                'telefon': request.form['telnum'],
                'city': request.form['city'],
                'amount': request.form['cooknumber'],
                'surgeter': request.form['surgeter'],
                'cv': request.form['CVV'],
                'kindofcook': request.form['kindof'],
                'time': request.form['time']}
        b = dumps(n)
        print(n)
        return redirect(url_for('tab'))
    else: return render_template('makeorder.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
