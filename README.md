Here’s the updated README.md with a Python icon added:


# 🌈 Rainbow Table Cracker

A Python-based script that generates and cracks rainbow tables for various hash algorithms. The tool supports multiple hash algorithms like MD5, SHA1, SHA256, SHA512, SHA3, BLAKE2, and Whirlpool. You can generate a rainbow table for a specified charset and word length, or use a precomputed table to crack hashes.

![Version](https://img.shields.io/badge/version-1.0-blue.svg) ![Python](https://img.shields.io/badge/python-3.x-brightgreen.svg) ![License](https://img.shields.io/badge/license-MIT-yellow.svg) ![Python](https://img.shields.io/badge/python-%F0%9F%92%BB-306998.svg)

## 🚀 Features

- **🔑 Rainbow Table Generation**: Generate rainbow tables for common hash algorithms.
- **🔐 Multiple Hash Algorithms**: Supports MD5, SHA1, SHA256, SHA512, SHA3, BLAKE2, Whirlpool.
- **💻 Command-Line Interface**: Supports command-line usage for both Windows and Linux.
- **🔤 Customizable Charset and Length**: Specify a custom charset and word length for generating the rainbow table.
- **🧩 Hash Cracking**: Crack hashes using precomputed rainbow tables.
- **⚡ Efficient**: Quickly generate and use rainbow tables for password cracking.

## 📦 Installation

### 1. Clone the repository:


- git clone https://github.com/yourusername/rainbow-table-cracker.git
- cd rainbow-table-cracker


### 2. Install Python dependencies:
Ensure you have Python 3.x installed.
If additional libraries are required (e.g., pycryptodome for Whirlpool), you can install them via:


- pip install pycryptodome


## 💡 Usage

### 🧩 Generate a Rainbow Table

To generate a rainbow table for a specific hash algorithm, charset, and word length:


- python rainbow_table_cracker.py --hash <hash_algorithm> --charset <charset> --min-len <min_length> --max-len <max_length> --generate


**Example:**

Generate a rainbow table for **MD5** hashes with the default charset (abcdefghijklmnopqrstuvwxyz0123456789) and word length between 1 and 3:


- python rainbow_table_cracker.py --hash md5 --generate


You can adjust the charset and word length by using the --charset, --min-len, and --max-len arguments.

### 🔓 Crack a Hash

To crack a specific hash using a precomputed rainbow table:


- python rainbow_table_cracker.py --hash <hash_algorithm> --crack <hash_to_crack>


**Example:**

Crack a **SHA256** hash:


- python rainbow_table_cracker.py --hash sha256 --crack <sha256_hash_here>


## 🧑‍💻 Supported Hash Algorithms

- **MD5** (md5)
- **SHA1** (sha1)
- **SHA256** (sha256)
- **SHA512** (sha512)
- **SHA3-256** (sha3_256)
- **SHA3-512** (sha3_512)
- **BLAKE2b** (blake2b)
- **Whirlpool** (whirlpool)

## 📋 Command-Line Arguments

| Argument           | Description                                                                                  |
|--------------------|----------------------------------------------------------------------------------------------|
| --hash           | The hash algorithm to use. Options: md5, sha1, sha256, sha512, sha3_256, sha3_512, blake2b, whirlpool. |
| --charset        | Charset for generating the rainbow table (default: abcdefghijklmnopqrstuvwxyz0123456789).    |
| --min-len        | Minimum word length for the rainbow table (default: 1).                                      |
| --max-len        | Maximum word length for the rainbow table (default: 3).                                      |
| --generate       | Flag to generate the rainbow table.                                                         |
| --crack          | The hash to crack using the precomputed rainbow table.                                       |

## 🖼️ Example Commands

1. **Generate a rainbow table for SHA256 with a custom charset:**

   
   - python rainbow_table_cracker.py --hash sha256 --charset abc123 --min-len 1 --max-len 3 --generate
   

2. **Crack a SHA512 hash:**

   
   - python rainbow_table_cracker.py --hash sha512 --crack <sha512_hash_here>
   

## 🗂️ File Structure

- rainbow_table_cracker.py: Main script for generating and cracking rainbow tables.
- db/rainbow_table.json: Stores the precomputed rainbow table (generated after running --generate).
  
## 🤝 Contributing

1. Fork the repository.
2. Create a new branch: git checkout -b feature-name.
3. Make your changes and commit: git commit -am 'Add new feature'.
4. Push to the branch: git push origin feature-name.
5. Create a new Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- Uses Python's hashlib library for hashing.
- Supports multiple hash algorithms, including MD5, SHA1, SHA256, SHA512, SHA3, BLAKE2, and Whirlpool.

---

### 💡 Additional Notes:

- **Linux/Windows**: The script supports both Linux and Windows. Just make sure you have Python 3.x installed and that your environment has access to the required dependencies.
- **Efficiency**: While this method is efficient for cracking short passwords, it may become impractical for long passwords due to the combinatorial explosion in possible combinations.
