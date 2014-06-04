import mailbox
import quopri
import email.utils
import lxml.html.clean
import re

def read_mail(path):
    mdir = mailbox.Maildir(path)
    return mdir

def extract_email_headers(msg):
    """Extract headers from email"""

    msg_obj = {}
    msg_obj["from"] = {}
    from_field = msg.getheaders('From')[0]
    msg_obj["from"]["name"], msg_obj["from"]["address"] = email.utils.parseaddr(from_field)
    msg_obj["to"] = email.utils.getaddresses(msg.getheaders('To'))
    

    msg_obj["subject"] = msg.getheaders('Subject')[0]
    msg_obj["date"] = msg.getheaders('Date')[0]

    return msg_obj

def format_plaintext_email(message):
    """Replace \n by <br> to display as HTML"""
    return message.replace('\n', '<br>')

def extract_email(msg):
    """Extract all the interesting fields from an email"""
    msg_obj = extract_email_headers(msg)
    
    fpPos = msg.fp.tell()
    msg.fp.seek(0)
    mail = email.message_from_string(msg.fp.read())
    contents = []
    for part in mail.walk():
        if part.get_content_type() == 'text/plain':
            charset = part.get_content_charset()

            if charset != None:
                payload = quopri.decodestring(part.get_payload()).decode(charset)
            else: # assume ascii
                payload = quopri.decodestring(part.get_payload()).decode('ascii')

            payload = format_plaintext_email(payload)
            contents.append(payload)

    content = "".join(contents)
    msg_obj["contents"] = lxml.html.clean.clean_html(content).encode('utf-8')
    return msg_obj

def get_emails(mdir):
    l = []
    for id, msg in mdir.iteritems():
        msg_obj = extract_email(msg)
        msg_obj["id"] = id
        l.append(msg_obj)
    return l

def get_email(mdir, id):
    msg = mdir.get(id)
    return extract_email(msg)
