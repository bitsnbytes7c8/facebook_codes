import helper

def get_non_senders():
  non_senders = [];
  friends = [];
  senders = [];
  f = open("friends_ids.txt", "r");
  for line in f:
    id1 = (line.split())[0];
    friends.append(id1);
  f.close();
  f = open("message_senders.txt", "r");
  for line in f:
    id1 = (line.split())[0];
    senders.append(id1);
  for id in friends:
    if id not in senders:
      non_senders.append(id);
  return non_senders;



open_browser();
