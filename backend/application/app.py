from flask import Flask, request, jsonify
from json import dumps
from httplib2 import Http

app = Flask(__name__)


def send_message_to_chat(message):
    url = "https://chat.googleapis.com/v1/spaces/AAAA5nih20g/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=u1QimSgFxbdfxnHZ28eXFDKLrTQEgYWedYZ05bF6FTM"
    app_message = {"text": message}
    message_headers = {"Content-Type": "application/json; charset=UTF-8"}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method="POST",
        headers=message_headers,
        body=dumps(app_message),
    )
    return response


@app.route("/webhook", methods=["POST"])
def send_message():
    data = request.json
    post = data.get("post", {})
    post_id = post.get("id")
    username = post.get("username")
    created_at = post.get("created_at")
    raw_content = post.get("raw")
    response_message = f"Received post with ID {post_id} from user {username} at {created_at}.\n  Content: {raw_content}"
    send_message_to_chat(response_message)

    print("Message sent successfully")

    return jsonify({"status": "Message sent successfully"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5173)
