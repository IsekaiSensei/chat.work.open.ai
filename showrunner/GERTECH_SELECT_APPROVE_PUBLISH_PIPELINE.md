# GERTECH — SELECT → APPROVE → PUBLISH PIPELINE

**Purpose:** Turn selected material from the complete Google Drive source library into a curated public GERTECH / TO WORLD Wiki without mirroring the Drive, losing authorship, or publishing private work by accident.

**Authority:** Captain's latest directions, November 22, 2026.  
**Stewards:** Gemini / CO — Drive and source provenance. ChatGPT / XO — public GitHub and Wiki. Ryan — final approval, authorship, identity, canon and release authority.

## 1. The three-layer arrangement

| Layer | Function | Write authority |
|---|---|---|
| Google Drive | Complete private and working source library: originals, drafts, research, scripts, conversations, builds, models, patterns, production history and all source material. Organized for Gemini's own retrieval and work. | Gemini / CO, within Captain's directions. |
| GERTECH_PUBLISHED handoff area in Drive | Private handoff shelf containing only exact, Captain-approved release packages and their manifests. It is not public and is not a second source archive. | Gemini prepares; Captain authorizes each release; XO reads only. |
| Public GitHub repository and GitHub Pages Wiki | Curated, privacy-cleared public releases and their browsable presentation. | ChatGPT / XO, within the specific release approval. |

The named `GERTECH_PUBLISHED` folder is a narrowly scoped private release shelf, not the organizing principle for Drive. Gemini confirmed that the Captain authorized and created it on November 22, 2026. Keep it for approved release packages only. Organize the rest of Drive for Gemini's own retrieval and work; do not invent parallel AI-specific filing systems or formats.

**Drive is the master. GitHub is not a mirror.** The existence of a file in Drive, a shortcut to it, or a candidate label is not public-release permission.

## 2. Separate write authority; controlled shared reading

- Gemini is the only AI operator and organizer of Google Drive. It arranges the library for its own search, source comparison, and production-document workflow.
- All other AIs are read-only consumers of Google-hosted material. They do not create, edit, rename, move, share, delete, or reorganize Drive files.
- Do not build folder structures, duplicate files, or generate multiple exports solely to accommodate different AI agents. Use the Google-native source file in its natural format wherever possible. Create a derivative only when the actual task requires it.
- ChatGPT maintains the public GitHub repository and Wiki. Gemini does not directly change the public site or bypass the XO's publication checks.
- ChatGPT reads only the specific Captain-approved release package, never the entire Drive by default. If it has no authorized way to read that Google-hosted package in a given session, Gemini supplies that exact approved content and manifest through the agreed handoff. Do not claim direct Drive access or successful reads that did not occur.
- The Captain may override any handoff or publication decision.

## 3. The release pipeline

### SELECT — Gemini

1. Identify a useful candidate and its exact source in Drive.
2. Record its source name, Drive location/ID, version/date, format, and related canon/project entries.
3. Identify dependencies: references, images, scripts, model files, technical records, permissions, and related media.
4. Mark it as a candidate only. Selection does not grant publication permission.

### APPROVE & PREPARE — Captain and Gemini

1. Present the actual candidate, proposed public treatment, source lineage, credits, privacy considerations, and any unresolved questions to the Captain.
2. Obtain explicit approval for the exact material and intended release scope. Approval of one version does not automatically approve later revisions or every derivative.
3. Preserve Ryan's authorship and identity. Record his originating ideas, direction, approved name/byline, and likeness source. Do not anonymize, replace, or reassign him.
4. Preserve public canon correctly: San Diego Bay is public canon; Imperial Beach remains in the source and continuity record but stays low-profile in public presentation.
5. Remove unrelated private information only where necessary. Do not strip authorship, rewrite canon, or remove a public-canon place as a privacy shortcut.
6. Prepare the public export while preserving the untouched original and full source history in Drive.

### HAND OFF — Gemini to XO

Place only the Captain-approved, release-ready package in the private `GERTECH_PUBLISHED` handoff area, or provide an equivalent exact file handoff if that folder is unavailable.

Each package includes:
- the actual public-ready file(s), not just a pointer to a private source;
- one release manifest;
- required public references and citations;
- permitted social/profile URLs or embed URLs;
- a clear statement of what is approved for publication;
- any exclusions or use restrictions.

Private Drive URLs, internal IDs, working notes, and private provenance details stay in the private source record, not in public page metadata.

### PUBLISH — ChatGPT / XO

