from test1.schema import MySubscription


def tSaveHandler(obj):
    MySubscription.broadcast(
        # Subscription group to notify clients in.
        group='group42',
        # Dict delivered to the `publish` method.
        payload=obj,
    )
