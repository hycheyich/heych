from django.urls import path, re_path
from . import views

urlpatterns = [
    path("coursecategory/", views.CourseCategoryModelAPIView.as_view()),
    path("course/", views.CourseModelAPIView.as_view()),
    path("chapter/", views.CourseChapterListAPIView.as_view()),
    re_path(r'(?P<pk>\d+)/', views.CourseRetrieveAPIView.as_view()),
]
