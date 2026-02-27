from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os


class SymmetricEncryption:
    """
    Provides high-level symmetric encryption using Fernet (AES-128 in CBC mode with HMAC).
    """

    @staticmethod
    def generate_key() -> bytes:
        """
        Generates a new secure Fernet key.
        """
        return Fernet.generate_key()

    @staticmethod
    def encrypt(data: bytes, key: bytes) -> bytes:
        """
        Encrypts data using the provided key.
        """
        f = Fernet(key)
        return f.encrypt(data)

    @staticmethod
    def decrypt(token: bytes, key: bytes) -> bytes:
        """
        Decrypts encrypted data using the provided key.
        """
        f = Fernet(key)
        return f.decrypt(token)
