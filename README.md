<div align="center">

<!-- PORTRAIT - Directly fetches your active GitHub profile picture -->
<img src="https://github.com/SGM-SHAH.png" width="220" style="border-radius: 50%; border: 3px solid #39D353;" alt="SGM SHAH">

<br><br>

<!-- NAME / TAGLINE - animated typing -->
<a href="https://github.com/SGM-SHAH">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=24&duration=2600&pause=900&color=39D353&center=true&vCenter=true&width=720&lines=SGM+SHAH;AI%2FML+Engineer;B.Tech+CSE+(AI%2FML)+%40+SRM-AP;Building+Intelligent+Full-Stack+Systems;Cricket+Enthusiast+%26+Avid+Reader" alt="typing banner">
</a>

<br>

<!-- SOCIALS & BADGES -->
<a href="https://www.linkedin.com/in/shaik-ghouse-mohiddin-shah"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
<a href="mailto:sgmshah07@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
<a href="https://sgm-shah.web.app/"><img src="https://img.shields.io/badge/Portfolio-111111?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Portfolio"></a>

<img src="https://komarev.com/ghpvc/?username=SGM-SHAH&style=flat&color=39d353&label=profile+views" alt="profile views">

</div>

---

## `~/` whoami

```console
$ cat about.txtHi, I'm SGM SHAH — an aspiring AI/ML Engineer and B.Tech CSE (AI/ML) undergraduate at SRM University-AP. I focus on training and deploying intelligent models, engineering scalable data workflows, and developing robust full-stack applications.

🔭 Currently building IPL Auction Simulator & deep learning models

🌐 Portfolio: sgm-shah.web.app

🏆 Hackathons & Highlights: My1stHack 2025 (Team Apex Coders) • AR/VR Immersive Workshop • Campus & Community Event Tech

📜 Industry Certifications: Google Project Management • Mastercard Cybersecurity • JPMorgan Chase Software Engineering

⚡ Focus: Applied Machine Learning, Data Processing Pipelines & Algorithmic Problem Solving

🏏 Fun fact: When not training models or debugging code, you'll find me watching cricket, debating, or deep into a book.
Project,Live / Demo,Stack,Description
Developer Portfolio,sgm-shah.web.app,React Tailwind CSS Firebase,"Clean personal developer portal showcasing projects, achievements, and technical stack."
IPL Auction Simulator,Simulate Auction,JavaScript Node.js Firebase,"Interactive auction room engine handling live bidding, squad constraints, and purse deduction logic."
Data Pipeline & Processor,View Engine,Python Pandas Power Query,High-throughput data processing workflow converting 400 MB JSON datasets into structured Excel sheets.
DSA & Systems Suite,View Source,C Java C# OOP Design,"Optimized implementations of tree traversals, matrix manipulation, and algorithm patterns."
01110100 01101000 01100001 01101110 01101011 01110011 00100000 01100110 01101111 01110010 00100000 01110011 01100011 01110010 01101111 01101100 01101100 01101001 01101110 01100111
name: Generate Snake Animation

on:
  schedule:
    # Run every 12 hours
    - cron: "0 */12 * * *"
  workflow_dispatch:
  push:
    branches:
      - main

permissions:
  contents: write

jobs:
  generate:
    runs-on: ubuntu-latest
    timeout-minutes: 5

    steps:
      - name: Generate contribution snake SVGs
        uses: Platane/snk/svg-only@v3
        with:
          github_user_name: SGM-SHAH
          outputs: |
            dist/github-contribution-grid-snake.svg
            dist/github-contribution-grid-snake-dark.svg?palette=github-dark

      - name: Deploy SVGs to output branch
        uses: crazy-max/ghaction-github-pages@v3.1.0
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
