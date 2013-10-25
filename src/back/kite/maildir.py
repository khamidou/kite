import mailbox

def read_mail(path):
    mdir = mailbox.Maildir(path)
    return mdir

def get_mails(mdir):
    l = []
    count = 0
    for id, msg in mdir.iteritems():
        msg_obj = {}
        msg_obj["from"] = msg.getheaders('From')[0]
        msg_obj["to"] = msg.getheaders('To')[0]
        msg_obj["subject"] = msg.getheaders('Subject')[0]
        msg_obj["contents"] = msg.fp.read()
        msg_obj["id"] = count
        count += 1
        l.append(msg_obj)
    return l


    
