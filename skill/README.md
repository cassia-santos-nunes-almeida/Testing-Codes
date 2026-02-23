# STACK Exam Builder — Claude Skill

A Claude skill that preserves full project context across chat sessions, so you never have to re-explain your project.

## Folder Structure

```
skill/
├── SKILL.md                  # Instructions for Claude (how to load and behave)
├── context.md                # Stable project facts, architecture, constraints
├── active-session.md         # Current tasks, next steps, blockers (changes often)
├── decisions-log.md          # Chronological record of all decisions + rationale
├── personal-preferences.md   # Your communication/coding style (reusable across projects)
├── secrets-NEVER-UPLOAD.md   # LOCAL ONLY — credential placeholders
├── context-template.md       # Blank template for starting new projects
└── README.md                 # This file
```

## Installation

### Step 1 — Prepare the ZIP

Create a ZIP containing **only these files**:

```
SKILL.md
context.md
active-session.md
decisions-log.md
personal-preferences.md
context-template.md
```

**Do NOT include:**
- `secrets-NEVER-UPLOAD.md` (contains credential placeholders)
- `README.md` (installation instructions, not needed by Claude)
- Any `.git` folders or OS files (`.DS_Store`, `Thumbs.db`)

### Step 2 — Create the ZIP

```bash
cd skill/
zip -r ../stack-exam-builder-skill.zip \
  SKILL.md \
  context.md \
  active-session.md \
  decisions-log.md \
  personal-preferences.md \
  context-template.md
```

### Step 3 — Upload to Claude.ai

1. Go to [claude.ai](https://claude.ai)
2. Open **Settings** (gear icon, bottom-left)
3. Navigate to **Profile** > **Custom Instructions** or **Capabilities** > **Skills** (depending on your Claude plan)
4. Upload the ZIP file
5. Start a new conversation — Claude should respond with: *"Context loaded. Ready to continue STACK Exam Builder."*

## Updating Context After a Session

### When Claude suggests updates

At the end of significant sessions, Claude will say:
> "Session summary: here's what should be updated in your context files"

Follow these steps:

1. **Copy** the suggested content for each file
2. **Open** the relevant file(s) in your local `skill/` folder
3. **Replace** the changed sections (Claude will indicate exactly which sections changed)
4. **Update** the "Last Updated" date at the bottom of each modified file
5. **Re-ZIP and re-upload** (see below)

### Manual updates

If you made changes Claude didn't catch:
1. Edit the relevant file directly
2. For new decisions, append to `decisions-log.md` using the existing format
3. For completed tasks, move them from "Next Steps" to "Completed" in `active-session.md`

## Re-ZIP and Re-Upload

Every time you update a context file:

```bash
cd skill/
zip -r ../stack-exam-builder-skill.zip \
  SKILL.md \
  context.md \
  active-session.md \
  decisions-log.md \
  personal-preferences.md \
  context-template.md
```

Then re-upload the new ZIP to Claude.ai (same location as initial upload — it replaces the previous version).

## Maintenance Schedule

### Every session (as needed)
- Update `active-session.md` with completed tasks and new next steps
- Append new entries to `decisions-log.md`

### Every 2 weeks
- Run the **Health Checklist** (paste the checklist prompt into Claude — see below)
- Remove completed tasks that are no longer relevant
- Archive old decisions that have become "obvious" background knowledge into `context.md`

### Monthly
- Review `context.md` for outdated architecture or constraints
- Review `personal-preferences.md` — does it still reflect how you work?
- Check that `active-session.md` reflects reality, not aspirations

## Using personal-preferences.md Across Multiple Projects

`personal-preferences.md` is intentionally project-agnostic. To reuse it:

1. Keep a **master copy** in a central location (e.g., `~/claude-skills/personal-preferences.md`)
2. When creating a new project skill, copy it into the new skill folder
3. Changes to your preferences should be made to the master copy first, then propagated to project copies
4. Alternatively, symlink it if your ZIP tool supports following symlinks

## Backup Strategy

### Recommended: Git repository

```
~/claude-skills/
├── personal-preferences.md          # Master copy (shared across projects)
├── stack-exam-builder/
│   ├── SKILL.md
│   ├── context.md
│   ├── active-session.md
│   ├── decisions-log.md
│   ├── personal-preferences.md      # Copy or symlink
│   ├── secrets-NEVER-UPLOAD.md      # In .gitignore
│   └── context-template.md
├── future-project-2/
│   ├── SKILL.md
│   ├── context.md
│   └── ...
└── .gitignore                       # Contains: secrets-NEVER-UPLOAD.md
```

Initialize with:
```bash
cd ~/claude-skills
git init
echo "secrets-NEVER-UPLOAD.md" >> .gitignore
echo ".DS_Store" >> .gitignore
git add -A && git commit -m "Initial skill files"
```

### Alternative: Cloud folder

Use the same folder structure in Google Drive, Dropbox, or OneDrive. Just ensure `secrets-NEVER-UPLOAD.md` is excluded from sync or stored in a separate encrypted vault.

## Health Checklist

Paste this into Claude every 2 weeks:

---

> Review my context files and tell me:
> 1. What's outdated or completed that should be removed?
> 2. What decisions lack a documented reason?
> 3. What's in context.md that should be in active-session.md or vice versa?
> 4. Is there anything that looks like a sensitive value that shouldn't be here?
> 5. Is personal-preferences.md free of project-specific content?
> 6. What important things from recent sessions are NOT captured yet?

---
