# Platform Capabilities and Integration Boundaries

## Core distinction

A Claude Agent Skill is an instruction package. It does not itself provide Instagram API access, OAuth, an API key, browser access, account credentials, or the ability to publish. Real execution requires an authorized connector, browser workflow, or application integration.

## Official integration model

Use the current Meta developer documentation as the source of truth. Instagram Platform capabilities and permissions differ by login configuration, account type, app review status, and API version. At a high level, professional accounts (Business/Creator) have API capabilities for selected publishing, comments, mentions, insights, and messaging workflows, subject to separate permissions and limitations. Personal/consumer accounts do not have identical capabilities.

Official references:
- Instagram Platform overview: https://developers.facebook.com/docs/instagram-platform/
- Content publishing: https://developers.facebook.com/docs/instagram-platform/content-publishing/
- Instagram API with Instagram Login: https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/
- Instagram API with Facebook Login: https://developers.facebook.com/docs/instagram-platform/instagram-api-with-facebook-login/

## Capability matrix

| Capability | Agent can prepare | External authorized access needed |
|---|---:|---:|
| Profile audit from supplied/public information | Yes | Optional for live profile data |
| Competitor/public content research | Yes, within available sources | Search/browser access |
| Generate hooks/captions/scripts | Yes | No |
| Create calendar and draft queue | Yes | No |
| Publish images/Reels/carousels | Prepare and validate | Yes; eligible account, permission, API/tool |
| Schedule posts | Prepare schedule | Yes; scheduler or application backend |
| Read comments on own media | No direct access by skill | Yes; supported API permission |
| Reply to comments on own media | Draft replies | Yes; supported API permission |
| Comment on other accounts' posts | Draft suggestions | Must verify current API support; do not assume arbitrary public commenting is supported |
| Edit existing post caption/fields | Propose edits | Yes; verify exact writable field for API version and media type |
| Replace existing media in-place | Do not assume | Often requires creating/publishing a new post; verify current API |
| Read own Insights | Analyze exported data | Yes; account insights permission or user export |
| Read competitor private Insights | No | Not available without account owner's authorized access |
| DM automation | Draft response workflows | Separate messaging permissions and policy constraints |

## Integration architecture recommendation

Keep the skill layer provider-agnostic. Implement actual actions in a separate adapter:
- OAuth and token lifecycle handled server-side.
- Least-privilege scopes and app review.
- Encrypted token storage; never expose tokens to prompts or logs.
- Explicit approval gate for each write operation.
- Idempotency and duplicate-send protection.
- Rate-limit handling and retry policy.
- Audit log with actor, target, payload hash, timestamp, and API result.
- Webhooks for async status where supported.
- Dry-run mode for all publishing and editing operations.

Never hardcode API versions or permission names from old tutorials. Confirm them against current Meta docs before implementation.
