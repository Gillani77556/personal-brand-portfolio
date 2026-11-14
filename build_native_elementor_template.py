import json
import uuid

def gen_id():
    return uuid.uuid4().hex[:7]

def make_widget(widget_type, settings):
    return {
        "id": gen_id(),
        "elType": "widget",
        "isInner": False,
        "widgetType": widget_type,
        "settings": settings,
        "defaultEditSettings": {"defaultEditRoute": "content"},
        "elements": []
    }

def make_column(size, widgets, settings=None):
    col_settings = {
        "_column_size": size,
        "_inline_size": None
    }
    if settings:
        col_settings.update(settings)
    return {
        "id": gen_id(),
        "elType": "column",
        "isInner": False,
        "settings": col_settings,
        "defaultEditSettings": {"defaultEditRoute": "content"},
        "elements": widgets
    }

def make_section(title, columns, settings=None):
    sec_settings = {
        "layout": "boxed",
        "gap": "default",
        "_title": title,
        "background_background": "classic",
        "background_color": "#060911",
        "padding": {
            "unit": "px",
            "top": "70",
            "right": "20",
            "bottom": "70",
            "left": "20",
            "isLinked": False
        }
    }
    if settings:
        sec_settings.update(settings)
    return {
        "id": gen_id(),
        "elType": "section",
        "isInner": False,
        "settings": sec_settings,
        "defaultEditSettings": {"defaultEditRoute": "content"},
        "elements": columns
    }

CDN = "https://personal-brand-portfolio-three.vercel.app"

# -------------------------------------------------------------
# Section 01: Header & Sticky Navigation
# -------------------------------------------------------------
header_col1 = make_column(30, [
    make_widget("image", {
        "image": {"url": f"{CDN}/assets/images/logo.svg", "id": ""},
        "image_size": "custom",
        "image_custom_dimension": {"width": 180, "height": 45},
        "align": "left",
        "link_to": "custom",
        "link": {"url": "#top", "is_external": False, "nofollow": False}
    })
])

header_col2 = make_column(50, [
    make_widget("text-editor", {
        "editor": """
        <div style="display: flex; gap: 20px; align-items: center; justify-content: center; font-weight: 500; font-size: 15px;">
          <a href="#about" style="color: #cbd5e1; text-decoration: none;">About</a>
          <a href="#services" style="color: #cbd5e1; text-decoration: none;">Services</a>
          <a href="#results" style="color: #cbd5e1; text-decoration: none;">Results</a>
          <a href="#reviews" style="color: #cbd5e1; text-decoration: none;">Reviews</a>
          <a href="#courses" style="color: #cbd5e1; text-decoration: none;">Free Academy</a>
          <a href="#faq" style="color: #cbd5e1; text-decoration: none;">FAQ</a>
          <a href="#contact" style="color: #cbd5e1; text-decoration: none;">Contact</a>
        </div>
        """,
        "align": "center"
    })
])

header_col3 = make_column(20, [
    make_widget("button", {
        "text": "Hire Me →",
        "link": {"url": "#contact", "is_external": False, "nofollow": False},
        "align": "right",
        "background_color": "#10b981",
        "button_text_color": "#ffffff",
        "border_radius": {"unit": "px", "top": "8", "right": "8", "bottom": "8", "left": "8", "isLinked": True}
    })
])

sec_01 = make_section("📌 01. Header & Brand Navigation", [header_col1, header_col2, header_col3], {
    "background_color": "#060911",
    "padding": {"unit": "px", "top": "16", "right": "24", "bottom": "16", "left": "24", "isLinked": False}
})

# -------------------------------------------------------------
# Section 02: Hero Showcase Section
# -------------------------------------------------------------
hero_left_widgets = [
    make_widget("heading", {
        "title": "🟢 AVAILABLE FOR 2 NEW SEO RETAINERS",
        "header_size": "h5",
        "align": "left",
        "title_color": "#10b981",
        "typography_typography": "custom",
        "typography_font_size": {"unit": "px", "size": 13, "sizes": []},
        "typography_font_weight": "700"
    }),
    make_widget("heading", {
        "title": "Grow Your Organic Traffic and Revenue With Asim SEO Wala",
        "header_size": "h1",
        "align": "left",
        "title_color": "#f8fafc",
        "typography_typography": "custom",
        "typography_font_family": "Inter",
        "typography_font_size": {"unit": "px", "size": 46, "sizes": []},
        "typography_font_weight": "800",
        "typography_line_height": {"unit": "em", "size": 1.15, "sizes": []}
    }),
    make_widget("text-editor", {
        "editor": "<p style='font-size: 1.1rem; line-height: 1.6; color: #94a3b8;'>100% White-Hat Search Strategy, High-Intent Keyword Targeting, and Real Business Growth—Zero Fluff, Zero Spam.</p>",
        "align": "left"
    }),
    make_widget("button", {
        "text": "Audit My Website Free →",
        "link": {"url": "#contact", "is_external": False, "nofollow": False},
        "align": "left",
        "background_color": "#10b981",
        "button_text_color": "#ffffff",
        "size": "md",
        "border_radius": {"unit": "px", "top": "8", "right": "8", "bottom": "8", "left": "8", "isLinked": True}
    }),
    make_widget("text-editor", {
        "editor": "<div style='margin-top: 15px; color: #cbd5e1; font-size: 0.95rem;'>⭐⭐⭐⭐⭐ <strong style='color:#f8fafc;'>4.9/5 Rating</strong> · 50+ Verified Client Reviews · Upwork Top Rated</div>",
        "align": "left"
    })
]

