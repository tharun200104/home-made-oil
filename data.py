from flask import Flask, request

app = Flask(__name__)

# Variable to store client datan
client_data = {}

# Endpoint to receive user input
@app.route('/store-data', methods=['POST'])
def store_data():
    data = request.form
    client_data['name'] = data.get('name')
    client_data['phone'] = data.get('phone')
    client_data['email'] = data.get('email')
    # Add more fields as needed
    
    return 'Data stored successfully'

if __name__ == '__main__':
    app.run(debug=True)
