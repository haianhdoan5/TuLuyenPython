from django.urls import path

from .views import RegisterView

urlpatterns = [
    # Đường dẫn API sẽ là: /api/register/
    path("register/", RegisterView.as_view(), name="register"),
]
