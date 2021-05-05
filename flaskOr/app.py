from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def main():
    return 'HELLO WORLD!'

@app.route('/howYouDoing')
def about1():
    return 'hey! how you doing? '

@app.route('/hello')
def hi():
    return redirect('/howYouDoing')


@app.route('/goBack')
def goMain():
 return redirect(url_for('main'))


if __name__ == '_main_':
    app.run(debbug=True)