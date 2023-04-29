from flask import render_template, request, session, redirect, url_for
from app.models import User
from app import app, db

# rota para a página principal
@app.route('/')
def home():
    # verifica se o usuário está logado
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    return render_template('home.html', user=user)

# rota de login do usuário
@app.route('/login', methods=['GET', 'POST'])
def login():
    # se o usuário já estiver logado, redireciona para a página principal
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        return render_template('home.html', user=user)

    # se o método da requisição for POST, tenta fazer o login do usuário
    if request.method == 'POST':
        email = request.form['email']

        # verifica se o e-mail correspondem a um usuário cadastrado
        user = User.query.filter_by(email=email).first()
        if not user:
            return render_template('login.html', error='E-mail inválido.')

        # faz o login do usuário e redireciona para a página principal
        session['user_id'] = user.id
        return redirect(url_for('home'))

    # se o método da requisição for GET, exibe o formulário de login
    return render_template('login.html')

# rota de logout do usuário
@app.route('/logout')
def logout():
    # remove o id do usuário da sessão
    session.pop('user_id', None)
    return redirect(url_for('login'))

# rota de cadastro de novo usuário
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone_number = request.form['phone_number'] # novo campo adicionado
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        gender = request.form['gender']

        if password != confirm_password:
            error = 'As senhas não coincidem'
            return render_template('register.html', error=error)

        # Separando o nome completo em nome e sobrenome
        first_name, last_name = request.form['first_name'], request.form['last_name']

        user = User(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, password=password, gender=gender)
        db.session.add(user)
        db.session.commit()

        return render_template('register.html', message='Usuário cadastrado com sucesso')

    # se o método da requisição for GET, exibe o formulário de cadastro
    return render_template('register.html')