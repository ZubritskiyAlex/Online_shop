from django.test import TestCase

from shop.mainapp.models import Notebook


class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Notebook.objects.create(diagonal=15.6, display_type='IPS', processor_freq=2.2,

                            ram="6 GB", video='Nvidia', time_without_charge='3 hours')

    def test_diagonal_label(self):
        notebook = Notebook.objects.get(id=1)
        field_label =notebook._meta.get_field('diagonal').verbose_name
        self.assertEquals(field_label, 'Диагональ')

    def test_display_type_label(self):
        notebook = Notebook.objects.get(id=1)
        field_label =notebook._meta.get_field('display_type').verbose_name
        self.assertEquals(field_label, 'Тип дисплея')


    def test_processor_freq_label(self):
        notebook = Notebook.objects.get(id=1)
        field_label =notebook._meta.get_field('processor_freq').verbose_name
        self.assertEquals(field_label, 'Частота процессора')

    def test_ram_label(self):
        notebook = Notebook.objects.get(id=1)
        field_label =notebook._meta.get_field('ram').verbose_name
        self.assertEquals(field_label, 'Оперативная память')

    def test_video_label(self):
        notebook = Notebook.objects.get(id=1)
        field_label =notebook._meta.get_field('video').verbose_name
        self.assertEquals(field_label, 'Видеокарта')

    def test_time_without_charge_label(self):
        notebook = Notebook.objects.get(id=1)
        field_label = notebook._meta.get_field('time_without_charge').verbose_name
        self.assertEquals(field_label, 'Время работы аккумулятора')


    def test_diagonal_label_max_length(self):
        notebook = Notebook.objects.get(id=1)
        max_length = notebook._meta.get_field('diagonal_label').max_length
        self.assertEquals(max_length, 255)

    def test_processor_freq_max_length(self):
        notebook = Notebook.objects.get(id=1)
        max_length = notebook._meta.get_field('processor_freq').max_length
        self.assertEquals(max_length, 255)

    def test_ram_label_max_length(self):
        notebook = Notebook.objects.get(id=1)
        max_length = notebook._meta.get_field('ram').max_length
        self.assertEquals(max_length, 255)

    def test_description_max_length(self):
        notebook = Notebook.objects.get(id=1)
        max_length = notebook._meta.get_field('video').max_length
        self.assertEquals(max_length, 255)

    def test_time_without_charge_max_length(self):
        notebook = Notebook.objects.get(id=1)
        max_length = notebook._meta.get_field('time_without_charge').max_length
        self.assertEquals(max_length, 255)