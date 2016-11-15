from django.db import models

# Create your models here.


class Professor(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    
    def __str__(self):
        return '%s %s' % (self.firstName, self.lastName)
    


class Rating(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)    
    rating0 = models.IntegerField()
    rating1 = models.IntegerField()
    def __str__(self):
        return '%s Rating' % (self.professor)
