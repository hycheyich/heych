from django.urls import path, re_path
from .views import CartAPIView

urlpatterns = [
    path('', CartAPIView.as_view({
        'post': 'add_cart',
        'get': 'get_cart_list',
        'put': 'change_selected_status',
        'delete': 'delete_course',
        'patch': 'change_expire',
    })),
    path("selected/", CartAPIView.as_view({"get": "get_select_course"}))
]
