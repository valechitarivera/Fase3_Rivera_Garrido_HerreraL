from django.test import TestCase
from .forms import compra_form, producto_form, marca_form
from .models import compra, producto, marca
from django.core.files.uploadedfile import SimpleUploadedFile

class compra_formsTest(TestCase):
    def test_valid_form(self):
        c = Compra.objects.create(name='Compra1', summary='Compra')
        data = {'name': c.name, 'summary': c.summary,}
        form = compra_form(data=data)
        self.assertTrue(form.is_valid())

        def test_invalid_form(self):
        c = Compra.objects.create(name='', summary='Compra')
        data = {'name': c.name, 'summary': c.summary,}
        form = compra_form(data=data)
        self.assertFalse(form.is_valid())

class producto_FormsTest(TestCase):
    def test_valid_form(self):
        Compra = compra.objects.create(name='1', summary='Prueba')
        Compra = compra.objects.get(pk=1).pk
        p = producto.objects.create(title='Prueba1', summary='Prueba')
        p.save()
        data = {'title': m.title, 'summary': m.summary, 'compra': Compra,}
        
        with open('catalogo/static/img/gatico.png', 'rb') as file:
            document = SimpleUploadedFile(file.name, file.read(), content_type='image/png')
        
        form = producto_form(data, {'image': document})
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        c = Compra.objects.create(name='Accion', summary='Prueba')
        p = producto.objects.create(title='', summary='Prueba', compra=c,)
        data = {'title': m.title, 'summary': m.summary, 'genre': p.compra, }
        form = producto_form(data=data)
        self.assertFalse(form.is_valid())