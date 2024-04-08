from flask import Flask,jsonify  # Import the Flask class
app = Flask(__name__)    # Create an instance of the class for our use

@app.route("/", methods=["GET"])
def say_hello():
    return jsonify({"msg": "Hello from Flask"})

if __name__ == "__main__":
    app.run(debug=True)