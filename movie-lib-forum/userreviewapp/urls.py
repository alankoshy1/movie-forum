from django.urls import path
from . import views
app_name='userreviewapp'

urlpatterns = [
    path('dispReview/',views.dispReview,name='dispReview'),
    path('addReview/',views.addReview,name='addReview'),
]