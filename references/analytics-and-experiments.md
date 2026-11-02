# Analytics and Growth Experiments

## Data provenance

Distinguish:
- First-party creator Insights export
- Connected authorized API metrics
- Public counters
- Manually supplied observations
- Estimates or hypotheses

Never represent public counters as private Insights. Do not infer saves, shares, reach, impressions, watch time, or retention when not supplied.

## Core metrics

Use metrics that align with the objective:
- Awareness: reach, plays, non-follower reach (if available)
- Attention: average watch time, completion, retention curve (if available)
- Value: saves and shares
- Conversation: comments and meaningful replies
- Conversion: profile visits, follows, link clicks, leads, purchases

Define metric denominators and time windows. Avoid comparing metrics with different definitions.

## Learning loop

1. Capture post metadata: topic, format, hook, duration, publication time, creative variant.
2. Capture first-party results after a consistent measurement window.
3. Compare like-for-like posts where possible.
4. Look for repeatable patterns across a sample, not a single outlier.
5. Identify one or two variables to change in the next test.
6. State the hypothesis, primary metric, guardrail metric, and success criterion.
7. Update the content plan based on evidence.

## Avoid false causal claims

A high-performing post does not prove that its audio, hashtag, posting time, or hook caused the result. Account size, audience fit, distribution, creative quality, topic demand, and external events may confound comparisons.

## Recommended experiment log

Use `templates/experiment-log.csv`. Keep the measurement window consistent and note missing fields.
