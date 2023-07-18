from flask import Flask, request, jsonify

app = Flask("ping")

@app.route('/ping', methods=['POST'])
def ping():
    message = request.get_json()
    result = {
        "response":"Message received!"
        }
    
    return jsonify(result)

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=9010)

