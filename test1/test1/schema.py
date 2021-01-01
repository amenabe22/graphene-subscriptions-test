import asyncio
import graphene
import channels_graphql_ws
from graphene_django import DjangoObjectType
from .subscriptions import MySubscription


class Query(graphene.ObjectType):
    data = graphene.String()

    def resolve_data(self, info):
        return "NIGGa"


class Subscription(graphene.ObjectType):
    """Root GraphQL subscription."""
    my_subscription = MySubscription.Field()


schema = graphene.Schema(query=Query, subscription=Subscription)
