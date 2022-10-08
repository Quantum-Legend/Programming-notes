# Command Line commands:

> The command line starts with a Current Working Directory (CWD) open.

---
## Directory:
| Command            | Action                                               |
|--------------------|------------------------------------------------------|
| dir                | opens a list of directories and files inside the CWD |
| dir Desktop/Videos | shows the directories inside the Videos folder without changing the path or the CWD |
| dir /a             | shows all the files and directories including the ones that are hidden |
| dir \*.png         | will only show those files that end with .png (The "\*" is a wild card character which tells that it doesnt matter what comes before but it should end with that specific thing) |
| tree               | shows the directory tree (Not only the folders inside the CWD but also what is inside those folders) |

---
## Changing Directory:
| Command           | Action                                               |
|-------------------|------------------------------------------------------|
| cd                | change directory |
| cd Desktop        | changes directory to Desktop inside the CWD  (You can use the Tab key to autocomplete the directory name) |
| cd Desktop/Videos | changes directory to Videos inside Desktop inside the CWD |
| cd ..             | goes back to the previous directory |
| cd ../..          | goes back 2 directories |

> You can also change the absolute path to a different directory instead of moving relatively

| Command               | Action                                               |
|-----------------------|------------------------------------------------------|
| cd Desktop            | moves the directory to Desktop which is inside the CWD (relative movement) |
| cd "C:/Program Files" | moves the directory to the given path which is an absolute path (The quotes are important whenever there are whitespaces in the path name) |

---
## Running or opening files:
> Typing the name of a file in the cmd line opens that file

| Command | Action                                               |
|---------|------------------------------------------------------|
| path    | displays the windows path (Environment Variables) |

> Typing a command to run a file (for example, a .exe file) after the path command, windows will look through the CWD for the file first, and if it is not there, it then searches for it in all the directories in the path variable. In this way, you can run a file from anywhere in the cmd line as long as it exists in a directory in the path variable.
> * From the GUI: Right click on your Computer,  go in properties, then Advanced System Settings, in there click on Environment Variables, then you can edit the PATH Variable

---
## Making and Deleting directories:
| Command       | Action                                               |
|---------------|------------------------------------------------------|
| mkdir name    | makes a new directory/folder called name in the CWD |
| rmdir name    | removes/deletes the directory called name from the CWD (the directory must be empty) |
| rmdir /s name | removes/deletes the directory called name along with all the contents in it from the CWD (shows a confirmation message) |

---
## Drives:
| Command | Action                                               |
|---------|------------------------------------------------------|
| wmic logicaldrives get name | gives all the available drives on your Computer |

> Typing in the drive letter in the cmd line changes the CWD to that drive

Eg:
```
C:/>e:
E:/>
```

---
## File Attributes:
> Type attrib /?

Example:
* Let's say you have a file called bacon.txt
* Type attrib in the cmd line, it will show the files with their attributes
* If you want to make this file hidden, type attrib +h bacon.txt
* If you want to remove this hidden attribute and add a read-only attribute, type attrib +r -h bacon.txt

| Command                        | Action                                               |
|--------------------------------|------------------------------------------------------|
| del bacon.txt                  | deletes the file bacon.txt |
| type bacon.txt                 | displays out the contents of bacon.txt |
| echo sometext > bacon.txt      | overwrites the contents of bacon.txt with sometext if the file already exists; creates a new file called bacon.txt with the text sometext, if the file does not exists. |
| echo somemoretext >> bacon.txt | appends the text somemoretext to the file bacon.txt instead of overwriting the contents |

> You can save the results of any command to a file by using the > symbol like echo

For example:
```
dir > directory.txt 
```
> This saves the output of the dir command to a text file directory.txt

---
## Copying and moving files:
| Command                      | Action                                               |
|------------------------------|------------------------------------------------------|
| copy [Source] [Detination]   | copies files |
_Example:_ copy bacon.txt TestFolder = copies the file bacon.txt to the folder TestFolder 
| xcopy [Source] [Destination] | copies files and directory trees (default: only copies files) |
_Example:_ xcopy Apples Bacons = copies contents of Apples to Bacons (Using the option /s (xcopy Apples Bacons /s) copies all contents of Apples directory to Bacons)
| move [Source] [Destination]  | moves a file or folder to a destination directory |
_Example:_ move Apples Bacons = moves the Apples folder to Bacons folder
| rename [Old name] [New name] | renames a folder |
_Example:_ rename Bacon Ham = changes the name of the folder Bacon to Ham

---
## Other Commands:
> Pressing the up and down arrow keys will take you through the command history (or all the commands you typed till then)

> Typing /? in front of a command displays the details of that command

| cls | clears screen

> Type color /? on your cmd line for information about this cmd

---
## Useful information:
> * The "Program Files" folder on your computer is the folder where most of your 64 bit applications are present. 
> * The Program Files (x86) folder on the other hand stores the 32 bit applications on your computer.
> * The Users folder has the folders of the different users using your computer