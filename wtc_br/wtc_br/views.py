from models import CommitMessage

def fetch_random_message(request):
    random_message = CommitMessage.fetch_random_message()

    ctx = {
        'permalink': u'{}'.format(message.permalink),
        'message': u'{}'.format(message.text),
    }

def fetch_message(request, id):
    message = CommitMessage.fetch_message(id=id)

    ctx = {
        'permalink': u'{}'.format(message.permalink),
        'message': u'{}'.format(message.text),
    }
