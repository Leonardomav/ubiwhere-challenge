from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Occurrence, Category


#File with all unit tests for app_challenge app. The implemented testsuit does not yet cover all the possible scenarios.

class ModelsTest(APITestCase):
	"""
	SuperClass for both models test suit. Used to initialize the same setUpClass() method.
	"""

	@classmethod
	def setUpClass(cls):
		super(ModelsTest, cls).setUpClass()	

		#create test user with staff permissions
		cls.admin_user = User.objects.create_user('testuser1', 'testpass1')
		cls.admin_user.is_staff = True
		cls.client_admin = APIClient()
		cls.client_admin.force_authenticate(cls.admin_user)

		#create test user without staff permissions
		cls.not_admin_user = User.objects.create_user('testuser2', 'testpass2')
		cls.client_not_admin = APIClient()
		cls.client_not_admin.force_authenticate(cls.not_admin_user)

		#create test category manually
		cls.category_entry=Category(name="test_cat2", description="test_desc2")
		cls.category_entry.save()

class CategoryTest(ModelsTest):
	"""
	This Class contains all the tests for the category model
	"""

	@classmethod
	def setUpClass(cls):
		super(CategoryTest, cls).setUpClass()	

	def test_create_category_admin(cls):
		"""
		Test category creation by admin. 
		Pass if status_code is equal to 201_CREATED.
		"""

		url = reverse("category-list")
		data = {'name': 'test_cat_1', 'description': 'test_desc_1'}
		response = cls.client_admin.post(url, data, format='json')
		cls.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_create_category_user(cls):
		"""
		Test category creation by non admin. 
		Pass if status_code is equal to 403_FORBIDDEN.
		"""

		url = reverse("category-list")
		data = {'name': 'test_cat_2', 'description': 'test_desc_2'}
		response = cls.client_not_admin.post(url, data, format='json')
		cls.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_list_categories_admin(cls):
		"""
		Test category listing by admin. 
		Pass if status_code is equal to 200_OK.
		"""

		url = reverse("category-list")
		response = cls.client_admin.get(url)
		cls.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_list_category_user(cls):
		"""
		Test category listing by non admin. 
		Pass if status_code is equal to 403_FORBIDDEN.
		"""

		url = reverse("category-list")
		response = cls.client_not_admin.get(url)
		cls.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_list_category_no_user(cls):
		"""
		Test category listing without login. 
		Pass if status_code is equal to 403_FORBIDDEN.
		"""

		no_client = APIClient()
		url = reverse("category-list")
		response = no_client.get(url)
		cls.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_retrieve_category_admin(cls):
		"""
		Test category retrival by admin. 
		Pass if status_code is equal to 200_OK.
		"""

		url = reverse("category-detail", kwargs={"pk":cls.category_entry.id})
		response = cls.client_admin.get(url)
		cls.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_patch_category_admin(cls):
		"""
		Test category patch by admin. 
		Pass if status_code is equal to 200_OK.
		"""

		url = reverse("category-detail", kwargs={"pk":cls.category_entry.id})
		data = {'name': 'test_cat_patch', 'description': 'test_desc_patch'}
		response = cls.client_admin.patch(url, data, format='json')
		cls.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_delete_category_admin(cls):
		"""
		Test deleting category by admin. 
		Pass if status_code is equal to 204_NO_CONTENT.
		"""

		url = reverse("category-detail", kwargs={"pk":cls.category_entry.id})
		response = cls.client_admin.delete(url)
		cls.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



class OccurrenceTests(ModelsTest):
	"""
	This Class contains all the tests for the occurence model
	"""

	@classmethod
	def setUpClass(cls):
		super(OccurrenceTests, cls).setUpClass()

	def test_list_occurrence_admin(cls):
		"""
		Test listing occurence by admin. 
		Pass if status_code is equal to 200_OK.
		"""

		url = reverse("occurrence-list")
		response = cls.client_admin.get(url)
		cls.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_list_occurrence_no_user(cls):
		"""
		Test listing occurence without login. 
		Pass if status_code is equal to 200_OK.
		"""

		no_client = APIClient()
		url = reverse("occurrence-list")
		response = no_client.get(url)
		cls.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_create_occurrence_admin(cls):
		"""
		Test creating occurence by admin. 
		Pass if status_code is equal to 200_OK.
		"""

		url = reverse("occurrence-list")
		data = {'description': 'occurrence_desc', 'category': cls.category_entry.id}
		response = cls.client_admin.post(url, data, format='json')
		cls.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_patch_occurrence_not_author(cls):
		"""
		Test patching category by someone who is neither admin nor author of said occurence. 
		Pass if status_code is equal to HTTP_403_FORBIDDEN.
		"""

		occurrence_entry=Occurrence.objects.create(description="test_desc", category=cls.category_entry, author = cls.admin_user)
		occurrence_entry.save()
		url = reverse("occurrence-detail", kwargs={"pk":occurrence_entry.id})
		data = {'description': 'occurrence_desc_patch'}
		response = cls.client_not_admin.patch(url, data, format='json')
		cls.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_change_status_occurrence_user(cls):
		"""
		Test creating an occurence with status 2, and changing occurence status without staff permissions.
		Pass if status_code for creation is equal to 201_CREATED and 
			if status_code for patching is equal to 200_OK and
			if occurence status is equal to 1.
		"""

		url = reverse("occurrence-list")
		data = {'description': 'occurrence_desc', 'category': cls.category_entry.id, 'status': 2}
		response = cls.client_not_admin.post(url, data, format='json')
		cls.assertEqual(response.status_code, status.HTTP_201_CREATED)

		url = reverse("occurrence-detail", kwargs={"pk":1})
		data = {'status': 2}
		response = cls.client_not_admin.get(url, data, format='json')
		cls.assertEqual(response.status_code, status.HTTP_200_OK)
		cls.assertEqual(response.json()['status'], 1)
