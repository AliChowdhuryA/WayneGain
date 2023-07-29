from flask import Flask, request, jsonify

app = Flask(__name__)

# Dictionary of stretches organized by muscle group
stretches_by_muscle = {
    "neck": ["Neck Side Stretch", "Neck Flexion Stretch", "Neck Extension Stretch"],
    "shoulders": ["Shoulder Stretch", "Shoulder Cross-Body Stretch", "Shoulder Circles"],
    "hamstrings": ["Standing Hamstring Stretch", "Seated Hamstring Stretch", "Lying Hamstring Stretch"],
    "quadriceps": ["Standing Quadriceps Stretch", "Seated Quadriceps Stretch", "Lying Quadriceps Stretch"],
    "calves": ["Standing Calf Stretch", "Seated Calf Stretch", "Wall Calf Stretch"],
    "lower back": ["Child's Pose", "Cat-Cow Stretch", "Seated Spinal Twist"],
    "chest": ["Chest Opener Stretch", "Chest Stretch Against a Wall", "Seated Chest Stretch"],
    "hip flexors": ["Standing Hip Flexor Stretch", "Kneeling Hip Flexor Stretch", "Lunges"],
    "triceps": ["Overhead Triceps Stretch", "Triceps Stretch with Bent Arm", "Triceps Stretch with Towel"],
    "glutes": ["Piriformis Stretch", "Seated Glute Stretch", "Supine Glute Stretch"],
}


@app.route('/api/get_stretches', methods=['POST', 'GET'])
def get_stretches():
    if request.method == 'POST':
        data = request.get_json()
        username = data['username']
        muscle = data['muscle']
        return handle_stretch_request(muscle)
    else:
        #if req in url
        muscle = request.args.get('muscle')
        if muscle is not None:
            return handle_stretch_request(muscle)
        #use text fields in webpage
        else:
            return '''<form method="get">
                    <label for="username">Enter your username:</label>
                    <input type="text" id="username" name="username">
                    <label for="muscle">Enter a muscle (e.g., hamstrings, shoulders):</label>
                    <input type="text" id="muscle" name="muscle">
                    <input type="submit" value="Submit">
                </form>'''





def handle_stretch_request(muscle):
    if muscle in stretches_by_muscle:
        stretches = stretches_by_muscle[muscle]
        response_message = f"Here are some stretches for {muscle}:"
        response_data = {'message': response_message, 'stretches': stretches}
        # Formats the json response for better readability
        return jsonify(response_data), 200, {'Content-Type': 'application/json; charset=utf-8'}
    else:
        return jsonify({'error': 'Muscle not found. Please provide a valid muscle name.'}), 404


if __name__ == '__main__':
    app.run(port=5008,debug=True)
