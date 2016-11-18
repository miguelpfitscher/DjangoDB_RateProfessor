from django.db import models
#from django.contrib.postgres.fields import ArrayField


class Professor(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
   # courses = ArrayField(
    #            models.CharField(max_length=200, blank=True)
    #            size=8,
    #        )
    course = models.CharField(max_length=200)
    university = models.CharField(max_length=200, default="UFSM")

    def __str__(self):
        return '%s %s' % (self.firstName, self.lastName)
    


class Rating(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)    
    rating0 = models.IntegerField(default = 0)
    rating1 = models.IntegerField(default = 0)
    rating2 = models.IntegerField(default = 0)
    rating3 = models.IntegerField(default = 0)
    
    def __str__(self):
        return '%s' % (self.professor)

class University(models.Model):
    name = models.CharField(max_length=400)
    sigla = models.CharField(max_length=40)
    class Meta:
        verbose_name_plural = ('Universities')

    def __str__(self):
        return ('%s - %s' % (self.name, self.sigla))
