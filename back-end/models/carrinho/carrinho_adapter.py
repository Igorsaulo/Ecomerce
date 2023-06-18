from models.models import Carrinho, User, Produto
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class CarrinhoAdapter:
  def __init__(self):
    engine = create_engine('sqlite:///database.db')
    Session = sessionmaker(bind=engine)
    self.session = Session()
    
  def create(self, carrinho_composer):
      user_id = carrinho_composer['user_id']
      produto_id = carrinho_composer['produto_id']

      user = self.session.query(User).filter_by(id=user_id).first()
      produto = self.session.query(Produto).filter_by(id=produto_id).first()

      carrinho = self.session.query(Carrinho).filter_by(user=user).first()

      if carrinho is None:
          carrinho = Carrinho(user=user, produtos=[produto])
          self.session.add(carrinho)
      else:
          carrinho.produtos.append(produto)

      self.session.commit()

      carrinho_dict = {
          'id': carrinho.id,
          'user_id': carrinho.user_id,
          'produto_ids': [produto.id for produto in carrinho.produtos],
      }
      return carrinho_dict

    
  def delete(self, id):
      carrinho = self.session.query(Carrinho).filter_by(id=id).first()
      self.session.delete(carrinho)
      self.session.commit()
      return True

