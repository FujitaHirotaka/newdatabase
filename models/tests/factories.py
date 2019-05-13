"""
import factory
from models.models.models_AnalysisTerm import Term
from models.models.models_Customer import Customer

class TermFactory(factory.django.DjangoModelFactory):
    name=factory.django.CharField()
    class Meta:
        model=Term
"""
# Create your tests here.
