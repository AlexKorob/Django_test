from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=60)

    def __str__(self):
        return self.first_name


class Group(models.Model):
    name = models.CharField(max_length=40)
    member = models.ManyToManyField(Person, through="Membership")


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="membership")
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_join = models.DateField(auto_now=True)
    invite_reason = models.CharField(max_length=40)
