
from django.urls import path,include
from . import views
urlpatterns = [


    path ('upload-cv/', views.upload_cv, name= 'add_cv'),
    path ('add-job/', views.add_job , name='add_job'),

    path ('add-catagory/',views.add_cv_catagory,name='add_cv_c'),
    path ('cv-catagory-list/',views.cv_catagory_list, name= 'cv_catagory'),
    path ('cv-catagory-list/<str:slug>/' ,views.cv_catagory_post_list ,name= "cv_catagory_post" ),
    path ('request_cv/<int:pk>/,',views.req_cv , name='request_cv'),
    path ('requested-cv',views.requested_cv_feedback, name='requested_cv'),
    path ('feedback/',views.requested_cv_feedback,name='feedback'),

    path ('job-circular/', views.job_circular_list , name= 'job_list' ),
    path ('job-circular/<str:slug>/',views.job_circular_details, name='job_details'),
]

