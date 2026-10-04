"""
Static-site generator for Sadguru Industrial Enterprises.

  site.json   -> company details and products
  content.py  -> FAQ, materials guide, glossary, how-to-order, knowledge guides
  build.py    -> writes finished pages into dist/

To change anything, edit site.json or content.py and run:  python build.py
Then upload the dist/ folder to the host.
"""

import json
import shutil
from datetime import date
from pathlib import Path

import content as C

ROOT = Path(__file__).parent
DIST = ROOT / "dist"

with open(ROOT / "site.json", encoding="utf-8") as f:
    SITE = json.load(f)

CO = SITE["company"]
PRODUCTS = SITE["products"]
DOMAIN = SITE["domain"].rstrip("/")
TODAY = date.today().isoformat()
YEARS = date.today().year - int(CO["founded"])

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">')


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def wa_link(message):
    return f"https://wa.me/{CO['whatsapp']}?text={message.replace(' ', '%20')}"


def json_ld(data):
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


def org_schema():
    return {
        "@context": "https://schema.org",
        "@type": ["LocalBusiness", "Manufacturer"],
        "@id": f"{DOMAIN}/#business",
        "name": CO["name"],
        "url": DOMAIN,
        "image": f"{DOMAIN}/{PRODUCTS[0]['image']}",
        "telephone": CO["phone_link"],
        "email": CO["email"],
        "foundingDate": CO["founded"],
        "founder": {"@type": "Person", "name": CO["proprietor"]},
        "taxID": CO["gst"],
        "numberOfEmployees": {"@type": "QuantitativeValue", "maxValue": 10},
        "address": {
            "@type": "PostalAddress",
            "streetAddress": CO["street_address"],
            "addressLocality": CO["city"],
            "addressRegion": CO["state"],
            "postalCode": CO["postal_code"],
            "addressCountry": "IN",
        },
        "areaServed": {"@type": "Country", "name": "India"},
        "openingHours": "Mo-Sa 09:00-18:00",
        "sameAs": [CO["indiamart_url"]],
        "knowsAbout": ["transformer insulation", "pressboard", "dovetail spacers", "phenolic laminate", "Permawood"],
    }


def breadcrumb_schema(items):
    """items: list of (name, url-path)"""
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": f"{DOMAIN}/{u}"} for i, (n, u) in enumerate(items)
        ],
    }


def faq_schema(pairs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs
        ],
    }


def faq_html(pairs):
    return '<div class="faq">' + "".join(
        f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in pairs
    ) + "</div>"


def crumbs_html(items, up):
    """items: list of (name, href-or-None)"""
    parts = []
    for name, href in items:
        parts.append(f'<a href="{up}{href}">{name}</a>' if href is not None else name)
    return '<div class="crumbs">' + " &rsaquo; ".join(parts) + "</div>"


# ---------------------------------------------------------------------------
# Page frame
# ---------------------------------------------------------------------------