hero_right_widgets = [
    make_widget("image", {
        "image": {"url": f"{CDN}/assets/images/asim-hero-headshot.webp", "id": ""},
        "image_size": "full",
        "align": "center",
        "border_radius": {"unit": "px", "top": "16", "right": "16", "bottom": "16", "left": "16", "isLinked": True}
    }),
    make_widget("text-editor", {
        "editor": """
        <div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 12px; padding: 14px 20px; margin-top: 15px; display: flex; justify-content: space-between; align-items: center;">
          <div>
            <div style="color: #10b981; font-weight: 800; font-size: 1.25rem;">+340% Traffic</div>
            <div style="color: #94a3b8; font-size: 0.85rem;">SaaS Ranking Case Study</div>
          </div>
          <div style="text-align: right;">
            <div style="color: #38bdf8; font-weight: 800; font-size: 1.25rem;">100% White-Hat</div>
            <div style="color: #94a3b8; font-size: 0.85rem;">Pure Manual Outreach</div>
          </div>
        </div>
        """
    })
]

sec_02 = make_section("🚀 02. Hero Showcase Section", [
    make_column(55, hero_left_widgets),
    make_column(45, hero_right_widgets)
], {
    "background_color": "#060911",
    "padding": {"unit": "px", "top": "60", "right": "20", "bottom": "60", "left": "20", "isLinked": False}
})

# -------------------------------------------------------------
# Section 03: Trust & Experience Stats Counters
# -------------------------------------------------------------
stat_col1 = make_column(25, [
    make_widget("counter", {
        "starting_number": 0,
        "ending_number": 8,
        "suffix": "+",
        "title": "Years Experience",
        "number_color": "#10b981",
        "title_color": "#cbd5e1"
    })
], {"background_color": "#0b1120", "padding": {"unit": "px", "top": "24", "right": "16", "bottom": "24", "left": "16", "isLinked": True}})

stat_col2 = make_column(25, [
    make_widget("counter", {
        "starting_number": 0,
        "ending_number": 150,
        "suffix": "+",
        "title": "Delivered Projects",
        "number_color": "#38bdf8",
        "title_color": "#cbd5e1"
    })
], {"background_color": "#0b1120", "padding": {"unit": "px", "top": "24", "right": "16", "bottom": "24", "left": "16", "isLinked": True}})

stat_col3 = make_column(25, [
    make_widget("counter", {
        "starting_number": 0,
        "ending_number": 25,
        "suffix": "M+",
        "title": "Organic Visitors",
        "number_color": "#10b981",
        "title_color": "#cbd5e1"
    })
], {"background_color": "#0b1120", "padding": {"unit": "px", "top": "24", "right": "16", "bottom": "24", "left": "16", "isLinked": True}})

stat_col4 = make_column(25, [
    make_widget("counter", {
        "starting_number": 0,
        "ending_number": 100,
        "suffix": "%",
        "title": "White-Hat Safe",
        "number_color": "#38bdf8",
        "title_color": "#cbd5e1"
    })
], {"background_color": "#0b1120", "padding": {"unit": "px", "top": "24", "right": "16", "bottom": "24", "left": "16", "isLinked": True}})

sec_03 = make_section("📊 03. Trust & Experience Stats", [stat_col1, stat_col2, stat_col3, stat_col4], {
    "background_color": "#080d1a",
    "padding": {"unit": "px", "top": "40", "right": "20", "bottom": "40", "left": "20", "isLinked": False}
})

