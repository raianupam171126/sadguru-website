"""
Editable text content for the SEO pages. Plain Python dicts and lists.
Edit here, then run:  python build.py
"""

# ---------------------------------------------------------------------------
# FAQ page (also used for FAQPage schema). Keep answers short and factual.
# ---------------------------------------------------------------------------
FAQ = [
    ("What products does Sadguru Industrial Enterprises make?",
     "We make insulation components for oil-filled transformers: pressboard strips, dovetail spacers and strips, "
     "hardwood rods, bakelite (phenolic laminate) strips, Permawood components, clack bands and complete transformer insulation kits."),
    ("Where are you located and where do you ship?",
     "Our factory is in Jhansi, Uttar Pradesh. We ship across India by road transport and courier. Jhansi sits on the "
     "Delhi–Mumbai and Delhi–Chennai rail and road corridors, so most of north, central and west India is reachable within 2 to 4 days."),
    ("Do you supply to transformer manufacturers (OEMs) and electricity boards?",
     "Yes. Our customers are transformer OEMs building distribution and power transformers, and state electricity utilities "
     "that maintain and rewind their own transformers."),
    ("Can you make parts to my drawing?",
     "Yes. Send a drawing, a sample or the transformer rating. We cut strips, spacers and machined parts to your dimensions. "
     "There is no fixed catalogue size; everything is made to order."),
    ("What is the minimum order quantity?",
     "There is no fixed minimum. Small trial lots are welcome. For regular supply we can hold stock of your standard sizes so repeat orders ship faster."),
    ("What pressboard grade do you use?",
     "We use electrical-grade transformer pressboard suitable for oil-filled transformers. If your specification calls for a particular "
     "grade or density, tell us when you enquire and we will confirm before quoting."),
    ("What is the difference between pressboard strips and bakelite strips?",
     "Pressboard is a dense kraft-paper board used for most insulation and spacing inside the winding. Bakelite (phenolic laminate) "
     "is harder and stronger, used where parts take mechanical load, such as terminal boards and support strips. See our materials guide for details."),
    ("How is pricing worked out?",
     "We do not publish fixed prices because material cost, thickness, cutting and quantity all change the figure. "
     "Send your drawing and quantity and we quote the same working day; the quote stays valid for the period stated on it."),
    ("What is the usual lead time?",
     "Standard strips and spacers usually ship within 7 to 10 working days of order confirmation. Machined Permawood parts and full "
     "insulation kits take longer depending on the drawing. We confirm the delivery date with the quotation."),
    ("Are you GST registered?",
     "Yes. Our GST number is 09BYQPS5818D1ZV. We issue GST invoices and can supply to registered buyers anywhere in India."),
    ("How do I get a quote?",
     "Call or WhatsApp us, email a drawing, or use the enquiry form on the contact page. Include the product, size, quantity and "
     "the transformer rating if you know it. We reply within one working day."),
]

