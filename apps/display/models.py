from django.db import models


class Photo(models.Model):
    image = models.ImageField(upload_to='upload_photography/')  # File will be saved to MEDIA_ROOT/<upload_to><filename>
