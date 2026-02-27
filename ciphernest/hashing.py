import hashlib


class Hashing:
    """
    Provides hashing utilities using SHA-256 and SHA-512.
    """

    @staticmethod
    def sha256(data: bytes) -> str:
        """
        Returns SHA-256 hash of the input data.
        """
        return hashlib.sha256(data).hexdigest()

    @staticmethod
    def sha512(data: bytes) -> str:
        """
        Returns SHA-512 hash of the input data.
        """
        return hashlib.sha512(data).hexdigest()
