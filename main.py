# ----------------------------
# main.py (Backend - Flask Server)
# ----------------------------

from flask import Flask, request, jsonify 
from flask_cors import CORS
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask is working!"

if __name__ == "__main__":
    app.run(debug=True)


app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Sample keyword-based responses for green campus chatbot
RESPONSES = {
    "recycle": "Recycle paper, plastic, and glass in designated blue bins around campus.",
    "waste": "Please use the compost bin for food waste and the recycling bin for plastics and metals.",
    "energy": "Turn off lights and electronic devices when not in use to conserve energy.",
    "water": "Report leaks and avoid wasting water. Use campus water refill stations.",
    "events": "The next sustainability event is 'Eco Awareness Week' starting on May 5th.",
    "transport": "Use bicycles, campus electric shuttles, or walk to reduce your carbon footprint.",
    "contact": "You can contact the Green Campus Office at greenoffice@university.edu."
}

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()

    for keyword, response in RESPONSES.items():
        if keyword in user_message:
            return jsonify({"response": response})

    return jsonify({"response": "I'm here to help with green campus initiatives. Ask me about recycling, events, transport, or sustainability tips!"})

if __name__ == "__main__":
    app.run(debug=True)

# ----------------------------
# index.html (Frontend - Simple Chat Interface)
# ----------------------------

# Save this part as index.html in the same folder:

"""
<!DOCTYPE html>
<html>
<head>
    <title>Green Campus Chatbot</title>
    <script>
        async function sendMessage() {
            const message = document.getElementById("message").value;
            const response = await fetch("http://localhost:5000/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ message: message })
            });
            const data = await response.json();
            document.getElementById("response").innerText = data.response;
        }
    </script>
</head>
<body>
    <h2>Green Campus Assistant</h2>
    <input type="text" id="message" placeholder="Ask a sustainability question...">
    <button onclick="sendMessage()">Send</button>
    <p id="response"></p>
</body>
</html>
"""