# Command Line Interface

## What is CLI?

> The Command Line Interface (CLI) is an editing environment that is text-based.
> It uses specified text (known as commands) to interact with the computer and
> perform numerous operations, including installing and working with programs.
>
> [https://www.freecodecamp.org/](https://www.freecodecamp.org/news/how-to-use-the-cli-beginner-guide/)

## Basic Command Unix-like

`man` : to show the usage manual, or help page, for a command

```bash
man <command>
man ls
```

`pwd` : to see where we are, we can print working directory

```bash
pwd
```

`ls` : lists the files and directories in the current working directory

```bash
ls
```

`cd` : to change directory

```bash
cd  <directory-name>
```

`cd ..` : to move up one directory

```bash
cd  ..
```

`mkdir` : to create a new directory(folder)

```bash
mkdir  <directory-name>
```

`touch` : to create a new file

```bash
touch  <file-name>
```

`rm` : to delete files or directories

```bash
rm <file-name>
rm -r <directory-name>
```

`echo` : to print the string pass to it as argument

```bash
echo "Hello world!"
```

`cat` : to print the contents of files

```bash
cat  file.txt
```

`exit` : to end a shell session

```bash
exit
```

`history` : to displays an enumerated list with the commands you’ve used in the
past

```bash
history
```

`clear` : to clean up the screen or you can use the shortcut `Ctrl + l`

```bash
clear
```

Windows CMD Equivalent Commands
1. Help or Manual:
In CMD, help provides a list of available commands or details about a specific command.

cmd
Copy code
help <command>
help dir
2. Print Working Directory:
Use cd without arguments to display the current directory.

cmd
Copy code
cd
3. List Files and Directories:
Use dir to list the contents of the current directory.

cmd
Copy code
dir
4. Change Directory:
Use cd to move between directories. cd .. moves up one directory.

cmd
Copy code
cd <directory-name>
cd ..
5. Create a Directory:
Use mkdir to create a new directory.

cmd
Copy code
mkdir <directory-name>
6. Create a File:
Windows CMD does not have a direct equivalent to touch. You can use echo to create a file or type nul to create an empty file.

cmd
Copy code
echo. > <file-name>
type nul > <file-name>
7. Delete Files or Directories:
Use del to delete files and rmdir to delete directories. Add /s to remove non-empty directories.

cmd
Copy code
del <file-name>
rmdir <directory-name>
rmdir /s <directory-name>
8. Print Text to Console:
Use echo to print a string to the console.

cmd
Copy code
echo Hello world!
9. Display File Contents:
Use type to print the contents of a file.

cmd
Copy code
type <file-name>
10. Exit Command Prompt:
Use exit to close the session.

cmd
Copy code
exit
11. Command History:
CMD does not have a history command, but you can use the doskey /history command to view the session's history.

cmd
Copy code
doskey /history
12. Clear Screen:
Use cls to clear the screen.

cmd
Copy code
cls

