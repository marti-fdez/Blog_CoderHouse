from django.urls import path
from Messages.views import NewChatView, ChatList, detalle_chat, EliminarChat, new_message_view

urlpatterns = [
    path('newchat', NewChatView.as_view(), name="newchat"),
    path('chats', ChatList.as_view(), name="chats"),
    path('detalle-chat/<int:pk>', detalle_chat, name="detalle-chat"),  # type: ignore
    path('newmessage/<int:pk>', new_message_view, name="newmessage"),  # type: ignore
    path('eliminar-chat/<int:pk>', EliminarChat.as_view(), name="eliminar-chat"),
] 
