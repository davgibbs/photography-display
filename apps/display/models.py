from django.db import models


def directory_path(file_name):
    # File will be saved to MEDIA_ROOT/upload_photos/<filename>
    return 'upload_photos/{0}'.format(filename)


class Photo(models.Model):
    image = models.ImageField(upload_to='upload_photos/')

