# yocket-profile

Yocket Assignment for post, comment creation and liking of posts

### Steps to run the project

pip install -r requirements.txt
export PYTHONPATH="/Users/shashankjain/Desktop/yocket/interfaces"


Then mongodb needed to be installed in the system which is needed to be run on port 27017
To run the mongodb server
> mongod –port 27017

cd interfaces/
python xaas/app.py

Which will run the server on
http://127.0.0.1:8888/api/

With following endpoints or namespaces to distinguish creation of users, creating a post, commenting on a post, likes/unlikes the post

Post
Comments
Users
Likes

These are the namespaces with following the api request to the server.


