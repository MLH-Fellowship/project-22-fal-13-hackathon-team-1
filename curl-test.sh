#!/bin/bash
curl -d "name=Tara&email=someemail@gmail.com&content=Testing this script" -X POST http://localhost:5000/api/timeline_post
curl http://localhost:5000/api/timeline_post

