from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend

def encryptUserData():
    # prompt user4data, encrypt, and display the res
    try:
        fullName = input("Enter your full name: ")
        email = input("Enter your email: ")

        data = f"Full Name: {fullName}\nEmail: {email}"

        with open("public_key.pem", "rb") as keyFile:
            publicKey = serialization.load_pem_public_key(
                keyFile.read(),
                backend=default_backend()
            )

        encryptedData = publicKey.encrypt(
            data.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        encryptedHex = encryptedData.hex()
        
        print("\033[37m\nEncrypted data\033[0m"+" (please copy this green text):")
        print("\033[32m"+encryptedHex+"\033[0m")
        
        print(f"\033[35m\nPlease save this encrypted data in a file named 'certs/YOUR_USERNAME.txt'\033[0m")
        print(f"\033[36mSubmit a pull request with the file to the repository, we will decrypt it and email you with the Certificate of Participation\n\033[0m")

    except Exception as e:
        print(f"Error encrypting data: {str(e)}")


def main():      
    encryptUserData()
    

if __name__ == "__main__":
    main()