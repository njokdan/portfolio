# Portfolio content. Only facts Daniel has stated or that are verifiable on the live sites.
# No invented metrics: where there is no usage number, the case study says what is known.

BASE = "https://njokdan.github.io/portfolio/"

PERSON = {
    "name": "Daniel Njoku",
    "role": "Software engineer",
    "city": "Lagos, Nigeria",
    "email": "njokdan@gmail.com",
    "whatsapp": "+234 809 445 1628",
    "wa_link": "https://wa.me/2348094451628",
    "linkedin": "https://www.linkedin.com/in/daniel-njoku-9790645b/",
    "x": "https://x.com/njokudanielo",
    "github": "https://github.com/njokdan",
    "calendly": "https://calendly.com/njokdan/odoo-discovery-call",
    "odoo_site": "https://njokdan.github.io/",
}

SDG = {
    1: ("No poverty", "#E5243B"),
    2: ("Zero hunger", "#DDA63A"),
    4: ("Quality education", "#C5192D"),
    7: ("Affordable and clean energy", "#FCC30B"),
    8: ("Decent work and economic growth", "#A21942"),
    9: ("Industry, innovation and infrastructure", "#FD6925"),
    10: ("Reduced inequalities", "#DD1367"),
    11: ("Sustainable cities and communities", "#FD9D24"),
    16: ("Peace, justice and strong institutions", "#00689D"),
}

