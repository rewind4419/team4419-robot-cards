# Team 4419 Rewind - Robot Design Gallery

Welcome to the Team 4419 programming team! This project is your first step into learning how we use Git and GitHub to collaborate on code.

## 🎨 View the Live Gallery

**See all team robot cards here:** https://rewind4419.github.io/team4419-robot-cards/

The gallery automatically updates when new cards are merged to main!

## What This Is

This is an onboarding project where you'll:
- Learn how to use Git (branches, commits, pull requests)
- Create your own robot design card
- Practice the same workflow we use for actual robot code
- See your card appear in our team gallery!

## Quick Start (Recommended for Workshop)

**The easiest way - works on any device, no downloads needed!**

### Step 1: Open the Template

1. Go to [`cards/template.yaml`](cards/template.yaml) in this repo
2. Click the file to view it
3. Copy the entire contents

### Step 2: Create Your Card File

1. Go back to the main repo page
2. Click **"Add file"** → **"Create new file"**
3. Name your file: `cards/your-username.yaml` (replace with your actual GitHub username)
4. Paste the template contents
5. Edit the fields with your robot design:
   - **username**: Your GitHub username
   - **robot_name**: Give your robot a cool name (80s references encouraged!)
   - **year**: Current competition year (2026)
   - **signature_mechanism**: What makes your robot special?
   - **ascii_art**: Draw your robot with text characters (use AI to help!)
   - **why_cool**: Why is your design awesome?
   - **design_philosophy**: Your approach to robot design

### Step 3: Commit to a New Branch

1. Scroll down to **"Commit new file"**
2. GitHub will say: *"You can't commit to main because it's protected"*
3. Select: **"Create a new branch for this commit and start a pull request"**
4. Name your branch: `add-your-username-card` (replace 'username' with your github username)
5. Click **"Propose new file"**

### Step 4: Create Pull Request

1. GitHub will take you to the Pull Request page
2. Title: `Add robot card for @your-username`
3. Add a brief description of your robot (optional)
4. Click **"Create pull request"**

### Step 5: Check That Your Card Works!

**Important:** After creating your PR, make sure the build passes! We do this by running an automated set of tests inside Github called "Actions".

1. On your Pull Request page, look for the **"Checks"** section
2. You should see `generate-and-deploy` running (yellow circle)
3. Wait for it to complete (should take ~30 seconds)
4. **Look for a green checkmark ✓** - This means your YAML file is valid!
5. **If you see a red X ✗** - Click "Details" to see what's wrong (usually a formatting issue)

**Don't submit for review until you see the green checkmark!** This ensures your card will work when merged.

### Step 6: Wait for Review

A Programming Lead or Mentor will review your card and approve it!

### Step 7: Merge & See It Live!

Once approved, click **"Merge pull request"** and your card will appear on the live gallery within a couple minutes:

**https://rewind4419.github.io/team4419-robot-cards/**

---

## Advanced: Working Locally

**For students who want to preview their card before submitting:**

This requires some setup, but lets you see exactly how your card will look before creating a PR.

### What You'll Need

