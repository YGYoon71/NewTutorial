from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='TAG')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='REG Time')

    def __str__(self):
        return self.name

    class Meta:
        # 테이블명 지정
        db_table = 'fastcampus_tag'
        verbose_name = 'TAG'
        verbose_name_plural = 'TAG'