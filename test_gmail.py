import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64
import pdb

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

def send_email(to_email: str, subject: str, body: str) -> None:
    """
    Send an email using Gmail API.

    Args:
        to_email (str): Recipient email address
        subject (str): Email subject
        body (str): Email body (plain text)
    """
        
    print("CALLED: send_email(to_email: str, subject: str, body: str) -> None:")
    creds = None


    # Load saved tokens if available
    credentials_path = "./.gmail-mcp/credentials.json"
    token_path = "./.gmail-mcp/token.json"
    pdb.set_trace()
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
        print("token found")

     # If no valid creds, go through OAuth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
            print("Credential file found")
        # Save token for next time
        with open(token_path, "w") as token_file:
            token_file.write(creds.to_json())

    # Build Gmail service
    service = build("gmail", "v1", credentials=creds)

    # Create email message
    message = MIMEText(body)
    message["to"] = to_email
    message["from"] = "me"
    message["subject"] = subject
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    # Send the email
    send_result = service.users().messages().send(
        userId="me", body={"raw": raw_message}
    ).execute()
    print(f"Send Result: {send_result}")

send_email("gitesh.grover@gmail.com", "TEst Subject", "Test Body")