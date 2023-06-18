from flask import Flask
from models.models import CreateDatabase
from controllers.user_controller import user_controller
from controllers.produto_controller import produto_controller
from controllers.carrinho_controller import carrinho_controller

app = Flask(__name__)

CreateDatabase().createAll()

app.register_blueprint(user_controller)
app.register_blueprint(produto_controller)
app.register_blueprint(carrinho_controller)

if __name__ == '__main__':
    app.run()
