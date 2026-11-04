# Setup & Deployment Guide for SGM SHAH's GitHub Profile

This repository is named **`SGM-SHAH`**, matching your GitHub username (`github.com/SGM-SHAH/SGM-SHAH`). That special repository's `README.md` is what automatically displays on your GitHub profile overview.

---

## 1. Local Preview & Tuning

You can open `preview.html` in your browser at any time to preview your generated SVGs (portrait, skill radar, language radar, and project cards) across both GitHub Dark and Light themes.

### Re-tuning your Dot-Matrix Portrait:
```powershell
# Color Reveal scan (default):
python scripts\dotify.py assets\avatar.png -o assets\portrait --cols 100 --equalize --detail 0.5 --color --reveal

# Green monochrome terminal look:
python scripts\dotify.py assets\avatar.png -o assets\portrait --cols 88 --equalize --detail 0.5 --animate

# Binary matrix look:
python scripts\dotify.py assets\avatar.png -o assets\portrait --mode binary --cols 62 --equalize --detail 0.5
```

### Refreshing Skill Radar:
Edit `assets/skills.json` and run:
```powershell
python scripts\radar.py --data assets\skills.json -o assets\radar
```

### Refreshing Language Radar:
```powershell
python scripts\radar.py --github SGM-SHAH -o assets\radar-langs --values --curve 0.4 --exclude "shell,makefile,dockerfile,batchfile,procfile"
```

### Refreshing Project & Stat Cards:
Edit `assets/projects.json` and run:
```powershell
python scripts\cards.py --user SGM-SHAH --projects assets\projects.json --out assets
```

---

## 2. GitHub Actions Automated Workflows

Your profile repository is equipped with GitHub Actions that automatically refresh your contribution visuals, charts, and project stats:

### A. Enable GitHub Actions Workflow Permissions
1. In your GitHub repository (`SGM-SHAH/SGM-SHAH`), go to **Settings** → **Actions** → **General**.
2. Scroll down to **Workflow permissions**.
3. Select **Read and write permissions**.
4. Click **Save**.

### B. Add `METRICS_TOKEN` (for 3D Isometric Calendar & Stats)
`lowlighter/metrics` needs a GitHub Personal Access Token (PAT) to read profile contribution stats:
1. Go to [https://github.com/settings/tokens](https://github.com/settings/tokens) → **Generate new token (classic)**.
2. Note: `SGM-SHAH-Profile-Metrics`
3. Scopes to check:
   - **`read:user`**
   - **`repo`** (optional, if you want private repository contributions counted)
4. Click **Generate token** and copy the token string (`ghp_...`).
5. Go to your repo: **Settings** → **Secrets and variables** → **Actions** → **New repository secret**.
6. Name: **`METRICS_TOKEN`**
7. Value: *(paste your generated token)* → Click **Add secret**.

### C. Trigger Workflows Manually for the First Time
Go to your repository's **Actions** tab on GitHub:
1. **Metrics** → click **Run workflow** (generates updated `assets/metrics.isocalendar.svg`, `assets/metrics.languages.svg`, `assets/metrics.achievements.svg`).
2. **Snake** → click **Run workflow** (generates snake eating contribution grid on the `output` branch).
3. **Charts and cards** → click **Run workflow** (refreshes radar charts and project cards).

