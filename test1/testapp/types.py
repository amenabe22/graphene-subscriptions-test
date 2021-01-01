from graphene_django import DjangoObjectType
# from .models import Testmodel
from django.apps import apps

TestM  = apps.get_model('testapp', 'Testmodel')


class TestModelType(DjangoObjectType):
    class Meta:
        model = TestM
