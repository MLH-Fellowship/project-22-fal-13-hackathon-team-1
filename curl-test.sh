#!/bin/bash

#create random post
curl -X POST http://localhost:5000/api/timeline_post -d 'name=Test&email=testemail@test.com&content=This is a test to see if database and the app are connected with reading, writing, and deleting.'

#show it's added
curl http://localhost:5000/api/timeline_post | jq '[.timeline_posts[]]'

#Delete 'test' user | For now hardcoded into __init__.py
curl -X DELETE http://localhost:5000/api/timeline_post

#show it's deleted
curl http://localhost:5000/api/timeline_post | jq '[.timeline_posts[]]'