# status: live | beta | building | client
CASES = [
    {
        "id": "kashfinda",
        "name": "Kashfinda",
        "kind": "Fintech marketplace",
        "status": "live",
        "line": "Find someone nearby who has physical naira, pay them by bank transfer, collect the cash in person.",
        "links": [("Visit kashfinda.com", "https://kashfinda.com")],
        "facts": [
            ("Role", "Product design, full-stack and mobile build"),
            ("Platforms", "Web, cross-platform mobile app, native Android and iOS apps"),
            ("Market", "Nigeria"),
            ("Status", "Live on the web"),
        ],
        "stack": ["React Native", "Native Android", "Native iOS", "Geolocation and maps", "Tiered KYC"],
        "sections": [
            ("The problem",
             ["When naira notes are scarce, people queue at ATMs that run dry or pay steep charges to cash agents. Meanwhile shops, traders and individuals a few streets away are holding cash they would happily swap for a bank transfer.",
              "The hard part is not matching the two sides. It is getting strangers to trust each other with money, in person, without the platform ever touching the cash."]),
            ("What I built",
             ["A proximity marketplace. You see who has cash near you on a map or a list, inside a 5 km radius by default, and agree a meeting point. You pay through your own bank app first, then meet for the handover.",
              "Both people confirm the exchange with a six-digit code, which closes the transaction. The platform charges a stated 1% fee.",
              "Verified businesses can register as meeting points, and the top merchant tier unlocks bulk cash and remote transaction modules."]),
            ("Key decisions",
             ["Trust scales with verification. Limits rise in three steps: phone verification allows ₦20,000, BVN or NIN allows ₦50,000, and a verified business premises allows ₦500,000. A new user can try the product quickly, but large amounts only move between people the platform knows more about.",
              "Transfer first, then cash, then code. Splitting the exchange into three visible steps gives both sides a clear point at which the deal is done, which is what the confirmation code records.",
              "Ship everywhere people are. I built the web app, a cross-platform mobile app, and separate native Android and iOS apps."]),
            ("Where it stands",
             ["Kashfinda is live at kashfinda.com. The next piece of work is integrating Nigeria's NIPOST digital postcode API so meeting points can be shared as precise, verifiable addresses."]),
        ],
        "sdgs": [(8, "Gives small merchants and individuals a new way to earn from idle cash."),
                 (10, "Widens access to physical cash for people underserved by ATMs and agents."),
                 (9, "Builds trusted digital infrastructure on top of existing bank transfers.")],
    },
    {
        "id": "danfo-code",
        "name": "Danfo Code",
        "kind": "Coding game for children",
        "status": "live",
        "line": "Children aged 6 and up write real Python to drive a yellow danfo bus across Lagos.",
        "links": [("Play at danfocode.com", "https://danfocode.com")],
        "facts": [
            ("Role", "Creator, product design and full-stack build"),
            ("Audience", "Children from age 6, families and schools"),
            ("Hosting", "Cloudflare, with a Supabase backend"),
            ("Status", "Launched, free with no ads"),
        ],
        "stack": ["Python in the browser", "Cloudflare", "Supabase", "Offline progress", "NDPA compliance"],
        "sections": [
            ("The problem",
             ["Most coding courses for children are built for somewhere else. The examples, places and jokes are foreign, the courses assume a laptop each, and many cost money or show ads.",
              "I wanted Nigerian children to learn real code, not drag-and-drop blocks, inside a world they recognise."]),
            ("What I built",
             ["A browser game where the player's Python program drives a danfo, the yellow Lagos minibus, through real routes. Wrong code means a missed turn, so feedback is immediate and physical.",
              "Progress saves on the device and several drivers can share one phone or computer, because that is how many families use technology. Free family and school accounts sync progress across devices and issue certificates.",
              "Schools get a curriculum map and can enter the Danfo Code Cup, with a live leaderboard and reporting for sponsors."]),
            ("Key decisions",
             ["Real Python from the first lesson. Children type actual code, so what they learn carries straight over to real programming.",
              "Privacy before growth. The game follows the Nigeria Data Protection Act: an age gate with parental consent, self-hosted fonts, and no tracking or session replay by default.",
              "Make it feel like home. Music, Lagos landmarks, and seasonal touches for Christmas, New Year and other festivals."]),
            ("Where it stands",
             ["Danfo Code has launched and is live at danfocode.com. It is the flagship title of Mantra Worlds, the games studio I founded."]),
        ],
        "sdgs": [(4, "Free, ad-free coding education for children, in a setting they recognise."),
                 (8, "Builds an early path into tech careers."),
                 (9, "Grows the local pool of future engineers.")],
    },
    {
        "id": "guardsbase",
        "name": "Guardsbase",
        "kind": "Workforce and compliance platform",
        "status": "live",
        "line": "Connects licensed security guards in Canada with shifts at security companies, and keeps every licence in date.",
        "links": [("Visit guardsbase.com", "https://guardsbase.com")],
        "facts": [
            ("Role", "Product design, full-stack and mobile build"),
            ("Platforms", "Web, installable offline-capable web app, cross-platform mobile app"),
            ("Market", "Canada"),
            ("Status", "Live"),
        ],
        "stack": ["React Native", "Progressive web app", "Geofencing", "Notifications", "Payouts"],
        "sections": [
            ("The problem",
             ["Security companies need licensed guards on short notice, and every guard on site must hold a valid licence and permits. Tracking that by spreadsheet and phone calls is slow and risky."]),
            ("What I built",
             ["A platform that matches licensed guards with open shifts, with real-time shift scheduling, geofenced check-in so a guard can only clock in on site, and automatic notifications.",
              "It tracks guard licences, SIN and permits automatically, aligned with Canada's PIPEDA privacy law, and handles weekly direct-deposit payouts.",
              "Guards use it as an installable web app that works offline, or as a cross-platform mobile app."]),
            ("Key decisions",
             ["Compliance is part of scheduling, not a separate report. A guard whose licence lapses cannot be booked, so the check happens before the shift rather than after an incident.",
              "Geofencing for check-in, because attendance disputes are a constant cost for guard companies."]),
            ("Where it stands",
             ["Guardsbase is live at guardsbase.com."]),
        ],
        "sdgs": [(8, "Makes shift work easier to find and fairer to track for guards.")],
    },
    {
        "id": "toonmate",
        "name": "ToonMate",
        "kind": "AI animation platform",
        "status": "live",
        "line": "Turns ideas into animated video by routing each job to the right AI video provider, in the background.",
        "links": [("Visit toonm8.com", "https://toonm8.com")],
        "facts": [
            ("Role", "Architecture, backend and deployment"),
            ("Backend", "Python, Celery workers and Celery Beat, Redis"),
            ("Hosting", "Docker on Render"),
            ("Status", "Live, with an admin platform"),
        ],
        "stack": ["Python", "Celery", "Redis", "Docker", "Render", "Google sign-in", "Text to speech"],
        "sections": [
            ("The problem",
             ["Generating video with AI takes minutes, providers fail in different ways, and quotas run out. A web request cannot wait that long, and one provider going down should not take the product down."]),
            ("What I built",
             ["A Python backend with Google sign-in, where each video job goes onto a Celery queue backed by Redis. Background workers call several video providers, and Celery Beat runs scheduled jobs.",
              "Text to speech in 12 languages, so animations can be voiced in Nigerian languages as well as English.",
              "An admin platform for running the service, deployed from a Dockerfile on Render."]),
            ("Hard problems I fixed in production",
             ["Every task ran twice. Both queues shared one exchange and routing key, so each job was delivered to both. I declared explicit exchanges and queues with distinct routing keys.",
              "Workers ran out of memory loading an image-text model at startup. I moved workers to a larger instance and ran them one task at a time.",
              "Scheduled jobs drifted after each deploy, because the scheduler's state file lived on a disk that is wiped on redeploy. I switched to fixed clock schedules that need no stored state.",
              "Database connections leaked across event loops inside tasks. I made each task dispose its database engines at start and finish.",
              "When a provider's key was malformed or its free quota ran out, jobs failed noisily. I added logging of provider error bodies and skip providers whose keys are missing."]),
            ("Where it stands",
             ["ToonMate is live at toonm8.com and was introduced publicly on LinkedIn. It is also the first stage of my DeepCatch work on synthetic media, which continues in Attestana."]),
        ],
        "sdgs": [(9, "Reliable AI media infrastructure built and run from Nigeria."),
                 (4, "Lets educators produce animated lessons in local languages.")],
    },
    {
        "id": "attestana",
        "name": "Attestana",
        "kind": "Deepfake and misinformation detection",
        "status": "building",
        "line": "Checks whether a video, image or voice note circulating online is synthetic or taken out of context, starting with Nigeria.",
        "links": [],
        "facts": [
            ("Role", "Founder, architecture and full build"),
            ("Backend", "Python API, async database layer, Celery, Docker"),
            ("Tests", "451 automated tests passing"),
            ("Status", "In development, not yet public"),
        ],
        "stack": ["Python", "Celery", "Docker", "Hive", "Reality Defender", "Google Cloud Vision", "TinEye", "WhatsApp"],
        "sections": [
            ("The problem",
             ["A widely shared AI-generated video falsely showed a well-known Nigerian pastor doing something he publicly said he never does. Fakes like this spread fastest on WhatsApp, in languages and contexts global detection tools rarely cover.",
              "Many harmful posts are not deepfakes at all. They are real photos or clips presented as new, or as a different event."]),
            ("What I built",
             ["A check API that fuses three independent signals into a verdict with a confidence band, plus a gate that stops weak verdicts being shown publicly.",
              "A registry of public figures and the facts they have confirmed about themselves, so a claim can be checked against what the person has actually said.",
              "A WhatsApp tipline where anyone can forward suspicious media, tracing of who first posted and who reshared, and a review console where people make the final call.",
              "Out-of-context detection using reverse image search and context records, reading captions in English, French, Swahili and Pidgin.",
              "An admin platform where every feature is grouped by version and can be switched on or off."]),
            ("Key decisions",
             ["People decide, the system advises. Automated signals inform a human reviewer instead of publishing verdicts on their own.",
              "Use the best existing detectors, then add what they miss. Attestana calls Hive and Reality Defender and adds local context, personas and provenance on top.",
              "Built in small, tested phases, 29 so far, so each layer works before the next one depends on it."]),
            ("Where it stands",
             ["Attestana is in development and the domain attestana.com is secured. Next come the review console and a Nigerian benchmark dataset, then a country-by-country rollout across Africa."]),
        ],
        "sdgs": [(16, "Protects public trust and access to accurate information."),
                 (10, "Covers languages and communities global tools overlook.")],
    },
    {
        "id": "blue-watch",
        "name": "Blue Watch Academy",
        "kind": "Cybersecurity training platform",
        "status": "live",
        "line": "Trains people from zero to job-ready in security operations and incident response, with scored hands-on labs.",
        "links": [("Open the academy", "https://blue-watch-academy.pages.dev"),
                  ("Source on GitHub", "https://github.com/njokdan/blue-watch-academy")],
        "facts": [
            ("Role", "Creator, curriculum and full-stack build"),
            ("Hosting", "Cloudflare Pages, Supabase"),
            ("Scale", "31+ courses, 156+ lessons, 24+ scored labs"),
            ("Status", "Live, source is public"),
        ],
        "stack": ["Cloudflare Pages Functions", "Supabase", "Paystack", "Flutterwave", "LLM report marking"],
        "sections": [
            ("The problem",
             ["Security operations jobs ask for hands-on experience that beginners cannot get without a job. Most training is video lectures with a multiple-choice test at the end."]),
            ("What I built",
             ["An academy with 31+ courses and 156+ lessons across 11 tracks and six levels, from first principles to a business email compromise capstone.",
              "More than 24 scored labs, including log analysis and an exposure assessment lab. Learners write end-of-shift reports that are marked against a rubric by a language model.",
              "Cohorts with verifiable certificates, mentorship, a jobs board, a portfolio with badges, flashcards and exam prep. A mentor character, Commander Adaeze, coaches each learner by name.",
              "An admin command centre and card or bank-transfer payments that the owner can switch on or off."]),
            ("Key decisions",
             ["Ground every claim. Course content is checked against OWASP Top 10:2025, MITRE ATLAS, the NIST AI Risk Management Framework, the CBN cybersecurity framework and the Nigeria Data Protection Act.",
              "Teach scanning safely. External attack-surface work is a bounded teaching lab, not a live scanner pointed at real systems.",
              "Own the hosting. I built a compatibility layer so the academy runs on Cloudflare Pages and Supabase with real authentication, payments and a live internships feed."]),
            ("Where it stands",
             ["Live at blue-watch-academy.pages.dev with public source. The same model now underpins three sister academies in development: Graphwise for Meta business tools, Edgecase for software testing, and Lemma for mathematics."]),
        ],
        "sdgs": [(4, "Practical, job-focused security education."),
                 (8, "A direct route into skilled security work.")],
    },
    {
        "id": "mantra-worlds",
        "name": "Mantra Worlds",
        "kind": "Learning games studio",
        "status": "live",
        "line": "A Lagos studio making free learning games about the industries that run Africa, from farming to power grids.",
        "links": [("Visit mantraworlds.com", "https://mantraworlds.com"),
                  ("Play Agric Kingdom (beta)", "https://agrickingdom.mantraworlds.com")],
        "facts": [
            ("Role", "Founder and CEO, lead engineer"),
            ("Titles", "20 learning games in the catalogue"),
            ("Hosting", "Cloudflare, shared Supabase backend"),
            ("Status", "Danfo Code live, Agric Kingdom in public beta, others in prototype"),
        ],
        "stack": ["Shared game engine", "Supabase", "Cloudflare", "Three.js", "On-device speech"],
        "sections": [
            ("The idea",
             ["Most young Africans never see how electricity reaches their homes, how crude oil becomes fuel, or how a farm feeds a city. Each Mantra game teaches one industry end to end, from beginner to professional, in places players recognise."]),
            ("What I built",
             ["A catalogue of 20 titles, including Danfo Code (coding), Agric Kingdom (farming), Volt Kingdom (power grids), Petro Kingdom (oil and gas), Nimbus Kingdom (cloud and data centres), Drone Kingdom, Servo Kingdom (robotics), Algo Kingdom (algorithms), Esho Guardians (security operations) and Workbench (WAEC science practicals).",
              "One shared engine and one shared backend for accounts, leaderboards, classrooms and cloud saves, with separate staging and production environments.",
              "A games registry that acts as the single source of truth for the website, the investor deck and the company documents, so they never disagree."]),
            ("Key decisions",
             ["A launch gate every game must pass. Each title is checked against the Nigeria Data Protection Act before it ships: age gate with parental consent, self-hosted fonts, no tracking by default, and read-aloud voices that run on the device only.",
              "Honest impact claims. Each game lists the UN Sustainable Development Goals it supports, with the wording that it supports a goal rather than achieves it.",
              "One flagship at a time. Launches are staggered so each game gets a full marketing window."]),
            ("Where it stands",
             ["The studio site is live at mantraworlds.com. Danfo Code is live, Agric Kingdom is in public beta, and the rest are in prototype or early access."]),
        ],
        "sdgs": [(4, "Free learning games across 20 subjects."),
                 (8, "Career guidance and job-ready skills in each title."),
                 (9, "Teaches how infrastructure and industry work."),
                 (2, "Agric Kingdom covers farming and food."),
                 (7, "Volt and Silica Kingdom cover power and solar."),
                 (16, "Cyber Nation and Esho Guardians cover national cyber defence.")],
    },
    {
        "id": "payroll-audit",
        "name": "Payroll reconciliation",
        "kind": "Odoo consulting",
        "status": "client",
        "line": "Reverse-engineered a manufacturing group's payroll from 19 salary sheets before rebuilding it in Odoo.",
        "links": [("My Odoo consulting site", "https://njokdan.github.io/")],
        "facts": [
            ("Role", "Independent Odoo consultant, through a Lagos Odoo partner"),
            ("Client", "A Nigerian manufacturing group, kept anonymous"),
            ("Scope", "253 employees across three grades"),
            ("Status", "Delivered"),
        ],
        "stack": ["Odoo HR and Payroll", "Odoo.sh", "Python", "pdftotext", "Nigeria Tax Act 2025"],
        "sections": [
            ("The problem",
             ["The client wanted its existing payroll moved into Odoo and improved. Nobody had a written specification of how pay was actually calculated. The only reliable record was the salary sheets themselves."]),
            ("What I did",
             ["I extracted 19 PDF payroll sheets covering 253 employees with layout-preserving text extraction, then wrote Python parsers to read every figure.",
              "From the numbers I derived the formulas for basic pay, housing, transport, overtime, absence deductions, PAYE, pension and union dues. They reconciled to the kobo for every employee except 13, and I documented each of those as a separate anomaly.",
              "I compared the findings against the project's requirements tracker and found gaps, including lunch subsidy, NHF, NHIA and employer pension contributions, plus one promoted employee still taxed at the junior rate."]),
            ("The finding that mattered",
             ["The client's PAYE used flat rates by grade, while the brief required the progressive bands of the Nigeria Tax Act 2025. That is a decision for the client, not the consultant, so I raised it for written confirmation before any configuration began."]),
            ("Delivery",
             ["A 20-page review in Word, PDF and Markdown. Every item carries a reference ID for findings, decisions, tracker items, anomalies and questions, with a response column so the partner could answer line by line. On the same engagement I turned 13 Excel invoice templates into Odoo invoices within three days."]),
        ],
        "sdgs": [(8, "Accurate, lawful pay for factory workers.")],
    },
]