# ---------------------------------------------------------------------------
# Per-product FAQs (slug -> list of (question, answer)). Added to product pages.
# ---------------------------------------------------------------------------
PRODUCT_FAQ = {
    "pressboard-strips": [
        ("What thicknesses of pressboard strips do you supply?",
         "Common strip thicknesses range from 1 mm to 8 mm. We cut from pressboard sheets to the width and length on your drawing."),
        ("Are the strips suitable for oil-filled distribution transformers?",
         "Yes. We use electrical-grade pressboard made for oil-filled transformers. It can be dried and oil-impregnated with the winding."),
        ("Do you sell pressboard strips by weight or by piece?",
         "By weight (per kg). This is standard for the trade and keeps pricing simple across different sizes."),
    ],
    "dovetail-spacers": [
        ("What is a dovetail spacer used for?",
         "Dovetail spacers slot into dovetail strips to form the radial cooling ducts between winding discs. They keep the duct spacing "
         "even and hold their position when the winding is clamped."),
        ("Can you supply matching dovetail strips?",
         "Yes. We cut dovetail strips to the same profile as the spacers so the two parts fit together correctly."),
        ("Can the profile be made to my drawing?",
         "Yes. We make standard dovetail profiles and custom profiles to drawing."),
    ],
    "hardwood-rods": [
        ("What diameters are available?",
         "6, 8, 10, 12, 14 and 16 mm as standard. Other diameters on request."),
        ("What is the maximum length?",
         "Up to about 2 metres (7 feet). We cut to shorter lengths on request."),
        ("Is the wood seasoned?",
         "Yes. We use seasoned hardwood so the rods stay straight and do not shrink or crack after fitting."),
    ],
    "transformer-insulation-kit": [
        ("What does a transformer insulation kit include?",
         "Typically all pressboard parts for one transformer: strips, dovetail spacers, cylinders, angle rings, packing pieces and "
         "any other items on your drawing. Hardwood rods and Permawood parts can be included."),
        ("Can you make kits for a range of ratings?",
         "Yes. Many customers standardise kits for their common ratings such as 25, 63, 100, 250 and 630 kVA. Send the drawings and we quote per kit."),
    ],
    "bakelite-strips": [
        ("What grade of bakelite do you use?",
         "F4 electrical grade phenolic laminate in cotton-fabric base. Paper-base grades are also available."),
        ("When should I use bakelite instead of pressboard?",
         "Use bakelite where the part carries mechanical load or needs to hold a screw: terminal boards, support strips, wedges and clamps. "
         "Use pressboard for general insulation and spacing inside the winding."),
    ],
    "permawood-components": [
        ("What is Permawood?",
         "Permawood (also called transformer wood or densified laminated wood) is wood veneer bonded under heat and pressure with resin. "
         "It is strong, machinable and insulating, so it is used for load-bearing parts inside transformers."),
        ("What parts do you machine from Permawood?",
         "Clamping blocks, cleats, pressure pads, support pieces and other components to your drawing."),
    ],
    "clack-bands": [
        ("What is a clack band?",
         "A round band of press paper fitted around winding sections to hold them in place during assembly and to support leads."),
    ],
}

# ---------------------------------------------------------------------------
# Materials & standards page
# ---------------------------------------------------------------------------
MATERIALS = [
    {
        "name": "Transformer pressboard",
        "what": "A dense board made from pure kraft pulp, pressed and dried. It is the most common solid insulation inside oil-filled transformers.",
        "standards": "IEC 60641 (pressboard and presspaper for electrical purposes); IS 1576 (solid pressboard for electrical purposes).",
        "properties": [
            "Thermal class A (105 °C) in transformer oil",
            "Thickness commonly 0.5 mm to 8 mm; thicker boards by lamination",
            "Can be dried and oil-impregnated with the winding",
            "Density roughly 1.0 to 1.3 g/cm³ depending on grade",
        ],
        "we_make": "Pressboard strips, dovetail strips and spacers, insulation kits, clack bands.",
        "link": "products/pressboard-strips.html",
    },
    {
        "name": "Phenolic laminate (Bakelite / Hylam)",
        "what": "Layers of paper or cotton fabric bonded with phenolic resin under heat and pressure. Hard, rigid and dimensionally stable.",
        "standards": "IS 2036 (phenolic laminated sheets); NEMA LI 1 grades for comparison.",
        "properties": [
            "Paper-base grades (P) for electrical use; fabric-base grades (F) for mechanical strength",
            "We supply F4 electrical grade as standard",
            "Good machinability: can be drilled, tapped and milled",
            "Resists transformer oil and moderate heat",
        ],
        "we_make": "Bakelite strips and small cut parts.",
        "link": "products/bakelite-strips.html",
    },
    {
        "name": "Permawood (densified laminated wood)",
        "what": "Thin wood veneers bonded with resin under high pressure. Much denser and stronger than natural wood, with good insulating properties.",
        "standards": "Supplied to manufacturer's specification; commonly used in place of pressboard where load-bearing strength is needed.",
        "properties": [
            "High compressive strength for clamping and pressure parts",
            "Machinable to tight tolerances",
            "Low moisture absorption after drying",
            "Compatible with transformer oil",
        ],
        "we_make": "Clamping blocks, cleats, pressure pads, machine components to drawing.",
        "link": "products/permawood-components.html",
    },
    {
        "name": "Seasoned hardwood",
        "what": "Natural hardwood, seasoned to reduce moisture, turned into round rods.",
        "standards": "Selected and seasoned to transformer industry practice.",
        "properties": [
            "Good insulating strength after drying and oil impregnation",
            "Straight, round and smooth after turning",
            "Low cost for simple support and spacing duties",
        ],
        "we_make": "Hardwood rods 6 mm to 16 mm diameter.",
        "link": "products/hardwood-rods.html",
    },
]

