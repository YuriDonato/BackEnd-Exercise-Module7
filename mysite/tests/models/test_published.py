import pytest
from blog.factories import PostFactory
from blog.models import Post

@pytest.fixture
def published_post():
    return PostFactory(slug='published-post', status=1)

@pytest.fixture
def unpublished_post():
    return PostFactory(status=0)

@pytest.mark.django_db
def test_query_published_posts(published_post, unpublished_post):    
    published_posts = Post.published_objects.published()
    
    assert published_post in published_posts
    assert unpublished_post not in published_posts