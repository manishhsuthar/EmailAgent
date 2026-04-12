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

from imapclient import IMAPClient
import email
from email.header import decode_header
import os
from dotenv import load_dotenv

load_dotenv()  # ✅ THIS WAS MISSING

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

    print("DEBUG EMAIL:", USERNAME)   # optional
    print("DEBUG PASS:", PASSWORD)    # optional

    with IMAPClient(HOST) as server:
        server.login(USERNAME, PASSWORD)
        server.select_folder('INBOX')

        messages = server.search(['UNSEEN'])

        email_list = []

        for uid in messages[-5:]:
            raw = server.fetch([uid], ['BODY[]'])
            msg = email.message_from_bytes(raw[uid][b'BODY[]'])

            subject = decode_mime_words(msg.get('Subject', 'No Subject'))
            from_ = decode_mime_words(msg.get('From', 'Unknown'))

            email_list.append(f"{from_} - {subject}")

        return email_list