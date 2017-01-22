from . import views, routers

router = routers.VolunteerRouter()
router.register(r'volunteers', views.VolunteerViewSet)
urlpatterns = router.urls