MORE = [
    ("GeoSec", "Maritime intelligence MVP that flags dark vessels near Niger Delta oil terminals by fusing Sentinel-1 radar imagery with AIS ship data.", "MVP", None),
    ("NeuraStore", "Open-source query engine in Rust that combines vector search with structured filters.", "In development", None),
    ("DOSSIER", "Suggests timely cybersecurity whitepaper topics and drafts full researched papers, with PDF and Word export. Next.js 14, Supabase and the Claude API.", "Working build", None),
    ("Multi-market grocery store", "Client e-commerce build for the UK, US and Canada with cold-chain shipping rules, soup-box subscriptions, UK VAT by product type and an owner dashboard. Medusa v2 and Next.js 16.", "Client work", None),
    ("Workbench", "Phone-based virtual science lab for WAEC practicals, with 15 physics, chemistry and biology practicals built.", "Prototype", "https://mantraworlds.com/games/workbench/"),
    ("Agric Kingdom", "Farm crops and livestock across Nigeria's climate zones, from seed to market.", "Public beta", "https://agrickingdom.mantraworlds.com"),
    ("Stryde and Ongo", "Driver and rider platforms for ride services, with fleet owners, a benefits engine and disputes.", "Built", None),
    ("NGR", "Geometry reasoning model: transformer, reinforcement learning with GRPO, a symbolic verifier and a benchmark pipeline.", "Research", None),
    ("Gatecode", "Installable web app on Nigeria's NIPOST digital postcodes: shareable Find Me links, a WhatsApp bot and address collection for sellers.", "In development", None),
    ("Graphwise, Edgecase and Lemma", "Sister training academies to Blue Watch, for Meta business tools, software testing and mathematics.", "In development", None),
]

