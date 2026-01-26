from flask import Flask

#Flask Constructor 
app = Flask(__name__)

#A route to tell the application which url is associated function
@app.route('/')
def hello():
    return 'HELLO1'

#sample route
@app.route('/world')
def world():
    return "hello world"
@app.route('/add')
def add():
    a = 5
    b = 10
    return str(a+b)

@app.route('/name/<name>')
def display(name):
    s = "My name is " + name
    return s

@app.route('/age/<int:age>')
def display_age(age):
    # s = "My age is " + str(age)
    # return s
    return "I am %d years old" % age

@app.route('/add/<int:a>&<int:b>')
def add_two_numbers(a,b):
    sum = a+b
    return str(sum)



#building a normal admin and user routes with redirect
Admins = ['admin','sutharsan']

from flask import redirect,url_for
@app.route('/admin')
def hello_admin():
    return "Hello Admin"

@app.route('/guest/<guest>')
def hello_guest(guest):
    return "Hello %s as guest" % guest

@app.route('/user/<user>')
def find_user(user):
    if(user in Admins):
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest = user))

if __name__ == '__main__' :
    app.run(debug=True)