from django.db import models
import uuid

class Model(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        abstract = True

from django_extensions.db.models import (
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel
)

class Contact(
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel,
	Model
	):

	class Meta:
		verbose_name_plural = "Contacts"

	email = models.EmailField(verbose_name="Email")

	def __str__(self):
		return f'{self.title}'