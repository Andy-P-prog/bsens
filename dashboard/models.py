from django.db import models

# Create your models here.
def file_path(instance,filename):
    path = "media/"
    format = 'uploaded-'+filename
    return os.path.join(path,format)

class fileHandler(models.Model):
    file_upload = models.FileField(upload_to=file_path)

    def __str__(self):
        return str(self.file_upload)