def page(title, description, body, path, keywords="", extra_head="", depth=0, og_image=None):
    up = "../" * depth
    canonical = f"{DOMAIN}/{path}".replace("/index.html", "/")
    og_image = og_image or f"{DOMAIN}/{PRODUCTS[0]['image']}"
    nav = "".join(
        f'<a href="{up}{href}">{label}</a>' for label, href in [
            ("Home", "index.html"), ("Products", "products/index.html"), ("Materials", "materials-and-standards.html"),
            ("Guides", "guides/index.html"), ("FAQ", "faq.html"), ("About", "about.html"),
        ]
    )
    product_links = "".join(f'<li><a href="{up}products/{p["slug"]}.html">{p["name"]}</a></li>' for p in PRODUCTS)
    keywords_tag = f'<meta name="keywords" content="{keywords}">' if keywords else ""

    return f"""<!DOCTYPE html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
{keywords_tag}
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta property="og:site_name" content="{CO['name']}">
<meta property="og:locale" content="en_IN">
<meta name="twitter:card" content="summary_large_image">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="geo.region" content="IN-UP">
<meta name="geo.placename" content="{CO['city']}">
<meta name="theme-color" content="#14283f">
{FONTS}
<link rel="stylesheet" href="{up}css/style.css">
{extra_head}
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{up}index.html" aria-label="{CO['name']} home">
      <span class="brand-mark" aria-hidden="true">S</span>
      <span class="brand-name">{CO['name']}<small>Transformer insulation components, {CO['city']}</small></span>
    </a>
    <button class="nav-toggle" aria-label="Open menu" aria-expanded="false" onclick="var n=document.querySelector('.nav');n.classList.toggle('open');this.setAttribute('aria-expanded',n.classList.contains('open'))">&#9776;</button>
    <nav class="nav" aria-label="Main">{nav}<a class="btn btn-primary" href="{up}contact.html">Get a quote</a></nav>
  </div>
</header>

{body}

<section class="cta-band">
  <div class="wrap">
    <div><h2>Have a drawing? Send it over.</h2><p>Price and delivery time back within one working day.</p></div>
    <div style="display:flex;gap:10px;flex-wrap:wrap">
      <a class="btn btn-primary" href="{up}contact.html">Request a quote</a>
      <a class="btn btn-light" href="{wa_link('Hello, I have an enquiry about transformer insulation components.')}" target="_blank" rel="noopener">WhatsApp</a>
    </div>
  </div>
</section>

<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <h3>{CO['name']}</h3>
        <p>Manufacturer of transformer insulation components since {CO['founded']}.<br>
        {CO['street_address']}<br>{CO['city']}, {CO['state']} {CO['postal_code']}, {CO['country']}<br>
        GST {CO['gst']}</p>
        <p>Phone: <a href="tel:{CO['phone_link']}">{CO['phone_display']}</a><br>
        Email: <a href="mailto:{CO['email']}">{CO['email']}</a></p>
      </div>
      <div><h3>Products</h3><ul>{product_links}</ul></div>
      <div><h3>Know-how</h3><ul>
        <li><a href="{up}materials-and-standards.html">Materials and standards</a></li>
        <li><a href="{up}guides/index.html">Guides</a></li>
        <li><a href="{up}glossary.html">Glossary</a></li>
        <li><a href="{up}faq.html">FAQ</a></li>
      </ul></div>
      <div><h3>Company</h3><ul>
        <li><a href="{up}about.html">About us</a></li>
        <li><a href="{up}how-to-order.html">How to order</a></li>
        <li><a href="{up}contact.html">Contact</a></li>
        <li><a href="{CO['indiamart_url']}" rel="nofollow noopener" target="_blank">IndiaMART profile</a></li>
      </ul></div>
    </div>
    <div class="copy">&copy; {date.today().year} {CO['name']}, {CO['city']}. All rights reserved.</div>
  </div>
</footer>
<a class="wa-float" href="{wa_link('Hello, I have an enquiry about transformer insulation components.')}" target="_blank" rel="noopener">WhatsApp us</a>
</body>
</html>
"""


