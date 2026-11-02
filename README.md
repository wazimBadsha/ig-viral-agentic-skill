# Instagram Agentic Skill Suite

An open-source, modular agent skill suite for end-to-end Instagram content operations: niche research, viral-content analysis, profile optimization, content creation, community engagement, publishing workflows, post improvement, and analytics.

**Independent project. Not affiliated with Meta/Instagram or Anthropic.** Skills provide workflows and decision logic; they do not magically grant Instagram access. Actions such as publishing, editing, commenting, replying, and messaging require an authorized integration, the right account permissions, and explicit approval.

## The 13 skills

| # | Skill | Purpose |
|---|---|---|
| 1 | Account Audit | Audit account positioning, content mix, profile, and goals |
| 2 | Niche Research | Research audiences, competitors, themes, and content gaps |
| 3 | Viral Discovery | Find public high-performing examples and extract patterns |
| 4 | Hook Lab | Generate and test opening hooks |
| 5 | Caption & Copywriter | Draft captions, CTAs, hashtags, and post copy |
| 6 | Content Studio | Create Reels, carousels, Stories, and static-post briefs |
| 7 | Profile Optimizer | Improve bio, name field, positioning, highlights, and conversion path |
| 8 | Content Calendar | Build a 7-day / 30-day plan and publishing queue |
| 9 | Outbound Engagement | Research relevant conversations and draft thoughtful comments |
| 10 | Comment Reply Manager | Classify and draft replies to comments on owned content |
| 11 | Publisher & Scheduler | Prepare, validate, schedule, and publish approved content through authorized APIs |
| 12 | Post Optimizer | Improve existing post copy, metadata, creative briefs, and repurposing plans |
| 13 | Analytics & Growth Coach | Analyze first-party performance and recommend experiments |

## Repository structure

- `.claude/skills/<skill-name>/SKILL.md`: 13 Claude Code discoverable skills.
- `SKILL.md`: master orchestrator, also usable as a single Claude custom skill.
- `references/`: shared research, policy, publishing, and analytics references.
- `templates/`: briefs, calendars, approval records, and experiment logs.
- `scripts/`: local validation and scoring utilities.

## Install

### Claude Code: all 13 skills

Clone the repository and place it in your project, or copy the skills into your personal Claude skills directory:

```bash
git clone https://github.com/wazimBadSha/ig-viral-agentic-skill.git
mkdir -p ~/.claude/skills
cp -R ig-viral-agentic-skill/.claude/skills/* ~/.claude/skills/
```

For project-only installation, copy the folders into `.claude/skills/` in your project.

### Claude.ai: master skill

Package the repository root `SKILL.md` with the `references/` directory into a ZIP and upload it through Claude's Skills settings. For the complete 13-skill set, install the individual skill folders in an environment that supports filesystem-based skills, such as Claude Code.

## Example requests

- "Audit my Instagram profile and give me a prioritized conversion-focused improvement plan."
- "Research the Indian AI creator niche and find repeatable Reel formats."
- "Analyze these 20 Reel URLs and extract hook and storytelling patterns."
- "Create a 7-day content calendar with scripts, captions, and CTAs."
- "Find relevant public conversations in my niche and draft non-spammy comments. Ask before posting."
- "Classify comments on my latest posts and draft replies for approval."
- "Prepare this Reel for publishing tomorrow at 6 PM. Validate it and ask me to approve before publishing."
- "Improve the caption and creative brief of this existing post without changing or deleting anything."
- "Analyze my exported Insights data and recommend the next three experiments."

## Action and permission model

| Action | Default behavior |
|---|---|
| Research public sources | Allowed through available, authorized search/browser tools |
| Draft content / captions / comments / replies | Allowed |
| Prepare a publishing queue | Allowed |
| Publish or schedule a post | Requires explicit approval and authorized publishing access |
| Edit an existing post | Requires explicit approval and API support for the exact field |
| Delete or archive content | Never inferred; separate explicit confirmation required |
| Post comments / replies / DMs | Requires explicit approval, supported permissions, and anti-spam checks |
| Bulk comments, mass following, engagement pods, scraping private data | Not supported |

The agent must never claim an action succeeded until the connected tool/API confirms it.

## Instagram access reality

A Claude Skill is a set of instructions and optional scripts. It is not a Meta integration, OAuth client, access token, or API key. The capabilities available at runtime depend on connected tools and account permissions.

For official API operations, consult the current Meta documentation. Instagram publishing, comment moderation, messaging, and insights are separate capabilities with separate eligibility and permissions. Consumer/personal accounts and professional accounts do not have identical API access. Public competitor research must use sources actually available to the agent; do not claim access to private Insights, saves, shares, reach, or watch-time for other accounts.

See `references/platform-capabilities.md` and `references/safety-and-approvals.md`.

## Validate

```bash
python3 scripts/validate_suite.py
python3 -m unittest discover -s tests -v
```

## License

MIT. See [LICENSE](LICENSE).
