import unittest
from peewee import *

from app import TimelinePost
from playhouse.shortcuts import model_to_dict
MODELS = [TimelinePost]

# use an in-memory SQLite for tests
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self) :
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db. create_tables (MODELS)

    def tearDown(self):
        test_db.drop_tables (MODELS)
        #close connection to database
        test_db.close()
    
    def test_timeline_post(self):
        first_post= TimelinePost.create(name='John Doe', 
email='john@example.com', content='Hello world, I\'m John!')
        assert first_post. id == 1
        second_post = TimelinePost.create(name='Jane Doe',
email='jame@example.com'
, content='Hello world, I\'m Jane!')
        assert second_post. id == 2 

#for assert statements
get_timeline_posts = [
    model_to_dict(item)
    for item in TimelinePost  
]


assert get_timeline_posts[0]['name'] == 'John Doe'
assert get_timeline_posts[1]['name'] == 'Jane Doe'
assert get_timeline_posts[0]['email'] == 'john@example.com'
assert get_timeline_posts[1]['email'] == 'jane@example.com'
assert get_timeline_posts[0]['content'] == 'Hello world, I\'m John!'
assert get_timeline_posts[1]['content'] == 'Hello world, I\'m Jane'