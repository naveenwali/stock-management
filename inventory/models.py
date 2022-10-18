from django.db import models

# Create your models here.

class Employee(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Units(models.Model):
	name = models.CharField(max_length=10,unique=True)

	def __str__(self):
		return self.name

class Supplier(models.Model):
	name = models.CharField(max_length=20)
	
	def __str__(self):
		return self.name

class Items(models.Model):
	code = models.CharField(max_length=20,unique=True)
	name = models.CharField(max_length=50)
	image = models.ImageField()
	date = models.DateTimeField()
	supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE)
	emp = models.ForeignKey(Employee,on_delete=models.CASCADE)
	unit = models.ForeignKey(Units,on_delete=models.CASCADE)

	def __str__(self):
		return self.code
