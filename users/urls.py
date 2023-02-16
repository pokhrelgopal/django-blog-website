from django.urls import path
from . import views as v

urlpatterns = [
    path('login/', v.loginUser, name='login'),
    path('signup/', v.signupUser, name='signup'),
    path('logout/', v.logoutUser, name='logout'),

    path('profile/', v.profilePage, name='profile'),
    path('profile/add-info/', v.addInfo, name="add-info"),

    path('add-blog/', v.addBlog, name='add-blog'),
    path('blog/update-blog/<str:id>/', v.updateBlog, name='update-blog'),
    path('blog/delete-blog/<str:id>/', v.deleteBlog, name='delete-blog'),


]
