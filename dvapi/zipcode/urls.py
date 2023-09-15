from django.urls import path

from . import views

urlpatterns = [
    path('zipcode/', views.ZipcodeView.as_view()),
    path('zipcode/<int:id>', views.ZipcodeView.as_view()),
    path('zipcodes/<str:zipcode>',views.ZipcodeSearchView.as_view()),
]