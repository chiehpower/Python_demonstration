from fastapi import FastAPI, HTTPException, Form
import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

app = FastAPI()

@app.post("/send-line-notification/")
async def send_line_notification(message: str = Form(...)):

    headers = {
        "Authorization": "Bearer " + TOKEN, 
    }

    files = {'imageFile': open("client_file.png", 'rb')}
    payload = {
        'message': 'Hi guys' 
    }
    r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=payload, files = files)
    # r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)

    print(f"Received Line notification: {message}")

    return {"status": "Notification sent successfully"}