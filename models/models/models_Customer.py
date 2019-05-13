from django.db import models
from models.models.models_AnalysisTerm import Term

number_of_AnalysisTerm=15

class Customer(models.Model):
    name=models.CharField("納入先名称", max_length=50, null=True)
    def __str__(self):
            return self.name
    class Meta:
        verbose_name_plural="納入先"


class SamplingSite(models.Model):
    customer=models.ForeignKey(Customer, related_name="customer", null=True, on_delete=models.CASCADE)
    name=models.CharField("採水サイト名称", max_length=50, null=True)
    for i in range(number_of_AnalysisTerm):
        exec("analysisterm"+str(i)+"=models.ForeignKey(Term, null=True, blank=True, related_name='term"+str(i)+"',verbose_name='分析項目"+str(i)+"', on_delete=models.CASCADE)")  
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="採水サイト"
        