def product_tile(p, up=""):
    price = f'<div class="price">{p["price"]}</div>' if CO["show_prices"] else ""
    return f"""<a class="tile" href="{up}products/{p['slug']}.html">
  <img src="{up}{p['image']}" alt="{p['name']} made by {CO['name']}, {CO['city']}" loading="lazy" width="676" height="507">
  <div class="tile-body"><h3>{p['name']}</h3><p>{p['short']}</p>{price}</div>
</a>"""


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def build_home():
    tiles = "".join(product_tile(p) for p in PRODUCTS)
    by_slug = {p["slug"]: p for p in PRODUCTS}
    hero_imgs = [by_slug["transformer-insulation-kit"], by_slug["dovetail-spacers"], by_slug["pressboard-strips"]]
    photos = "".join(f'<img src="{p["image"]}" alt="{p["name"]}" width="676" height="507">' for p in hero_imgs)
    guides = "".join(
        f'<a href="guides/{g["slug"]}.html"><h3>{g["title"]}</h3><p>{g["summary"]}</p></a>' for g in C.GUIDES[:3]
    )
    body = f"""
<section class="hero">
  <div class="wrap">
    <div>
      <h1>Transformer insulation parts, cut to your drawing</h1>
      <p class="lede">Pressboard strips, dovetail spacers, hardwood rods, bakelite strips, Permawood components and complete insulation kits for distribution and power transformers. Made in {CO['city']} since {CO['founded']}.</p>
      <div class="cta">
        <a class="btn btn-primary" href="contact.html">Request a quote</a>
        <a class="btn btn-light" href="products/index.html">See all products</a>
      </div>
    </div>
    <div class="hero-photos">{photos}</div>
  </div>
</section>
<div class="title-block">
  <dl class="wrap">
    <div><dt>Material</dt><dd>Pressboard, phenolic, Permawood, hardwood</dd></div>
    <div><dt>Scale</dt><dd>To your drawing or sample</dd></div>
    <div><dt>Made by</dt><dd>{CO['name']}, {CO['city']}</dd></div>
    <div><dt>In production since</dt><dd>{CO['founded']} · GST registered</dd></div>
  </dl>
</div>

<section>
  <div class="wrap">
    <div class="section-head">
      <h2>Products</h2>
      <p class="soft">Everything a transformer OEM or utility workshop needs for the insulation inside the tank. Every item is made to order.</p>
    </div>
    <div class="grid">{tiles}</div>
  </div>
</section>

<section class="tint">
  <div class="wrap">
    <div class="section-head"><h2>Why transformer makers buy from us</h2></div>
    <div class="features">
      <div class="feature"><h3>Made to your drawing</h3><p>Send a drawing or a sample. We cut strips, spacers and components to the exact size, in trial lots or regular supply.</p></div>
      <div class="feature"><h3>Electrical-grade materials</h3><p>Transformer-grade pressboard, F4 phenolic laminate, seasoned hardwood and Permawood, chosen for oil and heat.</p></div>
      <div class="feature"><h3>Complete kits</h3><p>Order one insulation kit per transformer and get every part cut, labelled and packed together.</p></div>
      <div class="feature"><h3>Direct from the factory</h3><p>You deal with the manufacturer, which keeps prices competitive and lead times short. GST invoices on every order.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <h2>Who we supply</h2>
      <p>Transformer manufacturers building distribution and power transformers, and state electricity boards that maintain and rewind their own units. {CO['city']} sits on the Delhi–Mumbai and Delhi–Chennai corridors, so most of north, central and west India is two to four days away by road.</p>
    </div>
    <div class="section-head" style="margin-top:36px">
      <h2>Know-how</h2>
      <p class="soft">Short, practical guides written for the engineers and buyers who specify these parts.</p>
    </div>
    <div class="guide-list">{guides}</div>
    <p style="margin-top:18px"><a href="guides/index.html">All guides</a> · <a href="materials-and-standards.html">Materials and standards</a> · <a href="glossary.html">Glossary</a></p>
  </div>
</section>
"""
    title = f"Transformer Insulation Components Manufacturer in {CO['city']} | {CO['name']}"
    desc = (f"{CO['name']} makes pressboard strips, dovetail spacers, hardwood rods, bakelite strips, Permawood components and "
            f"transformer insulation kits in {CO['city']}, {CO['state']}. Cut to your drawing. Supplying OEMs and utilities since {CO['founded']}.")
    kw = ("transformer insulation components, pressboard strips manufacturer, dovetail spacers, hardwood rod transformer, bakelite strips, "
          "permawood components, transformer insulation kit, Jhansi, Uttar Pradesh, transformer parts manufacturer India")
    website = {"@context": "https://schema.org", "@type": "WebSite", "name": CO["name"], "url": DOMAIN}
    return page(title, desc, body, "index.html", kw, json_ld(org_schema()) + json_ld(website))


def build_products_index():
    tiles = "".join(product_tile(p, "../") for p in PRODUCTS)
    body = f"""
<section>
  <div class="wrap">
    {crumbs_html([("Home", "index.html"), ("Products", None)], "../")}
    <div class="section-head">
      <h1>Transformer insulation products</h1>
      <p class="lede soft">Seven product lines, all manufactured in-house in {CO['city']}. Open any product for sizes, materials, uses and common questions.</p>
    </div>
    <div class="grid">{tiles}</div>
  </div>
</section>
"""
    title = f"Transformer Insulation Products | Pressboard, Dovetail, Permawood | {CO['name']}"
    desc = ("Pressboard strips, dovetail spacers, hardwood rods, insulation kits, bakelite strips, Permawood components and clack bands "
            f"for distribution and power transformers. Made to drawing by {CO['name']}, {CO['city']}.")
    return page(title, desc, body, "products/index.html", depth=1,
                extra_head=json_ld(breadcrumb_schema([("Home", ""), ("Products", "products/")])))


