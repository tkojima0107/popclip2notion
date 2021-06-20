import os
import sys

import urllib.request
import json


TOKEN= "Bearer " + os.environ['POPCLIP_OPTION_TOKEN']
if TOKEN == "":
    sys.exit(1)

DB_ID = os.environ['POPCLIP_OPTION_DATABASEID']
BLOCK_ID = os.environ['POPCLIP_OPTION_BLOCKID']
BLOCK_TYPE = os.environ['POPCLIP_OPTION_BLOCKTYPE']
mode = os.environ['POPCLIP_OPTION_MODE']
dbmode = mode == "database"
blockmode = mode == "block"

if dbmode and DB_ID == "":
    sys.exit(1)
elif blockmode and BLOCK_ID == "":
    sys.exit(1)

URL = "https://api.notion.com/v1/pages" if dbmode else "https://api.notion.com/v1/blocks/" + BLOCK_ID + "/children"

req_header = {
    "Authorization": TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13",
    "User-Agent": "popclip-to-notion/0.1",
}

if dbmode:
    req_data = json.dumps({
        "parent": {"database_id": DB_ID},
        "properties": {
            "Name": {"title": [ {"text": {"content": os.environ['POPCLIP_TEXT'] } } ]},
        }
    })
    method = "POST"
elif blockmode:
    req_data = json.dumps({
        "children": [
            {   "object": "block", "type": BLOCK_TYPE,
                BLOCK_TYPE: {
                    "text": [{ "type": "text", "text": {"content": os.environ['POPCLIP_TEXT']}}]
                }
            }
        ]
    })
    method = "PATCH"

req = urllib.request.Request(URL, data=req_data.encode(), method=method, headers=req_header)

try:
    with urllib.request.urlopen(req) as response:
        body = json.loads(response.read())
        headers = response.getheaders()
        status = response.getcode()
    print("Sent successfully")

except urllib.error.URLError as e:
    print(e)


