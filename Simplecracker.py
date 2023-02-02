import hashlib
import itertools
import threading
import time

hash_types = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]

def hash_cracker(hash_value, hash_type, wordlist):
    with open(wordlist, 'r') as f:
        for line in f:
            word = line.strip()
            if hash_type == "md5":
                hash_object = hashlib.md5(word.encode())
            elif hash_type == "sha1":
                hash_object = hashlib.sha1(word.encode())
            elif hash_type == "sha224":
                hash_object = hashlib.sha224(word.encode())
            elif hash_type == "sha256":
                hash_object = hashlib.sha256(word.encode())
            elif hash_type == "sha384":
                hash_object = hashlib.sha384(word.encode())
            elif hash_type == "sha512":
                hash_object = hashlib.sha512(word.encode())
            else:
                return "Error: Invalid hash type"
            hex_dig = hash_object.hexdigest()
            if hex_dig == hash_value:
                return word
    return "Password not found in wordlist"

def brute_force_attack(charset, max_length):
    for length in range(1, max_length + 1):
        for word in itertools.product(charset, repeat=length):
            yield "".join(word)

def crack(hash_value, hash_type, wordlists, max_length, charset):
    found = False
    for wordlist in wordlists:
        result = hash_cracker(hash_value, hash_type, wordlist)
        if result != "Password not found in wordlist":
            print("Password found:", result)
            found = True
            break
    if not found:
        print("Password not found in wordlists, starting brute force attack...")
        for word in brute_force_attack(charset, max_length):
            result = hash_cracker(hash_value, hash_type, [word])
            if result != "Password not found in wordlist":
                print("Password found:", result)
                break

hash_value = input("Enter hash value: ")
hash_type = input("Enter hash type: " + str(hash_types))
wordlists = input("Enter wordlist files (separatedby commas): ").split(',')
max_length = input("Enter max length for brute force attack: ")
charset = input("Enter charset for brute force attack: ")

start_time = time.time()
crack(hash_value, hash_type, wordlists, int(max_length), charset)
print("Time taken:", time.time() - start_time, "seconds")
