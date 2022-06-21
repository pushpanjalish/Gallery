from mediaapp.viewsets import ImgViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('img',ImgViewset)