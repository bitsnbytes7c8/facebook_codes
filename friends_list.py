#Writes all your friends names and ids to a file named friends_ids.txt

import urllib
import facebook
import access_token

token = access_token.get_token();
graph = facebook.GraphAPI(token);
profile = graph.get_object("me");
friends = graph.get_connections("me", "friends")
friends_list = [friend['id'] for friend in friends['data']]
friends_name = [friend['name'] for friend in friends['data']]

f = open("friends_ids.txt", "w");
for id,name in zip(friends_list, friends_name): 
  f.write((str(id) + " " + name+ "\n").encode('utf-8'));
