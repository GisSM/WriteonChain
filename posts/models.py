from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone
import hashlib
from .utils import send_transaction


class Post(models.Model):
    utente=models.ForeignKey(User, on_delete=models.CASCADE)
    titolo=models.CharField(max_length=120)
    testo=models.TextField()
    hash=models.CharField(max_length=32, blank=True, null=True)
    txId=models.CharField(max_length=66, blank=True, null=True, default='Invio transazione in corso...')
    data_creazione=models.DateTimeField(auto_now=False ,auto_now_add=True)
    data_pubblicazione = models.DateTimeField(blank=True, null=True)
    slug=models.SlugField()

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'id':self.id,'slug':self.slug})

    def save(self):
        if not self.data_pubblicazione:
            self.data_pubblicazione=timezone.now()
        self.slug = slugify(self.titolo)
        return super().save()

    def pubblished(self):
        self.data_pubblicazione = timezone.now()
        self.save()

    def write_on_chain(self):
        self.hash=hashlib.sha256(self.testo.encode('utf-8')).hexdigest()
        self.txId=send_transaction(self.hash)
        self.save()


