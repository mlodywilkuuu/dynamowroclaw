from flask import Flask

app = Flask(__name__)

# Definiujemy komponent ładowania jako czysty tekst HTML/CSS/JS
LADOWANIE_HTML = """
<style>
    #loader {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: #ffffff;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 9999;
        transition: opacity 0.6s ease, visibility 0.6s;
    }

    .loader-logo {
        width: 80px;
        height: auto;
        animation: pulse 1.5s infinite ease-in-out;
    }

    @keyframes pulse {
        0% { transform: scale(0.9); opacity: 0.7; }
        50% { transform: scale(1.1); opacity: 1; }
        100% { transform: scale(0.9); opacity: 0.7; }
    }

    .loader-hidden {
        opacity: 0;
        visibility: hidden;
    }
</style>

<div id="loader">
    <img src="static/FC-Dinamo-Wroclaw-1-32x32.png" alt="Dynamo Logo" class="loader-logo">
</div>

<script>
    window.addEventListener("load", function() {
        const loader = document.getElementById("loader");
        if (loader) {
            loader.classList.add("loader-hidden");
        }
    });
</script>
"""

@app.route('/')
def index():
    # Zwracamy loader oraz szkielet strony Dynamo
    return f"""
    <!DOCTYPE html>
    <html>
    <head><title>Dynamo Core</title></head>
    <body>
        {LADOWANIE_HTML}
        <div style="padding: 20px; text-align: center;">
            <div style="width: 100%; height: 200px; background: #eee; border: 2px solid #ccc;"></div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
