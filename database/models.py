from django.db import models
from django.conf import settings

class Peak(models.Model):
    symbol = models.CharField(max_length=255)
    peak = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'peak'

class Valley(models.Model):
    symbol = models.CharField(max_length=255)
    valley = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'valley'

class Order_placed(models.Model):
    symbol = models.CharField(max_length=255)
    order_id = models.CharField(max_length=255)
    side = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.FloatField()
    limit = models.FloatField()
    stop = models.FloatField()

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'order_placed'


# class Teleconference_transcribe(models.Model):
#     filename = models.CharField(max_length=100)
#     transcription = models.TextField(max_length=500)
#     transcription_baseline = models.TextField(max_length=500)

#     def __str__(self):
#         return str(self.id)

#     class Meta:
#         db_table = "teleconference_transcribe"



# class Example(models.Model):
#     account_id = models.IntegerField()
#     session_id = models.IntegerField()
#     slice_probabilities = models.TextField(max_length=100)
#     response_time = models.CharField(max_length=100)
#     threshold = models.FloatField()
#     PHQ8 = models.IntegerField()
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return str(self.account_id)

#     class Meta:
#        



