from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from catalogo.models import compra, producto, Marca

class CompraListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_compra = 13

        for compra_id in range(number_of_compra):
            compra.objects.create(
                name=f'Accion {compra_id}',
                summary=f'Prueba {compra_id}',
            )
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalogo/compra/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('compra'))
        self.assertEqual(response.status_code, 200)
           
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('compra'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogo/compra_detail.html')
        
    def test_pagination_is_ten(self):
        response = self.client.get(reverse('compra'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['compra_detail']) == 10)

    def test_lists_all_genres(self):
        response = self.client.get(reverse('compra')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['compra_detail']) == 3)

class productoListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_producto = 13

        p =producto.objects.create(name='Accion', summary='Prueba')
        with open('catalogo/static/img/gatico.png', 'rb') as file:
            document = SimpleUploadedFile(file.name, file.read(), content_type='image/png')

        for prducto_id in range(number_of_producto):
            test_producto = producto.objects.create(
                title=f'Rey Leon {producto_id}',
                summary=f'Prueba {producto_id}',
                compra= p,
                url=f'Prueba.com {producto_id}',
                image= document
            )
            
            test_producto.save()
    
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalogo/producto/')
        self.assertEqual(response.status_code, 200)
    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('producto'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('producto'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'plantilla_base.html', 'movies.html')
