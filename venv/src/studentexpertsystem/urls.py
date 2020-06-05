from django.urls import path
from .views import groups_list, boards_list,courses_list,detail_model_view

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'studentexpertsystem'

urlpatterns = [
    path('groups/', groups_list),
    path('courses/', courses_list),
    path('boards/',boards_list),
    path("detail_model/",detail_model_view)
   # path('api/', article_list),
   # path('detail/<int:pk>/', article_detail)
]


