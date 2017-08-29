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
{
	"name": "Cheatsheet Template",
	"description": "Cheatsheet template",
	"author": "Chris Read",
	"email": "centurix@gmail.com",
	"repository": "http://fipo.co",
	"version": "0.1",
	"sections": {
		"Section 1": {
			"Example 1": {
				"description": "Example 1 description",
				"code": "EXAMPLE 1 CODE"
			},
			"Example 2": {
				"description": "Example 2 description",
				"code": "EXAMPLE 2 CODE"
			}
		},
		"Section 2": {
			"Example 1": {
				"description": "Example 1 description",
				"code": "EXAMPLE 1 CODE"
			},
			"Example 2": {
				"description": "Example 2 description",
				"code": "EXAMPLE 2 CODE"
			}
		}
	}
}
```


### What to implement in the future:
- Argument command where it wgets the website and then extracts website data from it.
- Adjust cheaty configuration in the linux mint applet where user can choose the commands that it wants
- Finds the users path for cheaty to implement directly with interaction.
~### Current Problems:~
~Fix format of text and fix output as well. It is not iterating at the starting header~<br>

~Have to remove tags from the current strings that are stored in the keyCode array and the descriptions array:~
<br>
~Currently they have these tags with them.~
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
~What i want is something in the form of~
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
<br>
Thank you bgusach for code to replace certain words in a string
