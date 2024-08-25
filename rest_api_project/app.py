from flask import Flask, request, jsonify

app = Flask(__name__)

# GET method route
@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

# POST method route
@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.json.get("data", [])
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        highest_lowercase = max([char for char in alphabets if char.islower()], default="")
        
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",  # Replace with your actual full name and DOB
            "email": "john@xyz.com",  # Replace with your actual email
            "roll_number": "ABCD123",  # Replace with your actual roll number
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else []
        }
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
