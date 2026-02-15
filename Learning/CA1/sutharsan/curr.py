from flask import Flask,request,jsonify
import logging

# logging.basicConfig(
#     filename = "app.log",
#     level = logging.INFO,
#     format = "%(asctime)s - %(levelname)s - %(message)s"
# )

app = Flask(__name__)



@app.route('/currency',methods = ["POST"])
def convert():
    data = request.get_json()
    
    print(data)

    currency = str(data.get('currency'))
    price = int(data.get('price'))

    if currency == "ruppess":
        #logging.info("Currency is converted from ruppees to dollars")
        return jsonify({"converted":price * 1})
    elif  currency == "dollars":
        #logging.info("Currency is converted from dollars to ruppees")
        return jsonify({"converted": price*2 })
    
    return 0



app.run(port = 5002 ,debug=True)