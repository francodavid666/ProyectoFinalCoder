from django.test import TestCase

# Create your tests here.
from .models import *

from django.contrib.auth import get_user_model

User= get_user_model()

class CanalTestCase(TestCase):
    def SetUp(self):
        self.usuario_a = User.objects.create(username='BIUTUX', password = 'MICHUCHA333777555')
        self.usuario_b = User.objects.create(username='NABBORI', password = 'MICHUCHA333777555')
        self.usuario_c = User.objects.create(username='TAZZ', password = 'MICHUCHA333777555')
        
        
    def test_usuario_count(self):
        qs =User.objects.all()
        self.assertEqual(qs.count(), 3)
        
    def test_cada_usuario_canal(self):
        qs = User.objects.all()
        ['BIUTUX','NABBORI','TAZZ']
        for usuario in qs:
            canal_obj= Canal.objects.create
            canal_obj.usuarios.add(usuario)
            
        canal_qs = Canal-object.all()
        self.assertEqual(canal_qs.count(), 3)
            
            
       