# Local Development with Git

## Introduction

This guide is designed to help you practice and understand the various commands
and practices involved in version control using Git.

## Git Basics

### Initializing a New Repository

To start using Git in your project, initialize a new Git repository with the
following command:

```bash
git init
```

### Staging Changes

Use the Git CLI to stage changes before committing them:

```bash
git add <path>
```

### Checking Staged Changes

See what changes are staged using:

```bash
git status
```

### Committing Changes

Commit your changes with a descriptive message:

```bash
git commit -m "<message>"
```

### Viewing Repository History

Explore your repository's history with:

```bash
git log
```

### Branching

Create and manage branches with Git:

- Create a new branch: `git branch <branch-name>`
- Check out a branch: `git checkout <branch-name>`
- Create and check out a new branch: `git checkout -b <branch-name>`

### Merging Changes

Merge changes from one branch to another:

```bash
git merge <branch-name>
```

### Updating Your Branch

Keep your branch up-to-date with the main branch:

```bash
# Switch to the main branch
git checkout main

# Pull changes from the remote repository
git pull

# Switch back to your branch
git checkout <branch-name>

# Merge changes from main to your branch
git merge main
```

### Returning to a Previous Version

Go back to a previous version of your project using:

```bash
# View commit history
git log

# Checkout a specific commit
git checkout <commit-hash>
```

### Stashing Changes

Temporarily save and retrieve uncommitted changes with:

```bash
# Stash changes
git stash

# Retrieve stashed changes
git stash pop
```

### Remote Repositories

Manage remote repositories with Git:

```bash
# Display existing remote URLs
git remote -v

# Add a new remote repository URL
git remote add <shortname> <remote-url>

# Update a remote repository URL
git remote set-url <existing-shortname> <new-remote-url>

# Rename a remote repository URL
git remote rename <old-shortname> <new-shortname>

# Remove a remote repository URL
git remote rm <existing-shortname>
```

## .gitignore

Use a `.gitignore` file to specify files you don't want included in your Git
history.

## Visual Studio Code Integration

Enhance your Git experience in VSCode:

- Utilize the Git Graph extension to visualize your repo's commit history.
- Leverage the Git Lens extension to investigate your repository's commit
  history.
- Understand how the file tree in VSCode highlights files with uncommitted
  changes.

## Best Practices

### Atomic Commits

Save your development progress using small commits with clear and helpful
messages.

### Feature Branches

Organize your development process by creating feature branches. Each branch can
correspond to a specific part of your project, and changes can be merged into
the main branch when completed.