EXPERIENCE = [
    ("Independent Odoo ERP Consultant", "Self-employed", "Nov 2026 to now", "Remote",
     "Implementation, customisation, HR and payroll for clients through a Lagos Odoo partner."),
    ("Cybersecurity Solution Analyst", "Infoassure Limited", "May 2026 to now", "On-site, Lagos",
     "Security solutions for an auditing and GRC SaaS company, including a database activity monitoring proof of concept."),
    ("Founder", "Mantra Worlds", "2026 to now", "Lagos",
     "Learning games and simulation studio."),
    ("Software Engineer", "Infoassure Limited", "Sept 2025 to now", "Hybrid, Lagos",
     "Secure cloud and full-stack work on the company's GRC platform."),
    ("Cloud Technical Support Engineer", "Teknowledge", "Dec 2021 to Aug 2025", "Remote",
     "Supported and troubleshot customer workloads on Microsoft Azure App Services for almost four years."),
]
EARLIER = "Earlier roles at Flawa Systems, XL Africa Group, Digital Circle and Aptech Computer Education."

EDUCATION = [
    ("DevOps Engineer Nanodegree", "Udacity", "2022"),
    ("HND, Computer Science", "Institute of Management and Technology, Enugu", "2008"),
    ("OND, Computer Science", "Institute of Management and Technology, Enugu", "2005"),
    ("Certified LLM Security Professional", "In preparation", ""),
    ("Odoo Functional Certification", "In preparation", ""),
]

