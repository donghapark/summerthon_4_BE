from django.db import models


class Score(models.Model):
    testId = models.AutoField(primary_key=True)
    test_type=models.IntegerField(verbose_name='검사종류1~4',default=0)
    score1 = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='점수1',default=0.0)
    score2 = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='점수2',default=0.0)
    score3 = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='점수3',default=0.0)
    score4 = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='점수4',default=0.0)
    score5 = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='점수5',default=0.0)
    score6 = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='점수6',default=0.0)
    score7 = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='점수7',default=0.0)
    score8 = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='점수8',default=0.0)
    score9 = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='점수9',default=0.0)
    score10 =models.DecimalField(max_digits=5, decimal_places=2,verbose_name='점수10',default=0.0)



