import bcrypt

def get_password_hash(password: str) -> str:
    # Transforma a senha em bytes
    pwd_bytes = password.encode('utf-8')
    # Gera o "sal" (salt) e a senha criptografada
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(pwd_bytes, salt)
    # Retorna como string para salvar no banco
    return hashed_password.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    password_bytes = plain_password.encode('utf-8')
    hashed_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_bytes)