from django.db import models

# Create your models here.

class Guest(models.Model):
    gid = models.IntegerField(primary_key=True)
    gname = models.CharField(max_length=50)
    gemail = models.EmailField(unique=True)
    gmob_no = models.BigIntegerField(unique=True)
    gid_proof = models.BigIntegerField(unique=True)
    address = models.TextField()
    gl_password = models.CharField(max_length=100 , default=gid_proof)
    
    def __str__(self):
        return self.gname

class Room(models.Model):
    rid = models.IntegerField(primary_key=True)
    room_no = models.IntegerField()
    room_type = models.CharField(max_length=20)
    
    price_per_day = models.BigIntegerField()
    
    def __str__(self):
        return self.room_type
    
class Booking(models.Model):
    bid = models.IntegerField(primary_key=True)
    gid = models.ForeignKey(Guest , on_delete=models.CASCADE)
    rid = models.ForeignKey( Room , on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    total_day = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=50 , default="Not Book")

    def __str__(self):
        return self.status
    
class Payment(models.Model):
    pid = models.AutoField(primary_key=True)
    bid = models.ForeignKey(Booking, on_delete=models.CASCADE)
    rid = models.ForeignKey(Room, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_mode = models.CharField(max_length=50)
    paid = models.CharField(max_length=10)
    payment_date = models.DateField()
    
    def __str__(self):
        return self.paid
    
    