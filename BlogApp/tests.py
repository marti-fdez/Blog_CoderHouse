from django.test import TestCase

# Create your tests here.

from BlogApp.models import Articulo
from Messages.models import Message, Chat
from django.contrib.auth.models import User

import random
import string

class UsuarioTestCase(TestCase):
    pass

    def setUp(self):
        self.u1 = User.objects.create(username='user1', password='12345', is_staff=False)
    def test_user_creation(self):
    # Test1 - Comprobar creacion de usuarios comunes
        self.assertEqual(self.u1.is_active, True)
        self.assertEqual(self.u1.is_staff, False)
        self.assertEqual(self.u1.is_superuser, False)

class ArticuloTestCase(TestCase):
    pass

    def setUp(self):
        self.u1 = User.objects.create(username='user1')

    def test_create_articulo(self):
    # Test2 - Comprobar creacion articulos con letras random
        lista_letras_title = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        print(lista_letras_title)
        title_prueba = "".join(lista_letras_title)
        print(title_prueba)
        articulo_1 = Articulo.objects.create(titulo=title_prueba,autor=self.u1,subtitulo="Prueba Subtitulo",cuerpo="Lorem ipsum dolor sit amet",fecha_publicacion="2022-01-02", tematica="Pruebas")
        print(articulo_1)

        self.assertIsNotNone(articulo_1.id)
        self.assertEqual(articulo_1.titulo, title_prueba)
        print(articulo_1.titulo, articulo_1.subtitulo, articulo_1.cuerpo, articulo_1.autor)

class ChatMessageTestCase(TestCase):
    pass
    
    def setUp(self):
        self.u1 = User.objects.create(username='user1')
        self.u2 = User.objects.create(username='user2')
    
    def test_chat_creation(self):
        # Test3 - Comprobar creacion de chat y messages
        chat = Chat.objects.create(user1=self.u1, user2=self.u2)
        print(chat)
        newmessage_from_u1 = Message.objects.create(chat_id=chat, text="hola", author=self.u1)
        newmessage_from_u2 = Message.objects.create(chat_id=chat, text="hola, como estas?", author=self.u2)
        print(newmessage_from_u1.text, newmessage_from_u2.text)
        self.assertTrue(chat)
        self.assertTrue(newmessage_from_u1)
        self.assertTrue(newmessage_from_u2)