# -------------------------------------------------------------
# Section 04: About Asim & Mission
# -------------------------------------------------------------
about_left = make_column(50, [
    make_widget("heading", {
        "title": "WHO I AM & WHAT I STAND FOR",
        "header_size": "h5",
        "title_color": "#10b981",
        "typography_typography": "custom",
        "typography_font_size": {"unit": "px", "size": 13, "sizes": []},
        "typography_font_weight": "700"
    }),
    make_widget("heading", {
        "title": "Search Strategy Backed by Real Experience, Not Theory",
        "header_size": "h2",
        "title_color": "#f8fafc",
        "typography_typography": "custom",
        "typography_font_family": "Inter",
        "typography_font_size": {"unit": "px", "size": 34, "sizes": []},
        "typography_font_weight": "800"
    }),
    make_widget("text-editor", {
        "editor": """
        <p style="color: #cbd5e1; font-size: 1.05rem; line-height: 1.7;">
          I built my career on two simple commitments: helping international businesses grow their organic search revenue, and teaching practical freelancing skills to upcoming talent across Pakistan and beyond completely free of charge.
        </p>
        <p style="color: #94a3b8; font-size: 1rem; line-height: 1.6;">
          Starting with just a laptop, I tested Google search algorithms across hundreds of sites. I learned what truly moves rankings—sound technical foundations, high-intent content, and real editorial outreach—and rejected cheap spam tactics like PBNs and link farms.
        </p>
        <ul style="color: #cbd5e1; line-height: 1.8; margin-top: 15px;">
          <li><strong style="color: #10b981;">✓ 100% Manual Blogger Outreach</strong> (Zero PBN networks)</li>
          <li><strong style="color: #10b981;">✓ Transparent Monthly Analytics</strong> (Ahrefs & Search Console)</li>
          <li><strong style="color: #10b981;">✓ Direct Communication</strong> (No junior account managers)</li>
          <li><strong style="color: #10b981;">✓ Free Community Mentorship</strong> (Giving back to upcoming youth)</li>
        </ul>
        """
    })
])

about_right = make_column(50, [
    make_widget("image", {
        "image": {"url": f"{CDN}/assets/images/asim-executive-desk.webp", "id": ""},
        "image_size": "full",
        "border_radius": {"unit": "px", "top": "12", "right": "12", "bottom": "12", "left": "12", "isLinked": True}
    }),
    make_widget("image", {
        "image": {"url": f"{CDN}/assets/images/asim-china-expo.webp", "id": ""},
        "image_size": "full",
        "border_radius": {"unit": "px", "top": "12", "right": "12", "bottom": "12", "left": "12", "isLinked": True}
    })
])

sec_04 = make_section("👨‍💻 04. About Asim & Mission", [about_left, about_right], {
    "background_color": "#060911"
})

# -------------------------------------------------------------
# Section 05: Three Core SEO Services Grid
# -------------------------------------------------------------
srv_header_col = make_column(100, [
    make_widget("heading", {
        "title": "SERVICES & DELIVERABLES",
        "header_size": "h5",
        "align": "center",
        "title_color": "#10b981",
        "typography_typography": "custom",
        "typography_font_size": {"unit": "px", "size": 13, "sizes": []},
        "typography_font_weight": "700"
    }),
    make_widget("heading", {
        "title": "How I Help Your Business Grow on Google",
        "header_size": "h2",
        "align": "center",
        "title_color": "#f8fafc",
        "typography_typography": "custom",
        "typography_font_family": "Inter",
        "typography_font_size": {"unit": "px", "size": 34, "sizes": []},
        "typography_font_weight": "800"
    }),
    make_widget("text-editor", {
        "editor": "<p style='text-align: center; color: #94a3b8; max-width: 650px; margin: 0 auto 30px;'>Targeted search engine optimization designed to generate real paying customers, not just vanity rankings.</p>",
        "align": "center"
    })
])
sec_05_header = make_section("⚡ 05A. Services Header", [srv_header_col], {
    "background_color": "#0b1120",
    "padding": {"unit": "px", "top": "60", "right": "20", "bottom": "10", "left": "20", "isLinked": False}
})

card_settings = {
    "background_background": "classic",
    "background_color": "#0f172a",
    "border_border": "solid",
    "border_width": {"unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": True},
    "border_color": "rgba(255, 255, 255, 0.08)",
    "border_radius": {"unit": "px", "top": "12", "right": "12", "bottom": "12", "left": "12", "isLinked": True},
    "padding": {"unit": "px", "top": "30", "right": "24", "bottom": "30", "left": "24", "isLinked": False}
}

srv_col1 = make_column(33, [
    make_widget("heading", {
        "title": "🔍 Full-Stack SEO Strategy",
        "header_size": "h3",
        "title_color": "#f8fafc",
        "typography_font_size": {"unit": "px", "size": 22, "sizes": []}
    }),
    make_widget("text-editor", {
        "editor": """
        <p style="color: #94a3b8; font-size: 0.95rem;">Technical audits, Core Web Vitals remediation, keyword architecture, and on-page optimization built for sustainable search growth.</p>
        <ul style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.8; padding-left: 18px;">
          <li>Full Technical Crawl & Audit</li>
          <li>Competitor Keyword Gap Analysis</li>
          <li>On-Page & Schema Architecture</li>
          <li>Monthly Traffic & Ranking Reports</li>
        </ul>
        """
    }),
    make_widget("button", {
        "text": "Inquire About SEO →",
        "link": {"url": "#contact", "is_external": False, "nofollow": False},
        "background_color": "#10b981",
        "button_text_color": "#ffffff",
        "align": "center",
        "border_radius": {"unit": "px", "top": "6", "right": "6", "bottom": "6", "left": "6", "isLinked": True}
    })
], card_settings)

