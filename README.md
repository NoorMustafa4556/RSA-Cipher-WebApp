# RSA Cipher Web Application

This project is a web-based implementation of the RSA asymmetric encryption algorithm. It provides a user-friendly interface to generate public/private key pairs, encrypt messages with a public key, and decrypt them using the corresponding private key. The application is built with Python and Flask, demonstrating the core principles of modern cryptography in a practical, hands-on way.



## 🔑 Key Features

-   **Key Generation:** Dynamically generate unique public and private key pairs based on large prime numbers.
-   **Encryption:** Securely transform any plaintext message into ciphertext using a public key, ensuring the message is unreadable to anyone without the private key.
-   **Decryption:** Retrieve the original message from its ciphertext by using the correct private key.
-   **User-Friendly Interface:** A seamless and intuitive web interface built with Flask that simplifies the complex cryptographic process for the user.

## 🛠️ Implementation Details (Tech Stack)

-   **Backend & Cryptography:** **Python**
    -   Used for all cryptographic operations, including prime number generation, key creation, and the encryption/decryption logic.
-   **Web Framework:** **Flask**
    -   Used to create the web server, handle HTTP requests, and serve the user interface.
-   **Frontend:** **HTML & CSS**
    -   Used to structure and style the web pages for a clean and simple user experience.

## 🌐 Real-World Applications

The principles demonstrated in this project are the foundation for many modern security systems, including:
-   **Digital Signatures:** Verifying the authenticity and integrity of digital documents.
-   **Securing Online Communications:** Protecting data in transit, such as in TLS/SSL protocols for HTTPS.
-   **E-commerce & Secure Transactions:** Ensuring that financial information like credit card numbers is transmitted securely.

## 🚀 How to Run the Project Locally

To get a local copy up and running, follow these simple steps.

### Prerequisites

-   Python 3.x installed on your machine.
-   `pip` (Python package installer).

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/NoorMustafa4556/RSA-Cipher-WebApp
   
    ```

2.  **Create a virtual environment (Recommended):**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required packages:**
    You will need to install Flask. Create a `requirements.txt` file with the following content:
    ```txt
    Flask
    ```
    Then, run this command in your terminal:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask application:**
    ```bash
    python app.py 
    ```
    (Assuming your main Python file is named `app.py`)

5.  **Open in browser:**
    Navigate to `http://127.0.0.1:5000` in your web browser to use the application.

---
This project was developed to provide a clear and functional demonstration of the RSA encryption algorithm.
