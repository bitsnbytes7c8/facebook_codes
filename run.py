import sys;
import get_message_senders;
import friends_list;
import get_message_non_senders;

tokenfile = "token.txt";

def main():
  token = "";
  if len(sys.argv) == 1:
    f = open(tokenfile, "r");
    for line in f:
      token = line;
      break;
  else:
    token = sys.argv[1];

  get_message_senders.get_senders(token);
  friends_list.get_friends_list(token);
  get_message_non_senders.open_non_senders();

if __name__ == "__main__":
  main();