def build_product(p):
    rows = "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in p["specs"])
    apps = "".join(f"<li>{a}</li>" for a in p["applications"])
    price_block = f'<p class="price">Indicative price: {p["price"]} (excluding GST; final price on quotation)</p>' if CO["show_prices"] else ""
    faqs = C.PRODUCT_FAQ.get(p["slug"], [])
    faq_section = f"<h2>Common questions</h2>{faq_html(faqs)}" if faqs else ""
    related = "".join(f'<a href="{o["slug"]}.html">{o["name"]}</a>' for o in PRODUCTS if o["slug"] != p["slug"])

    product_schema = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": p["name"],
        "image": f"{DOMAIN}/{p['image']}",
        "description": p["short"],
        "brand": {"@type": "Brand", "name": CO["name"]},
        "manufacturer": {"@id": f"{DOMAIN}/#business"},
        "category": "Transformer insulation components",
        "url": f"{DOMAIN}/products/{p['slug']}.html",
        "offers": {"@type": "Offer", "availability": "https://schema.org/InStock", "priceCurrency": "INR",
                   "seller": {"@id": f"{DOMAIN}/#business"}, "areaServed": "IN"},
    }
    crumbs = breadcrumb_schema([("Home", ""), ("Products", "products/"), (p["name"], f"products/{p['slug']}.html")])
    head = json_ld(product_schema) + json_ld(crumbs) + (json_ld(faq_schema(faqs)) if faqs else "")

    body = f"""
<section>
  <div class="wrap">
    {crumbs_html([("Home", "index.html"), ("Products", "products/index.html"), (p["name"], None)], "../")}
    <div class="product-top">
      <img src="../{p['image']}" alt="{p['name']} by {CO['name']}, {CO['city']}" width="676" height="507">
      <div>
        <h1>{p['name']}</h1>
        <p class="lede">{p['description']}</p>
        {price_block}
        <div class="enquiry-box">
          <strong>Need this in a specific size?</strong>
          <p class="soft" style="margin:6px 0 0">Send the drawing, quantity and transformer rating. We reply with price and delivery time within one working day.</p>
          <div class="btns">
            <a class="btn btn-primary" href="../contact.html?product={p['slug']}">Request a quote</a>
            <a class="btn btn-wa" href="{wa_link('Hello, I need a quote for ' + p['name'] + '.')}" target="_blank" rel="noopener">WhatsApp</a>
            <a class="btn btn-outline" href="tel:{CO['phone_link']}">Call</a>
          </div>
        </div>
      </div>
    </div>

    <h2 style="margin-top:44px">Specifications</h2>
    <table class="spec-table">{rows}</table>

    <h2>Where it is used</h2>
    <ul>{apps}</ul>

    {faq_section}

    <h2 style="margin-top:36px">About the manufacturer</h2>
    <p>{CO['name']} has made transformer insulation components in {CO['city']}, {CO['state']} since {CO['founded']}. We are a GST-registered manufacturer supplying transformer OEMs and electricity utilities across India. <a href="../about.html">About us</a> · <a href="../how-to-order.html">How to order</a> · <a href="../materials-and-standards.html">Materials and standards</a></p>

    <h2 style="margin-top:36px">Other products</h2>
    <div class="related">{related}</div>
  </div>
</section>
"""
    title = f"{p['name']} Manufacturer in {CO['city']}, UP | {CO['name']}"
    desc = f"{p['short']} Made to drawing by {CO['name']}, {CO['city']}, {CO['state']}. Supplying transformer OEMs and utilities across India. Request a quote."
    return page(title, desc, body, f"products/{p['slug']}.html", p["keywords"], head, depth=1, og_image=f"{DOMAIN}/{p['image']}")