# ---------------------------------------------------------------------------
# Glossary
# ---------------------------------------------------------------------------
GLOSSARY = [
    ("Angle ring", "A pressboard ring with an L-shaped cross section, fitted at the ends of a winding to support the insulation and guide oil flow."),
    ("Axial duct", "A vertical oil channel along the height of a winding, formed by strips placed between the winding and the cylinder."),
    ("Bakelite", "Trade name that has become the common word for phenolic laminate sheet. See also Hylam."),
    ("Clack band", "A round press-paper band used to hold winding sections and leads in position."),
    ("Cleat", "A block, often of Permawood, that clamps and supports leads inside the transformer tank."),
    ("Clamping ring / pressure ring", "A strong ring (pressboard or Permawood) at the top and bottom of a winding through which clamping force is applied."),
    ("Cooling duct", "Any oil channel inside the winding that lets oil circulate and carry heat away."),
    ("Dovetail spacer", "A small pressboard block with a dovetail-shaped key. It slots into a dovetail strip to form radial cooling ducts."),
    ("Dovetail strip", "A pressboard strip with dovetail slots along its length, into which dovetail spacers lock."),
    ("Distribution transformer", "A transformer that steps voltage down for local supply, typically 11 kV or 33 kV to 415 V, up to a few MVA."),
    ("Hylam", "Another trade name for phenolic laminate sheet, widely used in India."),
    ("Insulation kit", "A complete set of insulation parts for one transformer, cut and packed together."),
    ("kVA", "Kilovolt-ampere, the unit used to rate transformer capacity."),
    ("Oil impregnation", "Filling the pores of dried insulation with transformer oil, usually under vacuum, to raise its insulating strength."),
    ("OEM", "Original equipment manufacturer. In this context, a company that builds transformers."),
    ("Permawood", "Densified laminated wood used for load-bearing insulation parts. Also called transformer wood or UDEL wood."),
    ("Power transformer", "A large transformer used in transmission and generation, generally above a few MVA."),
    ("Pressboard", "Dense kraft board used for most solid insulation and spacing inside oil-filled transformers."),
    ("Press paper", "Thin pressboard, typically under 0.8 mm, used for layer insulation and wrapping."),
    ("Radial duct", "A horizontal oil channel between winding discs, formed by dovetail spacers."),
    ("Static ring / static plate", "A shielded ring at the line end of a winding that evens out voltage stress."),
    ("Thermal class A", "An insulation rating for continuous operation up to 105 °C."),
    ("Winding cylinder", "A pressboard tube on which a winding is wound, insulating it from the core or the next winding."),
]

# ---------------------------------------------------------------------------
# How to order page
# ---------------------------------------------------------------------------
ORDER_STEPS = [
    ("Send your requirement",
     "A drawing is best. A sample or the transformer rating works too. Tell us the product, size, quantity and when you need it. "
     "Send by WhatsApp, email or the enquiry form."),
    ("We confirm and quote",
     "We check the material and dimensions, raise any questions, and send a quotation with price per kg or per piece, "
     "delivery time and payment terms. Usually within one working day."),
    ("You confirm the order",
     "Reply to the quotation or send a purchase order. For first orders we take an advance; for regular customers we agree credit terms."),
    ("We make and pack",
     "Parts are cut or machined, checked against the drawing, and packed in bundles or boxes labelled with your part names."),
    ("We dispatch",
     "By road transport or courier from Jhansi, with a GST invoice and LR copy sent to you on the day of dispatch."),
]

ORDER_CHECKLIST = [
    "Product name (for example, dovetail spacers)",
    "Drawing with dimensions, or a sample",
    "Material and grade, if your specification calls for one",
    "Quantity in kg or pieces",
    "Transformer rating and type (distribution or power)",
    "Delivery address and required date",
    "Your GST number for the invoice",
]

