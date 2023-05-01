from django.urls import path
from app import views

#se utiliza para especificar la url app:..., en base.html
app_name = 'app'

urlpatterns = [
    path('', views.mi_vista, name='app'),
    path('nosotros/', views.nuestra_vista, name='nosotros'),
    
    # juegos con vistas
    
    #path('juegos/crear/', views.crear_juego, name='alta_juego'),
    path('juegos/', views.lista_juegos, name='consultar_juegos'),
    #path('juegos/<int:id_juego>/eliminar/', views.eliminar_juego, name='eliminar_juego'),
    #path('juegos/<int:id_juego>/modificar/', views.modificar_juego, name='modificar_juego'),
    #path('juegos/<int:id_juego>/', views.mostrar_juego, name='mostrar_juego'),
    
    # juegos con CBV(clases basadas en vistas)
    
    #path('juegos/', views.ListaJuegos.as_view(), name='consultar_juegos'),
    path('juegos/crear/', views.CrearJuego.as_view(), name='alta_juego'),
    path('juegos/<int:pk>/', views.MostrarJuego.as_view(), name='mostrar_juego'),
    path('juegos/<int:pk>/eliminar/', views.EliminarJuego.as_view(), name='eliminar_juego'),
    path('juegos/<int:pk>/modificar/', views.ModificarJuego.as_view(), name='modificar_juego'),
    
    
    

    
]