from . import views, routers

router = routers.UserRouter()
router.register(r'users', views.UserViewSet)
# router.register(r'profiles', views.ProfileViewSet)
urlpatterns = router.urls
