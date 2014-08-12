#Contains helper functions for querying used by other programs

import json
import urllib
import webbrowser

def get_fql_json(query, access_token):
  params = urllib.urlencode({'q':query, 'access_token':access_token});
  url = "https://graph.facebook.com/fql?"+params;
  data = urllib.urlopen(url).read();
  rjson = json.loads(data);
  return rjson;

def get_name_from_id(uid, token):
  query = "SELECT name FROM user WHERE uid="+str(uid);
  name_json = get_fql_json(query, token);
  name = name_json['data'];
  for n in name:
    return n['name'];

def get_detail_from_id(detail, uid, token):
  query = "SELECT" + detail + "FROM user WHERE uid="+str(uid);
  detail_json = get_fql_json(query, token);
  detail = detail_json['data'];
  for d in detail:
    return d[detail];

def open_browser(id):
  webbrowser.open('http://facebook.com/' + id);
