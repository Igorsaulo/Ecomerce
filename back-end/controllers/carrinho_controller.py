from flask import Blueprint
from flask_restx import Api, Resource
from models.carrinho.carrinho_adapter import CarrinhoAdapter


carrinho_controller = Blueprint('carrinho', __name__)
api = Api(carrinho_controller)


@api.route('/carrinho')
class CarrinhoController(Resource):
    def post(self):
        carrinho_composer = api.payload
        new_carrinho = CarrinhoAdapter().create(carrinho_composer)
        return new_carrinho
      
      
@api.route('/carrinho/<int:id>')
class CarrinhoControllerWithId(Resource):
    def delete(self, id):
        CarrinhoAdapter().delete(id)
        return 'Produto removido do carrinho com sucesso!'