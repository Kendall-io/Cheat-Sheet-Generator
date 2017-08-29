##
# templateFormatter.py
# This program will read an html file that has lists and headers and those lists and headers will be put into a template used in the cheaty applet
# @author: Kendall Molas, Randy Martinez

from bs4 import BeautifulSoup
import re

# This will be for eventually parsing the website name
import os

# Holds all the header text in one place
headersArray = []

# Holds the amount of commands under each header
list_of_commands_under_header = []

# Holds the key shortcuts
keyCodeArray = []

# Holds the descriptions for the key shortcuts
descriptionArray = []

def main():
    #userInput = input('Input html file name here (DO NOT INCLUDE .html EXTNESION)')
    #if not os.path.exists(userInput + '.html'):
    #    os.makedirs(userInput)
    #os.chdir('userInput')
    readWebsite()
    outputCheatSheetFile()

##
# Open the website to be scrapped
def readWebsite():
    prevent_word_repeat = ''
    with open("Vim Cheat Sheet - English.html") as website:
        soup = BeautifulSoup(website,"lxml")

        # Want to find all headers in the webpage.
        # Notes: This will be updated in the future to not only specify <h2> tag specifically
        for headers in soup.find_all('h2'):
            if (headers.get_text() != 'Additional Resources'):
                headersArray.append(headers.get_text().encode('utf-8'))
                total_li_per_line = 0
                firstLine = False
                for unorderedLists in headers.find_next('ul'):
                    output = unorderedLists.find_next_sibling('li')
                    if (output is not None):

                        # Avoid the double output of the lines after the first <li>...</li> is outputted
                        if prevent_word_repeat != output and firstLine == False:
                            getData(output.encode('utf-8'))
                            prevent_word_repeat = output
                            firstLine = True
                            total_li_per_line = total_li_per_line + 1
                        else:
                            firstLine = False

                list_of_commands_under_header.append(total_li_per_line)

# Cleans and seperates the lines of text that are inputted
def getData(output):

    ##
    # Convert output from Navigable string to string
    output = str(output)
    keyPress = ''
    description = ''
    keyPressFound = False
    descriptionFound = False

    # The tags that need to be removed
    replacementTagsForKeys = {'<li>': '', '<kbd>': '', '</kbd>': ''}
    replacementTagsForDescription = {'</li>', ''}

    ##
    # Separates the key shortcut for vim commands from the description.
    try:
        for i in range(0,len(output)):
            if (output[i] != '-' and keyPressFound == False):
                keyPress += output[i]
            elif (output[i] == '-' and keyPressFound == False and descriptionFound == False):
                descriptionFound = True
                keyPressFound = True
            else:
                if (output[i] == ':'):
                    pass
                else:
                    description += output[i]

        # Removes the tags from the lines
        keyPress = tag_removal(keyPress, replacementTagsForKeys)

        # Tag_removal does not work due to function, so using .replace() is used instead
        description = description.strip().replace('</li>', '')

        ##
        # Save the key codes and the descriptions to the arrays for processing later on
        keyCodeArray.append('\"code\": \"' +  keyPress.encode('utf-8').strip() + '\"')
        descriptionArray.append(description.encode('utf-8').title())

    except:
        pass

# Thank you to bgusach for the multi-replacement string code using regex
# https://gist.github.com/bgusach/a967e0587d6e01e889fd1d776c5f3729

def tag_removal(string, replacements):
    substr = sorted(replacements, key = len, reverse=True)

    regexp = re.compile('|'.join(map(re.escape, substr)))

    return regexp.sub(lambda match: replacements[match.group(0)], string)

# Cheat Sheet format is as follows
'''
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
'''
# func - create the cheat sheet format for copying and pasting later on

def outputCheatSheetFile():
    sectionStart = '\"sections\": {\n\t'
    counter = 0

    ##
    # Iterate through descriptions and keycodes for each header
    for num in range(0, len(list_of_commands_under_header)):
        sectionStart += '\"' + headersArray[num] + '\": {\n'

        # Only want to input amount that are inside each header. Counter used
        for i in range(0, list_of_commands_under_header[num]):
            if i == list_of_commands_under_header[num] - 1:
                sectionStart += '\t\t\"' + descriptionArray[counter] + '\",\n' + '\t\t\t\"' + 'description\": ' + '\"' + descriptionArray[counter] + '\"\n\t\t\t' + keyCodeArray[counter] + '\n\t\t}\n'
            else:
                sectionStart += '\t\t\"' + descriptionArray[counter] + '\",\n' + '\t\t\t\"' + 'description\": ' + '\"' + descriptionArray[counter] + '\"\n\t\t\t' + keyCodeArray[counter] + '\n\t\t},\n'

            counter = counter + 1

        if (num == len(list_of_commands_under_header) - 1):
            sectionStart += '\n\t\t}\n\t'
        else:
            sectionStart += '\n\t},\n\t'

    createCheatSheet(sectionStart)

def createCheatSheet(section):
    with open('Vim.json', 'w') as chtSheet:
        chtSheet.write('{\n\t\"name\": ' + '\"Vim Template\",\n\t' + '\"description\":' + '\"Vim Template\",\n\t' + '\"author\",\n\t' + '\"email\":' + '\"repository\",\n\t' + '\"version\":' + '\"0.1\",\n\t')
        chtSheet.write(section)
        chtSheet.write('}\n}')

if __name__ == '__main__':
    main()
