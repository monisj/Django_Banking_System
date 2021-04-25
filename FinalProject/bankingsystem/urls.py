from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('add_new',views.add_new,name='add'),
    path('show',views.login,name='Show_All_Record'),
    path('adminshow',views.adminshow,name='AdminShow'),
    path('check',views.check,name='Check'),
    path('deposit',views.deposit,name='deposit'),
    path('comment',views.comment,name='comment'),
    path('dodeposite',views.dodeposit,name='dodeposit'),
    path('withdraw',views.withdraw,name='withdraw'),
    path('dowithdraw',views.dowithdraw,name='dowithdraw'),
    path('billpay',views.billpay,name='billpay'),
    path('dobillpay',views.dobillpay,name='dobillpay'),
    path('logout',views.logout)
]
