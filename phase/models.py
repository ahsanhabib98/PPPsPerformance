from django.db import models

# Create your models here.

class PhaseCategory(models.Model):
	name = models.CharField(max_length=100)

	class Meta:
		ordering = ['id']

	def __str__(self):
		return self.name



class PhaseSubCategory(models.Model):
	name = models.CharField(max_length=100)
	category = models.ForeignKey(PhaseCategory, null=True, blank=True, on_delete=models.SET_NULL)
	parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)

	class Meta:
		ordering = ['id']

	def __str__(self):
		return self.name

	@property
	def child(self):
		return PhaseSubCategory.objects.filter(parent=self)

