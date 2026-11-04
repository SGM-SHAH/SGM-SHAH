#!/usr/bin/env python3
"""
Generate elegant, self-hosted Achievements & Certifications card SVGs.
Replaces lowlighter/metrics achievements plugin which returns 'Unexpected error'
when user has no GitHub achievements or due to upstream GitHub API changes.
"""

from pathlib import Path

def generate_achievements_svg(theme="dark"):
    is_dark = theme == "dark"
    bg = "#0d1117" if is_dark else "#ffffff"
    border = "#30363d" if is_dark else "#d0d7de"
    card_bg = "#161b22" if is_dark else "#f6f8fa"
    card_border = "#30363d" if is_dark else "#e1e4e8"
    title_color = "#39d353" if is_dark else "#1a7f37"
    text_color = "#e6edf3" if is_dark else "#1f2328"
    sub_color = "#8b949e" if is_dark else "#57606a"

    items = [
        {
            "title": "My1stHack 2025",
            "badge": "HACKATHON",
            "badge_color": "#f0883e",
            "desc1": "Team Apex Coders",
            "desc2": "Rapid AI Prototyping",
            "icon_color": "#d29922",
            # Trophy icon
            "icon": "M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm6.5-.25A1.75 1.75 0 018.25 6h.5a1.75 1.75 0 011.75 1.75v.5A1.75 1.75 0 018.75 10h-.5A1.75 1.75 0 016.5 8.25v-.5z"
        },
        {
            "title": "Software Eng.",
            "badge": "SIMULATION CERT",
            "badge_color": "#58a6ff",
            "desc1": "Architecture & Quality",
            "desc2": "Industry Simulation",
            "icon_color": "#58a6ff",
            # Code brackets icon
            "icon": "M4.72 3.22a.75.75 0 011.06 1.06L2.06 8l3.72 3.72a.75.75 0 11-1.06 1.06L.47 8.53a.75.75 0 010-1.06l4.25-4.25zm6.56 0a.75.75 0 10-1.06 1.06L13.94 8l-3.72 3.72a.75.75 0 101.06 1.06l4.25-4.25a.75.75 0 000-1.06l-4.25-4.25z"
        },
        {
            "title": "Cybersecurity",
            "badge": "SIMULATION CERT",
            "badge_color": "#bc8cff",
            "desc1": "Threat Analysis & Defense",
            "desc2": "Industry Simulation",
            "icon_color": "#bc8cff",
            # Shield icon
            "icon": "M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25z"
        },
        {
            "title": "Project Mgmt.",
            "badge": "SIMULATION CERT",
            "badge_color": "#39d353",
            "desc1": "Agile & Delivery",
            "desc2": "Industry Simulation",
            "icon_color": "#39d353",
            # Check circle icon
            "icon": "M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"
        }
    ]

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 135" width="100%" height="135">',
        '  <style>',
        f'    .title {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 600; fill: {title_color}; }}',
        f'    .item-title {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 13px; font-weight: 600; fill: {text_color}; }}',
        f'    .item-desc {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 11px; fill: {sub_color}; }}',
        f'    .badge {{ font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, monospace; font-size: 9px; font-weight: 700; }}',
        '  </style>',
        f'  <rect width="800" height="135" rx="10" fill="{bg}" stroke="{border}" stroke-width="1"/>',
        f'  <text x="20" y="27" class="title">🏆 Achievements &amp; Certifications</text>',
        '  <g transform="translate(16, 40)">'
    ]

    for i, it in enumerate(items):
        x = i * 194
        out.append(f'    <g transform="translate({x}, 0)">')
        out.append(f'      <rect width="186" height="80" rx="8" fill="{card_bg}" stroke="{card_border}" stroke-width="1"/>')
        out.append(f'      <circle cx="22" cy="24" r="11" fill="{it["icon_color"]}20" />')
        out.append(f'      <path transform="translate(14, 16) scale(1)" fill="{it["icon_color"]}" d="{it["icon"]}"/>')
        out.append(f'      <text x="39" y="21" class="badge" fill="{it["badge_color"]}">{it["badge"]}</text>')
        out.append(f'      <text x="39" y="34" class="item-title">{it["title"]}</text>')
        out.append(f'      <text x="14" y="55" class="item-desc">{it["desc1"]}</text>')
        out.append(f'      <text x="14" y="69" class="item-desc">{it["desc2"]}</text>')
        out.append('    </g>')

    out.append('  </g>')
    out.append('</svg>')
    return '\n'.join(out)

def main():
    assets = Path("assets")
    assets.mkdir(parents=True, exist_ok=True)
    
    dark_svg = generate_achievements_svg("dark")
    light_svg = generate_achievements_svg("light")
    
    (assets / "card-achievements-dark.svg").write_text(dark_svg, encoding="utf-8")
    (assets / "card-achievements-light.svg").write_text(light_svg, encoding="utf-8")
    # Also write metrics.achievements.svg so anything referencing it gets the clean card
    (assets / "metrics.achievements.svg").write_text(dark_svg, encoding="utf-8")
    print("Wrote card-achievements-dark.svg, card-achievements-light.svg, and metrics.achievements.svg")

if __name__ == "__main__":
    main()
