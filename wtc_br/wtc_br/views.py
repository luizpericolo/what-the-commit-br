from models import CommitMessage
from django.shortcuts import render_to_response

def fetch_random_message(request):
    message = CommitMessage.fetch_random_message()

    ctx = {
        'permalink': u'/{}/'.format(message.identifier),
        'message': u'{}'.format(message.text),
    }

    return render_to_response("index.html", ctx)

def fetch_message(request, id):
    message = CommitMessage.fetch_message(identifier=id)

    ctx = {
        'permalink': u'/{}/'.format(message.identifier),
        'message': u'{}'.format(message.text),
    }
    
    return render_to_response("index.html", ctx)
