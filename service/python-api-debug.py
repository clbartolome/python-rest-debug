from flask import Flask, request

app = Flask(__name__)

@app.route('/debug', methods=['POST', 'GET', 'PUT'])
def print_payload():
    # Get the JSON payload from the request
    data = request.get_json()
    
    # Print the received payload
    print(data)
    
    # Return a response
    return "Payload received and printed", 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)