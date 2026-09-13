# BackTrack — product page and manual

Static site for the BackTrack Android app: a manual with the screens explained, what PRO adds,
and the privacy policy that Google Play links to.

| File | What it is |
|---|---|
| `index.html` | Manual + product page (one page, anchored sections) |
| `privacy.html` | Privacy policy — this is the URL that goes into Play Console |
| `style.css` | All styling. Colours are taken from the app (`ui/theme/Color.kt`, TacticalPalette) |
| `set-site-url.py` | One-shot helper that rewrites the public address everywhere |
| `assets/` | App icon, JetBrains Mono (SIL OFL 1.1, same file as in the APK), screenshots |

No build step, no framework, no JavaScript. Open `index.html` in a browser and it works.

---

## Screenshots

    py tools/zrzuty_na_strone.py        # in the BackTrack repo, phone connected

The script sets the font scale and resolution, builds its own straight four-vertex route,
loads it as guidance, drives the app through the debug simulator so the fix is live on every
frame, and writes WEBP straight into `assets/shots`. Run it after any UI change and most of
the manual is true again.

**It deliberately does not do all of them.** The welcome screen only exists on a clean
install; the measuring shots depend on where the camera happens to be; averaging takes thirty
seconds and closes itself; import and the offline panel need the system file picker. Those are
taken by hand and dropped into `assets/shots` under the same names. The script's own header
lists them and says why.

Screenshots use a simulated position, so no real tracks or home coordinates reach the website.