SKILLS = [
    ("Languages", "TypeScript, JavaScript, Python, PHP, Rust, SQL"),
    ("Web", "Next.js, React, Vue, Node.js, Express, FastAPI, Laravel, Tailwind CSS"),
    ("Mobile", "React Native, native Android and iOS, geolocation, geofencing, offline-first apps"),
    ("Cloud", "Microsoft Azure, AWS, Cloudflare Pages and Workers, Render, Docker, CI/CD"),
    ("Data", "PostgreSQL, Supabase, Redis, Celery job queues, vector search"),
    ("Security", "GRC, identity and access review, database activity monitoring, LLM security, NDPA and PIPEDA compliance"),
    ("ERP", "Odoo Online and Odoo.sh: accounting, invoicing, HR, payroll, Studio, Python and QWeb"),
]


# ---------------- v2: SEO / AEO / sales layer ----------------
UPDATED = "2026-11-14"
UPDATED_HUMAN = "14 November 2026"
BASE_PATH = "/portfolio/"          # change to "/" if the portfolio moves to its own domain
OPEN_TO_ROLES = False              # True adds "open to remote roles" wording publicly (your employer can see it)

HERO = {
    "hello": "Hi, I'm Daniel Njoku, a software engineer in Lagos.",
    "h1": "I turn real-world problems into software people actually use.",
    "intro": ("Cash that's hard to find. Guard shifts that won't fill. Children who deserve to learn real code. "
              "I design, build and ship the whole product, from web and mobile apps to the cloud and security behind them, "
              "and I kept customer apps on Microsoft Azure running for almost four years."),
    "route_hint": "Oya, pick a stop.",
}

