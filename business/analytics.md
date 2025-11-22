# Analytics & Measurement Strategy – curated.guide

We measure only what tells us if the core is working. No vanity metrics.

## What we measure (the only 4 questions that matter)

1. **Activation rate**  
   Signup → first guide published (public) within 7 days.

2. **Pride & depth**  
   Average items per guide + % of guides with cover image + % with personal notes ("why I love this").

3. **Sharing rate**  
   % of published guides that get shared (copy link or social button) at least once in first week.

4. **Retention**  
   % of creators who update a guide in week 2–4.

These four numbers tell us everything. If they go up, we win.

## Stack (minimal & free forever)

- Event tracking → PostHog (cloud, 1M events free)  
- Traffic & perf → Vercel Analytics + Web Vitals  
- Error tracking → Sentry (free tier)  
- Optional later → Plausible or Umami if we want zero-cookie mode

No Supabase events table, no custom forwarding. PostHog does everything we need.

## Events we actually track (5 events only)

| Event                  | When                          | Key properties                  |
|-----------------------|-------------------------------|---------------------------------|
| `user_signed_up`      | Signup complete               | source, referrer                |
| `guide_created`       | First save + publish          | guide_id, item_count, has_cover |
| `item_added`          | Every new item                | guide_id, has_note, has_image   |
| `guide_shared`        | Copy link or social button    | guide_id, channel               |
| `guide_updated`       | Any edit after day 1          | guide_id                        |

That's it. No more.

## Ritual

Every Monday morning:
- Open PostHog
- Look at the 4 numbers above
- Write 3 sentences in Notion: "This week activation X%, pride metrics Y, sharing Z. Doing A/B/C next."

No fancy dashboards, no cohort spreadsheets. Just these numbers.

## Privacy

- No PII in events
- Cookie banner: analytics optional (if declined → only Vercel perf data)
- User can request full event export with their data export
