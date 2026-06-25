from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hi, Flask"

@app.route("/about")
def about():
    return "About Page"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({
            "error": "No JSON data provided"
        }), 400

    if "age" not in data:
        return jsonify({
            "error": "Age is required"
        }), 400

    if not isinstance(data["age"], int):
        return jsonify({
            "error": "Age must be a number"
        }), 400

    age = data["age"]

    if age < 0 or age > 100:
        return jsonify({
            "error": "Age must be between 0 and 100"
        }), 400

    if age < 18:
        result = "child"
    else:
        result = "adult"

    return jsonify({
        "prediction": result
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)