PROOF = [
    ("6", "products live on the web"),
    ("3", "app platforms shipped: web, Android, iOS"),
    ("20", "learning games in my studio"),
    ("253", "employees' pay reconciled to the kobo"),
    ("451", "automated tests on Attestana"),
]

WHY = [
    ("I ship the whole thing",
     "Kashfinda went out as a web app, a cross-platform app and native Android and iOS apps. Design, backend, mobile and deployment, end to end.",
     "kashfinda"),
    ("I get the details right",
     "I rebuilt a factory's payroll from 19 PDF salary sheets and matched 253 employees to the kobo, then wrote up the 13 that didn't fit instead of hiding them.",
     "payroll-audit"),
    ("I build for real conditions",
     "Shared family phones, patchy networks, licences that lapse and privacy law. I design for them from day one, so products hold up after launch.",
     "danfo-code"),
]

SERVICES = [
    ("Build your product", "From idea to a launched first version on web and mobile, with the admin tools you need to run it.", "kashfinda"),
    ("Mobile apps", "Cross-platform apps in React Native, and native Android and iOS when the product calls for it.", "guardsbase"),
    ("Cloud and DevOps", "Deploy, scale and steady your app on Azure, AWS, Cloudflare or Render, and track down the production bugs that keep coming back.", "toonmate"),
    ("Security and compliance", "Products built to pass the Nigeria Data Protection Act and similar laws, plus access reviews and GRC support.", "blue-watch"),
    ("Odoo ERP", "Implementation, invoices, HR and payroll on Odoo Online and Odoo.sh.", None),
]

