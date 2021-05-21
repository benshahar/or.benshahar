

from flask import Flask, url_for, redirect
from flask import render_template

app = Flask(_name_)

@app.route('/', methods=['GET', 'POST', 'DELETE', 'PUT'])
def home():
    return render_template('CVWEB.html')

@app.route('/project7', methods=['GET', 'POST', 'DELETE', 'PUT'])
def hello_contact():
    return render_template('Contact.html')

@app.route('/Assignment8', methods=['GET', 'POST', 'DELETE', 'PUT'])
def hello_Assignment8():
    return render_template('Assignment8.html',
                           user={'name': "Or Benshahar"},
                           hobbies=['Basketball', 'Diving', 'Ski'])

@app.route('/howYouDoing')
def about1():
    return 'hey! how you doing? '

@app.route('/hello')
def hi():
    return redirect('/howYouDoing')


@app.route('/goBack')
def goMain():
 return redirect(url_for('main'))


if _name_ == '_main_':
    app.run()