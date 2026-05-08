from django.urls import path
from . import views

urlpatterns = [
    path('',                 views.lion_list,   name='lion_list'),
    #lions/ 주소로 요청이 오면 viwes.py의 lion_list 함수 실행, 이 주소의 별명은 'lion_list'
    path('new/',             views.lion_create,  name='lion_create'),
    #lions/new/ 주소로 요청이 오면 viwes.py의 lion_create 함수 실행, 이 주소의 별명은 'lion_create'
    path('<int:pk>/',        views.lion_detail,  name='lion_detail'),
    #<int:pk>는 정수형태의 기본키(primary key), 따라서 url 주소에서 숫자 부분을 뽑아서 pk변수에 담아라, pk = DB테이블의 id번호
    path('<int:pk>/edit/',   views.lion_edit,    name='lion_edit'),
    path('<int:pk>/delete/', views.lion_delete,  name='lion_delete'),
]