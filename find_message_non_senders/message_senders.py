#Contains functions used by get_message_senders.py"

import urllib
import json
import sys;
import helper

token_filename = "token.txt"

def get_fifty(start, end, token):
  query= "SELECT originator, thread_id,updated_time FROM thread WHERE viewer_id=me() AND folder_id=0 LIMIT " + str(start) + "," + str(end);
  
  mesg_ids = helper.get_fql_json(query, token);
  sender_names = set();
  
  try:
    if len(mesg_ids['data']) == 0:
      return None;
    for thread in mesg_ids['data']:
      id = thread['originator'];
      if id not in sender_names:
        sender_names.add(id);
    print len(sender_names);
    #for id in mesg_ids['data']:
      #thread_id = id['thread_id'];
      #time = id['updated_time'];
      #query = "SELECT author_id from message WHERE thread_id="+thread_id;
      #sent_ids = helper.get_fql_json(query, token);
      #try:
        #for sent_id in sent_ids['data']:
          #sender_id = sent_id['author_id']
          #if sender_id is not '1310093194' and sender_id != 1310093194:
            #name = helper.get_name_from_id(sender_id, token);
            #if name not in sender_names.keys():
              #sender_names[name] = sender_id;
            #break;
      #except KeyError:
        #print sent_id['error']['message'];
        #return None
      #except:
        #return None

  except TypeError as e:
    print e;
    return None;
  except KeyError as e:
    print mesg_ids['error']['message'];
    return None;
  except:
    return None;
  return sender_names;

