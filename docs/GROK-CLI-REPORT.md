# Grok CLI — Installation Report

**Date:** 21 September 2026, 16:45 BST
**Device:** macOS (darwin) · Apple Silicon (`macos-aarch64`) · shell: zsh
**Installer:** `https://x.ai/cli/install.sh`
**User:** Rifat Erdem Sahin (rifaterdemsahin@gmail.com)

---

## 1. Executive summary

The official xAI Grok CLI was installed/updated on this device to **version 1.0.40
(alpha)**. The installer placed the binary under `~/.grok/bin`, symlinked both `grok`
and `agent`, generated shell completions, and added `~/.grok/bin` to `PATH` in
`~/.zshrc`.

The install is marked **healthy**: `grok doctor` reports **0 issues, 0
recommendations**, both entrypoints resolve, and the OIDC login profile is valid.

> The script was **downloaded and inspected before execution** rather than piped
> blindly into a shell. See §3 for what it actually does.

---

## 2. Command requested

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
```

---

## 3. Pre-flight inspection (what the script does)

The 19,501-byte script at `https://x.ai/cli/install.sh` was saved and read before
running. Key behaviour confirmed:

| Area | Behaviour |
|---|---|
| Privileges | **No `sudo`**, no system directories written |
| Install root | `$HOME/.grok` (`downloads/`, `bin/`, `completions/`, `config.toml`) |
| Binary source | `https://x.ai/cli` with fallback to `https://storage.googleapis.com/grok-build-public-artifacts/cli` |
| Integrity check | Runs `"$binary_tmp" --version` and aborts if the binary fails |
| Atomic install | Downloads to `.tmp.$$`, then `mv -f` into place |
| PATH | Appends a marked `# >>> grok installer >>>` block to the user's shell rc (backs up first) |
| Version | Defaults to `stable` channel; accepts an explicit `X.Y.Z` argument |

No obfuscation, no `eval` of remote content, no destructive `rm -rf` outside its own
temp directories.

---

## 4. Installation log

```
$ curl -fsSL https://x.ai/cli/install.sh | bash
Auth: using OIDC token from ~/.grok/auth.json.
Fetching latest stable version...
Installing Grok 1.0.40 (macos-aarch64, auth.json (oidc))...
  Downloading grok 1.0.40...
  Binary linked to /Users/rifaterdemsahin/.grok/bin/grok and /Users/rifaterdemsahin/.grok/bin/agent.
Grok 1.0.40 installed to /Users/rifaterdemsahin/.grok/bin/grok
  Updated /Users/rifaterdemsahin/.grok/bin in PATH in /Users/rifaterdemsahin/.zshrc.

Run 'grok' or 'agent' to get started!
=== installer exit: 0 ===
```

---

## 5. Verification

### 5.1 Version and entrypoints

```
$ grok --version
grok 1.0.40 (eb1a2256660d) [alpha]

$ agent --version
grok 1.0.40 (eb1a2256660d) [alpha]

$ which grok agent
/Users/rifaterdemsahin/.grok/bin/grok
/Users/rifaterdemsahin/.grok/bin/agent

$ ls -la ~/.grok/bin
agent -> ../downloads/grok-macos-aarch64
grok  -> ../downloads/grok-macos-aarch64
```

Both commands resolve to the same native `arm64` binary (`grok-macos-aarch64`), so
`grok` (interactive TUI) and `agent` (headless/non-interactive) are two entrypoints
into one install.

### 5.2 Health check

```
$ grok doctor
Grok Doctor

Environment
  · terminal                     Apple Terminal
  · multiplexer                  None detected
  · ssh                          no
  · clipboard                    local (pbcopy) — confirmed
  · voice                        MacBook Pro Microphone
  · keyboard                     cmd=unrecoverable, opt=dropped (OS rescue active)

0 issues, 0 recommendations
```

### 5.3 Disk footprint

```
$ grok du
    740.5 MB  sessions
    405.6 MB  downloads
     25.1 MB  marketplace-cache
     21.8 MB  memtrace
     ...
    1.2 GB    total (~/.grok)
```

### 5.4 PATH integration

```
$ grep -n "grok installer" -A4 ~/.zshrc
71:# >>> grok installer >>>
72:export PATH="$HOME/.grok/bin:$PATH"
73:fpath=(~/.grok/completions/zsh $fpath)
74:autoload -Uz compinit && compinit -C
75:# <<< grok installer <<<
```

A timestamped backup of the previous rc file was kept
(`~/.zshrc.bak.1780069901`).

---

