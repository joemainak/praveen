from django.urls import path, include

urlpatterns = [
    path('users/', include('useraccounts.urls')),
    path('blog/', include('blog.urls'))
]