srv_col2 = make_column(33, [
    make_widget("heading", {
        "title": "🔗 Authority Guest Posting",
        "header_size": "h3",
        "title_color": "#f8fafc",
        "typography_font_size": {"unit": "px", "size": 22, "sizes": []}
    }),
    make_widget("text-editor", {
        "editor": """
        <p style="color: #94a3b8; font-size: 0.95rem;">100% manual, pitch-based editorial link outreach to real websites with verified organic search traffic. Zero PBNs or link farms.</p>
        <ul style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.8; padding-left: 18px;">
          <li>Pure Manual Blogger Outreach</li>
          <li>Ahrefs DR 40–80+ Real Traffic Sites</li>
          <li>DoFollow Contextual Placements</li>
          <li>Permanent Indexing Guarantee</li>
        </ul>
        """
    }),
    make_widget("button", {
        "text": "Order Guest Posts →",
        "link": {"url": "#contact", "is_external": False, "nofollow": False},
        "background_color": "#10b981",
        "button_text_color": "#ffffff",
        "align": "center",
        "border_radius": {"unit": "px", "top": "6", "right": "6", "bottom": "6", "left": "6", "isLinked": True}
    })
], card_settings)

srv_col3 = make_column(33, [
    make_widget("heading", {
        "title": "✍️ Conversion Content Writing",
        "header_size": "h3",
        "title_color": "#f8fafc",
        "typography_font_size": {"unit": "px", "size": 22, "sizes": []}
    }),
    make_widget("text-editor", {
        "editor": """
        <p style="color: #94a3b8; font-size: 0.95rem;">Human-crafted, research-backed copy designed to rank high on search engines while converting readers into paying customers.</p>
        <ul style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.8; padding-left: 18px;">
          <li>Commercial Intent Keyword Mapping</li>
          <li>Surfer / NLP Term Optimization</li>
          <li>Native English (Zero AI Jargon)</li>
          <li>Compelling Lead Conversion CTAs</li>
        </ul>
        """
    }),
    make_widget("button", {
        "text": "Get Content Strategy →",
        "link": {"url": "#contact", "is_external": False, "nofollow": False},
        "background_color": "#10b981",
        "button_text_color": "#ffffff",
        "align": "center",
        "border_radius": {"unit": "px", "top": "6", "right": "6", "bottom": "6", "left": "6", "isLinked": True}
    })
], card_settings)

sec_05_cards = make_section("⚡ 05B. Three Core Services Grid", [srv_col1, srv_col2, srv_col3], {
    "background_color": "#0b1120",
    "padding": {"unit": "px", "top": "10", "right": "20", "bottom": "60", "left": "20", "isLinked": False}
})

# -------------------------------------------------------------
# Section 06: Verified Case Studies & Results
# -------------------------------------------------------------
case_col1 = make_column(33, [
    make_widget("heading", {"title": "+340% Traffic", "header_size": "h2", "title_color": "#10b981"}),
    make_widget("heading", {"title": "B2B SaaS Platform (San Francisco)", "header_size": "h4", "title_color": "#f8fafc"}),
    make_widget("text-editor", {
        "editor": "<p style='color: #94a3b8;'>Scaled organic search from 0 to 85,000 monthly visitors in 7 months through high-intent comparison keywords and authoritative SaaS outreach.</p>"
    })
], card_settings)

case_col2 = make_column(33, [
    make_widget("heading", {"title": "+215% Revenue", "header_size": "h2", "title_color": "#38bdf8"}),
    make_widget("heading", {"title": "E-Commerce Fashion Store (UK)", "header_size": "h4", "title_color": "#f8fafc"}),
    make_widget("text-editor", {
        "editor": "<p style='color: #94a3b8;'>Achieved top-3 Google rankings for 18 competitive commercial keywords, driving an organic sales boost in 5 months of clean technical execution.</p>"
    })
], card_settings)

case_col3 = make_column(33, [
    make_widget("heading", {"title": "1.2M Impressions", "header_size": "h2", "title_color": "#10b981"}),
    make_widget("heading", {"title": "Tech Media & Publisher (Canada)", "header_size": "h4", "title_color": "#f8fafc"}),
    make_widget("text-editor", {
        "editor": "<p style='color: #94a3b8;'>Structured topic clusters and Core Web Vitals remediation, producing a +450% traffic surge and doubling display and affiliate revenues.</p>"
    })
], card_settings)

