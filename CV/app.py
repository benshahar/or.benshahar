
from flask import Flask, redirect, url_for, render_template, request, session,jsonify
app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'

userList = {
    "OrBensha": {"firstName": "Or", "email": "orbensha@post.bgu.ac.il", "password": "1195"},
    "HadarSim": {"firstName": "Hadar", "email": "hadarsim@post.bgu.ac.il", "password": "3592"},
    "BennyB": {"firstName": "Benny", "email": "bennyb@post.bgu.ac.il", "password": "1957"}
}


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

@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    if 'loggedIn' not in session:
        session['loggedIn'] = False
        session['username'] = ''
    if request.method == 'GET':
        if request.args:
            if "username" in request.args:
                reqUsername = request.args["username"]
                if reqUsername != '' and reqUsername in userList:
                    return render_template("assignment9.html", username=reqUsername, users=userList[reqUsername], found=True, search=True)
                elif reqUsername != '' and reqUsername not in userList:
                    return render_template("assignment9.html", found=False, search=True)
                else:
                    return render_template("assignment9.html", users=userList, search=True)
            else:
                return render_template("assignment9.html", search=False)
        else:
            return render_template("assignment9.html")
    elif request.method == 'POST':
        if request.form['username'] not in userList:
            userList[request.form['username']] = {"firstName": request.form['firstname'], "email": request.form['email'],
                                                  "password": request.form['password']}
            session['loggedIn'] = True
            session['username'] = request.form['username']
            return render_template("assignment9.html")
        else:
            session['loggedIn'] = False
            return render_template("assignment9.html", exists=True)

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

assignment10 = Blueprint('assignment10', __name__,
                         static_folder='static',
                         static_url_path='/assignment10',
                         template_folder='templates')
@Users.route('/')
@Users.route('/assignment11')
@Users.route('/assignment11/users/')
def users():
    if request.method == 'GET':
        query = "select * from users;"
        query_result = interact_db(query, query_type='fetch')
        if len(query_result) == 0:
            return jsonify({'success': 'False', 'data':[]})
        else:
            return jsonify({'success': 'True', 'data':query_result})
    else:
        return render_template('Assignment10.html')

@Users.route('/assignment11/users/selected/', defaults={'userId':3})
@Users.route('/assignment11/users/selected/<int:userId>')
def select_user(userId):
    query = "select * from users where id = '%s';" % userId
    query_result = interact_db(query, query_type='fetch')
    if len(query_result) == 0:
        return jsonify('Error, The User Not Exists!')
    else:
        return jsonify({'success': 'True', 'data':query_result[0]})