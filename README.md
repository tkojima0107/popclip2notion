## What is this?
This is an extension to connect [PopClip](https://pilotmoon.com/popclip/) to [Notion](https://www.notion.so/product) using an official notion API.

You can send a selected text to your notion workspace quickly.

For now, one database and one block(including a page) can be configure to be sent to.

This extension is disabled on notion client app.
If you want to enable it, delete the line  `<string>notion.id</string>` in Config.plist.

**Please use this extension at your own rick. We assume no responsibility whatsoever for any damages resulting from the use of this site.**

## Requirement
This extension is based on a python3 script.

If you don't install python3 on your Mac, please install it.

## Get your notion integrations
Before installing this extension, please create an integration (obtaining Internal Integration Token)
and invite it to your notion page or database, according to [the official instruction by Notion](https://developers.notion.com/docs/getting-started).

## How to install
1. Download this repository on your Mac
2. Just double click "popclip2notion.popclipext"

This is not an official extension. So, you will see a warning dialog when installing it.

Please see the link: https://github.com/pilotmoon/PopClip-Extensions#extension-signing

## How to setup
This extension support two methods to add a selected text to your notion workspace.

1. adding an entry to database
1. adding a child block to a parent block

For adding to database, please fill the following options:
* Internal Integration Token
* database ID

Then, choose "database" option for "adding to".

You can obtain the database ID from the URL.
Here is an offitial explanation

```
https://www.notion.so/myworkspace/a8aec43384f447ed84390e8e42c2e089?v=...
                                  |--------- Database ID --------|
```

For adding to a page of a block, please fill the following options:
* Internal Integration Token
* block ID
* block type

Then, choose "block" option for "adding to".

You can also obtain the block ID from the URL like as follows:
```
https://www.notion.so/myworkspace/'page title'-0123456789abcdef0123456789abcdef#0123456789abcdef0123456789abcdef
                                               |--------- Page ID ------------| |--------- block ID -----------|
```

Page ID is also block ID.
So, if you want to add a block to a page,
please specify the page ID as block ID.

You can choose a type of the added block as following:

* paragraph
* heading 1
* heading 2
* heading 3
* bulleted list item
* numbered list item
* to_do
* toggle

Currently, adding it as a child page is not supported.

## Checking the sending result
If the configuration is not valid (e.g., database ID is not specified), popclip will show "X".

For some error in accessing your notion,
it will show the error reason of HTTP.

In case of success,
it will show "Sent successfully"