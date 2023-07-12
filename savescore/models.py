from django.db import models


class Score(models.Model):
    testId = models.AutoField(primary_key=True)
    

    score1 = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='점수1')
    score2 = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='점수2')
    score3 = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='점수3')
    score4 = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='점수4')
    score5 = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='점수5')
    score6 = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='점수6')
    score7 = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='점수7')
    score8 = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='점수8')
    score9 = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='점수9')
    score10 =models.DecimalField(max_digits=5, decimal_places=2,verbose_name='점수10')