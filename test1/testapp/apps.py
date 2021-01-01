from django.apps import AppConfig


class TestappConfig(AppConfig):
    name = 'testapp'

    def ready(self):
        import testapp.signals