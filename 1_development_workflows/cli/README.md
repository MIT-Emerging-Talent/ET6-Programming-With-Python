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
________________________________________________________________________
Here is the Windows Command Prompt version written in the same style as your example:

```markdown
# Command Line Interface

## What is CLI?

> The Command Line Interface (CLI) is an editing environment that is text-based.
> It uses specified text (known as commands) to interact with the computer and
> perform numerous operations, including installing and working with programs.
>
> [https://www.freecodecamp.org/](https://www.freecodecamp.org/news/how-to-use-the-cli-beginner-guide/)

## Basic Commands in Windows CMD

`help` : to display a list of commands or show details about a specific command

```cmd
help <command>
help dir
```

`cd` : to print the current working directory or change directories

```cmd
cd
cd <directory-name>
```

`cd ..` : to move up one directory

```cmd
cd ..
```

`dir` : to list the files and directories in the current directory

```cmd
dir
```

`mkdir` : to create a new directory (folder)

```cmd
mkdir <directory-name>
```

`echo` : to create a new file or print a string to the console

```cmd
echo. > <file-name>
echo Hello world!
```

`type nul` : to create an empty file

```cmd
type nul > <file-name>
```

`del` : to delete files

```cmd
del <file-name>
```

`rmdir` : to delete directories (use `/s` to remove non-empty directories)

```cmd
rmdir <directory-name>
rmdir /s <directory-name>
```

`type` : to print the contents of files

```cmd
type <file-name>
```

`exit` : to end a Command Prompt session

```cmd
exit
```

`doskey /history` : to display a list of the commands you’ve used in the current session

```cmd
doskey /history
```

`cls` : to clear the screen

```cmd
cls
```
```