sec_06 = make_section("📈 06. Verified Case Studies & Results", [case_col1, case_col2, case_col3], {
    "background_color": "#060911"
})

# -------------------------------------------------------------
# Section 07: Client Testimonials
# -------------------------------------------------------------
rev_col1 = make_column(33, [
    make_widget("testimonial", {
        "testimonial_content": "Asim completely transformed our organic search pipeline. His technical audit uncovered issues three previous agencies missed, and his manual guest posting earned us authoritative mentions that actually move the needle.",
        "testimonial_name": "Mark R.",
        "testimonial_job": "SaaS Founder, San Francisco",
        "name_color": "#f8fafc",
        "job_color": "#10b981",
        "content_color": "#cbd5e1"
    })
], card_settings)

rev_col2 = make_column(33, [
    make_widget("testimonial", {
        "testimonial_content": "The guest posting outreach Asim handles is the cleanest in the industry. Real sites with actual traffic, completely transparent spreadsheets, and zero PBN fluff. Our organic revenue jumped by 215%.",
        "testimonial_name": "Sarah Jenkins",
        "testimonial_job": "E-commerce Director, UK",
        "name_color": "#f8fafc",
        "job_color": "#10b981",
        "content_color": "#cbd5e1"
    })
], card_settings)

rev_col3 = make_column(33, [
    make_widget("testimonial", {
        "testimonial_content": "Finding a reliable SEO partner who doesn't rely on PBNs or buzzwords is rare. Asim's strategic guidance doubled our ad revenue and scaled our organic impressions to over 1.2 million a month.",
        "testimonial_name": "David Chen",
        "testimonial_job": "Managing Editor, Toronto",
        "name_color": "#f8fafc",
        "job_color": "#10b981",
        "content_color": "#cbd5e1"
    })
], card_settings)

sec_07 = make_section("⭐ 07. International Client Reviews", [rev_col1, rev_col2, rev_col3], {
    "background_color": "#0b1120"
})

# -------------------------------------------------------------
# Section 08: Free Learning Academy & Sunday Zoom
# -------------------------------------------------------------
acad_left = make_column(60, [
    make_widget("heading", {
        "title": "FREE EDUCATION PLATFORM",
        "header_size": "h5",
        "title_color": "#10b981",
        "typography_font_size": {"unit": "px", "size": 13, "sizes": []}
    }),
    make_widget("heading", {
        "title": "Learn SEO and Freelancing for Free",
        "header_size": "h2",
        "title_color": "#f8fafc",
        "typography_font_size": {"unit": "px", "size": 32, "sizes": []}
    }),
    make_widget("text-editor", {
        "editor": """
        <p style="color: #cbd5e1; font-size: 1.05rem;">
          I believe knowledge should be accessible to everyone. Through free video tutorials in Urdu/Hindi and weekly Sunday live Zoom sessions, I teach upcoming freelancers and business owners how to master Google search without paying thousands for guru courses.
        </p>
        <ul style="color: #94a3b8; line-height: 1.8;">
          <li>✓ 100% Free Urdu/Hindi Video Tutorials</li>
          <li>✓ Weekly Live Sunday Zoom Mentorship & Q&A</li>
          <li>✓ Practical Client Closing & Outreach Blueprints</li>
          <li>✓ Zero Paid Courses, Zero Hidden Funnels</li>
        </ul>
        """
    })
])

acad_right = make_column(40, [
    make_widget("heading", {
        "title": "📅 Weekly Sunday Live Zoom Class",
        "header_size": "h3",
        "title_color": "#f8fafc"
    }),
    make_widget("text-editor", {
        "editor": """
        <p style="color: #cbd5e1;">Every Sunday at 8:00 PM PKT. Live site audits, student questions, and freelancing career guidance.</p>
        <div style="background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 12px; margin-bottom: 16px;">
          <strong style="color: #10b981;">100% Free Entry</strong> · Open to All Students
        </div>
        """
    }),
    make_widget("button", {
        "text": "Join Free Sunday Class →",
        "link": {"url": "#contact", "is_external": False, "nofollow": False},
        "background_color": "#10b981",
        "button_text_color": "#ffffff",
        "align": "center",
        "border_radius": {"unit": "px", "top": "6", "right": "6", "bottom": "6", "left": "6", "isLinked": True}
    })
], card_settings)

sec_08 = make_section("🎓 08. Free Learning Academy & Live Mentorship", [acad_left, acad_right], {
    "background_color": "#060911"
})

