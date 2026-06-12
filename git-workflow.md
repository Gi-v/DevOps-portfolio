1. The Purpose of Git
Git is a Distributed VCS designed to track changes in source code during software development. Its primary purposes are:
Collaboration:Allows multiple developers to work on the same project simultaneously without overwriting each other's work.
History:Maintains a complete record of every change made, allowing you to "time travel" to any previous version of the project.
Experimentation:Through branching, developers can test new features in isolation without affecting the stable "main" code.

---

2. Essential Git Commands
   10 key commands:

1.  **git init**: Initializes a new Git repository in your current folder.
2.  **git clone**: Creates a local copy of a remote repository from GitHub.
3.  **git status**: Shows which files are staged, unstaged, or untracked.
4.  **git add <file>**: Moves changes from the working directory to the **Staging Area**.
5.  **git commit -m "msg"**: Saves your staged changes permanently into the **Local Repository**.
6.  **git branch <name>**: Creates a new line of development (a branch).
7.  **git checkout <branch>**: Switches your working directory to a different branch.
8.  **git pull**: Fetches updates from GitHub and merges them into your local branch.
9.  **git push**: Sends your local commits to the remote repository on GitHub.
10. **git merge <branch>**: Combines changes from one branch into your current branch.

---

3.Git States
Working Directory:The actual files you are editing on your computer. Changes here are untracked or modified
Staging Area: the git add area. It is a file that stores information about what will go into your next commit.
Repository (.git folder): Where Git stores the metadata and the compressed database for your project's history. not ton be touched. stay with you to the end

---

4. Good Commit Messages
A good commit message explains why a change was made in a simple but definative message

Examples:
* `feat: add login functionality to the user dashboard`
* `fix: resolve database connection timeout in RDS`
* `docs: update README with installation steps for Tomcat`
---

5. .gitignore
The `.gitignore` file tells Git which files or folders to ignore. You should use it for:
* **Sensitive Data:** Never commit `.env` files, API keys, or passwords.
* **System Files:** Ignore OS-specific files like `.DS_Store` (macOS) or `Thumbs.db` (Windows).
* **Dependencies:** Folders like `node_modules` or `target/` (for Java) which can be recreated using package managers.
* **Logs & Build Artifacts:** Temporary files created during the build process that don't belong in version control.

---

6. Branching & Merging Workflow
Branching is one of Git's most powerful features. It lets you develop features, fix bugs, or experiment in isolation without affecting the stable `main` branch.

**The Standard Feature Branch Workflow:**

1. **Create a new branch** from `main` for your work:
   ```
   git checkout -b feature/add-login-page
   ```

2. **Make your changes**, then stage and commit them with a good message:
   ```
   git add .
   git commit -m "feat: add login page with form validation"
   ```

3. **Push the branch** to GitHub:
   ```
   git push origin feature/add-login-page
   ```

4. **Open a Pull Request (PR)** on GitHub so teammates can review your changes.

5. **Merge the PR** into `main` once approved:
   ```
   git checkout main
   git merge feature/add-login-page
   ```

6. **Delete the branch** after merging to keep the repo tidy:
   ```
   git branch -d feature/add-login-page
   ```

**Why branches matter in DevOps:**
* **CI/CD pipelines** trigger automated tests on each branch before merging.
* **Protected branches** (e.g., `main`) prevent unreviewed code from going to production.
* **Short-lived branches** keep changes small and easy to review — a core DevOps practice.
