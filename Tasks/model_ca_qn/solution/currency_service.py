from flask import Flask, jsonify, request

app = Flask(__name__)

USD_TO_INR = 83.0
INR_TO_USD = 1 / USD_TO_INR

@app.route("/convert", methods=["POST"])
def convert_currency():
    data = request.json
    amount = data.get("amount")
    from_currency = data.get("from_currency")
    to_currency = data.get("to_currency")

    if from_currency == "USD" and to_currency == "INR":
        converted = amount * USD_TO_INR
    elif from_currency == "INR" and to_currency == "USD":
        converted = amount * INR_TO_USD
    else:
        return jsonify({"error": "Unsupported conversion"}), 400

    return jsonify({
        "original_amount": amount,
        "from_currency": from_currency,
        "converted_amount": round(converted, 2),
        "to_currency": to_currency
    })

if __name__ == "__main__":
    app.run(port=5003, debug=True)
