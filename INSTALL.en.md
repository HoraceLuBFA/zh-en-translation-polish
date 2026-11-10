# zh-en-translation-polish installation guide

[GitHub repository](https://github.com/HoraceLuBFA/zh-en-translation-polish) · [Detail page](https://www.lumenghe.com/en/skills/zh-en-translation-polish/)

## Install from GitHub

1. **Check prerequisites.** An Agent Skills host; Python 3 with its standard library for the advisory scanner.
2. **Inspect the existing installation.** Check `~/.agents/skills/zh-en-translation-polish/` and the host's same-named entry, including directories, files, symlinks and broken links. Preserve the existing version and local changes before an update. Use the README's GitHub installation command for a new installation; review and merge changes when updating an existing checkout.

## Install the website ZIP

3. **Select and verify the package.** [Release metadata](https://www.lumenghe.com/skills/zh-en-translation-polish/release.json) lists the source commit, ZIP URL and SHA-256. Download into a temporary directory and compare the checksum. Inspect member paths: one `zh-en-translation-polish/` root, relative paths within it, and safe link destinations. Stop installation if checksum or path validation fails.
4. **Place the complete skill.** Extract `SKILL.md`, README, installation guides, license, scripts and reference files together into `~/.agents/skills/zh-en-translation-polish/`, preserving directory structure and executable permissions. For an existing installation, retain its backup and apply the reviewed merge or replacement.

## Configure and verify

5. **Configure the host entry.** Codex uses the shared `~/.agents/skills/` directory. Claude Code uses `~/.claude/skills/`; inspect its entry and create a symlink to the shared skill when that path is free. Follow the current host documentation for other agents. Keep changes within this skill and its discovery entry; interactive authentication stays with the user.
6. **Verify and report.** Check `SKILL.md`, supporting files and dependencies; confirm discovery in the host's skill list or a new session. Use a temporary sample for any requested behavior check. Report the installation path, source commit, dependency and discovery results, checks performed and retained backup.

The [plain-text website guide](https://www.lumenghe.com/en/skills/zh-en-translation-polish/install.txt) includes the current package URL and checksum.
