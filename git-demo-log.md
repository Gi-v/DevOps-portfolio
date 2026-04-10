# Git Workflow — Practical Demonstration (Parts 2–6)

This file documents running each Git concept from `git-workflow.md` Parts 2 through 6 in this real repository.

---

## Part 2 — Essential Git Commands (in practice)

| # | Command | What it did in this repo |
|---|---------|--------------------------|
| 1 | `git init` | Already initialised — the `.git/` folder exists at the root |
| 2 | `git clone` | This repo was cloned from `https://github.com/Gi-v/DevOps-portfolio` |
| 3 | `git status` | Shows current branch, staged/unstaged files (see Part 3 demo below) |
| 4 | `git add <file>` | Used to stage `.gitignore`, `git-workflow.md`, and demo files |
| 5 | `git commit -m "msg"` | Every commit in this PR uses a proper conventional message |
| 6 | `git branch <name>` | Branch `copilot/create-screenshots-and-pull-request` was created for this work |
| 7 | `git checkout <branch>` | Switched onto the feature branch before making changes |
| 8 | `git pull` | Pulled latest from `origin` before starting |
| 9 | `git push` | Pushes all commits to `origin` to open the Pull Request |
| 10 | `git merge <branch>` | Will happen when this PR is merged into `main` on GitHub |

---

## Part 3 — Git States (live demo)

Three states were demonstrated by creating, staging, and committing a temporary file:

### State 1 — Working Directory (Untracked)
```
$ echo "# Temporary demo file" > demo_state_example.txt
$ git status

On branch copilot/create-screenshots-and-pull-request
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        demo_state_example.txt

nothing added to commit but untracked files present
```

### State 2 — Staging Area (after `git add`)
```
$ git add demo_state_example.txt
$ git status

On branch copilot/create-screenshots-and-pull-request
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   demo_state_example.txt
```

### State 3 — Repository (after `git commit`)
```
$ git commit -m "docs: demonstrate Git states - working dir, staging, committed"
[copilot/create-screenshots-and-pull-request 0cbb18d] docs: demonstrate Git states - working dir, staging, committed
 1 file changed, 1 insertion(+)
 create mode 100644 demo_state_example.txt

$ git status
On branch copilot/create-screenshots-and-pull-request
nothing to commit, working tree clean
```

---

## Part 4 — Good Commit Messages (used throughout this PR)

All commits in this PR follow the **Conventional Commits** standard:

```
docs: demonstrate Git states - working dir, staging, committed
chore: remove temporary git states demo file
fix: expand .gitignore with OS, Node, Python, IDE, and secrets patterns
docs: add Part 6 — branching and merging workflow to git-workflow.md
docs: add git-demo-log.md with Parts 2–6 practical demonstration
```

Format: `<type>: <short description>`
- `feat` — new feature
- `fix` — bug fix or correction
- `docs` — documentation only
- `chore` — maintenance (no production code change)

---

## Part 5 — `.gitignore` (expanded)

The `.gitignore` file was expanded from a basic Jekyll template to cover:

- 🔒 **Sensitive files** — `.env`, `*.pem`, `*.key`, `secrets.yml`
- 💻 **OS files** — `.DS_Store`, `Thumbs.db`
- 📦 **Dependencies** — `node_modules/`, `venv/`, `target/`
- 🪵 **Logs & artifacts** — `*.log`, `*.tmp`, `logs/`, `build/`
- 🛠️ **IDE files** — `.vscode/`, `.idea/`

See the updated [`.gitignore`](.gitignore) for the full list.

---

## Part 6 — Branching & Merging Workflow (live demo)

This entire set of changes was done on a **feature branch**:

```
$ git checkout -b copilot/create-screenshots-and-pull-request
Switched to a new branch 'copilot/create-screenshots-and-pull-request'

$ git push origin copilot/create-screenshots-and-pull-request
```

Commit history on this branch:
```
b61cfc6  chore: remove temporary git states demo file
0cbb18d  docs: demonstrate Git states - working dir, staging, committed
e0ddd6c  gitWorkflow   ← branch point from main
```

This Pull Request on GitHub will merge all of the above into `main`, completing the full feature branch lifecycle:

**`main`** ← merge ← **`copilot/create-screenshots-and-pull-request`**
