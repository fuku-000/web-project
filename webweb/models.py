from django.db import models

# Create your models here.
#適当なユーザーテーブルを追加

class Test(models.Model):
    column1 = models.CharField(max_length=10)
    column2 = models.CharField(max_length=20)
    
class User_Models(models.Model):


    class Meta:
        db_table = 'User'

    user_id = models.CharField(
        verbose_name='userid',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    user_name = models.CharField(
        verbose_name='username',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    user_age = models.CharField(
        verbose_name='userage',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    user_email = models.CharField(
        verbose_name='useremail',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    def __str__(self):
        return self.user_id