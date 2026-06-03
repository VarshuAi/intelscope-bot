<!-- ========================================================================= -->
<!--                        INTELSCOPE — README                                -->
<!--       Pastel OSINT Theme  |  Dynamic Vector Card  |  Soft Light style      -->
<!-- ========================================================================= -->

<div align="center">

<!-- ============================== BANNER ============================== -->

<img src="https://capsule-render.vercel.app/api?type=slice&color=E0F2F1,E0F7FA,E8EAF6&height=180&section=header&text=IntelScope&fontSize=48&fontColor=00BFA5&fontAlignY=38&animation=fadeIn" width="100%"/>

<!-- ============================== TYPING SVG ============================== -->

<br/>

<a href="https://github.com/VarshuAi/intelscope-bot"><img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=600&size=22&duration=3000&pause=1000&color=00BFA5&center=true&vCenter=true&multiline=true&repeat=true&random=false&width=700&height=80&lines=%F0%9F%94%8D%20Welcome%20to%20IntelScope!%20%F0%9F%94%8D;%E2%9C%A8%20Powered%20by%20Python%20%7C%20Fast%20%26%20Accurate%20OSINT%20%E2%9C%A8;%F0%9F%9B%A1%EF%B8%8F%20Footprint%20usernames%20%7C%20Audit%20DNS%20%7C%20IP%20Reputation" alt="Typing SVG"/></a>

<br/>

<img src="https://img.shields.io/badge/Version-1.0-00BFA5?style=for-the-badge&logo=github&logoColor=white" alt="Version"/>
<img src="https://img.shields.io/badge/Python-OSINT-00B0FF?style=for-the-badge&logo=python&logoColor=white" alt="Language"/>
<img src="https://img.shields.io/badge/Status-Active-00C853?style=for-the-badge&logo=git&logoColor=white" alt="Status"/>

<img src="https://capsule-render.vercel.app/api?type=slice&color=E0F2F1,E0F7FA,E8EAF6&height=60&section=header&text=&fontSize=0" width="100%"/>

</div>

<!-- ============================== ABOUT ============================== -->

<h2>
<samp>🛡️ ABOUT</samp>
</h2>

```yaml
project: IntelScope
version: 1.0
type: OSINT Bot
author: VarshuAi
primary_tech: Python
description: >
  A powerful and accurate Open-Source Intelligence (OSINT) Telegram bot.
  It helps footprint usernames, resolve DNS, discover subdomains via CT logs,
  analyze IP threat reputations, and run SMTP handshake email checks.
```

<!-- ============================== CENTRAL GRAPHIC ============================== -->

<br>
<div align="center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 550 140" width="100%" height="140">
  <defs>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#F9F9FB"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="4" stdDeviation="4" flood-opacity="0.04"/>
    </filter>
  </defs>
  
  <rect x="4" y="4" width="542" height="132" rx="16" fill="url(#cardGrad)" stroke="#00BFA5" stroke-width="1.5" filter="url(#shadow)"/>
  
  <rect x="24" y="28" width="80" height="80" rx="12" fill="#00BFA5" fill-opacity="0.06"/>
  <g transform="translate(24, 33) scale(1)">
    <path d="M40,10 L15,20 L15,40 C15,55 25,65 40,70 C55,65 65,55 65,40 L65,20 Z M40,25 L40,55 M28,38 L40,50 L52,30" fill="none" stroke="#00BFA5" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  
  <text x="124" y="48" font-family="'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="700" fill="#1A1A24">IntelScope OSINT</text>
  <text x="124" y="74" font-family="'Segoe UI', Roboto, sans-serif" font-size="12.5" fill="#5A5A66">Secure technical OSINT aggregator for Telegram groups & PMs.</text>
  
  <rect x="124" y="92" width="75" height="22" rx="6" fill="#00BFA5" fill-opacity="0.08"/>
  <text x="134" y="106" font-family="'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="600" fill="#00BFA5">Python 3.10+</text>
  
  <circle cx="215" cy="103" r="4.5" fill="#4CAF50"/>
  <text x="226" y="106" font-family="'Segoe UI', Roboto, sans-serif" font-size="10.5" fill="#4CAF50" font-weight="600">Active</text>
</svg>
</div>
<br>

<!-- ============================== FEATURES ============================== -->

<h2>
<samp>✨ FEATURES</samp>
</h2>

- 🔍 **Username footprinting** — Scan for user availability across 50+ websites concurrently.
- 🌐 **Domain & DNS Scan** — Query DNS records (MX, A, TXT, NS) and discover subdomains via `crt.sh` log monitor.
- 🖥️ **IP reputation scan** — Fetch geolocation statistics and check IP reputations via AlienVault OTX feeds.
- 📧 **SMTP Verification** — Confirm email address configurations and SMTP check handshakes.

<!-- ============================== COMMANDS ============================== -->

<h2>
<samp>💫 COMMANDS & USAGE</samp>
</h2>

```bash
# ── Query Commands ────────────────────────────────────
/start          →  Boot the interactive welcome card
/user <name>    →  Footprint target username (50+ networks)
/domain <host>  →  Perform DNS audit and CT subdomain discovery
/ip <address>   →  Look up Geo IP information and reputation indicators
/email <addr>   →  Verify email host configurations & active user checks
```

<!-- ============================== SETUP ============================== -->

<h2>
<samp>🍓 SETUP & RUN</samp>
</h2>

```bash
# 1. Clone repository remote
git clone https://github.com/VarshuAi/intelscope-bot.git
cd intelscope-bot

# 2. Install library dependencies
pip install -r requirements.txt

# 3. Configure credentials
cp sample.env .env
# → Edit .env with your Telegram TOKEN

# 4. Start polling
python bot.py
```

<!-- ============================== STRUCTURE ============================== -->

<h2>
<samp>📂 STRUCTURE</samp>
</h2>

```
intelscope-bot/
├── recon/
│   ├── usernames.py   # Username footprints checker
│   ├── domains.py     # DNS resolve & crt.sh query
│   ├── ips.py         # Geo IP & AlienVault OTX client
│   └── emails.py      # SMTP handshake validator
├── bot.py             # Main pyTelegramBotAPI engine
├── requirements.txt   # Dependency configurations
├── sample.env         # Configuration template
└── README.md
```

<!-- ============================== FOOTER ============================== -->

<div align="center">

<br/>

<img src="https://capsule-render.vercel.app/api?type=slice&color=E0F2F1,E0F7FA,E8EAF6&height=80&section=footer&text=&fontSize=0" width="100%"/>

<br/>

<a href="https://github.com/VarshuAi"><img src="https://readme-typing-svg.demolab.com?font=Poppins&size=14&duration=4000&pause=1000&color=00BFA5&center=true&vCenter=true&width=500&lines=Made+with+%E2%9D%A4%EF%B8%8F+by+VarshuAi;Secure.+Scalable.+Clean." alt="Typing SVG"/></a>

<br/>

<a href="https://github.com/VarshuAi"><img src="https://img.shields.io/badge/VarshuAi-Profile-00BFA5?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Profile"/></a>
<a href="https://github.com/VarshuAi/intelscope-bot"><img src="https://img.shields.io/badge/intelscope--bot-Repo-FFA6C9?style=for-the-badge&logo=github&logoColor=white" alt="Repository"/></a>

<br/>

</div>
