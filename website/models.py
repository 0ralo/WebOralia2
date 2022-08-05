from django.db import models


class Skill(models.Model):
	name = models.CharField(max_length=32)
	percent = models.SmallIntegerField()

	class Meta:
		verbose_name = "Skill"
		verbose_name_plural = "Skills"

