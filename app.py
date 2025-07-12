# [cite: 1]
from flask import Flask, render_template, request, jsonify
from rsa import generate_keys, encrypt, decrypt # Assuming rsa.py is in the same directory

app = Flask(__name__)

@app.route("/")
def home():
    """Renders the main encryption page.""" # [cite: 1]
    return render_template("index.html") # [cite: 1]

@app.route("/generate_keys", methods=["GET"])
def generate_keys_route():
    """Generates RSA key pair and returns as JSON or renders template.""" # [cite: 1]
    try:
        public_key, private_key = generate_keys() # [cite: 1]
        # Return JSON specifically for AJAX requests from the frontend # [cite: 1]
        if request.headers.get("X-Requested-With") == "XMLHttpRequest": # [cite: 1, 2]
            return jsonify({"public_key": public_key, "private_key": private_key}) # [cite: 1]
        # Fallback for direct access (though primarily designed for AJAX) # [cite: 1]
        return render_template("index.html", public_key=public_key, private_key=private_key) # [cite: 1]
    except Exception as e: # [cite: 1]
        error_msg = str(e) # [cite: 2]
        if request.headers.get("X-Requested-With") == "XMLHttpRequest": # [cite: 2]
            return jsonify({"error": error_msg}) # [cite: 2]
        return render_template("index.html", error=error_msg) # [cite: 2]

@app.route("/encrypt", methods=["POST"])
def encrypt_message():
    """Handles message encryption requests.""" # [cite: 2]
    try:
        message = request.form.get("message", "").strip() # [cite: 2]
        if not message: # [cite: 2]
            raise ValueError("Message cannot be empty.") # [cite: 2]
        public_key_e = int(request.form.get("public_key_e", "0")) # [cite: 2]
        public_key_n = int(request.form.get("public_key_n", "0")) # [cite: 3]
        if public_key_e <= 0 or public_key_n <= 0: # [cite: 3]
            raise ValueError("Public key values are invalid.") # [cite: 3]
        
        ciphertext = encrypt(message, (public_key_e, public_key_n)) # [cite: 3]
        return render_template("result.html", operation="Encryption", result=ciphertext, success=True) # [cite: 3]
    except Exception as ex: # [cite: 3]
        return render_template("result.html", operation="Encryption", result=str(ex), success=False) # [cite: 3]

@app.route("/decrypt", methods=["GET", "POST"])
def decrypt_message():
    """Handles message decryption requests.""" # [cite: 3]
    if request.method == "GET": # [cite: 3]
        # Show the decryption form on GET request # [cite: 3]
        return render_template("decrypt.html") # [cite: 3]
    
    # Process the form submission on POST request # [cite: 4]
    try:
        ciphertext = request.form.get("ciphertext", "").strip() # [cite: 4]
        if not ciphertext: # [cite: 4]
            raise ValueError("Ciphertext cannot be empty.") # [cite: 4]
        private_key_d = int(request.form.get("private_key_d", "0")) # [cite: 4]
        private_key_n = int(request.form.get("private_key_n", "0")) # [cite: 4]
        if private_key_d <= 0 or private_key_n <= 0: # [cite: 4]
            raise ValueError("Private key values are invalid.") # [cite: 4]

        plaintext = decrypt(ciphertext, (private_key_d, private_key_n)) # [cite: 5]
        return render_template("result.html", operation="Decryption", result=plaintext, success=True) # [cite: 5]
    except Exception as ex: # [cite: 5]
        return render_template("result.html", operation="Decryption", result=str(ex), success=False) # [cite: 5]

if __name__ == "__main__": # [cite: 5]
    # Runs the Flask development server # [cite: 5]
    # Debug=True allows for automatic reloading and provides detailed error pages # [cite: 5]
    app.run(debug=True) # [cite: 5]