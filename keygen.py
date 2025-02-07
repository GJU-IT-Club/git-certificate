from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend


def generateKeys():
    # gen public and private RSA keys and save them to files
    try:
        privateKey = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        publicKey = privateKey.public_key()

        with open("private_key.pem", "wb") as f:
            f.write(privateKey.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ))

        with open("public_key.pem", "wb") as f:
            f.write(publicKey.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))
        
        print("Keys generated successfully!")
        
    except Exception as e:
        print(f"Error generating keys: {str(e)}")

def main():
    generateKeys()
        

if __name__ == "__main__":
    main()