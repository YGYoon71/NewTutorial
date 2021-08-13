from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name='SUBJECT')
    contents = models.TextField(verbose_name='CONTENTS')
    writer = models.ForeignKey('fcuser.Fcuser', on_delete=models.CASCADE, verbose_name='AUTHOR')
    tags = models.ManyToManyField('tag.Tag', verbose_name='TAG')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='REG Time')

    def __str__(self):
        return self.title

    class Meta:
        # 테이블명 지정
        db_table = 'fastcampus_board'
        verbose_name = 'NamoWebiz 게시글'
        verbose_name_plural = 'NamoWebiz 게시글'