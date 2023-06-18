from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.models import User
from services.passmaster import PassMaster

class UserRepository:
    def __init__(self, user):
        engine = create_engine('sqlite:///database.db')
        Session = sessionmaker(bind=engine)
        self.session = Session()

        self.user = user


    def create(self):
        self.user.senha = PassMaster.hashed_senha(self.user.senha)
        self.session.add(self.user)
        self.session.commit()
        user_dict = {
            'nome': self.user.nome,
            'email': self.user.email,
            'senha': self.user.senha
        }
        return user_dict
    
    
    def update(self, id ):
        user = self.session.query(User).filter_by(id=id).first()
        user.nome = self.user.nome
        user.email = self.user.email
        user.senha = PassMaster.hashed_senha(self.user.senha)
        self.session.commit()
        user_dict = {
            'nome': user.nome,
            'email': user.email,
            'senha': user.senha
        }
        return user_dict
    
    
    @staticmethod
    def get_user_by_email(email):
        engine = create_engine('sqlite:///database.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        user = session.query(User).filter_by(email=email).first()
        return user
    
    @staticmethod
    def get_all_users():
        engine = create_engine('sqlite:///database.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        users = session.query(User).all()
        users_dict = []
        for user in users:
            users_dict.append({
                'id': user.id,
                'nome': user.nome,
                'email': user.email,
                'senha': user.senha
            })
        return users_dict
    
    @staticmethod
    def get_user_by_id(id):
        engine = create_engine('sqlite:///database.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        user = session.query(User).filter_by(id=id).first()
        produto_dict = []
        for produto in user.carrinho.produtos:
            produto_dict.append({
                'id': produto.id,
                'nome': produto.nome,
                'preco': produto.preco,
            })
        user_dict = {
            'id': user.id,
            'nome': user.nome,
            'email': user.email,
            'senha': user.senha,
            'carrinho': produto_dict
        }
        return user_dict
    
    
    @staticmethod
    def delete_user_by_id(id):
        engine = create_engine('sqlite:///database.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        user = session.query(User).filter_by(id=id).first()
        session.delete(user)
        session.commit()
        session.close()
        return True
