import base64
import hashlib
from django.contrib.auth.hashers import get_random_string


class Encryption:
    """
    AES256 encryption utility
    """
    @staticmethod
    def generate_salt(length=12):
        return get_random_string(length=length)

    @classmethod
    def build_encryption_key(cls, password_hash):
        reduced = password_hash[:32].encode('utf-8')
        return base64.urlsafe_b64encode(reduced)

    @staticmethod
    def hash(key):
        return hashlib.sha512(key).hexdigest()
