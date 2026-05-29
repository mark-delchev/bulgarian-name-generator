from flask import Flask, render_template, jsonify
import generator

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    name = generator.generate_name()
    return jsonify({"name": name})

if __name__ == "__main__":
    app.run(debug=True)