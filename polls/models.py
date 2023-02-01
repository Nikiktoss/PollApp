from django.contrib.auth.models import User
from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title")
    topic = models.TextField(verbose_name="Topic of the poll")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name="Date of publishing")
    last_modified = models.DateTimeField(auto_now=True, verbose_name="Last modified")
    is_active = models.BooleanField(default=True, verbose_name="Is still active")

    def __str__(self):
        return self.title


class Choice(models.Model):
    choice_text = models.TextField(verbose_name="Text")
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} selected {self.choice} in {self.poll} "
