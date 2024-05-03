from .views.watch_view import WatchProductionView
from .views.create_info_view import CreateInfoView
from .views.update_info_view import UpdateInfoView
from .views.read_info_view import ReadInfoView
from .views.delete_view import DeleteInfoView
from .views.create_admin_profile_view import CreateAdminProfileView

from django.urls import path

urlpatterns = [
    path('createInfo', CreateInfoView.as_view()),
    path('updateInfo', UpdateInfoView.as_view()),
    path('readInfo/id=<int:pk>', ReadInfoView.as_view(), name='read_info'),
    path('deleteInfo/<int:pk>', DeleteInfoView.as_view()),
    path('createAdminProfile', CreateAdminProfileView.as_view()),
    path('watchProduction', WatchProductionView.as_view())
]