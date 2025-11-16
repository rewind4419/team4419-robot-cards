# Git & GitHub Workshop
## Team 4419 Programming Onboarding

**Duration:** 1 hour

---

## What is Git & GitHub?

### The Problem
How do 10 people work on the same code without overwriting each other's work?

### The Solution: Git

**Git** is version control software. Think of it like Google Docs revision history, but way more powerful.

- See every change ever made (who, what, when, why)
- Work on your own copy without breaking the main code
- Undo mistakes easily
- Merge everyone's work together intelligently

**GitHub** is a website that hosts Git projects online.

- Cloud storage for code
- Collaboration tools (discussions, reviews, automation)
- Industry standard (Google, Microsoft, NASA, everyone uses it)

---

## Key Concepts

### Repository (Repo)
A project folder that Git tracks. Contains all your code and its complete history.

### Branch
Your own workspace to make changes without affecting the main code.

**Analogy:** Like making a copy of a Google Doc to try different edits, then merging the good stuff back.

```
main branch:      A --- B --- C ----------- E
                           \               /
your branch:                D --- review ---
```

- **main** = stable, working version
- **your-branch** = experimental workspace

### Commit
A saved snapshot of your changes with a description.

Like hitting "Save" but with a note: "Added shooter motor code"

### Pull Request (PR)
You're asking: "I made some changes. Can someone review them before we merge?"

**Yes, the name is weird.** Blame the Git inventors.

**The flow:**
1. You make changes in your branch
2. You open a PR
3. Programming Lead reviews your code
4. They approve (or ask for changes)
5. You merge - your code goes live!

**This is how Google, Microsoft, and NASA write code.**
**This is how we write robot code.**

---

## Today's Exercise

### The Mission
Create a YAML file describing your dream robot design (with ASCII art!).

When approved and merged, it appears here: https://rewind4419.github.io/team4419-robot-cards/

### What You'll Learn
The complete workflow that professional developers use:
- Clone → Branch → Commit → Push → Pull Request → Review → Merge

**Same workflow we use for robot code, scouting apps, everything.**

### The Review Process
- Programming Leads or Mentors review your PR
- They check formatting, look at your design, maybe ask questions
- If good, they approve
- You merge and your card goes live!

**Why review?** Catches mistakes, ensures quality, everyone learns.

---

## Getting Started

### Step 1: Create Your GitHub Account

**Choose your username wisely** - it's public and permanent.

Good patterns:
- Initials + numbers (`ak2026`)
- Nickname (`codewizard`)
- Professional-sounding (`techstudent`)

Think: "Would I put this on a college application?"

Go to **github.com/signup** and create your account.

### Step 2: Share Your Username

Post in Discord: `GitHub username: your-username`

We'll add you to the `rewind4419` organization and `Programming` team.

**Wait for confirmation before continuing.**

### Step 3: Follow the README

Once you're added to the team, **open README.md** for step-by-step instructions on:
- Cloning the repo
- Creating your branch
- Designing your robot card
- Committing and pushing
- Creating your Pull Request

---

## Why This Matters

### For FRC
- This is how we build robot code together
- Multiple people can work without conflicts
- Code review prevents bugs from reaching competition
- Safe experimentation without breaking things

### For Your Future
- Git/GitHub used in virtually every tech job
- Your contributions show on your GitHub profile
- Collaboration skills matter for college and career
- You're learning professional tools, not "student versions"

---

## Common Questions

**What if I mess up?**
Git is forgiving - you can undo almost anything. Ask for help!

**What if my PR gets rejected?**
Reviewer tells you what to fix. Make changes, push again, PR auto-updates.

**Do I need programming experience?**
Nope! Today is about the workflow, not complex code.

**Chromebook friendly?**
Yes! Press `.` on the repo page for a browser editor.

---

## After Today

You'll use this same workflow for:
- Robot code (C++ (what we use today) or Java or Python)
- Scouting apps
- Vision processing
- Documentation

**Keep learning:** https://skills.github.com/

**Questions?** Ask in Discord `#programming`

---

**Ready? Head to README.md and let's build something!**

