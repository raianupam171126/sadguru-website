# Sadguru Industrial Enterprises — website

A fast static website. No database, no plugins, nothing to update or patch.

## What is in this folder

| Item | What it is |
|---|---|
| `site.json` | Company details and every product. Edit this for products, prices, contact details. |
| `content.py` | FAQ, materials guide, glossary, ordering steps and the knowledge guides. Edit this to add or change articles. |
| `build.py` | Turns `site.json` into finished web pages. Run it after any edit. |
| `css/style.css` | Site design. |
| `images/` | Placeholder product images. Replace with real photos (see below). |
| `dist/` | The finished website. **Upload this folder's contents to the host.** |

## Before going live — fill in these placeholders in `site.json`

1. `phone_display`, `phone_link`, `whatsapp` — the real business number (currently +91 XXXXX XXXXX). `whatsapp` is digits only with country code, e.g. `919876543210`.
2. `email` — a real address, ideally `info@<your-domain>`.
3. `street_address` and `postal_code` — the factory address. This also feeds Google's local-business data.
4. `domain` — the domain you buy, e.g. `https://sadguruinsulation.com`. This sets canonical links and the sitemap.
5. `form_action` — the contact form needs a free form service. Sign up at formspree.io, create a form, and paste the URL it gives you. Until then the form will not send.
6. Product photos — the pages currently load the photos from IndiaMART's servers. If those ever change, the site shows a "photo coming soon" placeholder instead. Better: take 7 photos (one per product), save them as `images/<slug>.jpg` and change each product's `image` in `site.json` to `images/<slug>.jpg`.

Then run `python build.py` and re-upload `dist/`.

## How to put it online (about 30 minutes)

1. **Buy the domain** at Hostinger, GoDaddy India or Namecheap. Sadguruinsulation.com and sadguruindustrial.in looked free on 4 Oct 2026.
2. **Host it free** on Netlify: go to app.netlify.com, drag the `dist` folder onto the page. It goes live on a netlify.app address immediately.
3. **Connect the domain**: in Netlify, Domain settings → Add custom domain → follow the DNS steps at the registrar. HTTPS is automatic.
4. **Google Search Console** (search.google.com/search-console): add the domain, verify, submit `https://<domain>/sitemap.xml`.
5. **Google Business Profile** (business.google.com): create a listing for the Jhansi factory with the same name, address and phone as the site. This matters as much as the website for local search.
6. Add the new website link to the IndiaMART profile.

## Adding a guide article

Open `content.py`, copy one entry in `GUIDES`, give it a new `slug` and `title`, write the body as paragraphs, `("h2", ...)` headings, `("list", [...])` bullets or `("table", header, rows)`. Run `python build.py`. The article, its listing, sitemap entry and schema are generated.

## Adding or changing a product

Open `site.json`, copy one product block, change `slug` (lowercase, hyphens, no spaces), name, specs, applications. Run `python build.py`. A new page, sitemap entry, footer link and home-page card appear automatically.

To hide prices site-wide, set `"show_prices": false`.
