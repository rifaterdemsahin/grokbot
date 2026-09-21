# GrokBot — Installation, File Scan & LinkedIn Real-Time Report

**Date:** 21 September 2026
**Device:** macOS (darwin), Homebrew Python 3.14.7
**Repository:** [rifaterdemsahin/grokbot](https://github.com/rifaterdemsahin/grokbot)
**Live site:** https://rifaterdemsahin.github.io/grokbot/

---

## 1. Executive summary

This report documents four things:

1. **Installation** of GrokBot on this device, verified end-to-end.
2. **A full file scan** and a rename pass that turns 14 unfriendly numeric screenshot
   filenames into descriptive, phase-numbered names.
3. **Logical grouping** of the repository (files) and the website navigation (menus),
   plus install/usage documentation added to the pages.
4. **Why running the LinkedIn pipeline inside Grok Bot matters**, and why it must be
   close to real time for an IT contractor who wins roles in the UK.

Two distinct things share the name "GrokBot" in this repo, and both are documented:

| Track | What it is | Where |
|---|---|---|
| **A — Python PoC** | The repo's runnable CLI agent (`grok_bot.py`) calling the xAI API | [`src/grok_bot.py`](../src/grok_bot.py) |
| **B — Grok Bot desktop agent** | xAI's computer-use agent that operates a real browser and LinkedIn | External desktop app (screenshots) |

---

## 2. Installation log (Track A — local Python PoC)

### 2.1 Environment created

```bash
python3 -m venv venv
./venv/bin/python -m pip install --upgrade pip
./venv/bin/pip install -r requirements.txt
```

### 2.2 Verified packages

```
$ ./venv/bin/pip list | grep -Ei 'openai|dotenv|requests'
openai          3.16.2
python-dotenv   1.2.3
requests        2.34.2
```

| Requirement | Declared | Installed |
|---|---|---|
| `openai` | `>=1.40.0` | 3.16.2 |
| `python-dotenv` | `>=1.0.0` | 1.2.3 |
| `requests` | `>=2.31.0` | 2.34.2 |

### 2.3 Run verification (keyless simulation mode)

No API key is committed to the repository, so the PoC correctly fell back to its
deterministic simulation. This proves the virtual environment, imports, and
entrypoint all function:

```
$ ./venv/bin/python src/grok_bot.py "Why is GrokBot unique from first principles?"
============================================================
⚡ GrokBot: First-Principles AI Agent
============================================================

⚠️  [Setup Required]: XAI_API_KEY not found or is default.
...
🤖 [GrokBot (First Principles Simulation)]:
1. Information Latency: Collapsing time between real-world events and intelligence to near zero using live X telemetry.
2. Epistemic Integrity: Prioritizing empirical physics and mathematical truth over corporate alignment filters.
3. Supercomputing Scale: Powered by Memphis Colossus 100k+ liquid-cooled GPU cluster.
```

### 2.4 Enabling live API mode

```bash
cp .env.example .env
# edit .env and set: XAI_API_KEY="xai-..."
./venv/bin/python src/grok_bot.py "Explain quantum entanglement from first principles"
```

`XAI_BASE_URL` defaults to `https://api.x.ai/v1` and `GROK_MODEL` defaults to
`grok-2-latest`; both are configurable in `.env`.

---

## 3. Installation (Track B — Grok Bot desktop agent)

The screenshots in [`images/`](../images) document the desktop agent that performs the
LinkedIn work. Setup sequence:

1. Install the **Grok Bot** desktop application and sign in with the xAI account.
2. Add the productivity plugins: **Gmail**, **Google Calendar**, **Google Drive**.
3. Connect **1Password** so credentials are served from a dedicated vault rather than
   pasted into chat.
4. Create the custom bots that scope the work (see §5).
5. Grant computer and browser control when prompted.

During the documented run the agent opened Chrome, navigated LinkedIn's OAuth chain,
paused at LinkedIn's "Check your LinkedIn app" 2FA checkpoint, then scanned the
recruiter inbox and drafted replies for approval.

---

## 4. File scan and rename map

### 4.1 Problem

The repository root contained 14 screenshots named with opaque numeric IDs
(`5875341263672906134.jpg` … `5875341263672906289.jpg`). Nothing in the filename
indicated content, order, or purpose, and all 14 sat loose in the repo root next to
source code and config.

### 4.2 Rename map

All 14 were moved into `images/` and renamed with a phase order prefix plus a
description of what the frame proves.

| Before | After |
|---|---|
| `5875341263672906134.jpg` | `images/01-grokbot-linkedin-signin-request.jpg` |
| `5875341263672906135.jpg` | `images/02-linkedin-browser-credential-banner.jpg` |
| `5875341263672906136.jpg` | `images/03-linkedin-google-account-chooser.jpg` |
| `5875341263672906137.jpg` | `images/04-google-signin-pexabo-account.jpg` |
| `5875341263672906148.jpg` | `images/05-google-account-chooser-loading.jpg` |
| `5875341263672906159.jpg` | `images/06-linkedin-app-2fa-checkpoint.jpg` |
| `5875341263672906171.jpg` | `images/07-grokbot-scanning-recruiter-inbox.jpg` |
| `5875341263672906172.jpg` | `images/08-grokbot-recruiter-reply-template.jpg` |
| `5875341263672906205.jpg` | `images/09-linkedin-sent-recruiter-reply.jpg` |
| `5875341263672906207.jpg` | `images/10-grokbot-daily-followup-routine.jpg` |
| `5875341263672906249.jpg` | `images/11-cursor-usage-grok-bot-cua-tokens.jpg` |
| `5875341263672906287.jpg` | `images/12-grokbot-custom-bots-sidebar.jpg` |
| `5875341263672906288.jpg` | `images/13-grokbot-plugin-marketplace.jpg` |
| `5875341263672906289.jpg` | `images/14-grokbot-featured-plugins-added.jpg` |

`git mv` was used throughout, so file history is preserved.

### 4.3 What each rename reveals

The numbering encodes a narrative in four phases:

- **Phase 01 (01–06)** — secure sign-in: task intake, real browser session, federated
  Google login, contractor identity, OAuth hand-off, 2FA checkpoint.
- **Phase 02 (07–09)** — scan, draft, send: inbox scan, voice/template training, sent reply.
- **Phase 03 (10–11)** — always-on routine and its measured computer-use token cost.
- **Phase 04 (12–14)** — the bot and plugin stack that makes it repeatable.

---

## 5. Logical grouping

### 5.1 Repository structure

```
grokbot/
├── index.html              # Interactive guide (GitHub Pages entrypoint)
├── src/
│   └── grok_bot.py         # Runnable Python PoC
├── images/                 # 14 renamed, phase-ordered screenshots
├── docs/
│   └── REPORT.md           # This report
├── requirements.txt
├── .env.example
├── .gitignore              # NEW — excludes venv/ and .env secrets
├── README.md
├── AGENTS.md / agents.md   # Coordinator rules
└── .github/workflows/static.yml
```

**Grouping principle:** code in `src/`, evidence in `images/`, prose in `docs/`, and
only the site entrypoint plus project config at the root. The GitHub Pages workflow
uploads the whole repository, so image and report links resolve without changes.

### 5.2 Menu grouping

The site navigation was a single flat row of five Bloom's-taxonomy links. It is now
four purpose-grouped dropdowns, so the page scales beyond a single linear guide:

| Menu group | Items |
|---|---|
| **🧠 Guide** | Remember · Understand · Analyse · Evaluate · Create |
| **⚡ Install & Use** | Install on this device · Usage & run commands · Custom bots & plugins |
| **💼 LinkedIn Playbook** | Why real-time matters · Daily recruiter routine · Reply template |
| **🖼️ Evidence** | Screenshot gallery · Installation report · Report summary |

The footer repeats the same grouping as flat links, and the scroll-spy highlight
still tracks the active section.

### 5.3 Content added to the pages

- **Install section** — both tracks, with the verified command sequence and the
  agent setup checklist.
- **Usage section** — CLI usage, desktop-agent usage, safety rules, and the observed
  verified output on this device.
- **Custom bots & plugins** — the three named bots and a purpose-grouped plugin table.
- **LinkedIn Playbook** — rationale, workflow, and the reply template.
- **Screenshot gallery** — all 14 screenshots, grouped into the four phases.
- **Report section** — summary cards linking to this document.

---

## 6. Why LinkedIn here must be near real time (UK IT contractor)

### 6.1 The income equation

```
Contract income ≈ (role supply) × (match precision) × (response speed)
```

Role supply and match precision are mostly fixed by skills and CV. **Response speed is
the only variable fully under your control — and it decays fastest.**

### 6.2 Why the UK contract market is especially time-sensitive

1. **Same-day shortlists.** UK contract roles can be shortlisted the working day they
   are released. Recruiters send InMails in parallel and submit the first credible CVs
   to the client; an hour's delay can remove you from the running.
2. **Agency right-to-represent.** Once one agency submits you to a client, competing
   agencies usually cannot. Responding first keeps you in control of representation.
3. **Inside / Outside IR35.** Status changes effective take-home by roughly 20–30%.
   Clarifying it in the first reply prevents the recruiter from moving to the next name
   while waiting for an answer.
4. **SC / BPSS / CNI clearance.** Public-sector and Critical National Infrastructure
   roles filter hard on active clearance and UK eligibility. Stating both up front
   removes the biggest screening objection immediately.
5. **Short notice, fast starts.** Contracts frequently start within 2–4 weeks.
   Recruiters screen availability first, so a same-hour reply that confirms notice
   period beats a stronger CV that replies tomorrow.
6. **Inbox decay.** InMails pile up per role. An unanswered thread goes cold within
   roughly a day and is then buried under newer messages.

### 6.3 What "close to real time" buys you

| Dimension | Manual / once-a-day | Grok Bot near real-time |
|---|---|---|
| Detection latency | Hours to days | Minutes on the daily routine; continuous while running |
| Unanswered threads | Accumulate | Target zero; backlog worked daily |
| Reply quality | Rushed or generic | Consistent pitch, correct CV link, clearance stated |
| IR35 / rate clarity | Deferred to a call | Clarified in the first reply |
| Right-to-represent risk | High | Low — first credible responder keeps control |

### 6.4 Why *this* machine is the right place to run it

The agent runs on the same computer that already holds the CV library, calendar, and
credential vault. That co-location removes the manual steps between *"a recruiter
messaged"* and *"an accurate, personalised reply is sent"*. The human stays in the loop
— every draft is approved before sending — but the latency is bounded by minutes, not
by when you next open LinkedIn.

> Figures in this section are directional UK-market benchmarks used to illustrate the
> latency economics, not guarantees.

---

## 7. Operations, security and cost

- **Credentials** are entered directly into the sign-in page and never stored in chat;
  1Password can serve them from a dedicated vault.
- **2FA is preserved.** The documented run paused at LinkedIn's app-approval
  checkpoint, requiring human action.
- **Human-in-the-loop sending.** Replies are drafted and reviewed before dispatch.
- **Cost is observable.** Computer-use (`grok-bot-cua`) token usage is tracked in the
  provider usage dashboard (see screenshot 11).
- **Secrets hygiene.** `.gitignore` now excludes `venv/` and `.env`; only
  `.env.example` is tracked.

---

## 8. Verification checklist

- [x] `venv` created and dependencies installed (`openai` 3.16.2, `python-dotenv` 1.2.3, `requests` 2.34.2)
- [x] `src/grok_bot.py` executes and streams/prints a complete response
- [x] All 14 screenshots renamed via `git mv` (history preserved)
- [x] Repository grouped into `src/`, `images/`, `docs/`
- [x] Navigation grouped into four menus; footer mirrors the grouping
- [x] Install, usage, LinkedIn rationale, workflow, and reply template documented on the page
- [x] Gallery wired to the renamed images
- [x] `.gitignore` added for `venv/` and `.env`

---

## 9. Recommended next steps

1. Add `XAI_API_KEY` to `.env` to switch the CLI from simulation to live inference.
2. Add a screenshot-to-phase caption check whenever new evidence is captured, keeping
   the `NN-description.jpg` convention.
3. Extend the GitHub Actions workflow to lint the Python PoC on push.
4. Keep the CV library (`CVLauncher`) link mapping current, since the agent depends on
   per-role CV selection.
