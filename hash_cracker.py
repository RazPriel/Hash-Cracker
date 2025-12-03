#First we import the necessary libraries
import os
import hashlib

#Here we are asking the user for the neccesery information in order to perform the attack
type_of_hash = str(input("[+] Which type of hash you want to crack: ")).lower()
wordlist_path = str(input("[+] Enter path to the wordlist file: "))
hash_to_decrypt = str(input("[+] Enter hash value to crack: "))

if os.path.exists(wordlist_path):
    pass
else:
    print("[-] Wordlist file doesn't exist! Check again to see if this file really does exist...")
    exit(1)

print("\n\n[ --- Cracking " + type_of_hash + " Hash Value: " + hash_to_decrypt + " --- ]\n\n")

with open(wordlist_path, 'r') as file:
    for line in file.readlines():
        if type_of_hash == "md5":
            hash_object = hashlib.md5(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print("[!!] Found MD5 Value: " + str(line.strip()))
                exit(0)
        if type_of_hash == "sha1":
            hash_object = hashlib.sha1(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print("[!!] Found SHA1 Value: " + str(line.strip()))
                exit(0)
        else:
            print("[-] Hash type cannot be cracked in this program, Please try a different hash type.")
            exit(1)

    print("[-] Password not in wordlist file.")
