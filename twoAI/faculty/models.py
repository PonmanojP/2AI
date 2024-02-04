from django.db import models

class Faculty(models.Model):
    No = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    photo = models.ImageField(upload_to='faculty/images/')
    position = models.CharField(max_length = 100)
    experience = models.IntegerField()
    description = models.CharField(max_length=1000)
    officiallink = models.URLField()

    def __str__(self):
        return f'{self.name}'
