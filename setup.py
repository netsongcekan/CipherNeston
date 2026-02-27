from setuptools import setup, find_packages

setup(
    name="CipherNest",
    version="0.1.0",
    author="Your Name",
    description="Lightweight cryptographic toolkit for secure encryption and hashing",
    packages=find_packages(),
    install_requires=[
        "cryptography>=42.0.0"
    ],
    python_requires=">=3.8",
)
