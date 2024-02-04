from fastapi import FastAPI, HTTPException, Form
import requests

app = FastAPI()

@app.post("/send-line-notification/")
async def send_line_notification(message: str = Form(...)):

    # key_ = ''
    # headers = {
    #     "Authorization": "Bearer " + key_, 
    #     "Content-Type" : "application/x-www-form-urlencoded"
    # }

    # payload = {
    #     'message': 'Hi guys' 
    # }

    # r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)

    print(f"Received Line notification: {message}")

    return {"status": "Notification sent successfully"}