# Local/Remote Development

## GitHub SSH Key

### Connecting with SSH

Enhance the security of your GitHub interactions by connecting your computer to
your GitHub account using an SSH key. This enables secure cloning, pushing, and
pulling using your SSH connection.

## GitHub Repositories

### Creating and Configuring Repositories

- **Creating a New Repository:** Initialize a new repository on GitHub with
  ease.

- **Writing Repository Descriptions:** Craft meaningful descriptions for your
  repositories to convey their purpose and functionality.

- **GitHub Pages:** Turn on GitHub Pages to host a website directly from your
  repository.

- **Main Branch Protection:** Configure your repository to block pushing to the
  main branch and merging until Continuous Integration (CI) checks pass.

## Git Remote/Local Connection

### Mastering Git Commands

- **Cloning Repositories:** Use `git clone <remote-url>` to clone a remote
  repository to your local machine.

- **Initializing and Connecting Repositories:** Set up a new local repository
  and link it to an empty remote repository.

- **Pushing and Pulling:** Utilize `git push` to upload local content to a
  remote repository. Understand the difference between `git fetch` and
  `git pull`.

- **Branch Operations:** Manage changes by pushing and pulling between remote
  and local branches. Distinguish between `git fetch` and `git pull`.

## Pull Requests

### Collaborative Code Integration

- **Creating Pull Requests:** Generate pull requests between branches for
  seamless integration.

- **Pull Request Templates:** Implement PR templates with checklists to ensure
  code quality before merging to the main branch.

## Continuous Integration

### Maintaining Code Quality

- **GitHub Actions:** Leverage GitHub Actions to run CI checks before merging a
  pull request to the main branch.

## Local/Remote Branching Workflow

### Best Practices for Collaboration

1. **Check Out a New Local Branch:** Create a new local branch for your
   contribution.

2. **Synchronize with Main:** Keep your local main in sync with remote main by
   pulling changes.

3. **Merge Workflow:** Merge changes from local main to your new branch,
   resolving conflicts if necessary.

4. **Code Formatting and Linting:** Ensure code quality by formatting and
   linting your changes.

5. **Push to Remote:** Push your local branch to the remote repository.

6. **Open Pull Request:** Initiate a pull request from your branch to the main
   branch.

7. **PR Checklist:** Complete the PR checklist to verify the correctness of your
   changes.

8. **CI Checks:** Confirm that all CI checks pass successfully.

9. **Merge to Main:** Merge your remote branch into the main branch.

10. **Branch Cleanup:** Optionally, delete the branch after successful merging.
