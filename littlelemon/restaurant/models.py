from django.db import models
import datetime

# Create your models here.
class Booking(models.Model):
    TableID=models.IntegerField()
    Name=models.CharField(max_length=255)
    No_of_guests=models.IntegerField()
    BookingDate=models.DateField(default=datetime.date.today)

class Menu(models.Model):
    MenuID=models.IntegerField()
    Title=models.CharField(max_length=255)
    Price=models.DecimalField(max_digits=10,decimal_places=2)
    Inventory=models.IntegerField()
