import bcrypt

class PassMaster:
    @staticmethod
    def hashed_senha(senha):
        return bcrypt.hashpw(
            senha.encode('utf-8'),
            bcrypt.gensalt()
        ).decode('utf-8')
    
    @staticmethod
    def check_senha(hashed_senha,senha):
        return bcrypt.checkpw(
            senha.encode('utf-8'),
            hashed_senha.encode('utf-8')
        )