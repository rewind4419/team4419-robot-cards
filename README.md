# Team 4419 Rewind - Robot Design Gallery

Welcome to the Team 4419 programming team! This project is your first step into learning how we use Git and GitHub to collaborate on code.

## What This Is

This is an onboarding project where you'll:
- Learn how to use Git (branches, commits, pull requests)
- Create your own robot design card
- Practice the same workflow we use for actual robot code
- See your card appear in our team gallery!

## Workshop Instructions

### Step 1: Get the Code

**Option A: Clone the repository (if you have Git installed)**
```bash
git clone https://github.com/zredlined/team4419-robot-cards.git
cd team4419-robot-cards
```

**Option B: Use GitHub.dev (Chromebook-friendly!)**
1. Go to the repository on GitHub
2. Press the `.` key (period) on your keyboard
3. This opens a browser-based VS Code editor - no installation needed!

### Step 2: Create Your Branch

Branches let you work on your own changes without affecting the main code.

```bash
git checkout -b add-your-username-card
```

Replace `your-username` with your actual GitHub username!

### Step 3: Create Your Robot Card

1. Copy the template:
   ```bash
   cp cards/template.yaml cards/your-username.yaml
   ```

2. Open `cards/your-username.yaml` in your editor

3. Fill in your dream robot design:
   - **username**: Your GitHub username
   - **robot_name**: Give your robot a cool name (80s references encouraged!)
   - **year**: Current competition year (2025)
   - **signature_mechanism**: What makes your robot special?
   - **ascii_art**: Draw your robot with text characters (use AI to help!)
   - **why_cool**: Why is your design awesome?
   - **design_philosophy**: Your approach to robot design

### Step 4: Test Locally (Optional - Skip on Chromebooks)

If you have Python installed, you can preview your card:

```bash
# Install dependencies
pip install -r requirements.txt

# Generate the gallery
python generate.py

# Open generated/index.html in your browser to see your card!
```

**Chromebook users**: Don't worry! You can skip this step and see your card after it's merged.

### Step 5: Commit Your Changes

Save your work with a commit:

```bash
# Add only your YAML file
git add cards/your-username.yaml

# Commit with a descriptive message
git commit -m "Add robot card for your-username"
```

### Step 6: Push Your Branch

Send your branch to GitHub:

```bash
git push -u origin add-your-username-card
```

### Step 7: Create a Pull Request

1. Go to the repository on GitHub
2. Click "Pull requests" → "New pull request"
3. Select your branch from the dropdown
4. Click "Create pull request"
5. Add a title like "Add robot card for @your-username"
6. Submit and wait for a mentor to review!

## What Happens After Your PR is Merged?

Once a mentor approves and merges your pull request:
1. A GitHub Action automatically runs
2. It generates a new HTML gallery with ALL team cards
3. Your robot design appears on the team gallery page!
4. You're officially part of the programming team!

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
