from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken

from .models import Post


class PostAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(
            username='saulojustiniano', password='saulo@123')
        self.access_token = AccessToken.for_user(self.user)
        self.authorization_header = f'Bearer {self.access_token}'

    def test_create_post(self):
        response = self.client.post(
            '/api/post/', {'title': 'Novo Post', 'content': 'Conteúdo do novo post'}, HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        post = Post.objects.first()
        self.assertEqual(post.title, 'Novo Post')
        self.assertEqual(post.content, 'Conteúdo do novo post')

    def test_retrieve_post(self):
        post = Post.objects.create(title='Post', content='Conteúdo')
        response = self.client.get(
            f'/api/post/{post.id}/', HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], post.title)
        self.assertEqual(response.data['content'], post.content)

    def test_update_post(self):
        post = Post.objects.create(title='Post', content='Conteúdo')
        response = self.client.patch(
            f'/api/post/{post.id}/', {'title': 'Post Atualizado'}, HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.get().title, 'Post Atualizado')

    def test_delete_post(self):
        post = Post.objects.create(title='Post', content='Conteúdo')
        response = self.client.delete(
            f'/api/post/{post.id}/', HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)

    def test_create_post_unauthenticated(self):
        response = self.client.post('/api/post/', {'title': 'Novo Post', 'content': 'Conteúdo do novo post'},
                                    HTTP_AUTHORIZATIO='')
        self.assertEqual(response.status_code, 401)
