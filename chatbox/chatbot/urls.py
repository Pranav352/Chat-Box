from django.urls import path
from .views import chatbot_api, chat_page

urlpatterns = [
    path('api/', chatbot_api, name='chatbot_api'),
    path('', chat_page, name='chatbot_chat'),
]
