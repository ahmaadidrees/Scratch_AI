from flask import Flask, request, jsonify, send_file
from converter import convert_to_scratch
import io

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    print("Received a request")  # Debug print
    ai_code = request.json.get('code')
    print(f"Received code: {ai_code}")  # Debug print
    if not ai_code:
        print("No code provided")  # Debug print
        return jsonify({"error": "No code provided"}), 400
    
    try:
        scratch_project = convert_to_scratch(ai_code)
        print(f"Converted project size: {len(scratch_project)} bytes")  # Debug print
        
        # Create a BytesIO object from the scratch_project bytes
        project_file = io.BytesIO(scratch_project)
        
        print("Sending file")  # Debug print
        # Send the file
        return send_file(
            project_file,
            mimetype='application/x-zip-compressed',
            as_attachment=True,
            download_name='scratch_project.sb3'  # Changed from attachment_filename to download_name
        )
    except Exception as e:
        print(f"Error occurred: {str(e)}")  # Debug print
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)