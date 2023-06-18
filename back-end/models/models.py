from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String, unique=True)
    senha = Column(String)
    carrinho = relationship('Carrinho', back_populates='user',uselist=False)


class Carrinho(Base):
    __tablename__ = 'carrinho'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='carrinho')
    produtos = relationship('Produto', back_populates='carrinho')


class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    preco = Column(Integer)
    carrinho_id = Column(Integer, ForeignKey('carrinho.id'))
    carrinho = relationship('Carrinho', back_populates='produtos')


class CreateDatabase:
    def __init__(self):
        self.createAll()

    @staticmethod
    def createAll():
        database_url = 'sqlite:///database.db'
        engine = create_engine(database_url, echo=True)
        Base.metadata.create_all(bind=engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        session.commit()
        session.close()
