#Writes all your friends names and ids to a file named friends_ids.txt

import urllib
import helper
#import facebook
#import access_token

filename = "friends_ids.txt";

def get_friends_list(token):
  query = "SELECT uid,name FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1=me() )";
  friends_json = helper.get_fql_json(query, token);
  print "Retrieved " + str(len(friends_json['data'])) + "friends";
  friends_list = []
  friends_name = [];
  i = 0;
  for person in friends_json["data"]:
    friends_list.append(person['uid']);
    friends_name.append(person['name']);
  f = open(filename, "w");
  for id,name in zip(friends_list, friends_name): 
    f.write((str(id) + " " + name+ "\n").encode('utf-8'));

