from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from crum import get_current_user


# App_challenge model files. Models imported from django.contrib.gis.db instead of the default django.db

class Category(models.Model):
    """
    Model Description:
        Occurrence category;

    Field - name:
        Name of the category;
    Field - description:
        Description of the category;
    """
    
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        # set model string and model name
        return self.name


class Occurrence(models.Model):
    """
    Model Description:
        Main model - Urban occurrence model;

    Field - description:
        Description of the category;
    Field - point:
        Occurrence spacial location. Default location is set to latitude 0 longitude 0
    Field - created_at:
        Occurrence created date;
    Field - updated_at:
        Occurrence updated date. Equals created_at until modified;
    Field - author:
        User ForeignKey that created the occurrence. Default auth.User is used;
    Field - category:
        Occurrence category. ForeignKey to category model;
    Field - status:
        Occurrence status. Choice from 3 pre-defined options;
    """

    NOT_VALIDATED = 1
    VALIDATED = 2
    SOLVED = 3

    STATUS_CHOICES = (
        (NOT_VALIDATED, 'Not Validated'),
        (VALIDATED, 'Validated'),
        (SOLVED, 'Solved'),
    )

    description = models.CharField(max_length=200)
    point = models.PointField(default=Point(0, 0))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', blank=True, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    status = models.IntegerField(choices=STATUS_CHOICES, default=NOT_VALIDATED)

    def save(self, *args, **kwargs):
        """ Overwrite save function in order to set the author only at creation. """
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.author = user
        super(Occurrence, self).save()
