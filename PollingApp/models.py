from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=250)
    pwd = models.CharField(max_length=150)

    class Meta:
        db_table = "User"

    def __str__(self):
        return self.user_name

    def get_absolute_url(self):
        return reversed('post', kwargs={'id': self.id})


class TaskList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=2000)
    task_category = models.IntegerField(null=True)
    task_description = models.CharField(max_length=5000,null=True)

    class Meta:
        db_table = "TaskList"

    def __str__(self):
        return self.task_name

    def get_absolute_url(self):
        return reversed('post', kwargs={'id': self.id})
