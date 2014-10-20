from django.db import models

class Tour(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    departure = models.DateField('Дата отправления')
    arrive = models.DateField('Дата прибытия')
    cost = models.IntegerField()
    def __str__(self):
        return self.title

class Claim(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.EmailField()
    tour = models.ForeignKey(Tour)

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "images/")
    thumbnail = models.ImageField(upload_to = "images_thumb/")
    text = models.TextField(blank = True)
    def __str__(self):
        return self.title
    def admin_image(self):
        if (self.thumbnail):
            return '<img src="%s" width="100" height="100" />' % self.thumbnail.url
        else:
            return ''
    admin_image.allow_tags = True
    admin_image.short_description = 'Image'

class Carousel(models.Model):
    image = models.ForeignKey(Image)
    def carousel_image(self):
        return '<img src="%s" width="100" height="100" />' % self.image.thumbnail.url
    carousel_image.allow_tags = True
    def title(self):
        return self.image.title