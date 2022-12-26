from django.urls import path
from account.views import make_ac

app_name = 'account'
urlpatterns = [
    path('account/',make_ac, name='account')
]
        