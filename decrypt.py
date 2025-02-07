from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend

def decrypt_file(filename):
    # decr with the private key
    try:

        with open("private_key.pem", "rb") as keyFile:
            privateKey = serialization.load_pem_private_key(
                keyFile.read(),
                password=None,
                backend=default_backend()
            )

    
        with open(filename, "r") as f:
            encryptedHex = f.read().strip()
            encryptedData = bytes.fromhex(encryptedHex)

        
        decryptedData = privateKey.decrypt(
            encryptedData,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        print("\nDecrypted data:")
        print(decryptedData.decode())

    except Exception as e:
        print(f"Error decrypting file: {str(e)}")


def main():
    
    filename = input("Enter the filename to decrypt: ")
    decrypt_file("certs/"+filename)
        

if __name__ == "__main__":
    main()