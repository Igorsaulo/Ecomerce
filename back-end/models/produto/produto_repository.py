from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.models import Produto

class ProdutoRepository:
    def __init__(self, produto):
        engine = create_engine('sqlite:///database.db')
        Session = sessionmaker(bind=engine)
        self.session = Session()

        self.produto = produto

    def create(self):
        self.session.add(self.produto)
        self.session.commit()
        produto_dict = {
            'nome': self.produto.nome,
            'preco': self.produto.preco,
        }
        return produto_dict
    
    def update(self, id ):
        produto = self.session.query(Produto).filter_by(id=id).first()
        produto.nome = self.produto.nome
        produto.preco = self.produto.preco
        self.session.commit()
        produto_dict = {
            'nome': produto.nome,
            'preco': produto.preco,
        }
        return produto_dict
    
    @staticmethod
    def get_produto_by_id(id):
        engine = create_engine('sqlite:///database.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        produto = session.query(Produto).filter_by(id=id).first()
        produto_dict = {
            'id': produto.id,
            'nome': produto.nome,
            'preco': produto.preco,
        }
        return produto_dict
    
    @staticmethod
    def get_all_produtos():
        engine = create_engine('sqlite:///database.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        produtos = session.query(Produto).all()
        produtos_dict = []
        for produto in produtos:
            produtos_dict.append({
                'id': produto.id,
                'nome': produto.nome,
                'preco': produto.preco,
            })
               
        return produtos_dict
    
    @staticmethod
    def delete_produto_by_id(id):
        engine = create_engine('sqlite:///database.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        produto = session.query(Produto).filter_by(id=id).first()
        session.delete(produto)
        session.commit()
        return True