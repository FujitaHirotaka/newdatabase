from django.db import models

class Term(models.Model):
    name=models.CharField(verbose_name="項目名", max_length=90, null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="水質分析項目"



