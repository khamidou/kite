import mailbox

def read_mail(path):
    mdir = mailbox.Maildir(path)
    return mdir

def extract_email(msg):
    """Extract all the interesting fields from an email"""
    msg_obj = {}
    msg_obj["from"] = msg.getheaders('From')[0]
    msg_obj["to"] = msg.getheaders('To')[0]
    msg_obj["subject"] = msg.getheaders('Subject')[0]
    msg_obj["date"] = msg.getheaders('Date')[0]
    msg_obj["contents"] = msg.fp.read()
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
    print "ID: %s, %s", (id, msg)
    return extract_email(msg)
