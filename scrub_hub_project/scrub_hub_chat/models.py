from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

class ConversationParticipant(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	# This will hold the conversation's symmetric key, encrypted with the user's public asymetric key.
	encrypted_key = models.BinaryField(max_length=50, blank=True) # ??? length TODO (this field isn't used at all yet)

class Conversation(models.Model):
	participants = models.ManyToManyField(to=ConversationParticipant)
	start_date = models.DateTimeField("date of first message", default=timezone.now)
	last_message_date = models.DateTimeField(
		"date of most recent message",
		null=True,
	)