PROCESS = [
    ("A free 30-minute call", "Tell me what you're trying to fix or build. I'll tell you honestly whether I'm the right person."),
    ("A clear plan", "A written scope, timeline and price before any work starts. No surprises later."),
    ("Working software every week", "You see real progress in a short demo each week, not slides."),
    ("Launch and handover", "Deployed, documented and yours, with the code in your own repository."),
]

FAQ = [
    ("Who is Daniel Njoku?",
     "Daniel Njoku is a software engineer based in Lagos, Nigeria, who designs, builds and ships web, mobile, cloud and security products. "
     "He works at Infoassure Limited as a Software Engineer and Cybersecurity Solution Analyst, founded the learning games studio Mantra Worlds, "
     "and consults independently on Odoo ERP."),
    ("What has Daniel Njoku built?",
     "His live products include Kashfinda, a proximity cash-exchange marketplace for Nigeria; Danfo Code, a free game that teaches children Python; "
     "Guardsbase, a shift and compliance platform for security guards in Canada; ToonMate, an AI animation platform; and Blue Watch Academy, "
     "a cybersecurity training platform. Attestana, a deepfake and misinformation checker, is in development."),
    ("What technologies does Daniel Njoku work with?",
     "TypeScript, JavaScript, Python, PHP and Rust; Next.js, React, Vue, Node.js, FastAPI and Laravel on the web; React Native and native Android and iOS on mobile; "
     "Microsoft Azure, AWS, Cloudflare, Render and Docker in the cloud; PostgreSQL, Supabase, Redis and Celery for data and background jobs; and Odoo for ERP."),
    ("Does Daniel Njoku build mobile apps?",
     "Yes. He built the cross-platform mobile apps for Kashfinda and Guardsbase, and native Android and iOS apps for Kashfinda."),
    ("Does Daniel Njoku work with clients outside Nigeria?",
     "Yes. Guardsbase serves security companies in Canada, he has built an e-commerce platform for a UK business selling into the UK, US and Canada, "
     "and he takes Odoo ERP clients worldwide."),
    ("How do I hire Daniel Njoku?",
     "Email njokdan@gmail.com, message +234 809 445 1628 on WhatsApp, or book a free 30-minute call. "
     "Projects start with a written scope, timeline and price, then a short demo of working software every week until launch."),
]

