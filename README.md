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

### Step 0: 🚀 Share your GitHub username in #programming

1. Post your GitHub username in Discord
2. Wait for a mentor to add you to the `Programming` team
3. **Check your email!** You'll get an invite to join the `rewind4419` organization
4. Click the link in the email and accept the invitation
5. Once accepted, you can start with Step 1 below

### Step 1: Create Your Card File

1. Go to the main repo page: https://github.com/rewind4419/team4419-robot-cards
2. Click **"+"** (Add file button) → **"Create new file"**
3. Name your file: `cards/your-username.yaml`
   - Example: `cards/zredlined.yaml`
   - Replace `your-username` with your actual GitHub username!

### Step 2: Add Your Robot Design

Copy this template and fill in your information:

```yaml
# Your robot design card
username: "your-github-username"
robot_name: "My Awesome Robot"
year: 2026
signature_mechanism: "Describe your robot's coolest feature"
ascii_art: |
     ___
    |   |
    |___|
    0   0
why_cool: "Explain what makes your design special"
design_philosophy: "Your approach to robot design (speed vs power, simple vs complex, etc.)"
```

**Fill in each field:**
- `username` - Your GitHub username (in quotes)
- `robot_name` - A cool name for your robot
- `year` - 2026
- `signature_mechanism` - What makes your robot special?
- `ascii_art` - Keep it simple for now (we'll improve it in the next step!)
- `why_cool` - Why is your design awesome?
- `design_philosophy` - Your design approach

### Step 3: First Commit - Create Your Branch

1. Scroll down to **"Commit new file"**
2. GitHub will say: *"You can't commit to main because it's protected"*
3. Select: **"Create a new branch for this commit and start a pull request"**
4. **Branch name:** `add-your-username-card` (replace with your username - remember this!)
5. **Commit message:** `Add robot card for your-username`
6. Click **"Propose new file"**
7. **STOP - Don't create the PR yet!**

### Step 4: Go Back to Your Branch to Make More Edits

1. Go back to the repo home: https://github.com/rewind4419/team4419-robot-cards
2. Click the **branch dropdown** (button that says "main" with a ▼)
3. Find and click your branch: `add-your-username-card`
4. Click the `cards` folder
5. Click your file: `your-username.yaml`

You're now looking at your file on your branch!

### Step 5: Improve Your ASCII Art with AI

Let's make your robot look cooler with AI help!

1. Open your favorite AI (ChatGPT, Claude, etc.)
2. Copy this prompt and fill in your robot description:

```
Create ASCII art for my robot design. Here's my robot concept: [DESCRIBE YOUR ROBOT HERE].

Please use these special characters for a cooler look:
═ ║ ╔ ╗ ╚ ╝ ╠ ╣ ╦ ╩ ╬
□ ■ ◉ ● ○ ◈ ◆ ▓ ▒ ░

Keep it under 40 characters wide and around 8-10 lines tall.
```

3. Copy the ASCII art the AI generates

### Step 6: Update Your Card with Better ASCII Art

1. From your file view, click the **pencil icon (✏️)** to edit
2. Replace the simple `ascii_art` section with your new AI-generated art
3. Scroll down to **"Commit changes"**
4. **Commit message:** `Improve ASCII art for robot design`
5. Make sure **"Commit directly to the `add-your-username-card` branch"** is selected
6. Click **"Commit changes"**

### Step 7: Create Pull Request

Now you're ready to submit!

1. Go back to the repo home: https://github.com/rewind4419/team4419-robot-cards
2. You should see a yellow banner: **"add-your-username-card had recent pushes"**
3. Click the green **"Compare & pull request"** button
4. **Title:** `Add robot card for @your-username`
5. Add a brief description (optional)
6. Click **"Create pull request"**

### Step 8: Wait for Review

A Programming Lead or Mentor will review your card and approve it! They'll check:
- Your YAML formatting is correct
- All required fields are filled in
- Your ASCII art looks good

If they request changes, just edit your file on your branch and commit again - the PR will update automatically!

### Step 9: Merge & See It Live!

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
