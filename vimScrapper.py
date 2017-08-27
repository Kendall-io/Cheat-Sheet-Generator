from bs4 import BeautifulSoup
import os

# Holds all the header text in one place
headersArray = []

# Holds the amount of commands under each header
list_of_commands_under_header = []

# Holds the key shortcuts
keyCodeArray = []

# Holds the descriptions for the key shortcuts
descriptionArray = []

# Cleans and seperates text objects
def getData(output):

    ##
    # Convert output from Navigable string to string
    output = str(output)
    keyPress = ''
    description = ''
    keyPressFound = False
    descriptionFound = False

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

        ##
        # Save the key codes and the descriptions to the arrays for processing later on
        keyCodeArray.append('keycode: ' +  keyPress.encode('utf-8'))
        descriptionArray.append('description: ' + description.encode('utf-8').strip())
    except:
        pass

##
# Open the website to be scrapped
def openFile():
    with open("Vim Cheat Sheet - English.html") as website:
        soup = BeautifulSoup(website,"lxml")
        for headers in soup.find_all('h2'):
            if (headers.get_text() != 'Additional Resources'):
                headersArray.append(headers.get_text().encode('utf-8'))
                i = 0
                for unorderedLists in headers.find_next('ul'):
                    output = unorderedLists.find_next_sibling('li')
                    if (output is not None and (output.previous_sibling != output and output.previous_sibling is not None)):
                        getData(output.get_text().encode('utf-8'))
                        print output.get_text()
                        i = i + 1
                list_of_commands_under_header.append(i)
                print '------'

##
# Cheat Sheet format is as follows
# sectionstart += '\"' + headersarray[i].title() + '\": {\n' + '\t\"' + descriptionarray[i] + '\",\n' + '\t\t\"' + keycodearray[i] + '\",\n},'
# func - create the cheat sheet format for copying and pasting later on
def outputCheatSheetFile():
    sectionStart = '\"sections:\" {\n'
    tempNum = 0
    for i in range(0, len(headersArray)):
        sectionStart += '\"' + headersArray[i].title() + '\": {\n'
        for commands in range(0, len(list_of_commands_under_header)):
            if commands != 0:
                tempNum = tempNum + list_of_commands_under_header[i]
                #for amount_of_previous_commands in range (0, len(commands)):
                #    tempNum = amount_of_previous_commands + commands[outCommands]
        for length in range(0, tempNum):
            if length == tempNum - 1:
                sectionStart += '\t\"' + descriptionArray[length].title() + '\",\n' + '\t\t\"' + keyCodeArray[length] + '\",\n}'
            else:
                sectionStart += '\t\"' + descriptionArray[length].title() + '\",\n' + '\t\t\"' + keyCodeArray[length] + '\",\n},'
        tempNum = 0
        sectionStart += '\n},'
    print sectionStart

def main():
    openFile()
    #outputCheatSheetFile()

    # Debugging
    for i in range (0, len(list_of_commands_under_header)):
        print list_of_commands_under_header[i]
        print '---'
main()
