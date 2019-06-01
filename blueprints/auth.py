


from flask import Blueprint, render_template, request as req, redirect, session
auth = Blueprint('auth',__name__, template_folder="../templates", static_folder="../static")



@auth.route('/')
@auth.route('/index')
def index():
    if 'username' in session:
        return f"""
            Hello {session['username']}<br>
            <a href='/logout'>logout</a>
        """
    else:
        return """
            Hello World<br>
            <a href='/login'>login</a>
        """



@auth.route('/login', methods=['GET','POST'])
def login():
    if req.method == 'GET':
        return render_template('auth/login.html')
    if req.method == 'POST':
        username = req.form.get('username')
        if username is not None:
            session['username'] = username
            return redirect('/index')
        else:
            return "<a href='/login'>Please Input Correct Username</a>"




@auth.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/index')



@auth.route('/register',methods=['GET','POST'])
def register():
    if req.method == 'GET':
        return render_template('auth/register.html')
    if req.method == 'POST':
        username = req.form.get('username')
        password = req.form.get('password')

        if any([username is None, password is None]):
            return "Please input correct Username/Password!"
        else:
            pass