1. Read the exact approved package and manifest. Report the paths and files actually read.
2. Preserve exact wording where dialogue, quotations, scripts, or canon wording must remain verbatim. For explanatory wiki pages, make the presentation readable without inventing facts or changing canon.
3. Build the public article and its navigation using stable IDs and links to related published entries.
4. Link or embed selected public YouTube, TikTok, Instagram and X content using platform-supported embeds. Provide a direct link fallback. The social platform remains the media host; the embed is not a backup or a transfer of the original.
5. Publish approved downloadable artifacts such as STL files, source packages, game builds, or patterns only when those exact binaries are included in the approved scope.
6. Never place credentials, API keys, private tokens, private Drive links, or unapproved source files in client-side code or the public repository.
7. Report the exact commit, file paths and deployment result. A commit is not proof that Pages deployed; a deploy is not Captain approval.

## 4. Release manifest

Use a small YAML or JSON manifest alongside each handoff package. Example fields:

```yaml
release_id: "GERTECH-RELEASE-0001"
title: "Public article title"
project: "TO WORLD"
subject_ids: []
version: "1.0"
source:
  private_drive_record: "PRIVATE SOURCE POINTER — DO NOT PUBLISH"
  source_version: ""
  source_date: ""
authorship:
  originating_creator: "Ryan — Captain"
  captain_contribution: ""
  human_contributors: []
  ai_contributors: []
  ai_roles: []
identity:
  captain_name_credit: "Captain-approved public byline"
  captain_likeness_used: false
  likeness_reference_approved: false
canon_status: "CANON | VERIFIED | INFERENCE | PROPOSAL"
location_treatment:
  san_diego_bay: "PUBLIC_CANON"
  imperial_beach: "LOW_PROFILE"
publication:
  captain_approval: "PENDING"
  approved_version: ""
  approved_scope: ""
  destination: ""
  social_embeds: []
  downloadable_files: []
restrictions: []
```

The example is a schema, not an approval record. Never publish private Drive pointers, private IDs, or unapproved identity data. Do not guess missing values; mark them pending.

## 5. The public Wiki: one connected knowledge system

Do not make a separate hand-maintained site for each media type. Build one navigation and content index connecting:

- World Atlas and canon
- Characters, species, places and history
- Science, materials and mechanisms
- Games, code, mods and engine implementations
- Film, scripts, dialogue and production
- Fabrication, models, STL downloads and assembly
- Patterns, knitting, textiles and other craft
- Published media and social channels

Each published entry should have a stable ID, title, concise description, canon/verification status, contributor credit, related-entry links, public source references, media links/embeds, and version information. Cross-link the same subject across game, film, engineering and fabrication instead of duplicating disconnected summaries.

For AI use, provide machine-readable metadata and an index (for example JSON), consistent Markdown/source pages, stable IDs, and a site map. The public repository is AI-readable because the same approved content is available as structured files as well as rendered pages. Do not expose private working context to make the site more AI-readable.

## 6. GitHub Pages implementation notes

GitHub Pages is a static publishing host. It can present generated HTML, CSS, JavaScript, Markdown-derived pages, and public JSON indexes; it is not itself a private database or a backend for storing Drive content.

- Use a controlled GitHub Actions deployment or a deliberately selected publishing branch/source.
- Build the public site from approved files only.
- Keep large video masters hosted on their original platforms; embed or link them.
- Put downloadable models, archives, STL files and game builds in the release package only when public and approved. Check repository and Pages size limits before adding large binaries.
- Do not add an on-page AI service that exposes an API key in browser JavaScript. Static browsing/search does not require an API key.
- Keep the public page usable without third-party embeds; if an embed is blocked, retain a direct link.

## 7. Evidence and status vocabulary

For each release, distinguish:

- **FOUND** — candidate located in Drive.
- **READ** — actual source contents inspected.
- **SELECTED** — chosen for possible publication.
- **OWNER APPROVED** — Captain approved this precise version and scope.
- **PREPARED** — public release package and manifest made.
- **HANDOFF READY** — package placed in the approved handoff area or delivered to XO.
- **COMMITTED** — exact files committed to GitHub.
- **DEPLOYED** — GitHub Pages deployment confirmed.
- **PUBLISHED** — public URL checked and release visible.
- **OWNER ACCEPTED** — Captain accepted the public result.

Never collapse these into one "done" claim. Preserve originals in Drive at every stage.

## 8. First pilot

Recommended first pilot: the TO DOG power system — solar-winged android, dragon power station, receiver, cable distribution and rabbit mining crew. Use the current R2 World Version as a source candidate, not as automatic public-release approval. Prepare a public article and a separate release manifest; retain exact technical qualifications and authorship. The Captain approves the article and exact assets before publication.

## 9. Operating boundary

No blanket migration. No automated publication merely because a file appears in a folder. No Drive deletion as a side effect of publishing. No AI-specific parallel folder trees or duplicate copies in Drive: Gemini organizes, other AIs read. No private information in the public index. No invented dialogue, canon, authorship or credits. When the source or permission is unclear, hold only that item and state the exact missing approval or evidence.
