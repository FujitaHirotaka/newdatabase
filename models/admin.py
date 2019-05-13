from django.contrib import admin
from models.models.models_AnalysisTerm import Term
from models.models.models_Customer import Customer, SamplingSite


admin.site.register(Customer)
admin.site.register(SamplingSite)
admin.site.register(Term)