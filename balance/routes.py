from balance import app

@app.route("/")
def inicio():
    return "Hello, World!"