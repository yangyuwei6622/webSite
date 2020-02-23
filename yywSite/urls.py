from django.urls import path
from yywSite import views
urlpatterns = [
    path('test/', views.test),


    path('getTest1/',views.getTest1),
    path('getTest1/getTest2/',views.getTest2),
    path('getTest1/getTest3/',views.getTest3),
    path('postTest1/',views.postTest1),
    path('postTest2/',views.postTest2),

    path('cookieTest/',views.cookieTest),
    path('redirectTest/',views.redirectTest),

    path('session1/',views.session1),
    path('session2/', views.session2),
    path('session2_handle/',views.session2_handle),
    path('session3/', views.session3),

    path('image/', views.image),
    path('uploadImage/', views.uploadImage),
    path('uploadHandle/', views.uploadHandle)
]