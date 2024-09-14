from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('sobre/', views.about, name='sobre'),
    path('trabalhe-conosco/', views.jobs, name='trabalhe-conosco'),  # type: ignore
    path('franquias/', views.franchises, name='franquia'),  # type: ignore
    path('investidores/', views.investors, name='relacoes-investidores'),  # type: ignore
    path('fale-conosco/', views.contact, name='fale-conosco'),  # type: ignore
    path('pesquisa', views.satisfation, name='pesquisa-satisfacao'), 
    path('privacidade', views.privacy_policy, name='politica-privacidade'), # type: ignore
    path('troca', views.devolution, name='politica-troca-devolucao'),  # type: ignore
    path('cookies', views.cookies_policy, name='politica-cookies'),  # type: ignore
    path('cupons', views.coupons, name='cupons'),  # type: ignore
    path('cardapio/', views.menu, name='cardapio'),  # type: ignore
    path('app/', views.app, name='app'),  # type: ignore
    path('clube/', views.club, name='clube'),  # type: ignore
    path('delivery/', views.delivery, name='dlv'),  # type: ignore
]

