from django.urls import path
from . import views

app_name = 'tool'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/' , views.CreateToolView.as_view() , name = 'post'),#P446
    path('post_done/', views.PostSuccessView.as_view(), name= 'post_done'),

    path('tools/<int:category>', views.CategoryView.as_view(), name= 'tools_cat'), #475
    
    path('user-list/<int:user>', views.UserView.as_view(), name= 'user_list'), #482

    path('tool-detail/<int:pk>', views.DetailView.as_view(), name='tools_detail'),

    path('accounts/profile/', views.MypageView.as_view(), name = 'mypage'),
    
    path('tool/<int:pk>/delete/', views.ToolDeleteView.as_view(), name='tool_delete'),#505
    
    path('category_list/', views.CategoryListView.as_view(), name='category_list')


]