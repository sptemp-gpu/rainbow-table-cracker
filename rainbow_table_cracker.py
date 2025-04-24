import hashlib
import json
import argparse
import os

# Function to create a rainbow table for multiple hash algorithms
def generate_rainbow_table(hash_type, charset, min_len=1, max_len=3):
    table = {}
    for length in range(min_len, max_len + 1):
        for word in generate_words(charset, length):
            hashed = hash_word(hash_type, word)
            table[hashed] = word
    return table

def generate_words(charset, length):
    """Generates all possible combinations of characters of a given length"""
    if length == 1:
        for c in charset:
            yield c
    else:
        for c in charset:
            for suffix in generate_words(charset, length - 1):
                yield c + suffix

def hash_word(hash_type, word):
    """Hashes a word with the specified hash algorithm"""
    if hash_type == 'md5':
        return hashlib.md5(word.encode('utf-8')).hexdigest()
    elif hash_type == 'sha1':
        return hashlib.sha1(word.encode('utf-8')).hexdigest()
    elif hash_type == 'sha256':
        return hashlib.sha256(word.encode('utf-8')).hexdigest()
    elif hash_type == 'sha512':
        return hashlib.sha512(word.encode('utf-8')).hexdigest()
    elif hash_type == 'sha3_256':
        return hashlib.sha3_256(word.encode('utf-8')).hexdigest()
    elif hash_type == 'sha3_512':
        return hashlib.sha3_512(word.encode('utf-8')).hexdigest()
    elif hash_type == 'blake2b':
        return hashlib.blake2b(word.encode('utf-8')).hexdigest()
    elif hash_type == 'whirlpool':
        return hashlib.new('whirlpool', word.encode('utf-8')).hexdigest()
    else:
        raise ValueError("Unsupported hash type")

def save_table(table, file_path):
    """Save the generated rainbow table to a file"""
    with open(file_path, 'w') as f:
        json.dump(table, f)
    print(f"Rainbow table saved to {file_path}")

def load_table(file_path):
    """Load the precomputed rainbow table from a file"""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return {}

def crack_hash(hash_type, hash_to_crack, table):
    """Crack a hash using the precomputed rainbow table"""
    if hash_to_crack in table:
        print(f"Cracked hash: {hash_to_crack} -> {table[hash_to_crack]}")
    else:
        print("Hash not found in the rainbow table.")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Rainbow Table Cracker")

    # Required arguments
    parser.add_argument('--hash', type=str, required=True, choices=['md5', 'sha1', 'sha256', 'sha512', 'sha3_256', 'sha3_512', 'blake2b', 'whirlpool'],
                        help="Specify the hash type to generate or crack. Choose from md5, sha1, sha256, sha512, sha3_256, sha3_512, blake2b, whirlpool.")
    parser.add_argument('--charset', type=str, default='abcdefghijklmnopqrstuvwxyz0123456789',
                        help="Charset for generating rainbow tables (default: 'abcdefghijklmnopqrstuvwxyz0123456789').")
    parser.add_argument('--min-len', type=int, default=1, help="Minimum word length to generate in the rainbow table (default: 1).")
    parser.add_argument('--max-len', type=int, default=3, help="Maximum word length to generate in the rainbow table (default: 3).")
    parser.add_argument('--generate', action='store_true', help="Flag to generate the rainbow table.")
    parser.add_argument('--crack', type=str, help="Hash to crack using the rainbow table.")

    # Parse arguments
    args = parser.parse_args()

    # Generate rainbow table
    if args.generate:
        print(f"Generating rainbow table for hash type: {args.hash} with charset: {args.charset}")
        table = generate_rainbow_table(args.hash, args.charset, args.min_len, args.max_len)
        save_table(table, "db/rainbow_table.json")

    # Crack a hash
    if args.crack:
        print(f"Cracking hash: {args.crack} with hash type: {args.hash}")
        loaded_table = load_table("db/rainbow_table.json")
        crack_hash(args.hash, args.crack, loaded_table)

if __name__ == "__main__":
    main()
