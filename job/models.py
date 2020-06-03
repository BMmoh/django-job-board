from django.db import models


# Create your models here.

JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time')
)


class Job(models.Model):
    Title = models.CharField(max_length=100)
    # Location = models
    Job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    Description = models.TextField(max_length=1000)
    Published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    Salary = models.IntegerField(default=0)
    Category = models.ForeignKey('Category', models.CASCADE, null=True)
    Experience = models.IntegerField(default=1)

    def __str__(self):
        return self.Title


class Category(models.Model):
    Name = models.CharField(max_length=30)

    def __str__(self):
        return self.Name
