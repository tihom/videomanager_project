# ref: http://www.django-rest-framework.org/api-guide/routers/
from rest_framework.routers import Route, DynamicDetailRoute, DefaultRouter, SimpleRouter

class VolunteerRouter(SimpleRouter):
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
        Route(
            url=r'^team/add-member$',
            mapping={'post': 'add_team_member'},
            name='team-add',
            initkwargs={'suffix': 'Detail'}
        ),
        Route(
            url=r'^team/members/(?P<user_id>\d+)$',
            mapping={'put': 'update_team_member'},
            name='team-update',
            initkwargs={'suffix': 'Detail'}
        ),
        Route(
            url=r'^team/members/(?P<user_id>\d+)$',
            mapping={'delete': 'delete_team_member'},
            name='team-delete',
            initkwargs={'suffix': 'Detail'}
        ),
    ]