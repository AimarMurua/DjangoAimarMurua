from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('etxeak/', views.etxeak, name = 'etxeak'), 

    path('gehitu/', views.gehitu, name = 'gehitu'), 
    path('gehitu/gehitupertsona/', views.gehitupertsona, name = 'gehitupertsona'),

    path('etxeak/gehituetxea/', views.gehituetxea, name = 'gehituetxea'), 
    path('etxeak/gehituetxea/gehituetxeaerregistroa/', views.gehituetxeaerregistroa, name = 'gehituetxeaerregistroa'),

    path('ezabatu/<p_nan>', views.ezabatu, name = 'ezabatu'), 
    path('etxeak/ezabatuetxea/<id>', views.ezabatuetxea, name = 'ezabatuetxea'), 

    path('eguneratu/<p_nan>', views.eguneratu, name = 'eguneratu'), 
    path('eguneratu/eguneratuerregistroa/<p_nan>', views.eguneratuerregistroa, name = 'eguneratuerregistroa'),

    path('etxeak/eguneratuetxea/<id>', views.eguneratuetxea, name = 'eguneratuetxea'),
    path('etxeak/eguneratuetxea/eguneratuetxeaerregistroa/<id>', views.eguneratuetxeaerregistroa, name = 'eguneratuetxeaerregistroa'),

    path('alokairua/', views.alokairua, name = 'alokairua'),
    path('alokairua/gehitualokairua/', views.gehitualokairua, name = 'gehitualokairua'), 
    path('alokairua/gehitualokairua/gehitualokairuaerregistroa/', views.gehitualokairuaerregistroa, name = 'gehitualokairuaerregistroa'),
]