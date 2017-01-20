# ref: http://www.django-rest-framework.org/api-guide/routers/
from rest_framework.routers import Route, DynamicDetailRoute, DefaultRouter, SimpleRouter

class UserRouter(SimpleRouter):
    """
    Custom router for user related api endpoints
    """

    # routes = DefaultRouter.routes + 
    routes = [
        Route(
            url=r'^lookupuser$',
            mapping={'get': 'lookupuser'},
            name='user-lookup',
            initkwargs={'suffix': 'Detail'}
        ),
        Route(
            url=r'^team$',
            mapping={'get': 'get_team'},
            name='team-list',
            initkwargs={'suffix': 'List'}
        ),
    ]