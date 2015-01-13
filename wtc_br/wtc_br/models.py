from django.db import models

class CommitMessage(models.Model):
    text = models.CharField(max_length=255)
    identifier = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        import hashlib

        if not self.identifier:
            m = hashlib.md5()
            m.update(self.text)
            self.identifier = u"{}".format(m.hexdigest())

        super(CommitMessage, self).save(*args, **kwargs)


    @classmethod
    def fetch_random_message(cls):
        import random
        return random.choice(cls.objects.all())

    @classmethod
    def fetch_message(cls, identifier):
        return cls.objects.get(identifier=identifier)
