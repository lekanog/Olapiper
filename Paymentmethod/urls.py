from django.urls import path
from . import views

app_name = 'Paymentmethod'
urlpatterns = [
    path('add-card/', views.AddCardView.as_view()),
    path('history/', views.CardHistory.as_view()),

]
