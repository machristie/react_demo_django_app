import os

from django.apps import AppConfig

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Settings:
    WEBPACK_LOADER = {
        "REACT_DEMO": {
            "BUNDLE_DIR_NAME": "react_demo_django_app/dist/",  # must end with slash
            "STATS_FILE": os.path.join(
                BASE_DIR,
                "static",
                "react_demo_django_app",
                "dist",
                "webpack-stats.json",
            ),
        }
    }

class ReactDemoDjangoAppConfig(AppConfig):
    # Standard Django app configuration. For more information on these settings,
    # see https://docs.djangoproject.com/en/2.2/ref/applications/#application-configuration
    name = 'react_demo_django_app'
    label = name
    verbose_name = "React Demo Django App"

    # The following are Airavata Django Portal specific custom Django app settings

    # Set url_home to a namespaced URL that will be the homepage when the custom
    # app is selected from the main menu
    url_home = "react_demo_django_app:demo"

    # Set fa_icon_class to a FontAwesome CSS class for an icon to associate with
    # the custom app. Find an icon class at https://fontawesome.com/icons?d=gallery&p=2&s=regular,solid&m=free
    fa_icon_class = "fa-atom"

    # Second level navigation. Defines sub-navigation that displays on the left
    # hand side navigation bar in the Django Portal. This is optional but
    # recommended if your custom Django app has multiple entry points. See the
    # description of *nav* in
    # https://apache-airavata-django-portal.readthedocs.io/en/latest/dev/new_django_app/#appconfig-settings
    # for more details for more details.

    # Webpack loader
    settings = Settings()
