from django.db import models

# Create your models here.

class Fcuser(models.Model):
    username = models.CharField(max_length=64, verbose_name='Name')
    useremail = models.EmailField(max_length=128, verbose_name='Email')
    password = models.CharField(max_length=64, verbose_name='Password')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='REG Time')

    def __str__(self):
        return self.username

    class Meta:
        # 테이블명 지정
        db_table = 'fastcampus_fcuser'
        verbose_name = 'NamoWebiz 사용자'
        verbose_name_plural = 'NamoWebiz 사용자'