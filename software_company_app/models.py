from django.db import models

class Error(models.Model):
    code = models.CharField(max_length=50)
    description = models.TextField()
    date_received = models.DateField()
    error_level = models.CharField(max_length=20)
    functionality_category = models.CharField(max_length=50)
    source = models.CharField(max_length=50)

class Programmer(models.Model):
    code = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

class ErrorCorrection(models.Model):
    correction_code = models.CharField(max_length=50)
    error_code = models.CharField(max_length=50)
    start_date = models.DateField()
    correction_period = models.IntegerField()
    programmer = models.ForeignKey(Programmer, on_delete=models.CASCADE)
    cost_per_day = models.DecimalField(max_digits=10, decimal_places=2)
