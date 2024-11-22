# SPARKLEE Encryptor

# 🔐 Encryptor & Decryptor

A Python-based encryption and decryption tool. This program allows you to securely encrypt and decrypt text strings using a unique character map while adding a fun visual touch with ASCII art.

---

## ✨ Features
- **Encrypt Strings**: Transform any text into an encrypted format using randomly assigned special characters.
- **Decrypt Strings**: Easily decrypt encrypted text using stored encryption maps.
- **ASCII Art Integration**:
  - Dynamically generate ASCII art for user input.
- **Secure Map Storage**: Each encryption process generates a unique encryption map stored in a `.pkl` file for secure and later decryption.

---

## 🛠️ How It Works
1. **Encryption**:
   - Generates a random encryption map for all unique characters in the input string.
   - Preserves spaces and non-alphabetic characters.
   - Saves the encryption map as a `.pkl` file for later use.
2. **Decryption**:
   - Allows you to select the correct map from saved files.
   - Reverses the encryption map to decrypt the text.

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.7+
- Install the required libraries:
  ```bash
  pip install pyfiglet
  ```

### 2. Clone the Repository
```bash
git clone https://github.com/your-username/ascii-encryptor.git
cd ascii-encryptor
```

### 3. Run the Program
Run the tool using:
```bash
python encryptor.py
```

---

## 📝 Usage

### 1. Encrypt a String
- Select the **encryption option (1)**.
- Enter the string you want to encrypt.
- View the generated ASCII art and encrypted string.
- The encryption map is saved automatically (e.g., `encryption_map_1690001234.pkl`).

### 2. Decrypt a String
- Select the **decryption option (2)**.
- Choose the correct encryption map from the displayed list.
- Enter the encrypted string.
- View the decrypted text.

---

## 📂 File Structure
```plaintext
ascii-encryptor/
├── encryptor.py      # Main Python script
├── encryption_maps/  # Folder to store encryption maps (created dynamically)
└── README.md         # Project documentation
```

---

## 🛡️ Security
- **Randomized Encryption Maps**: Each encryption session generates a unique mapping for security.
- **Storage of Maps**: Encryption maps are stored in `.pkl` files for retrieval.

---

## 🏗️ Contributing
We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add feature-name'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

---

## 🖇️ License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 💬 Acknowledgments
- ASCII art generation powered by [pyfiglet](https://github.com/pwaller/pyfiglet).
- Inspired by the fun and creativity of text-based tools.