def build_about():
    body = f"""
<section>
  <div class="wrap">
    {crumbs_html([("Home", "index.html"), ("About", None)], "")}
    <h1>About {CO['name']}</h1>
    <p class="lede">{CO['name']} started in {CO['founded']} in {CO['city']}, {CO['state']}. The firm is run by its proprietor, {CO['proprietor']}, and makes insulation components for distribution and power transformers.</p>
    <p>Over {YEARS} years we have built a simple reputation: parts that match the drawing, delivered on time, at a fair price. Our customers are transformer manufacturers and electricity utilities who need a steady supply of pressboard strips, dovetail spacers, hardwood rods, bakelite strips, Permawood parts and complete insulation kits.</p>

    <h2>What we do</h2>
    <ul>
      <li>Cut pressboard strips and dovetail spacers to size from electrical-grade pressboard</li>
      <li>Turn hardwood rods in diameters from 6 mm to 16 mm</li>
      <li>Cut F4-grade bakelite (phenolic laminate) strips</li>
      <li>Machine Permawood / transformer-wood components to drawing</li>
      <li>Assemble complete insulation kits per transformer rating</li>
      <li>Make press-paper clack bands for power transformers</li>
    </ul>

    <h2>Facts</h2>
    <table class="spec-table">
      <tr><th>Established</th><td>{CO['founded']}</td></tr>
      <tr><th>Business type</th><td>Manufacturer (sole proprietorship)</td></tr>
      <tr><th>Proprietor</th><td>{CO['proprietor']}</td></tr>
      <tr><th>Location</th><td>{CO['city']}, {CO['state']}, {CO['country']}</td></tr>
      <tr><th>GST number</th><td>{CO['gst']}</td></tr>
      <tr><th>Team</th><td>{CO['employees']} people</td></tr>
      <tr><th>Customers</th><td>Transformer OEMs and electricity utilities across India</td></tr>
    </table>

    <h2>How to work with us</h2>
    <p>Send a drawing, a sample or just the transformer rating. We confirm the material and size, send a quotation, and ship from {CO['city']}. For regular supply we can hold stock of your standard sizes. <a href="how-to-order.html">See the ordering steps</a>.</p>
  </div>
</section>
"""
    title = f"About {CO['name']} | Transformer Insulation Manufacturer, {CO['city']}"
    desc = (f"{CO['name']} is a GST-registered manufacturer of transformer insulation components in {CO['city']}, {CO['state']}, "
            f"run by {CO['proprietor']} since {CO['founded']}.")
    return page(title, desc, body, "about.html", extra_head=json_ld(org_schema()) + json_ld(breadcrumb_schema([("Home", ""), ("About", "about.html")])))


def build_contact():
    options = "".join(f'<option value="{p["name"]}">{p["name"]}</option>' for p in PRODUCTS)
    body = f"""
<section>
  <div class="wrap">
    {crumbs_html([("Home", "index.html"), ("Contact", None)], "")}
    <h1>Contact us</h1>
    <p class="lede soft">Tell us what you need and we reply with a price and delivery time, usually within one working day.</p>
    <div class="contact-grid">
      <div>
        <ul class="contact-list">
          <li><strong>Phone / WhatsApp</strong><a href="tel:{CO['phone_link']}">{CO['phone_display']}</a></li>
          <li><strong>Email</strong><a href="mailto:{CO['email']}">{CO['email']}</a></li>
          <li><strong>Address</strong>{CO['name']}<br>{CO['street_address']}<br>{CO['city']}, {CO['state']} {CO['postal_code']}, {CO['country']}</li>
          <li><strong>Contact person</strong>{CO['proprietor']}, Proprietor</li>
          <li><strong>GST</strong>{CO['gst']}</li>
          <li><strong>Working hours</strong>Monday to Saturday, 9:00 am to 6:00 pm</li>
        </ul>
        <p style="margin-top:20px"><a class="btn btn-wa" href="{wa_link('Hello, I have an enquiry about transformer insulation components.')}" target="_blank" rel="noopener">Chat on WhatsApp</a></p>
        <p class="soft" style="margin-top:20px">Not sure what to send? See <a href="how-to-order.html">how to order</a> for a short checklist.</p>
      </div>
      <div>
        <form action="{CO['form_action']}" method="POST">
          <label for="name">Your name</label>
          <input id="name" name="name" required autocomplete="name">
          <label for="company">Company</label>
          <input id="company" name="company" autocomplete="organization">
          <label for="phone">Phone</label>
          <input id="phone" name="phone" type="tel" required autocomplete="tel">
          <label for="email">Email</label>
          <input id="email" name="email" type="email" autocomplete="email">
          <label for="product">Product</label>
          <select id="product" name="product"><option value="">Select a product</option>{options}<option>Other / multiple</option></select>
          <label for="message">Requirement (size, quantity, transformer rating)</label>
          <textarea id="message" name="message" required></textarea>
          <button class="btn btn-primary" type="submit">Send enquiry</button>
        </form>
      </div>
    </div>
  </div>
</section>
<script>
  var slug = new URLSearchParams(location.search).get('product');
  if (slug) {{
    var sel = document.getElementById('product'), key = slug.replace(/-/g, '').slice(0, 8);
    for (var i = 0; i < sel.options.length; i++) {{
      if (sel.options[i].text.toLowerCase().replace(/[^a-z]/g, '').indexOf(key) === 0) {{ sel.selectedIndex = i; break; }}
    }}
  }}
</script>
"""
    title = f"Contact {CO['name']} | Quote for Transformer Insulation Parts, {CO['city']}"
    desc = (f"Call, WhatsApp or email {CO['name']} in {CO['city']} for pressboard strips, dovetail spacers, hardwood rods and "
            "transformer insulation kits. Quotes within one working day.")
    return page(title, desc, body, "contact.html", extra_head=json_ld(org_schema()))


