from imapclient import IMAPClient
import email
from email.header import decode_header

def decode_mime_words(s):
    decoded = decode_header(s)
    return ''.join(
        str(t[0], t[1] or 'utf-8') if isinstance(t[0], bytes) else t[0]
        for t in decoded
    )

def check_emails():
    HOST = 'imap.gmail.com'
    USERNAME = 'YOUR_EMAIL_ADDRESS'
    PASSWORD = 'YOUR_EMAIL_PASSWORD'

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