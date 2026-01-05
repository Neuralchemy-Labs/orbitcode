# 🚀 Publishing Orbit to GitHub

This guide will help you publish your Orbit project to GitHub.

## Prerequisites

- GitHub account
- Git installed on your machine
- Project already initialized (✅ Done!)

## Step 1: Create a New Repository on GitHub

1. Go to [GitHub](https://github.com)
2. Click the **"+"** icon in the top right → **"New repository"**
3. Repository details:
   - **Name**: `orbit` (or `orbit-offline-assistant`)
   - **Description**: `🌍 Offline coding assistant with context-aware code generation. Privacy-first, runs 100% locally.`
   - **Visibility**: Public
   - **DO NOT** initialize with README, .gitignore, or license (we already have these!)
4. Click **"Create repository"**

## Step 2: Connect Local Repository to GitHub

After creating the repository, GitHub will show you commands. Use these PowerShell commands:

```powershell
# Add the remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/orbit.git

# Verify the remote was added
git remote -v

# Push to GitHub (first time)
git push -u origin master
```

**Example:**
```powershell
git remote add origin https://github.com/zenith-dev/orbit.git
git push -u origin master
```

## Step 3: Verify on GitHub

1. Refresh your GitHub repository page
2. You should see all your files uploaded!
3. GitHub will automatically display your `README.md` on the main page

## Step 4: Add Repository Topics (Recommended)

1. On your GitHub repository page, click **"⚙️ Settings"** (or find the gear icon near "About")
2. Add topics/tags:
   - `offline-assistant`
   - `coding-assistant`
   - `llama-cpp`
   - `privacy-first`
   - `gguf`
   - `local-llm`
   - `gradio`
   - `qwen`
   - `ai-development`

## Step 5: Add a Repository Description

In the "About" section (top right of your repo), add:
```
🌍 Offline coding assistant with context-aware code generation. Privacy-first, runs 100% locally with GGUF models.
```

## Future Commits

After making changes to your code:

```powershell
# See what changed
git status

# Add all changes
git add .

# Commit with a message
git commit -m "Add feature XYZ"

# Push to GitHub
git push
```

## Troubleshooting

### Authentication Issues

If GitHub asks for credentials, you have two options:

**Option 1: Personal Access Token (Recommended)**
1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token with `repo` scope
3. Use the token as your password when pushing

**Option 2: GitHub CLI**
```powershell
# Install GitHub CLI
winget install GitHub.cli

# Authenticate
gh auth login

# Then use git commands normally
```

### Push Rejected

If you get "push rejected", try:
```powershell
git pull origin master --rebase
git push origin master
```

## What Goes to GitHub vs. What Stays Local

### ✅ Goes to GitHub (Committed):
- All Python code
- Documentation (README, CONTRIBUTING)
- Templates
- Example context files (`*.example`)
- System context file
- Configuration examples

### ❌ Stays Local (Ignored):
- Your personal `contexts/project.txt`
- Your personal `contexts/conventions.txt`
- Downloaded models (`models/*.gguf`)
- Python cache files
- Virtual environment

This ensures your **personal context and large model files** stay private while sharing the code!

## Next Steps

1. **Add a README badge**: Add GitHub stars/forks badges
2. **Enable Discussions**: Settings → Features → Discussions
3. **Create Issues**: Add some "good first issue" labels for contributors
4. **Add GitHub Actions**: Automate testing (optional)
5. **Share it**: Post on Reddit, Twitter, etc.!

---

**🎉 Congratulations! Your project is now open source!**
