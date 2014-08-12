#Scans the files storing friends ids and ids of message senders and opens the profile of non-senders to unfriend if needed

import helper

friends_names = {};

friends_ids = "friends_ids.txt"
message_senders = "message_senders.txt"

def get_non_senders():
  non_senders = [];
  friends = [];
  senders = [];
  f = open(friends_ids, "r");
  for line in f:
    nameid = line.split();
    id1 = nameid[0];
    friends_names[id1] = nameid[1];
    if len(nameid) >= 3:
      friends_names[id1] = friends_names[id1] + " " + nameid[2];
    friends.append(id1);
  f.close();
  f = open(message_senders, "r");
  for line in f:
    id1 = (line.split())[0];
    senders.append(id1);
  senders_dict = {};
  for sender in senders:
    if sender not in senders_dict.keys():
      senders_dict[sender] = 1;
  print len(senders_dict.keys());
  print len(senders);
  print "Got " + str(len(friends)-len(senders)) + " friends who never sent you any messages."
  for id in friends:
    if id not in senders:
      non_senders.append(id);
  print len(non_senders);
  return non_senders;

def open_non_senders():
  non_senders = get_non_senders();
  for i in non_senders:
    response = raw_input("Do you consider unfriending " + friends_names[i] + "? (Y/N): ");
    if response is "Y" or response is 'y':
      helper.open_browser(i);
      enter = raw_input("Press Enter when you are done: ");
    else:
      continue;

