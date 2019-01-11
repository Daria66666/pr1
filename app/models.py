from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=50)
    currency = models.CharField(max_length=50)
    value = models.FloatField(default=0)
    notes = models.CharField(max_length=150)

class Incomes(models.Model):
    name = models.CharField(max_length=50)
    acc = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.FloatField(default=0)
    category = models.CharField(max_length=50)
    notes = models.CharField(max_length=150)

class Expenses(models.Model):
    name = models.CharField(max_length=50)
    acc = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.FloatField(default=0)
    category = models.CharField(max_length=50)
    rate = models.IntegerField(default=0)
    place = models.CharField(max_length=50)
    notes = models.CharField(max_length=150)

class Transfers(models.Model):
    name = models.CharField(max_length=50)
    acc = models.ManyToManyField(Account)
    date = models.DateField()
    value = models.FloatField(default=0)
    notes = models.CharField(max_length=150)

class Saved(models.Model):
    acc = models.ForeignKey(Account, on_delete=models.CASCADE)
    value = models.FloatField(default=0)
    date1 = models.DateField()
    date2 = models.DateField()
    surcharge = models.FloatField(default=0)

class Goals(models.Model):
    name = models.CharField(max_length=50)
    value = models.FloatField(default=0)
    surcharge = models.FloatField(default=0)
    description = models.CharField(max_length=500)
    image = models.ImageField()

