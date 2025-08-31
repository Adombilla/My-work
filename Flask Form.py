from flask import Flask, request, render_template

app = Flask(__name__)

storage = {"latest": None}

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/save", methods=["POST"])
def save():
    text = request.form.get("user_text")
    if text:
        storage["latest"] = text
        return f"Text saved successfully: {text}"
    return "No text provided!"

@app.route("/get", methods=["GET"])
def get_text():
    if storage["latest"]:
        return f"Latest saved text: {storage['latest']}"
    return "No text has been saved yet."

if __name__ == "__main__":
    app.run(debug=True)