def build_faq():
    body = f"""
<section>
  <div class="wrap">
    {crumbs_html([("Home", "index.html"), ("FAQ", None)], "")}
    <h1>Frequently asked questions</h1>
    <p class="lede soft">Answers to the questions we hear most from transformer makers and utility buyers.</p>
    {faq_html(C.FAQ)}
    <p style="margin-top:28px">Something else? <a href="contact.html">Ask us directly</a>.</p>
  </div>
</section>
"""
    title = f"FAQ: Transformer Insulation Parts, Ordering and Delivery | {CO['name']}"
    desc = "Answers on pressboard grades, minimum order, lead times, pricing per kg, shipping from Jhansi, GST and how to get a quote."
    return page(title, desc, body, "faq.html", extra_head=json_ld(faq_schema(C.FAQ)) + json_ld(breadcrumb_schema([("Home", ""), ("FAQ", "faq.html")])))


def build_materials():
    blocks = ""
    for m in C.MATERIALS:
        props = "".join(f"<li>{x}</li>" for x in m["properties"])
        blocks += f"""
<div class="material">
  <div>
    <h3>{m['name']}</h3>
    <p>{m['what']}</p>
    <div class="std"><strong>Standards:</strong> {m['standards']}</div>
  </div>
  <div>
    <h4>Properties</h4>
    <ul>{props}</ul>
    <p><strong>We make from it:</strong> {m['we_make']} <a href="{m['link']}">View product</a></p>
  </div>
</div>"""
    body = f"""
<section>
  <div class="wrap">
    {crumbs_html([("Home", "index.html"), ("Materials and standards", None)], "")}
    <h1>Materials and standards</h1>
    <p class="lede soft">The four insulation materials we work with, what they are, which standards apply, and which parts we make from each.</p>
    {blocks}
    <h2 style="margin-top:40px">Quick comparison</h2>
    <table class="spec-table">
      <thead><tr><th>Material</th><th>Strength</th><th>Oil impregnation</th><th>Cost</th><th>Typical parts</th></tr></thead>
      <tr><th>Pressboard</th><td>Moderate</td><td>Excellent</td><td>Lowest</td><td>Strips, spacers, cylinders, rings</td></tr>
      <tr><th>Phenolic laminate</th><td>High</td><td>Limited</td><td>Medium</td><td>Terminal boards, support strips</td></tr>
      <tr><th>Permawood</th><td>Very high</td><td>Good</td><td>Highest</td><td>Pressure rings, clamping blocks, cleats</td></tr>
      <tr><th>Hardwood</th><td>Moderate</td><td>Good</td><td>Low</td><td>Rods, pegs, simple spacers</td></tr>
    </table>
    <p>Read more: <a href="guides/pressboard-vs-bakelite-vs-permawood.html">which material to use where</a>.</p>
  </div>
</section>
"""
    title = f"Transformer Insulation Materials and Standards: Pressboard, Phenolic, Permawood | {CO['name']}"
    desc = "Plain guide to transformer pressboard (IEC 60641, IS 1576), phenolic laminate (IS 2036), Permawood and hardwood: properties, standards and what each is used for."
    kw = "transformer pressboard IEC 60641, IS 1576 pressboard, IS 2036 phenolic laminate, permawood properties, transformer insulation materials"
    return page(title, desc, body, "materials-and-standards.html", kw,
                json_ld(breadcrumb_schema([("Home", ""), ("Materials and standards", "materials-and-standards.html")])))


