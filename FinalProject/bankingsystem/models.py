from django.db import models
class Register(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    account=models.CharField(max_length=30,primary_key=True)
    password=models.CharField(max_length=100)
    amount=models.IntegerField()

    def __str__(self):
        return self.account

class Deposit(models.Model):
    account=models.ForeignKey(Register,on_delete=models.CASCADE)
    password=models.CharField(max_length=100)
    amount=models.IntegerField()

    def __str__(self):
        return self.account

class Comment(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    account=models.ForeignKey(Register,on_delete=models.CASCADE)
    comment=models.CharField(max_length=100)
    def __str__(self):
        return self.account

class WithDraw(models.Model):
    account=models.ForeignKey(Register,on_delete=models.CASCADE)
    password=models.CharField(max_length=100)
    amount=models.IntegerField()
    def __str__(self):
        return self.account

class Bill(models.Model):
    account=models.ForeignKey(Register,on_delete=models.CASCADE)
    password=models.CharField(max_length=100)
    amount=models.IntegerField()
    billno=models.IntegerField()
    def __str__(self):
        return self.account

class Total(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    account=models.ForeignKey(Register,on_delete=models.CASCADE)
    amount=models.IntegerField()

    def __str__(self):
        return self.account

class State(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    account=models.CharField(max_length=30)
    Status=models.CharField(max_length=30)

    def __str__(self):
        return self.Name