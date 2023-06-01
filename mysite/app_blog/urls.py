"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (HomePageView, ArticleDetail, ArticleList, ArticleCategoryList)

urlpatterns = [
    path(r'', HomePageView.as_view(), name='home'),
    path(r'articles', ArticleList.as_view(),
        name='articles-list'),
    path(r'articles/category/<slug>',
        ArticleCategoryList.as_view(),
        name='articles-category-list'),
    path(r'articles/<year>/<month>/<day>/<slug>',
        ArticleDetail.as_view(),
        name='news-detail'),
    path(r'articles/category/<slug>',
        ArticleCategoryList.as_view(),
        name='articles-category-list'),
]
