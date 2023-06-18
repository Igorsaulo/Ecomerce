import jwt
import os
from dotenv import load_dotenv
from models.models import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from services.passmaster import PassMaster


class UserAuth:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
        engine = create_engine('sqlite:///database.db')
        Session = sessionmaker(bind=engine)
        self.session = Session()
    
    def authenticate(self):
        print(self.email)
        user = self.session.query(User).filter_by(email=self.email).first()
        if user is None:
          return False
        if PassMaster.check_senha(user.senha, self.senha):
            load_dotenv()
            token = jwt.encode({'id': user.id, 'email': user.email,'nome':user.nome}, os.getenv('SECRET_KEY'), algorithm='HS256')
            return token
        return False