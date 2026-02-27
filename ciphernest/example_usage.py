from ciphernest.encryption import SymmetricEncryption
from ciphernest.hashing import Hashing
from ciphernest.keyderivation import KeyDerivation


def main():
    password = "my_secure_password"

    # Derive key from password
    key, salt = KeyDerivation.derive_key(password)

    message = b"Hello from CipherNest!"

    # Encrypt
    encrypted = SymmetricEncryption.encrypt(message, key)
    print("Encrypted:", encrypted)

    # Decrypt
    decrypted = SymmetricEncryption.decrypt(encrypted, key)
    print("Decrypted:", decrypted.decode())

    # Hash
    print("SHA-256:", Hashing.sha256(message))


if __name__ == "__main__":
    main()
