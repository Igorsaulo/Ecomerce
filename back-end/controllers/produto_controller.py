from flask import Blueprint
from flask_restx import Api, Resource
from models.models import Produto
from models.produto.produto_repository import ProdutoRepository

produto_controller = Blueprint('produto', __name__)
api = Api(produto_controller)


@api.route('/produto')
class UserController(Resource):
    def post(self):
        produto = api.payload
        new_produto = ProdutoRepository(Produto(**produto)).create()
        return new_produto
      
    def get(self):
        produtos = ProdutoRepository.get_all_produtos()
        return produtos


@api.route('/produto/<int:id>')
class UserResource(Resource):
    def get(self, id):
        produto = ProdutoRepository.get_produto_by_id(id)
        return produto
    
    def delete(self, id):
        ProdutoRepository.delete_produto_by_id(id)
        return 'Produto deleted', 200
      
    def patch(self, id):
        produto = api.payload
        new_produto = ProdutoRepository(Produto(**produto)).update(id)
        return new_produto
