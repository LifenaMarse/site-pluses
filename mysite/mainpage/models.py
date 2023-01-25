from django.db import models


class Skill(models.Model):
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title


class Demand(models.Model):
    title = models.CharField(max_length=255, blank=True)
    tableTitle = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title


class Geography(models.Model):
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title


class Pie(models.Model):
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title






