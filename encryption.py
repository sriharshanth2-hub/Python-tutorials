import random
import string

char = " " + string.ascii_letters + string.punctuation + string.digits
char = list(char)

key = char.copy()
random.shuffle(key)
choice = input("Enter your choice (ENCRYPTION/DECRYPTION): ").upper()
if choice == "ENCRYPTION":
    print("-----ENCRYPTION-----")
    org_text = input("Enter original message: ")
    enc_text = ""

    for letter in org_text:
        index = char.index(letter)
        enc_text += key[index]

    print(f"The original message is {org_text}")
    print(f"The encrypted message is {enc_text}")

elif choice == "DECRYPTION":
    print("-----DECRYPTION-----")
    enc_text = input("Enter encrypted message: ")
    org_text = ""

    for letter in enc_text:
        index = key.index(letter)
        org_text += char[index]

    print(f"The encrypted message is {enc_text}")
    print(f"The original message is {org_text}")

else:
    print("Invalid choice")
 