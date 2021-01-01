from django.contrib import admin
from django.urls import path
from graphene_file_upload.django import FileUploadGraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from graphql_playground.views import GraphQLPlaygroundView


class GqlView(FileUploadGraphQLView, LoginRequiredMixin):
    pass


urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GqlView.as_view(graphiql=True))),
    path('playground/', GraphQLPlaygroundView.as_view(endpoint="/graphql/")),
]
