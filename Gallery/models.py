from django.db import models
from django.contrib.auth.models import User
import hashlib
import uuid
# Create your models here.
def hash_password(password):
	salt = uuid.uuid4().hex
	return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(hashed_password,user_password):
	password,salt = hashed_password.split(':')
	return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

# Create your models here.

class user(models.Model):
	username = models.CharField(max_length=20)
	email_id = models.CharField(max_length=50,unique=True,primary_key=True)
	password = models.CharField(max_length=512)

	def __str__(self):
		return (self.username)

	@classmethod
	def checkUserExists(cls,email_id):
		s = cls.objects.filter(email_id=email_id)
		if s:
			return 1
		else:
			return 0

	@classmethod
	def registerUser(cls,username,email_id,password):
		try:
			if cls.checkUserExists(email_id):
				return -1
			else:
				#password = hash_password(password)
				u = cls(username=username,email_id=email_id,password=password)
				u.save()
				return u
		except Exception as e:
			return e

	@classmethod
	def loginUser(cls,email_id,password):
		s = cls.objects.filter(email_id=email_id)
		if s:
			if s[0].password==password:

				return s[0]
			else:
				return -1
		else:
			return -1

class Gallery(models.Model):
	name = models.CharField(max_length =60)
	image = models.ImageField(null=True,blank=True)



	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
		     self._imageURL
		except:
			url = ''
		return url




