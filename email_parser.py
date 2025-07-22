import os
from email import policy
from email.parser import BytesParser

def parse_email_file(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    if ext == '.eml':
        with open(filepath, 'rb') as f:
            msg = BytesParser(policy=policy.default).parse(f)
        subject = msg['subject'] or ''
        if msg.is_multipart():
            body = ''
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    body += part.get_content()
        else:
            body = msg.get_content()
        return subject, body
    else:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        return '', content 