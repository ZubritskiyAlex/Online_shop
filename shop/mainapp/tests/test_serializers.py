from django.test import TestCase

from shop.mainapp.models import Notebook

from shop.mainapp.api.serializers import NotebookSerializer


class NotebookSerializerTest(TestCase):

    def setUp(self):
        self.notebook_attributes = {
            "diagonal": 15.6,
            "display_type": "IPS",
            "processor_freq": 2.3,
            "ram": "6 GB",
            "video": "GeForce",
            "time_without_charge": "4 hours"

        }

        self.serializer_data = {
            "diagonal": 13.6,
            "display_type": "AMOLED",
            "processor_freq": 3.2,
            "ram": "4 GB",
            "video": "GeForce",
            "time_without_charge": "2 hours",
        }

        self.staff = Notebook.objects.create(**self.notebook_attributes)
        self.serializer = NotebookSerializer(instance=self.staff, context={'request': None})

    def test_diagonal_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["diagonal"], self.notebook_attributes["diagonal"])

    def test_display_type_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["display_type"], self.notebook_attributes["display_type"])

    def test_processor_freq_content(self):
        data = self.serializer.data
        self.assertEqual(data["processor_freq"], self.notebook_attributes["processor_freq"])

    def test_ram_fields(self):
        data = self.serializer.data
        self.assertEqual(data["ram"], self.notebook_attributes["ram"])

    def test_video_content(self):
        data = self.serializer.data
        self.assertEqual(data["video"], self.notebook_attributes["video"])

    def test_time_without_charge_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["time_without_charge"], self.notebook_attributes["time_without_charge"])

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {"diagonal", "display_type", "processor_freq", "ram","video", "time_without_charge"})
