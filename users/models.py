from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)


    def __str__(self):
        return self.email



class TravellerDetails(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    seatNumber = models.CharField(max_length=40)
    age = models.IntegerField()
    gender = models.CharField(max_length=40)
    fare = models.IntegerField()
    etstNumber = models.CharField(max_length=40)
    seatStatus = models.CharField(max_length=40)


class TicketDetails(models.Model):
    etstnum = models.CharField(max_length=40)
    pnrnum = models.CharField(max_length=40)
    ticketStatus = models.CharField(max_length=40)
    ticketdump = models.CharField(max_length=40)

