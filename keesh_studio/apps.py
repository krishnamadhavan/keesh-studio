"""
keesh_studio Django application initialization.
"""

from django.apps import AppConfig


class KeeshStudioConfig(AppConfig):
    """
    Configuration for the keesh_studio Django application.
    """

    name = 'keesh_studio'

    keesh_studio = {
        'url_config': {
            'cms.djangoapp': {
                'namespace': 'keesh_studio',
                'regex': '^api/',
                'relative_path': 'urls',
            },
        },
    }
