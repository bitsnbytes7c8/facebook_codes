facebook_codes
==============

Contains python codes for facebook apps.

===========================================================================================================================

== Find Message Non Sender:

This folder contains code to track all the friends who have sent you a message and open the profiles of others (after asking you) to consider unfriending them.

To run, run the command:
  python run.py <accesstoken>
  
  where <accesstoken> is the access token generated by facebook (with permissions to read messages). If this command line arg is omitted, you can save the access token to a file named "token.txt" and it will be read from there. Doing neither will throw an exception and stop the program.
  
The files need to be in the same folder as the facebook-sdk (which is not included here) inorder for the friends_ids.py to run (I intent to fix this later).

===========================================================================================================================