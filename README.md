# Cheat Sheet Generator
### Prerequisites
* BeautifulSoup4
* Python2.7

### Purpose
Webscrapes a webpage and gets the data from it if it is formed in similar syntax:
```
Key Code - Description

Example:

H - move cursor left
```
<br>

The format of the template is:
```
"sections": {
    "Section Description": {
         "What the command does": {
             "description": "",
             "code": ""
         },
         "Example 2": {
             "description": "",
             "code": ""
         }
    },

```

### Current Problems:
Have to remove tags from the current strings that are stored in the keyCode array and the descriptions array:
<br>
Currently they have these tags with them.
```
keycode: <li><kbd>:o file</kbd>
keycode: <li><kbd>:saveas file</kbd>
keycode: <li><kbd>:close</kbd>
keycode: <li><kbd>K</kbd>
keycode: <li><kbd>h</kbd>
keycode: <li><kbd>j</kbd>
keycode: <li><kbd>k</kbd>
keycode: <li><kbd>l</kbd>
keycode: <li><kbd>H</kbd>

```

What i want is something in the form of
```
keycode: h

```

~~For some reason, it will read anything after the first li tags twice.~~
<br>
~~Example shown:~~
```
:help keyword - open help for keyword
:o file - open file
:o file - open file
:saveas file - save file as
:saveas file - save file as
:close - close current pane
:close - close current pane
K - open man page for word under the cursor
K - open man page for word under the cursor
------

```

### Credits:
Thank you centurix for the template that he provided in the downloads.