# -------------------------------------------------------------
# Section 09: Video Tutorials Showcase
# -------------------------------------------------------------
vid_col1 = make_column(50, [
    make_widget("heading", {
        "title": "🎥 Fiverr Gig Ranking 2026 Blueprint",
        "header_size": "h4",
        "title_color": "#f8fafc"
    }),
    make_widget("text-editor", {
        "editor": "<p style='color: #94a3b8;'>Step-by-step video breakdown showing how to research low-competition Fiverr keywords, structure gig packages, and gain initial orders without artificial reviews.</p>"
    }),
    make_widget("button", {
        "text": "Watch Video Tutorial →",
        "link": {"url": "https://youtube.com", "is_external": True, "nofollow": True},
        "background_color": "rgba(255, 255, 255, 0.08)",
        "button_text_color": "#cbd5e1"
    })
], card_settings)

vid_col2 = make_column(50, [
    make_widget("heading", {
        "title": "🎥 Cold Email Guest Post Outreach Demo",
        "header_size": "h4",
        "title_color": "#f8fafc"
    }),
    make_widget("text-editor", {
        "editor": "<p style='color: #94a3b8;'>Live screen-recording demonstrating how to find real editor contact information, craft personalized pitches, and secure high DR backlinks on genuine publications.</p>"
    }),
    make_widget("button", {
        "text": "Watch Video Tutorial →",
        "link": {"url": "https://youtube.com", "is_external": True, "nofollow": True},
        "background_color": "rgba(255, 255, 255, 0.08)",
        "button_text_color": "#cbd5e1"
    })
], card_settings)

sec_09 = make_section("🎥 09. Video Tutorials Showcase", [vid_col1, vid_col2], {
    "background_color": "#0b1120"
})

# -------------------------------------------------------------
# Section 10: Frequently Asked Questions (Native Accordion)
# -------------------------------------------------------------
faq_col = make_column(100, [
    make_widget("heading", {
        "title": "CLIENT FAQ",
        "header_size": "h5",
        "align": "center",
        "title_color": "#10b981",
        "typography_font_size": {"unit": "px", "size": 13, "sizes": []}
    }),
    make_widget("heading", {
        "title": "Frequently Asked Questions by Clients",
        "header_size": "h2",
        "align": "center",
        "title_color": "#f8fafc",
        "typography_font_size": {"unit": "px", "size": 34, "sizes": []}
    }),
    make_widget("accordion", {
        "tabs": [
            {
                "_id": "faq_01",
                "tab_title": "Do you use Private Blog Networks (PBNs) or automated link schemes?",
                "tab_content": "Never. Every single guest post and backlink is secured through 100% manual, personalized blogger outreach to real, active websites with verified organic search traffic (Ahrefs DR 40–80+). Zero PBNs, zero link farms, and zero algorithmic risk."
            },
            {
                "_id": "faq_02",
                "tab_title": "How long does it take to see measurable SEO ranking improvements?",
                "tab_content": "Technical fixes, Core Web Vitals remediation, and indexation corrections produce noticeable Search Console gains within 2 to 4 weeks. Competitive commercial keyword jumps and scalable organic revenue compounding typically mature over 3 to 6 months of steady execution."
            },
            {
                "_id": "faq_03",
                "tab_title": "What payment methods and currencies do you support for international clients?",
                "tab_content": "We accommodate global clients with flexible invoicing in USD, EUR, GBP, and PKR. Payments can be processed securely via Wise (formerly TransferWise), Payoneer, Direct International Bank Wire, or Stripe."
            },
            {
                "_id": "faq_04",
                "tab_title": "Do you offer white-label guest posting and SEO services for digital agencies?",
                "tab_content": "Yes. We act as a dedicated outreach backend for multiple marketing agencies across the US, UK, and Australia. We deliver unbranded, white-label client spreadsheets, live URL verification reports, and customized anchor text strategies."
            },
            {
                "_id": "faq_05",
                "tab_title": "Are there long-term lock-in contracts?",
                "tab_content": "No lock-in contracts. Client retainers operate on a month-to-month basis with transparent deliverables, and guest posting packages can be purchased as one-time campaigns or ongoing monthly orders."
            }
        ],
        "title_color": "#f8fafc",
        "tab_active_color": "#10b981",
        "content_color": "#cbd5e1"
    })
])

sec_10 = make_section("❓ 10. Frequently Asked Questions (FAQ)", [faq_col], {
    "background_color": "#060911"
})

