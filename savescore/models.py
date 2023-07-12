from django.db import models


class Score(models.Model):
    testId = models.AutoField(primary_key=True)
    test_type=models.IntegerField(null=True,blank=True,verbose_name='검사종류1~4',default=0)
    score1 = models.DecimalField(null=True,blank=True,max_digits=5, decimal_places=2,verbose_name='점수1',default=0.0)
    score2 = models.DecimalField(null=True,blank=True,max_digits=5, decimal_places=2,verbose_name='점수2',default=0.0)
    score3 = models.DecimalField(null=True,blank=True,max_digits=5, decimal_places=2,verbose_name='점수3',default=0.0)
    score4 = models.DecimalField(null=True,blank=True,max_digits=5, decimal_places=2,verbose_name='점수4',default=0.0)
    score5 = models.DecimalField(null=True,blank=True,max_digits=5, decimal_places=2,verbose_name='점수5',default=0.0)
    score6 = models.DecimalField(null=True,blank=True,max_digits=5, decimal_places=2,verbose_name='점수6',default=0.0)
    score7 = models.DecimalField(null=True,blank=True,max_digits=5, decimal_places=2,verbose_name='점수7',default=0.0)
    score8 = models.DecimalField(null=True,blank=True,max_digits=5, decimal_places=2,verbose_name='점수8',default=0.0)
    score9 = models.DecimalField(null=True,blank=True,max_digits=5, decimal_places=2,verbose_name='점수9',default=0.0)
    score10 =models.DecimalField(null=True,blank=True,max_digits=5, decimal_places=2,verbose_name='점수10',default=0.0)


    # def score_sum1(self):
    #     return self.score1 + self.score2
    # def score_sum2(self):
    #     return self.score3 + self.score4
    # def score_sum3(self):
    #     return self.score5 + self.score6
    # def score_sum4(self):
    #     return self.score7 + self.score8
    # def score_sum5(self):
    #     return self.score9 + self.score10

