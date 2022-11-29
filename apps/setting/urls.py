from django.urls import path
from .views import index,liquidity,faq
from django.contrib.auth.views import LogoutView

urlpatterns = [ 
    path('',index,name='index'),
    path('logout/', LogoutView.as_view(next_page = 'index'), name="logout"),
    path('liquidity/',liquidity,name='liquidity'),
    path('faq/',faq,name='faq'),
]