# from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from crum import get_current_user


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Occurrence(models.Model):
    NOT_VALIDATED = 1
    VALIDATED = 2
    SOLVED = 3

    STATUS_CHOICES = (
        (NOT_VALIDATED, 'Not Validated'),
        (VALIDATED, 'Validated'),
        (SOLVED, 'Solved'),
    )

    description = models.CharField(max_length=200)
    default_point = Point(0, 0)
    point = models.PointField(default=default_point)
    created_at = models.DateTimeField(auto_now_add=True)  # might not work properly
    updated_at = models.DateTimeField(auto_now=True)  # might not work properly
    author = models.ForeignKey('auth.User', blank=True, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    status = models.IntegerField(choices=STATUS_CHOICES, default=NOT_VALIDATED)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.author = user
        super(Occurrence, self).save()