# -------------------------------------------------------------
# Section 11: Contact Section & WhatsApp CTA
# -------------------------------------------------------------
contact_left = make_column(45, [
    make_widget("heading", {
        "title": "GET IN TOUCH",
        "header_size": "h5",
        "title_color": "#10b981",
        "typography_font_size": {"unit": "px", "size": 13, "sizes": []}
    }),
    make_widget("heading", {
        "title": "Ready to Grow Your Website Traffic on Google?",
        "header_size": "h2",
        "title_color": "#f8fafc",
        "typography_font_size": {"unit": "px", "size": 32, "sizes": []}
    }),
    make_widget("text-editor", {
        "editor": """
        <p style="color: #cbd5e1; font-size: 1.05rem; line-height: 1.6;">
          Whether you need a dedicated SEO strategist, a high-authority guest posting campaign, or compelling conversion copy, I am ready to help.
        </p>
        <p style="color: #94a3b8; margin-top: 15px;">
          ⚡ <strong style="color: #f8fafc;">Response Guarantee:</strong> Direct reply within 12–24 business hours.<br>
          📧 <strong style="color: #f8fafc;">Direct Email:</strong> asimseowala@gmail.com
        </p>
        """
    }),
    make_widget("button", {
        "text": "💬 Chat on WhatsApp Instantly →",
        "link": {
            "url": "https://wa.me/?text=Hi%20Asim%2C%20I%20am%20interested%20in%20SEO%20and%20ranking%20for%20my%20website",
            "is_external": True,
            "nofollow": False
        },
        "background_color": "#10b981",
        "button_text_color": "#ffffff",
        "size": "lg",
        "border_radius": {"unit": "px", "top": "8", "right": "8", "bottom": "8", "left": "8", "isLinked": True}
    })
])

contact_right = make_column(55, [
    make_widget("heading", {
        "title": "Send a Project Inquiry",
        "header_size": "h3",
        "title_color": "#f8fafc"
    }),
    make_widget("text-editor", {
        "editor": """
        <form id="client-inquiry-form" style="display: flex; flex-direction: column; gap: 14px; margin-top: 16px;">
          <div>
            <label style="color: #cbd5e1; font-size: 0.9rem; font-weight: 600; display: block; margin-bottom: 6px;">Your Full Name</label>
            <input type="text" placeholder="e.g. John Doe" style="width: 100%; background: #0b1120; border: 1px solid rgba(255,255,255,0.12); color: #f8fafc; padding: 12px 14px; border-radius: 8px;" required>
          </div>
          <div>
            <label style="color: #cbd5e1; font-size: 0.9rem; font-weight: 600; display: block; margin-bottom: 6px;">Business Email</label>
            <input type="email" placeholder="e.g. john@company.com" style="width: 100%; background: #0b1120; border: 1px solid rgba(255,255,255,0.12); color: #f8fafc; padding: 12px 14px; border-radius: 8px;" required>
          </div>
          <div>
            <label style="color: #cbd5e1; font-size: 0.9rem; font-weight: 600; display: block; margin-bottom: 6px;">Website URL</label>
            <input type="url" placeholder="https://yourwebsite.com" style="width: 100%; background: #0b1120; border: 1px solid rgba(255,255,255,0.12); color: #f8fafc; padding: 12px 14px; border-radius: 8px;">
          </div>
          <div>
            <label style="color: #cbd5e1; font-size: 0.9rem; font-weight: 600; display: block; margin-bottom: 6px;">Service Needed</label>
            <select style="width: 100%; background: #0b1120; border: 1px solid rgba(255,255,255,0.12); color: #f8fafc; padding: 12px 14px; border-radius: 8px;">
              <option>Full-Stack SEO Strategy</option>
              <option>High-Authority Guest Posting</option>
              <option>Conversion Content Writing</option>
              <option>Free Initial Website Audit</option>
            </select>
          </div>
          <div>
            <label style="color: #cbd5e1; font-size: 0.9rem; font-weight: 600; display: block; margin-bottom: 6px;">Project Goals & Details</label>
            <textarea rows="4" placeholder="Tell me about your current rankings, target audience, and monthly revenue goals..." style="width: 100%; background: #0b1120; border: 1px solid rgba(255,255,255,0.12); color: #f8fafc; padding: 12px 14px; border-radius: 8px;" required></textarea>
          </div>
          <button type="submit" style="background: #10b981; color: #fff; font-weight: 700; font-size: 1rem; padding: 14px; border: none; border-radius: 8px; cursor: pointer; margin-top: 8px;">Send Project Inquiry →</button>
        </form>
        """
    })
], card_settings)

sec_11 = make_section("📬 11. Contact & Lead Consultation", [contact_left, contact_right], {
    "background_color": "#0b1120"
})

# -------------------------------------------------------------
# Section 12: Legal Policies, Terms & Disclaimer
# -------------------------------------------------------------
legal_col1 = make_column(33, [
    make_widget("heading", {"title": "🔒 Privacy Policy", "header_size": "h4", "title_color": "#f8fafc"}),
    make_widget("text-editor", {
        "editor": "<p style='color: #94a3b8; font-size: 0.9rem;'>We respect your data privacy. Inquiries and website credentials shared for audits are held under strict confidentiality. We never sell or share client data with third parties.</p>"
    })
], card_settings)