# Per case: answer-first summary, SEO title/description, schema hints, closing CTA
EXTRA = {
    "kashfinda": dict(
        tldr="Kashfinda is a live proximity cash-exchange marketplace for Nigeria, built by Daniel Njoku. People find someone nearby with physical naira, pay them by bank transfer and collect the cash in person, with a six-digit code confirming each handover and verification tiers from ₦20,000 to ₦500,000.",
        title="Kashfinda: cash-exchange app case study | Daniel Njoku",
        desc="How Daniel Njoku built Kashfinda, a live Nigerian marketplace for finding cash nearby, on web, Android and iOS, with tiered KYC and code-confirmed handovers.",
        schema="SoftwareApplication", cat="FinanceApplication", os="Web, Android, iOS",
        cta="Need a marketplace or fintech app built?"),
    "danfo-code": dict(
        tldr="Danfo Code is a free, ad-free browser game where children aged 6 and up write real Python to drive a yellow danfo bus across Lagos. Daniel Njoku created it as the flagship of his studio Mantra Worlds; it runs on Cloudflare with a Supabase backend and follows the Nigeria Data Protection Act.",
        title="Danfo Code: Python coding game for kids | Daniel Njoku",
        desc="Danfo Code is a free game that teaches Nigerian children real Python by driving a danfo through Lagos. Built by Daniel Njoku on Cloudflare and Supabase.",
        schema="SoftwareApplication", cat="EducationalApplication", os="Web browser",
        cta="Want a learning product people actually finish?"),
    "guardsbase": dict(
        tldr="Guardsbase is a live platform, built by Daniel Njoku, that connects licensed security guards in Canada with shifts at security companies. It handles real-time scheduling, geofenced check-in, licence and permit tracking aligned with PIPEDA, and weekly direct-deposit payouts, on web and mobile.",
        title="Guardsbase: security guard shift platform | Daniel Njoku",
        desc="How Daniel Njoku built Guardsbase, a live Canadian platform for security guard shifts with geofenced check-in, licence tracking and payouts, on web and mobile.",
        schema="SoftwareApplication", cat="BusinessApplication", os="Web, Android, iOS",
        cta="Running shift work or field staff?"),
    "toonmate": dict(
        tldr="ToonMate is a live AI animation platform at toonm8.com, built by Daniel Njoku. A Python backend queues each video job with Celery and Redis, routes it to several AI video providers, and voices it in 12 languages. The case study covers five production bugs he found and fixed on Render.",
        title="ToonMate: AI animation platform case study | Daniel Njoku",
        desc="How Daniel Njoku built ToonMate, an AI animation platform on Python, Celery, Redis and Docker on Render, and the five production bugs he fixed.",
        schema="SoftwareApplication", cat="MultimediaApplication", os="Web browser",
        cta="Production bugs that won't go away?"),
    "attestana": dict(
        tldr="Attestana is a deepfake and misinformation detection platform in development by Daniel Njoku, starting with Nigeria. It fuses three detection signals into a confidence-banded verdict, checks claims against what public figures have confirmed, takes tips over WhatsApp and flags real media shown out of context. It has 451 automated tests passing.",
        title="Attestana: deepfake detection for Nigeria | Daniel Njoku",
        desc="Attestana, in development by Daniel Njoku, detects deepfakes and out-of-context media for Nigeria, with a WhatsApp tipline, human review and 451 passing tests.",
        schema="SoftwareApplication", cat="SecurityApplication", os="Web, API, WhatsApp",
        cta="Working on trust, safety or misinformation?"),
    "blue-watch": dict(
        tldr="Blue Watch Academy is a live cybersecurity training platform built by Daniel Njoku that takes people from zero to job-ready in security operations and incident response. It has 31+ courses, 156+ lessons, 24+ scored labs, AI-marked incident reports and verifiable certificates, and its source is public on GitHub.",
        title="Blue Watch Academy: SOC training platform | Daniel Njoku",
        desc="Blue Watch Academy, built by Daniel Njoku, trains people for security operations with 31+ courses, 24+ scored labs and AI-marked reports.",
        schema="SoftwareApplication", cat="EducationalApplication", os="Web browser",
        cta="Need a training platform for your team?"),
    "mantra-worlds": dict(
        tldr="Mantra Worlds is a Lagos learning games studio founded by Daniel Njoku. It makes free games that teach the industries that run Africa, with 20 titles in its catalogue: Danfo Code is live, Agric Kingdom is in public beta, and the rest are in prototype. Every game passes a data protection launch gate before release.",
        title="Mantra Worlds: African learning games studio | Daniel Njoku",
        desc="Mantra Worlds, founded by Daniel Njoku, makes free learning games about African industries: 20 titles, with Danfo Code live and Agric Kingdom in beta.",
        schema="Organization", cat=None, os=None,
        cta="Want to build a game or simulation together?"),
    "payroll-audit": dict(
        tldr="Before moving a Nigerian manufacturing group's payroll into Odoo, Daniel Njoku reverse-engineered it from 19 PDF salary sheets covering 253 employees. Every payslip reconciled to the kobo except 13 documented anomalies, and he flagged that flat-rate PAYE conflicted with the Nigeria Tax Act 2025.",
        title="Odoo payroll reconciliation case study | Daniel Njoku",
        desc="How Daniel Njoku reverse-engineered a manufacturing group's payroll from 19 salary sheets, reconciled 253 employees to the kobo and prepared it for Odoo.",
        schema="CreativeWork", cat=None, os=None,
        cta="Moving payroll or invoices into Odoo?"),
}

QUESTION_HEADINGS = {
    "The problem": "What problem does {name} solve?",
    "What I built": "What I built",
    "Key decisions": "Why I built it this way",
    "Where it stands": "Where {name} is today",
    "The idea": "Why Mantra Worlds exists",
}