def build_glossary():
    items = "".join(f"<dt>{t}</dt><dd>{d}</dd>" for t, d in C.GLOSSARY)
    schema = {"@context": "https://schema.org", "@type": "DefinedTermSet", "name": "Transformer insulation glossary",
              "hasDefinedTerm": [{"@type": "DefinedTerm", "name": t, "description": d} for t, d in C.GLOSSARY]}
    body = f"""
<section>
  <div class="wrap">
    {crumbs_html([("Home", "index.html"), ("Glossary", None)], "")}
    <h1>Transformer insulation glossary</h1>
    <p class="lede soft">Plain definitions of the terms used on this site and on transformer drawings.</p>
    <dl class="glossary">{items}</dl>
  </div>
</section>
"""
    title = f"Transformer Insulation Glossary: Dovetail, Pressboard, Permawood and More | {CO['name']}"
    desc = "Short definitions of transformer insulation terms: angle ring, axial duct, dovetail spacer, pressure ring, Permawood, press paper, static ring and more."
    return page(title, desc, body, "glossary.html", extra_head=json_ld(schema) + json_ld(breadcrumb_schema([("Home", ""), ("Glossary", "glossary.html")])))


def build_how_to_order():
    steps = "".join(f"<li><div><h3>{t}</h3><p>{d}</p></div></li>" for t, d in C.ORDER_STEPS)
    checklist = "".join(f"<li>{x}</li>" for x in C.ORDER_CHECKLIST)
    howto = {"@context": "https://schema.org", "@type": "HowTo", "name": f"How to order transformer insulation parts from {CO['name']}",
             "step": [{"@type": "HowToStep", "name": t, "text": d} for t, d in C.ORDER_STEPS]}
    body = f"""
<section>
  <div class="wrap">
    {crumbs_html([("Home", "index.html"), ("How to order", None)], "")}
    <h1>How to order</h1>
    <p class="lede soft">Five steps from your drawing to parts on your floor.</p>
    <ol class="steps">{steps}</ol>
    <h2 style="margin-top:40px">What to include in your enquiry</h2>
    <ul>{checklist}</ul>
    <p style="margin-top:24px"><a class="btn btn-primary" href="contact.html">Send an enquiry</a></p>
  </div>
</section>
"""
    title = f"How to Order Transformer Insulation Parts | {CO['name']}, {CO['city']}"
    desc = "How ordering works: send a drawing, get a quote within a day, confirm, we cut and pack, we dispatch from Jhansi with GST invoice. Plus a checklist of what to send."
    return page(title, desc, body, "how-to-order.html", extra_head=json_ld(howto) + json_ld(breadcrumb_schema([("Home", ""), ("How to order", "how-to-order.html")])))


def render_body(blocks):
    out = ""
    for b in blocks:
        if isinstance(b, str):
            out += f"<p>{b}</p>"
        elif b[0] == "h2":
            out += f"<h2>{b[1]}</h2>"
        elif b[0] == "list":
            out += "<ul>" + "".join(f"<li>{x}</li>" for x in b[1]) + "</ul>"
        elif b[0] == "table":
            head = "".join(f"<th>{h}</th>" for h in b[1])
            rows = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in b[2])
            out += f'<table class="spec-table"><thead><tr>{head}</tr></thead>{rows}</table>'
    return out