# ---------------------------------------------------------------------------
# Knowledge guides (short articles). Each becomes guides/<slug>.html
# Paragraphs are plain strings; lists are tuples ("list", [...]); tables ("table", header, rows)
# ---------------------------------------------------------------------------
GUIDES = [
    {
        "slug": "choosing-pressboard-strip-thickness",
        "title": "How to choose pressboard strip thickness for a transformer winding",
        "summary": "A practical guide to picking strip thickness and width for axial ducts, packing and clamping in distribution transformers.",
        "keywords": "pressboard strip thickness, transformer strip size, axial duct strip, pressboard strip width",
        "body": [
            "Pressboard strips do three jobs inside a winding: they form axial cooling ducts, they pack gaps so the winding sits tight, "
            "and they carry clamping force at the ends. The right thickness depends on which job the strip is doing.",
            ("h2", "Strips for axial cooling ducts"),
            "Duct strips sit between the winding cylinder and the first layer of conductor, running the full height of the winding. "
            "Their thickness sets the width of the oil channel. For small distribution transformers (up to about 250 kVA) duct strips of "
            "4 mm to 6 mm are common. Larger units use 6 mm to 8 mm or even laminated strips. A wider duct cools better but takes space "
            "and increases the winding diameter.",
            ("h2", "Strips for packing"),
            "Packing strips fill the small gaps that remain after winding so nothing can move in service. Thin strips of 1 mm to 3 mm are "
            "usual, often used in combination to reach an exact dimension. Keep a range of thicknesses in stock so the fitter can make up "
            "any gap.",
            ("h2", "Strips for clamping"),
            "At the top and bottom of the winding, strips and blocks transfer the clamping force from the pressure ring into the winding. "
            "These see the highest load, so use thicker strips (6 mm to 10 mm) or Permawood blocks for larger units.",
            ("h2", "Width"),
            "Width is usually set by the number of strips around the circumference. More, narrower strips give more even support; "
            "fewer, wider strips are quicker to fit. Widths of 15 mm to 40 mm cover most distribution transformers.",
            ("h2", "A simple rule of thumb"),
            ("table", ["Duty", "Typical thickness", "Typical width"], [
                ["Axial duct, up to 250 kVA", "4 – 6 mm", "15 – 25 mm"],
                ["Axial duct, 315 kVA – 2.5 MVA", "6 – 8 mm", "20 – 40 mm"],
                ["Packing", "1 – 3 mm", "as needed"],
                ["End clamping", "6 – 10 mm or Permawood", "25 – 50 mm"],
            ]),
            "These are starting points. Your design engineer's drawing always takes priority, and we cut to whatever it specifies.",
        ],
    },
    {
        "slug": "dovetail-spacers-explained",
        "title": "Dovetail spacers explained: how radial cooling ducts are built",
        "summary": "What dovetail spacers and strips do, why the dovetail shape matters, and how to specify them.",
        "keywords": "dovetail spacers, radial cooling duct, dovetail strip, transformer winding spacers, disc winding spacers",
        "body": [
            "In a disc or helical winding, each turn or disc has to be separated from the next by a gap that oil can flow through. "
            "These horizontal gaps are called radial ducts. Dovetail spacers are the small blocks that create them.",
            ("h2", "Why the dovetail shape"),
            "A plain block would slip out as the winding is wound and clamped. A dovetail spacer has a tapered key on its back that slots "
            "into a matching groove in a dovetail strip running up the winding. Once in the strip, the spacer cannot fall out, and a row of "
            "spacers stays exactly in line from top to bottom of the winding.",
            ("h2", "How many spacers"),
            "Spacers are placed at regular intervals around the circumference, usually 8 to 24 per layer depending on winding diameter. "
            "The number of layers equals the number of discs. A 100 kVA distribution transformer may use a few hundred spacers; a large power "
            "transformer uses thousands.",
            ("h2", "What to specify"),
            ("list", [
                "Spacer thickness (sets the duct height): commonly 3 mm to 6 mm",
                "Spacer width and length: matched to the conductor width",
                "Dovetail profile: standard, or to your drawing",
                "Matching dovetail strip dimensions",
                "Quantity, in kg or pieces",
            ]),
            ("h2", "Material"),
            "Both spacer and strip are made from electrical-grade pressboard so they dry and oil-impregnate along with the rest of the "
            "winding. The pressboard must be dense enough that the dovetail does not crush under clamping force.",
            "We supply spacers and matching strips together so the fit is right first time.",
        ],
    },
    {
        "slug": "pressboard-vs-bakelite-vs-permawood",
        "title": "Pressboard, bakelite or Permawood: which insulation material to use where",
        "summary": "A plain comparison of the three main solid insulation materials used inside transformers and the parts each is best for.",
        "keywords": "pressboard vs bakelite, permawood vs pressboard, transformer insulation materials, phenolic laminate transformer",
        "body": [
            "Transformer makers use three main solid insulation materials: pressboard, phenolic laminate (bakelite) and densified wood "
            "(Permawood). Each has a place. Choosing the wrong one costs money or, worse, causes failures.",
            ("table", ["", "Pressboard", "Bakelite (phenolic)", "Permawood"], [
                ["Made from", "Kraft pulp", "Paper or fabric + phenolic resin", "Wood veneer + resin"],
                ["Strength", "Moderate", "High", "Very high in compression"],
                ["Machinability", "Cut and punch", "Drill, tap, mill", "Drill, tap, mill"],
                ["Oil impregnation", "Excellent", "Limited", "Good after drying"],
                ["Cost", "Lowest", "Medium", "Highest"],
                ["Best for", "Strips, spacers, cylinders, angle rings", "Terminal boards, support strips, wedges", "Pressure rings, clamping blocks, cleats"],
            ]),
            ("h2", "Use pressboard for"),
            "Anything inside the winding that needs to be oil-impregnated: strips, dovetail spacers, cylinders, angle rings, layer insulation. "
            "It is the cheapest and it dries and impregnates with the winding.",
            ("h2", "Use bakelite for"),
            "Parts that take a screw, a bolt or a mechanical load but do not need deep oil impregnation: terminal boards, tap-changer supports, "
            "support strips and wedges. F4 grade is the usual choice for electrical work.",
            ("h2", "Use Permawood for"),
            "The heavy-duty parts: pressure rings, clamping blocks, lead cleats and anything that must hold the winding tight under short-circuit "
            "force. It is the most expensive, so use it only where strength is needed.",
            ("h2", "Hardwood"),
            "Plain seasoned hardwood still has a place for simple rods, pegs and spacers in distribution transformers, where cost matters "
            "more than strength.",
            "If you are unsure, send the drawing and tell us the duty of the part. We will suggest the material.",
        ],
    },
    {
        "slug": "distribution-transformer-insulation-kit-checklist",
        "title": "Insulation kit checklist for a distribution transformer",
        "summary": "The parts that usually go into an insulation kit for an 11 kV distribution transformer, and how to order them as one set.",
        "keywords": "distribution transformer insulation kit, transformer insulation parts list, 11kV transformer insulation, transformer pressboard kit",
        "body": [
            "An insulation kit is simply every insulation part for one transformer, cut and packed together. Ordering as a kit means "
            "one purchase order, one delivery and no missing pieces on the assembly line.",
            ("h2", "What a typical 11 kV distribution transformer kit contains"),
            ("list", [
                "LV winding cylinder (pressboard tube)",
                "HV winding cylinder",
                "Axial duct strips, LV and HV",
                "Dovetail strips and spacers for radial ducts (if disc-wound)",
                "Angle rings, top and bottom, LV and HV",
                "End insulation blocks or packing",
                "Layer insulation (press paper), if required",
                "Clamping strips or Permawood blocks",
                "Lead support strips and cleats",
                "Hardwood rods or pegs",
                "Packing strips in assorted thicknesses",
            ]),
            ("h2", "Information we need to quote a kit"),
            ("list", [
                "Transformer rating (kVA) and voltage class",
                "Winding type: layer or disc",
                "Drawings or a parts list with dimensions",
                "Material for each part (pressboard unless stated)",
                "Number of kits per month, if regular",
            ]),
            ("h2", "Standardising kits"),
            "Most OEMs build a handful of ratings repeatedly: 25, 63, 100, 160, 250, 400 and 630 kVA are common. Once we have the drawings "
            "for each rating, repeat orders need only the rating and the quantity. We can hold stock of parts for your fastest-moving ratings.",
            "Kits are priced per kg, with the total weight shown on the quotation so you can compare against buying parts separately.",
        ],
    },
]
