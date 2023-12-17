import pytest

from blog.factories import PostFactory, UserFactory

@pytest.fixture
def post_with_different_author():
    author = UserFactory()
    return PostFactory(title='Post with different author', author=author)

@pytest.mark.django_db
def test_create_post_with_different_author(post_with_different_author):
    assert post_with_different_author.title == 'Post with different author'
    assert post_with_different_author.author.username == post_with_different_author.author.username