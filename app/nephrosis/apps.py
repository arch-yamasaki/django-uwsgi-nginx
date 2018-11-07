from django.apps import AppConfig


class NephrosisConfig(AppConfig):
    name = 'nephrosis'

    def __str__(self):
        return self.nephrosis_text
