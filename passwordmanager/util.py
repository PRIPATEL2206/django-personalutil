import base64
from cryptography.fernet import Fernet
from django.conf import settings


class EncryptHelper:
    cipher_suite = Fernet(settings.ENCRYPTION_KEY) 
    def encrypt(txt):
        try:
            txt = str(txt)
            encrypted_text = EncryptHelper.cipher_suite.encrypt(txt.encode('ascii'))
            encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode("ascii") 
            return encrypted_text
        except Exception as e:
            print(e)
            return None
        
    def decrypt(string):
        try:
            txt = base64.urlsafe_b64decode(string)
            decoded_text = EncryptHelper.cipher_suite.decrypt(txt).decode("ascii")   
            return decoded_text
        except Exception as e:
            print(e)
            return None
