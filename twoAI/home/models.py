from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 250)
    image = models.ImageField(upload_to ='home/images/')
    url = models.URLField(blank = True)
    def __str__(self):
        return f'{self.title}'

class Announcement(models.Model):
    Enter_Title = models.CharField(max_length =50)
    Enter_Announcement = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.Enter_Title}'