def build_guides_index():
    items = "".join(f'<a href="{g["slug"]}.html"><h3>{g["title"]}</h3><p>{g["summary"]}</p></a>' for g in C.GUIDES)
    body = f"""
<section>
  <div class="wrap">
    {crumbs_html([("Home", "index.html"), ("Guides", None)], "../")}
    <h1>Guides</h1>
    <p class="lede soft">Short, practical notes for the engineers and buyers who specify transformer insulation. Written from the workshop floor, not a textbook.</p>
    <div class="guide-list">{items}</div>
  </div>
</section>
"""
    title = f"Transformer Insulation Guides: Pressboard, Dovetail Spacers, Kits | {CO['name']}"
    desc = "Practical guides on choosing pressboard strip thickness, how dovetail spacers work, pressboard vs bakelite vs Permawood, and insulation kit checklists."
    return page(title, desc, body, "guides/index.html", depth=1, extra_head=json_ld(breadcrumb_schema([("Home", ""), ("Guides", "guides/")])))


def build_guide(g):
    article = {"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["summary"],
               "datePublished": TODAY, "dateModified": TODAY, "author": {"@type": "Organization", "name": CO["name"]},
               "publisher": {"@id": f"{DOMAIN}/#business"}, "mainEntityOfPage": f"{DOMAIN}/guides/{g['slug']}.html"}
    crumbs = breadcrumb_schema([("Home", ""), ("Guides", "guides/"), (g["title"], f"guides/{g['slug']}.html")])
    others = "".join(f'<a href="{o["slug"]}.html">{o["title"]}</a>' for o in C.GUIDES if o["slug"] != g["slug"])
    body = f"""
<section>
  <div class="wrap">
    {crumbs_html([("Home", "index.html"), ("Guides", "guides/index.html"), (g["title"], None)], "../")}
    <article class="article">
      <h1>{g['title']}</h1>
      <p class="lede soft">{g['summary']}</p>
      {render_body(g['body'])}
    </article>
    <h2 style="margin-top:44px">More guides</h2>
    <div class="related">{others}</div>
  </div>
</section>
"""
    title = f"{g['title']} | {CO['name']}"
    return page(title, g["summary"], body, f"guides/{g['slug']}.html", g["keywords"], json_ld(article) + json_ld(crumbs), depth=1)


def build_404():
    body = """
<section><div class="wrap" style="text-align:center;padding:60px 22px">
  <h1>Page not found</h1>
  <p class="soft" style="margin:0 auto 20px">That page does not exist. Try the product list instead.</p>
  <a class="btn btn-primary" href="/products/index.html">See products</a>
</div></section>
"""
    return page("Page not found | " + CO["name"], "Page not found.", body, "404.html")


def build_sitemap():
    urls = ["", "products/", "about.html", "contact.html", "faq.html", "materials-and-standards.html", "glossary.html",
            "how-to-order.html", "guides/"]
    urls += [f"products/{p['slug']}.html" for p in PRODUCTS] + [f"guides/{g['slug']}.html" for g in C.GUIDES]
    entries = "".join(f"<url><loc>{DOMAIN}/{u}</loc><lastmod>{TODAY}</lastmod></url>" for u in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{entries}</urlset>\n'


# ---------------------------------------------------------------------------
# Write everything
# ---------------------------------------------------------------------------

def write(path, text):
    full = DIST / path
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(text, encoding="utf-8")


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    shutil.copytree(ROOT / "css", DIST / "css")
    shutil.copytree(ROOT / "images", DIST / "images")

    write("index.html", build_home())
    write("products/index.html", build_products_index())
    for p in PRODUCTS:
        write(f"products/{p['slug']}.html", build_product(p))
    write("about.html", build_about())
    write("contact.html", build_contact())
    write("faq.html", build_faq())
    write("materials-and-standards.html", build_materials())
    write("glossary.html", build_glossary())
    write("how-to-order.html", build_how_to_order())
    write("guides/index.html", build_guides_index())
    for g in C.GUIDES:
        write(f"guides/{g['slug']}.html", build_guide(g))
    write("404.html", build_404())
    write("sitemap.xml", build_sitemap())
    write("CNAME", DOMAIN.replace("https://", "") + "\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
    print(f"Built {len(list(DIST.rglob('*.html')))} pages into {DIST}")


if __name__ == "__main__":
    main()
