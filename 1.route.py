from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'

@app.route('/home')
def home():
    return 'home'


@app.route('/admin')
def admin():
    return "hi admin"

#name='dharshan'
@app.route('/guest/<guest>')
def guest(guest):
    return "hi " + guest + " as guest"

@app.route('/user/<name>')
def user(name):
    if name=="admin":
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', guest=name))


if __name__ == '__main__':
    app.run()
    
