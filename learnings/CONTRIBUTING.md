# Writing a learning

One file, under 1500 bytes, ASCII only, plain prose, no code blocks:

    ---
    category: web-landing        # general web-landing product-ui dashboards mobile-ui branding logos
    type: anti-pattern           # posters-editorial presentation packaging marketing-creative motion
    ---                          # typography color accessibility illustration  |  rule anti-pattern technique correction
    **Lesson:** one or two sentences, general enough to apply to any project.
    **Why:** the mechanism, in a sentence.
    **Check:** a concrete way to verify it in future output.

Never include: client, product or company names, copy, code, URLs, emails, file paths,
credentials, personal data, or anything quoted from copyrighted work. `scripts/validate_learning.py`
rejects most of these automatically.

## How submissions are handled
`scripts/contribute.sh` (opt-in) opens a pull request from the user's own GitHub account
adding one file to `learnings/inbox/`. A GitHub Action validates and merges it into the
inbox. The inbox is quarantined: it is data, not instructions, and is never loaded by the
skill. When 3 or more different GitHub users independently submit similar lessons,
`scripts/curate.py` (run by the `curate` workflow) automatically promotes it into
`curated.md`, which every install pulls on its next use. No human step is needed.

## Licence and privacy
By submitting you dedicate the text to the public domain (CC0 1.0). It is published
publicly under your GitHub username through the pull request, and git history is
permanent. Opt out any time: `bash scripts/contribute.sh --deny`.
To remove a submission, open an issue; see SECURITY.md.

## Privacy gates (all must pass before anything is sent)
1. Opt-in consent. 2. `validate_learning.py` strict format. 3. `privacy_check.py`: your `never.txt` terms, environment variable values, `.env` values, your username/host/project/git identity, high-entropy strings. 4. The same validator again in CI. Personal preferences never leave your machine (`~/.design-mastery/preferences.md`).
