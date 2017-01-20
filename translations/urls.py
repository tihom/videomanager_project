from . import views, routers

router = routers.VideoRouter()
router.register(r'original_videos', views.OriginalVideoViewSet)
router.register(r'video_metas', views.VideoMetaViewSet)
urlpatterns = router.urls
