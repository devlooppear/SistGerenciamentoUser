DATABASE = 'infosuser'
PORTA = '5432'
SENHA = '<sua_senha_aqui>'

DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "jdshbfkjsdbjdfjkghjsd"
SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:{SENHA}@localhost:{PORTA}/{DATABASE}"