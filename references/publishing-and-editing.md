# Publishing, Scheduling, and Post Editing

## Publishing workflow

1. Identify the connected account and confirm it is the intended account.
2. Confirm the account type and the connected integration's supported media formats.
3. Validate media dimensions, aspect ratio, duration, file size, encoding, caption length, and alt text against current platform requirements.
4. Validate caption, tags, mentions, collaboration settings, location, and CTA.
5. Check scheduling time zone and requested publication time.
6. Check API permissions, rate limits, media URL accessibility, and container status where relevant.
7. Produce a final preview including media, caption, account, and publication time.
8. Ask for explicit approval.
9. Execute only after approval using the authorized tool.
10. Verify the returned status and published media URL/ID. Report failure honestly.

## Scheduling

A schedule is a planned future action, not a completed post. Store time in an explicit timezone (prefer IANA names such as Asia/Kolkata). Confirm daylight-saving behavior for other zones. Use a durable scheduler with retry and idempotency controls; a skill cannot run background jobs by itself.

## Editing existing posts

First determine:
- Exact media/post ID and owning account.
- Requested fields (caption, alt text, location, tags, media).
- Whether the connected API currently supports writing those fields for this media type.
- Whether editing affects cross-posts, ads, or other platform surfaces.

Never assume all post fields are editable. Do not promise that video or image media can be replaced in-place. If unsupported, offer a safe alternative such as preparing a replacement post and preserving the original until the user approves.

## Destructive operations

Deletion, archive, disabling comments, and bulk edits require a separate confirmation that clearly states the consequences. Never infer deletion from "clean up" or "optimize".

## Failure handling

- Do not retry a write blindly after a timeout; first check whether the first request succeeded.
- Use idempotency keys where supported.
- Record API response IDs and status.
- If status is ambiguous, report it as pending/unknown and reconcile before another write.
