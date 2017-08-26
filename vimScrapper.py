from bs4 import BeautifulSoup
import os

headersArray = []
list_of_commands_under_header = []
keyCodeArray = []
descriptionArray = []

# Cleans and seperates text objects
def getData(output):
    # Convert output from Navigable string to string
    output = str(output)
    keyPress = ''
    keyPressFound = False
    descriptionFound = False
    description = ''
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

        keyCodeArray.append('keycode: ' +  keyPress.encode('utf-8'))
        descriptionArray.append('description: ' + description.encode('utf-8').strip())
    except:
        pass

def openFile():
    with open("Vim Cheat Sheet - English.html") as website:
        soup = BeautifulSoup(website,"lxml")
        for headers in soup.find_all('h2'):
            if (headers.get_text() != 'Additional Resources'):
                headersArray[i].append(headers.get_text().encode('utf-8'))
                i = 0
                for unorderedLists in headers.find_next('ul'):
                    output = unorderedLists.find_next_sibling('li')
                    if (output is not None):
                        getData(output.get_text().encode('utf-8'))
                        i = i + 1
                    list_of_commands_under_header.append(i)

# Cheat Sheet format is as follows
def outputCheatSheetFile():
    sectionStart = '\"sections:\" {\n'
    tempNum = 0
    for i in range(0, len(headersArray)):
        #sectionstart += '\"' + headersarray[i].title() + '\": {\n' + '\t\"' + descriptionarray[i] + '\",\n' + '\t\t\"' + keycodearray[i] + '\",\n},'
        sectionstart += '\"' + headersArray[i].title() + '\": {\n'
        for commands in range(0, len(list_of_commands_under_header)):
            if commands != 0:
                tempNum = tempNum + list_of_commands_under_header[i]
                #for amount_of_previous_commands in range (0, len(commands)):
                #    tempNum = amount_of_previous_commands + commands[outCommands]
        for length in range(0, tempNum):
            if length == tempNum - 1:

            else:
                sectionstart += '\t\"' + descriptionArray[length].title() + '\",\n' + '\t\t\"' + keyCodeArray[length] + '\",\n},'
        tempNum = 0
        sectionStart += '\n},'
    print sectionStart

def main():
    openFile()

main()
