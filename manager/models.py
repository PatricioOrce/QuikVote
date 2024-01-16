from django.db import models

# Create your models here.
class Poll(models.Model):
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

class Option(models.Model):
    description = models.CharField(max_length=100)
    interactions = models.IntegerField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return self.description + ' - ' + self.poll.description