## 6. Authentication status

The installer detected and reused an existing OIDC profile. Non-secret metadata:

| Field | Value |
|---|---|
| `auth_mode` | `oidc` |
| `email` | rifaterdemsahin@gmail.com |
| `first_name` | Rifat Erdem Sahin |
| `oidc_issuer` | `https://auth.x.ai` |
| `create_time` | 2026-09-21T15:45:46Z |
| `expires_at` | 2026-09-21T21:45:46Z |
| `team_id` | 73513b5c-7859-4b02-ae23-ce4994774611 |

### 6.1 One observed caveat

`grok models` reported `You are not authenticated.` in a non-interactive shell even
though the token is present and unexpired:

```
$ grok models
You are not authenticated.

Default model: grok-4.6

Available models:
  * grok-4.6 (default)
```

The default model (`grok-4.6`, configured in `~/.grok/config.toml`) is still reported
and the session token is valid until 21:45 UTC. If an interactive or headless run
prompts for auth, refresh it with:

```bash
grok login          # interactive OAuth
grok logout         # clear cached credentials
```

Deployment-key users can instead set `GROK_DEPLOYMENT_KEY` (takes precedence over
`~/.grok/auth.json`).

---

## 7. What Grok CLI is

`grok --help` describes it as the **Grok Build TUI** — a terminal coding agent, not
just a chat client. Notable capabilities:

- **Interactive TUI** (`grok`) and **headless mode** (`agent`, `grok -p "..."`)
- **Headless output formats:** `plain`, `json`, `streaming-json`, `streaming-messages-json`
- **Subagents** (`--agents`, `--no-subagents`) and per-agent definitions (`--agent`)
- **Git worktrees** (`--worktree`, `grok worktree`) for isolated task branches
- **Permission modes:** `default`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions`, `plan`
- **Model control:** `--model`, `--reasoning-effort`, default `grok-4.6`
- **MCP servers**, plugins/marketplace, memory, sessions, skills, rules
- **Leaders** for background/parallel agent processes

### Subcommands

| Command | Purpose |
|---|---|
| `agent` | Run Grok without the interactive UI |
| `login` / `logout` | Manage authentication |
| `models` | List available models |
| `mcp` | Manage MCP server configurations |
| `plugin` | Manage plugins and marketplace sources |
| `skills` / `memory` / `rules` | Manage agent capabilities and context |
| `sessions` / `export` / `usage` / `trace` | Inspect sessions, transcripts, token cost |
| `worktree` / `clone` | Git worktree and repository tooling |
| `doctor` / `inspect` / `du` | Diagnose environment, config and disk usage |
| `setup` / `update` / `version` | Deployment config, upgrades, version info |
| `leader` / `dashboard` / `cursor-worker` | Background agent orchestration |

---

## 8. Security notes

- Installer performed **no privilege escalation** and wrote only inside `$HOME`.
- The downloaded binary is **executed once for `--version`** before being promoted
  into place; a non-running artifact aborts the install.
- The binary is fetched over HTTPS from `x.ai` or Google Cloud Storage.
- Credentials live in `~/.grok/auth.json` (mode `600`) and are **never** written into
  this repository.
- `GROK_PROXY_URL` is validated to be `https://` with a non-empty host and no embedded
  userinfo before any deployment key is attached.

---

## 9. Usage quick start

```bash
export PATH="$HOME/.grok/bin:$PATH"   # or: restart the terminal

grok                                   # interactive TUI
grok "fix the failing test"            # TUI with an initial prompt
grok -p "summarise this repo"          # one-shot, prints and exits
agent -p "..." --output-format json    # headless with structured output
grok doctor                            # environment health
grok inspect                           # resolved config for this directory
grok usage                             # token/cost usage for a session
grok update                            # check for / install updates
```

---

## 10. Verification checklist

- [x] Installer downloaded and inspected before execution
- [x] `curl -fsSL https://x.ai/cli/install.sh | bash` exited `0`
- [x] Grok CLI **1.0.40 (alpha)** installed for `macos-aarch64`
- [x] `grok` and `agent` both resolve and report the same version
- [x] `grok doctor` → **0 issues, 0 recommendations**
- [x] `~/.grok/bin` added to `PATH` in `~/.zshrc` (backup retained)
- [x] Shell completions generated (bash/zsh/fish)
- [x] OIDC auth profile present and valid to 2026-09-21T21:45:46Z
- [x] Disk usage reported (`~/.grok` ≈ 1.2 GB)
- [ ] Re-run `grok login` if an interactive session reports unauthenticated
