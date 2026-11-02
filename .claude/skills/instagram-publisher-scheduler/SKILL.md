---
name: instagram-publisher-scheduler
description: Prepare, validate, schedule, and publish approved Instagram content using an authorized publishing integration. Use for posting and scheduling requests.
---
# Instagram Publisher and Scheduler

This skill coordinates publishing; it does not provide API access on its own.

## Preflight
- Confirm account identity and account eligibility.
- Confirm media format and current platform constraints.
- Validate media URL/accessibility, dimensions, duration, file size, caption, alt text, tags, mentions, and CTA.
- Confirm time and timezone.
- Check permission scopes, publishing limits, and container status if exposed.
- Prepare a final preview with account, media, caption, and schedule.

## Approval gate
Before any write call, ask the user to approve the exact account, exact content, and exact publish time. A prior general instruction is not blanket approval for future posts.

## Execution and verification
Use only the connected authorized tool. Handle retries idempotently; after timeouts, reconcile status before retrying. Report the confirmed result, media ID/URL, timestamp, or honest failure state. Never say "posted" when only scheduled or drafted.
