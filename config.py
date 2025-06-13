DEBUG = True

# Conectando com o banco de dados
USERNAME = 'root'
PASSWORD = ''
SERVER = 'localhost'
DB = 'api_flask'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
# Verifica em tempo real modificações no database durante a sessão
SQLALCHEMY_TRACK_MODIFICATIONS = True