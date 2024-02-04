import requests

def send_line_notification(message):
    url = "http://0.0.0.0:8123/send-line-notification/"

    data = {"message": message}
    
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        print("Notification sent successfully")
    except requests.exceptions.RequestException as e:
        print(f"Error sending notification: {e}")

if __name__ == "__main__":
    message_to_send = "Hello, this is a Line notification!"
    send_line_notification(message_to_send)