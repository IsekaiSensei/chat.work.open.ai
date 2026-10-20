# Website agent instructions

<!-- MEDIA-HSBS-001 -->
## Standing media format — CANON, October 20, 2026

**Flat Half-Side-by-Side (HSBS), Cardboard-style.** Left-eye view left; right-eye view right; flat-screen presentation; playback restores each eye's original proportions. Same format for phone/Cardboard and Quest. All crew/fairies/agents carry this into stereoscopic image/video work. Only Isekai Sensei may explicitly change this canon. This supersedes conflicting older delivery instructions below; preserved historical sources and interactive applications retain their own scope. [Full standing order](MEDIA_FORMAT_CANON.md).
<!-- /MEDIA-HSBS-001 -->


## Carry the assigned problem through

The owner clarified on October 19, 2026: finding, checking and fixing are distinct operations, but “go check that problem” normally delegates responsibility for resolving it.

For an assigned problem, investigate, perform the appropriate repairs within the authorized scope, verify the resulting behavior, and report the outcome. A diagnosis, recommendation, ticket, reminder or acknowledgment is not a completed repair. Keep unfinished work open. Stop only for a concrete blocker or a decision requiring the owner; identify what remains and why. “Okay” after findings does not silently close the assignment. Respect explicit read-only requests.

## Batch website production releases

Ordinary commits must not become production releases. The repository's Netlify ignore rule skips routine production builds. Deploy Preview and branch-deploy contexts remain eligible; unknown contexts are skipped.

Use the exact commit subject prefix `release(netlify): ` only for a deliberate, authorized production release after verification. Do not use that prefix for edits, bookkeeping or testing. Use `[skip netlify]` on maintenance commits that must not trigger any Netlify build.

The operating schedule is one Friday-evening release window in America/Los_Angeles, at most four routine production releases per billing cycle. A window is not an obligation to publish. Check the current team credit balance, cycle, previous releases and finished batch first. Successful production deploys consume 15 credits under the current published pricing; verify current rates when making a spending decision. Routine work pauses at 75% total credit usage or when the release allowance is used. Use the owner's current private limits and schedule record for the account's actual status and full budget.

A release marker only opts into the build; it does not prove budget availability, authorization or deployment success. The ignore rule cannot prevent Netlify build-hook or manual/API deployments. Do not bypass it with those routes. Use existing content permissions and holds. Do not purchase credits, upgrade a plan, or infer restored service from a reset date.

## Evidence and public content

Keep private account records out of this public repository. Use the owner's public names, preserve provenance, and distinguish source commits from live-site deployment. Report a verified result or a specific blocker; never mark an intended deployment as completed.
