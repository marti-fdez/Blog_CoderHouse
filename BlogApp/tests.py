from django.test import TestCase

# Create your tests here.

from BlogApp.models import Articulo
from django.contrib.auth.models import User

import random
import string

class ArticuloTestCase(TestCase):
    pass

    def setUp(self):
        self.u1 = User.objects.create(username='user1')

    def test_create_articulo(self):
    # Test1 - Comprobar creacion articulos con letras random
        lista_letras_title = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        print(lista_letras_title)
        title_prueba = "".join(lista_letras_title)
        print(title_prueba)
        articulo_1 = Articulo.objects.create(titulo=title_prueba,autor=self.u1,subtitulo="Prueba Subtitulo",cuerpo="Lorem ipsum dolor sit amet",fecha_publicacion="2022-01-02", tematica="Pruebas")
        print(articulo_1)

        self.assertIsNotNone(articulo_1.id)
        self.assertEqual(articulo_1.titulo, title_prueba)
        print(articulo_1.titulo, articulo_1.subtitulo, articulo_1.cuerpo, articulo_1.autor)