from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    debut_year = models.IntegerField()
    image = models.ImageField(upload_to='artists/', blank=True, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='albums/', blank=True, null=True)

    def __str__(self):
        return self.title