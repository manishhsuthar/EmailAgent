from imapclient import IMAPClient
import email
from email.header import decode_header

import os
from dotenv import load_dotenv
load_dotenv()

def decode_mime_words(s):
    decoded = decode_header(s)
    return ''.join(
        str(t[0], t[1] or 'utf-8') if isinstance(t[0], bytes) else t[0]
        for t in decoded
    )

def check_emails():
    HOST = 'imap.gmail.com'
    USERNAME = os.getenv('EMAIL')
    PASSWORD = os.getenv('PASSWORD')

    if not USERNAME or not PASSWORD:
        raise ValueError("Missing EMAIL or PASSWORD in environment variables")

    with IMAPClient(HOST) as server:
        print("➡️ Connecting to server...")
        server.login(USERNAME, PASSWORD)
        print("✅ Logged in")

        server.select_folder('INBOX', readonly=True)
        print("📂 Inbox selected")

        messages = server.search(['UNSEEN'])[-5:] 
        print("📩 Latest unread messages:", messages)

        if not messages:
            print("✅ No unread emails")
            return []

        email_list = []

        raw_messages = server.fetch(messages, ['BODY[]'])

        for uid, data in raw_messages.items():
            msg = email.message_from_bytes(data[b'BODY[]'])

            subject = decode_mime_words(msg.get('Subject', 'No Subject'))
            from_ = decode_mime_words(msg.get('From', 'Unknown'))

            email_data = f"{from_} - {subject}"
            print("📧", email_data)

            email_list.append(email_data)

        return email_list