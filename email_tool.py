from imapclient import IMAPClient
import email
from email.header import decode_header
import os
from dotenv import load_dotenv

load_dotenv()

def get_last_uid():
    try:
        with open("last_uid.txt", "r") as f:
            return int(f.read().strip())
    except:
        return 0

def save_last_uid(uid):
    with open("last_uid.txt", "w") as f:
        f.write(str(uid))


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

        server.select_folder('INBOX', readonly=False)
        print("📂 Inbox selected")

        last_uid = get_last_uid()

        messages = server.search(['ALL'])[-50:]

        print("Last UID:", last_uid)
        print("All message IDs:", messages[:10])

        messages = [uid for uid in messages if uid > last_uid]

        print("📩 New messages:", messages)

        if not messages:
            print("✅ No new emails")
            return []

        raw_messages = server.fetch(messages, ['BODY.PEEK[HEADER]'])

        email_list = []
        max_uid = last_uid

        for uid, data in raw_messages.items():
            # IMAPClient stores fetched header bytes under BODY[HEADER] for BODY.PEEK[HEADER].
            raw_header = (
                data.get(b'BODY[HEADER]')
                or data.get(b'BODY[]')
                or data.get(b'RFC822')
            )
            if not raw_header:
                print(f"⚠️ Skipping UID {uid}: no header/body payload found in fetch response")
                continue

            msg = email.message_from_bytes(raw_header)

            subject = decode_mime_words(msg.get('Subject', 'No Subject'))
            from_ = decode_mime_words(msg.get('From', 'Unknown'))

            email_data = f"{from_} - {subject}"
            print("📧", email_data)

            email_list.append(email_data)

            server.add_flags(uid, ['\\Seen'])

            if uid > max_uid:
                max_uid = uid

        save_last_uid(max_uid)
        return email_list
