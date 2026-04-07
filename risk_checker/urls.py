# risk_checker/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('breast-cancer/', views.breast_cancer_form, name='breast-cancer-form'),
    path('breast-cancer/predict/', views.predict_cancer, name='predict-cancer'),


    path("diabetes/", views.predict_diabetes, name="diabetes"),
    path("diabetes/predict/", views.predict_diabetes, name="predict-diabetes"),

    # ✅ Add heart disease routes here
    path('heart/', views.predict_heart, name='heart'),
    path('heart/predict/', views.predict_heart, name='predict_heart'),

    path('kidney/', views.predict_kidney, name='kidney'),
    path('kidney/predict/', views.predict_kidney, name='predict_kidney'),

    path('liver/', views.predict_liver, name='liver'),
    path('liver/predict/', views.predict_liver, name='predict_liver'),

    # ✅ Disease Overview Page
    path('disease-overview/', views.disease_overview, name='disease-overview'),
]