legal_col2 = make_column(33, [
    make_widget("heading", {"title": "⚖️ Terms of Service", "header_size": "h4", "title_color": "#f8fafc"}),
    make_widget("text-editor", {
        "editor": "<p style='color: #94a3b8; font-size: 0.9rem;'>All retainer engagements and guest posting campaigns operate with clearly defined scopes, transparent deliverable reports, and zero lock-in contracts.</p>"
    })
], card_settings)

legal_col3 = make_column(33, [
    make_widget("heading", {"title": "📢 AdSense & Affiliate", "header_size": "h4", "title_color": "#f8fafc"}),
    make_widget("text-editor", {
        "editor": "<p style='color: #94a3b8; font-size: 0.9rem;'>Educational resources and software tool reviews on this site may feature affiliate links. We only recommend tools we personally test and use on client campaigns.</p>"
    })
], card_settings)

sec_12 = make_section("📜 12. Legal Policies & Disclaimers", [legal_col1, legal_col2, legal_col3], {
    "background_color": "#060911"
})

# -------------------------------------------------------------
# Section 13: Master 4-Column Footer
# -------------------------------------------------------------
footer_col1 = make_column(40, [
    make_widget("image", {
        "image": {"url": f"{CDN}/assets/images/logo.svg", "id": ""},
        "image_size": "custom",
        "image_custom_dimension": {"width": 180, "height": 45},
        "align": "left"
    }),
    make_widget("text-editor", {
        "editor": "<p style='color: #94a3b8; font-size: 0.95rem; margin-top: 12px;'>Top-Rated SEO Specialist & Outreach Consultant helping international brands scale organic search revenue and mentoring talent for free.</p>"
    })
])

footer_col2 = make_column(20, [
    make_widget("heading", {"title": "Quick Links", "header_size": "h5", "title_color": "#f8fafc"}),
    make_widget("text-editor", {
        "editor": """
        <div style="line-height: 2; font-size: 0.9rem;">
          <a href="#about" style="color: #cbd5e1; text-decoration: none;">About Me</a><br>
          <a href="#results" style="color: #cbd5e1; text-decoration: none;">Portfolio</a><br>
          <a href="#reviews" style="color: #cbd5e1; text-decoration: none;">Testimonials</a><br>
          <a href="#contact" style="color: #cbd5e1; text-decoration: none;">Contact Me</a>
        </div>
        """
    })
])

footer_col3 = make_column(20, [
    make_widget("heading", {"title": "Services", "header_size": "h5", "title_color": "#f8fafc"}),
    make_widget("text-editor", {
        "editor": """
        <div style="line-height: 2; font-size: 0.9rem;">
          <a href="#services" style="color: #cbd5e1; text-decoration: none;">Full SEO Strategy</a><br>
          <a href="#services" style="color: #cbd5e1; text-decoration: none;">Guest Posting</a><br>
          <a href="#services" style="color: #cbd5e1; text-decoration: none;">Content Writing</a><br>
          <a href="#contact" style="color: #cbd5e1; text-decoration: none;">Free Audit</a>
        </div>
        """
    })
])

footer_col4 = make_column(20, [
    make_widget("heading", {"title": "Free Learning", "header_size": "h5", "title_color": "#f8fafc"}),
    make_widget("text-editor", {
        "editor": """
        <div style="line-height: 2; font-size: 0.9rem;">
          <a href="#courses" style="color: #cbd5e1; text-decoration: none;">Free Academy</a><br>
          <a href="#courses" style="color: #cbd5e1; text-decoration: none;">Sunday Zoom</a><br>
          <a href="#courses" style="color: #cbd5e1; text-decoration: none;">Video Hub</a><br>
          <a href="#faq" style="color: #cbd5e1; text-decoration: none;">Client FAQ</a>
        </div>
        """
    })
])

sec_13 = make_section("⚓ 13. Master 4-Column Footer", [footer_col1, footer_col2, footer_col3, footer_col4], {
    "background_color": "#060911",
    "padding": {"unit": "px", "top": "50", "right": "20", "bottom": "30", "left": "20", "isLinked": False}
})

# Assemble all sections
all_sections = [
    sec_01,
    sec_02,
    sec_03,
    sec_04,
    sec_05_header,
    sec_05_cards,
    sec_06,
    sec_07,
    sec_08,
    sec_09,
    sec_10,
    sec_11,
    sec_12,
    sec_13
]

template = {
    "version": "0.4",
    "title": "Asim SEO Wala - 100% Native Elementor Master Template",
    "type": "page",
    "content": all_sections,
    "page_settings": {}
}

output_file = "asim-seowala-native-elementor-template.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(template, f, ensure_ascii=False, indent=2)

# Also update the primary asim-seowala-elementor-template.json
with open("asim-seowala-elementor-template.json", "w", encoding="utf-8") as f:
    json.dump(template, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {output_file} with {len(all_sections)} 100% native Elementor sections!")
