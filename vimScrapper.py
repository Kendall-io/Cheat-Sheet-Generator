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

##
# Open the website to be scrapped
def openFile():
    prevent_word_repeat = ''
    with open("Vim Cheat Sheet - English.html") as website:
        soup = BeautifulSoup(website,"lxml")

        # Want to find all headers in the webpage.
        # Notes: This will be updated in the future to not only specify <h2> tag specifically
        for headers in soup.find_all('h2'):
            if (headers.get_text() != 'Additional Resources'):
                headersArray.append(headers.get_text().encode('utf-8'))
                i = 0
                firstLine = False
                for unorderedLists in headers.find_next('ul'):
                    output = unorderedLists.find_next_sibling('li')
                    if (output is not None):

                        # Avoid the double output of the lines after the first <li>...</li> is outputted
                        if prevent_word_repeat != output and firstLine == False:
                            getData(output.encode('utf-8'))
                            prevent_word_repeat = output
                            firstLine = True
                            i = i + 1
                        else:
                            firstLine = False

                list_of_commands_under_header.append(i)

# Cleans and seperates text objects
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
    replacementTagsForDescriptions = {'</li>', ''}

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
        keyCodeArray.append('\"code\": \"' +  keyPress.encode('utf-8') + '\"')
        #descriptionArray.append('description: ' + description.encode('utf-8').title())
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
# sectionstart += '\"' + headersarray[i].title() + '\": {\n' + '\t\"' + descriptionarray[i] + '\",\n' + '\t\t\"' + keycodearray[i] + '\",\n},'
# func - create the cheat sheet format for copying and pasting later on
def outputCheatSheetFile():
    sectionStart = '\"sections:\" {\n\t'
    tempNum = 0

    ##
    # Iterate through descriptions and keycodes for each header
    for i in range(0, len(headersArray)):
        sectionStart += '\"' + headersArray[i].title() + '\": {\n'
        tempNum += list_of_commands_under_header[i]

        for length in range(0, tempNum):
            if length == tempNum - 1:
                sectionStart += '\t\t\"' + descriptionArray[length] + '\",\n' + '\t\t\t\"' + 'description: ' + '\"' + descriptionArray[length] + '\"\n\t\t\t' + keyCodeArray[length] + '\n\t\t}\n'
            else:
                sectionStart += '\t\t\"' + descriptionArray[length] + '\",\n' + '\t\t\t\"' + 'description: ' + '\"' + descriptionArray[length] + '\"\n\t\t\t' + keyCodeArray[length] + '\n\t\t},\n'
        #tempNum = 0
        if (i == len(headersArray) - 1):
            sectionStart += '\n\t\t}\n\t\t'
        else:
            sectionStart += '\n\t\t},\n\t\t'
    print sectionStart

def main():
    openFile()
    outputCheatSheetFile()

main()
