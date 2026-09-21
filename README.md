# GrokBot

Grok Bot proof of concept + the near-real-time LinkedIn recruiter pipeline for a UK IT contractor.

- **Grok Bot (desktop agent):** https://x.ai/bot
- **Grok CLI installer:** https://x.ai/cli/install.sh
- **Live guide:** https://rifaterdemsahin.github.io/grokbot/

## What's here

| Path | Purpose |
|---|---|
| `index.html` | Interactive Bloom's-taxonomy guide, install/usage docs, LinkedIn playbook, screenshot gallery |
| `src/grok_bot.py` | Runnable first-principles xAI agent (CLI) |
| `images/` | 14 phase-ordered evidence screenshots of the LinkedIn agent run |
| `docs/REPORT.md` | Installation, file-scan/rename, grouping and real-time rationale report |
| `docs/GROK-CLI-REPORT.md` | Grok CLI (`grok`/`agent`) install, health check, auth and usage report |
| `.env.example` | Environment template (`XAI_API_KEY`, `XAI_BASE_URL`, `GROK_MODEL`) |
| `requirements.txt` | Python dependencies |

## Install (verified)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # then set XAI_API_KEY
```

## Install the Grok CLI

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # installs to ~/.grok/bin, no sudo
grok --version                                   # grok 1.0.40 (alpha)
grok doctor                                      # 0 issues, 0 recommendations
```

See `docs/GROK-CLI-REPORT.md` for the full inspection, verification and auth details.

## Install Grok Bot (desktop agent)

Grok Bot is xAI's computer-use agent that operates a persistent cloud computer, opens
real browser tabs and completes multi-step tasks in the background — this is what drives
the LinkedIn recruiter workflow in the screenshots.

```text
Install: https://x.ai/bot   →   sign in   →   add Gmail / Google Calendar / Google Drive
                           →   connect 1Password   →   create "LinkedIn Contractor Responses"
```

## Usage

```bash
# Python PoC — streams from the xAI API (falls back to a simulation without a key)
python3 src/grok_bot.py "Explain quantum entanglement from first principles"

# Grok CLI (installed to ~/.grok/bin)
grok "explain this repo"              # interactive TUI
grok -p "summarise README.md"         # one-shot, headless
grok doctor                           # environment health check

# Local docs site (port policy: 30,000+)
python3 -m http.server 30110
open -a "Google Chrome" http://localhost:30110/index.html
```

## Why real-time LinkedIn matters

For a UK IT contractor, contractor income is roughly
`(role supply) × (match precision) × (response speed)`. Supply and precision are fixed
by your CV; response speed is the controllable variable that decays fastest — UK roles
are shortlisted the same working day, agencies claim right-to-represent on submission,
and IR35 status plus SC/BPSS clearance are screened in the first reply. Running LinkedIn
inside Grok Bot collapses that latency from "when I next log in" to "minutes", with a
human approving every draft. See `docs/REPORT.md` and the **LinkedIn Playbook** section
of the live guide for the full argument.
