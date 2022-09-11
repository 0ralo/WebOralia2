from django.db import models


class Person(models.Model):
	name = models.CharField(max_length=20)
	age = models.SmallIntegerField(default=0)
	gender = models.IntegerField(choices=((1, "Male"), (2, "Female"), (0, "Undefined")), default=0)

	class Meta:
		verbose_name = "Человек"
		verbose_name_plural = "Люди"


class Employee(Person):
	stage = models.IntegerField(default=0)

	class Meta:
		verbose_name = "Работник"
		verbose_name_plural = "Работники"
