from flask import Flask, jsonify

app = Flask(__name__)

# Function to get the latest coordinates
def get_latest_coordinates():
    try:
        with open("coordinates.txt", "r") as file:
            lines = file.readlines()
            if lines:  # Ensuring the file is not empty
                lat, lon = map(float, lines[-1].strip().split(","))  # Read last line
                return {"latitude": lat, "longitude": lon}
    except Exception as e:
        import sys
        print("Error reading coordinates:", e, file=sys.stderr)
    return {"latitude": 0, "longitude": 0}  # Default if error

@app.route('/location', methods=['GET'])
def location():
    return jsonify(get_latest_coordinates())  # Always get the latest data

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
