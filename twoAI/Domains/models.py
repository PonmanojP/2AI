from django.db import models

class DeletedItem(models.Model):
    Announcement1 = models.TextField(max_length=300)
    Announcement2 = models.TextField(max_length=300)
    Announcement3 = models.TextField(max_length=300)
    Link_text_1 = models.TextField(max_length=100)
    Link_1 = models.URLField(null=False)
    Link_text_2 = models.TextField(max_length=100)
    Link_2 = models.URLField(null=False)
    Link_text_3 = models.TextField(max_length=100)
    Link_3 = models.URLField(null=False)
    Link_text_4 = models.TextField(max_length=100)
    Link_4 = models.URLField(null=False)
    def __str__(self):
        return f'Deleted Item : {self.Announcement1}'

class ML(models.Model):
    Announcement1 = models.TextField(max_length=300)
    Announcement2 = models.TextField(max_length=300)
    Announcement3 = models.TextField(max_length=300)
    Link_text_1 = models.TextField(max_length=100)
    Link_1 = models.URLField(null=False)
    Link_text_2 = models.TextField(max_length=100)
    Link_2 = models.URLField(null=False)
    Link_text_3 = models.TextField(max_length=100)
    Link_3 = models.URLField(null=False)
    Link_text_4 = models.TextField(max_length=100)
    Link_4 = models.URLField(null=False)
    def __str__(self):
        return f'ML : {self.Announcement1}'

class DL(models.Model):
    Announcement1 = models.TextField(max_length=300)
    Announcement2 = models.TextField(max_length=300)
    Announcement3 = models.TextField(max_length=300)
    Link_text_1 = models.TextField(max_length=100)
    Link_1 = models.URLField(null=False)
    Link_text_2 = models.TextField(max_length=100)
    Link_2 = models.URLField(null=False)
    Link_text_3 = models.TextField(max_length=100)
    Link_3 = models.URLField(null=False)
    Link_text_4 = models.TextField(max_length=100)
    Link_4 = models.URLField(null=False)
    def __str__(self):
        return f'DL : {self.Announcement1}'

class Bigdata(models.Model):
    Announcement1 = models.TextField(max_length=300)
    Announcement2 = models.TextField(max_length=300)
    Announcement3 = models.TextField(max_length=300)
    Link_text_1 = models.TextField(max_length=100)
    Link_1 = models.URLField()
    Link_text_2 = models.TextField(max_length=100)
    Link_2 = models.URLField()
    Link_text_3 = models.TextField(max_length=100)
    Link_3 = models.URLField()
    Link_text_4 = models.TextField(max_length=100)
    Link_4 = models.URLField()
    def __str__(self):
        return f'Bigdata : {self.Announcement1}'

class Vision(models.Model):
    Announcement1 = models.TextField(max_length=300)
    Announcement2 = models.TextField(max_length=300)
    Announcement3 = models.TextField(max_length=300)
    Link_text_1 = models.TextField(max_length=100)
    Link_1 = models.URLField(null=False)
    Link_text_2 = models.TextField(max_length=100)
    Link_2 = models.URLField(null=False)
    Link_text_3 = models.TextField(max_length=100)
    Link_3 = models.URLField(null=False)
    Link_text_4 = models.TextField(max_length=100)
    Link_4 = models.URLField(null=False)
    def __str__(self):
        return f'Vision : {self.Announcement1}'

class Cloud(models.Model):
    Announcement1 = models.TextField(max_length=300)
    Announcement2 = models.TextField(max_length=300)
    Announcement3 = models.TextField(max_length=300)
    Link_text_1 = models.TextField(max_length=100)
    Link_1 = models.URLField(null=False)
    Link_text_2 = models.TextField(max_length=100)
    Link_2 = models.URLField(null=False)
    Link_text_3 = models.TextField(max_length=100)
    Link_3 = models.URLField(null=False)
    Link_text_4 = models.TextField(max_length=100)
    Link_4 = models.URLField(null=False)
    def __str__(self):
        return f'Cloud : {self.Announcement1}'

class Edge(models.Model):
    Announcement1 = models.TextField(max_length=300)
    Announcement2 = models.TextField(max_length=300)
    Announcement3 = models.TextField(max_length=300)
    Link_text_1 = models.TextField(max_length=100)
    Link_1 = models.URLField(null=False)
    Link_text_2 = models.TextField(max_length=100)
    Link_2 = models.URLField(null=False)
    Link_text_3 = models.TextField(max_length=100)
    Link_3 = models.URLField(null=False)
    Link_text_4 = models.TextField(max_length=100)
    Link_4 = models.URLField(null=False)
    def __str__(self):
        return f'Edge : {self.Announcement1}'

class Design(models.Model):
    Announcement1 = models.TextField(max_length=300)
    Announcement2 = models.TextField(max_length=300)
    Announcement3 = models.TextField(max_length=300)
    Link_text_1 = models.TextField(max_length=100)
    Link_1 = models.URLField(null=False)
    Link_text_2 = models.TextField(max_length=100)
    Link_2 = models.URLField(null=False)
    Link_text_3 = models.TextField(max_length=100)
    Link_3 = models.URLField(null=False)
    Link_text_4 = models.TextField(max_length=100)
    Link_4 = models.URLField(null=False)
    def __str__(self):
        return f'Design : {self.Announcement1}'

class NLP(models.Model):
    Announcement1 = models.TextField(max_length=300)
    Announcement2 = models.TextField(max_length=300)
    Announcement3 = models.TextField(max_length=300)
    Link_text_1 = models.TextField(max_length=100)
    Link_1 = models.URLField(null=False)
    Link_text_2 = models.TextField(max_length=100)
    Link_2 = models.URLField(null=False)
    Link_text_3 = models.TextField(max_length=100)
    Link_3 = models.URLField(null=False)
    Link_text_4 = models.TextField(max_length=100)
    Link_4 = models.URLField(null=False)
    def __str__(self):
        return f'NLP : {self.Announcement1}'

class Web(models.Model):
    Announcement1 = models.TextField(max_length=300)
    Announcement2 = models.TextField(max_length=300)
    Announcement3 = models.TextField(max_length=300)
    Link_text_1 = models.TextField(max_length=100)
    Link_1 = models.URLField(null=False)
    Link_text_2 = models.TextField(max_length=100)
    Link_2 = models.URLField(null=False)
    Link_text_3 = models.TextField(max_length=100)
    Link_3 = models.URLField(null=False)
    Link_text_4 = models.TextField(max_length=100)
    Link_4 = models.URLField(null=False)
    def __str__(self):
        return f'Web : {self.Announcement1}'