1. **Git** - Download [GitHub Desktop](https://desktop.github.com/) (easiest for beginners)
2. **IDE** - Download [VS Code](https://code.visualstudio.com/)
3. **Python** - Download [Python 3.7+](https://www.python.org/downloads/)

### Local Workflow

**Step 1: Clone the Repository**

Using GitHub Desktop:
1. Open GitHub Desktop
2. File → Clone Repository
3. Search for `rewind4419/team4419-robot-cards`
4. Choose where to save it locally
5. Click "Clone"

Using command line:
```bash
git clone https://github.com/rewind4419/team4419-robot-cards.git
cd team4419-robot-cards
```

**Step 2: Create Your Branch**

Using GitHub Desktop:
1. Click "Current Branch" dropdown
2. Click "New Branch"
3. Name it: `add-your-username-card`
4. Click "Create Branch"

Using command line:
```bash
git checkout -b add-your-username-card
```

**Step 3: Create Your Robot Card**

1. Open the project folder in VS Code
2. Copy `cards/template.yaml` to `cards/your-username.yaml`
3. Fill in your robot design (see fields in template)

**Step 4: Preview Your Card Locally**

This is the cool part - see your card before submitting!

```bash
# Install dependencies (first time only)
pip install -r requirements.txt

# Generate the gallery
python generate.py

# Open the generated file
open generated/index.html     # Mac
start generated/index.html    # Windows
xdg-open generated/index.html # Linux
```

You should see your robot card in the gallery!

**Step 5: Commit Your Changes**

Using GitHub Desktop:
1. You'll see `cards/your-username.yaml` in the "Changes" list
2. Add a commit message: `Add robot card for your-username`
3. Click "Commit to add-your-username-card"

Using command line:
```bash
git add cards/your-username.yaml
git commit -m "Add robot card for your-username"
```

**Step 6: Push to GitHub**

Using GitHub Desktop:
1. Click "Push origin" button at the top

Using command line:
```bash
git push -u origin add-your-username-card
```

**Step 7: Create Pull Request**

1. GitHub Desktop will show "Create Pull Request" button - click it
2. Or go to https://github.com/rewind4419/team4419-robot-cards
3. Click the yellow "Compare & pull request" button
4. Title: `Add robot card for @your-username`
5. Click "Create pull request"

**Step 8: Check the Build**

Wait for the green checkmark ✓ in the "Checks" section to confirm your YAML is valid!

**Step 9: Wait for Review & Merge**

Same as the quick start method - a Programming Lead will review and approve!

---

## Tips for Success

### ASCII Art Ideas

Use characters like these to draw your robot:
```
═ ║ ╔ ╗ ╚ ╝ ╠ ╣ ╦ ╩ ╬
□ ■ ◉ ● ○ ◈ ◆ ▓ ▒ ░
```

**Pro tip**: Ask an AI like ChatGPT or Claude to help you create ASCII art! Just describe your robot and ask for a text-based drawing.

### Design Philosophy Examples

Not sure what to write? Here are some approaches:
- "Speed and agility over raw power"
- "Simple and reliable beats complex and fragile"
- "If we can automate it, we should"
- "Defense wins championships"
- "Redundancy is reliability"

### Common Git Commands

```bash
# Check what branch you're on
git status

# See what you've changed
git diff

# Switch back to main branch
git checkout main

# Update your local copy
git pull

# See all branches
git branch -a
```

## Local Setup (For Testing)

If you want to run the generator locally:

### Requirements
- Python 3.7 or newer
- pip (Python package manager)

### Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Run the generator
python generate.py
```

The generated gallery will be in `generated/index.html`.

## Getting Help

Stuck? Here's how to get help:
- Ask a mentor during the workshop
- Check out [GitHub's Git Handbook](https://guides.github.com/introduction/git-handbook/)
- Post in the team Slack/Discord

## For Mentors

### Reviewing Pull Requests

When reviewing student PRs:
1. Check that the YAML file follows the naming convention (`username.yaml`)
2. Verify all required fields are filled in
3. Make sure ASCII art renders correctly (no broken formatting)
4. Provide encouraging feedback!
5. Merge when ready - the Action will auto-generate the gallery

### Manual Gallery Generation

```bash
python generate.py
```

## Repository Structure

```
team4419-robot-cards/
├── cards/                  # Student robot card YAML files
│   ├── template.yaml      # Template to copy
│   └── zredlined.yaml     # Example card
├── generated/             # Auto-generated HTML (gitignored)
│   └── index.html         # The gallery page
├── assets/                # Additional styling
│   └── style.css          # Custom CSS (optional)
├── .github/workflows/     # GitHub Actions
│   └── generate-gallery.yml
├── generate.py            # Python generator script
├── requirements.txt       # Python dependencies
└── README.md             # This file!
```

---

**Welcome to the team! We can't wait to see your robot design!** 🤖
