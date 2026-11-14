import json
import re
import uuid

def gen_id():
    return uuid.uuid4().hex[:7]

def make_elementor_section(title, html_content):
    return {
        "id": gen_id(),
        "elType": "section",
        "isInner": False,
        "settings": {
            "layout": "full_width",
            "gap": "no",
            "_title": title
        },
        "defaultEditSettings": {
            "defaultEditRoute": "content"
        },
        "elements": [
            {
                "id": gen_id(),
                "elType": "column",
                "isInner": False,
                "settings": {
                    "_column_size": 100,
                    "_inline_size": None
                },
                "defaultEditSettings": {
                    "defaultEditRoute": "content"
                },
                "elements": [
                    {
                        "id": gen_id(),
                        "elType": "widget",
                        "isInner": False,
                        "widgetType": "html",
                        "settings": {
                            "html": html_content
                        },
                        "defaultEditSettings": {
                            "defaultEditRoute": "content"
                        },
                        "elements": []
                    }
                ]
            }
        ]
    }

# Read base files
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

with open('contact.html', 'r', encoding='utf-8') as f:
    contact_html = f.read()

with open('assets/css/styles.min.css', 'r', encoding='utf-8') as f:
    css_min = f.read()

CDN_BASE = "https://personal-brand-portfolio-three.vercel.app"

def clean_urls(html):
    # Replace relative asset paths
    html = re.sub(r'assets/images/([a-zA-Z0-9_\-\.]+)', f'{CDN_BASE}/assets/images/\\1', html)
    # Replace internal page links with smooth anchor links
    html = re.sub(r'href="index\.html"', 'href="#top"', html)
    html = re.sub(r'href="about\.html"', 'href="#about"', html)
    html = re.sub(r'href="services\.html"', 'href="#services"', html)
    html = re.sub(r'href="services-seo\.html"', 'href="#services"', html)
    html = re.sub(r'href="services-guest-posting\.html"', 'href="#services"', html)
    html = re.sub(r'href="services-content-writing\.html"', 'href="#services"', html)
    html = re.sub(r'href="portfolio\.html"', 'href="#results"', html)
    html = re.sub(r'href="free-courses\.html#zoom"', 'href="#zoom"', html)
    html = re.sub(r'href="free-courses\.html"', 'href="#courses"', html)
    html = re.sub(r'href="videos\.html"', 'href="#videos"', html)
    html = re.sub(r'href="blog\.html"', 'href="#courses"', html)
    html = re.sub(r'href="article-fiverr-ranking\.html"', 'href="#courses"', html)
    html = re.sub(r'href="contact\.html#faq"', 'href="#faq"', html)
    html = re.sub(r'href="contact\.html#privacy"', 'href="#privacy"', html)
    html = re.sub(r'href="contact\.html#terms"', 'href="#terms"', html)
    html = re.sub(r'href="contact\.html#disclaimer"', 'href="#disclaimer"', html)
    html = re.sub(r'href="contact\.html"', 'href="#contact"', html)
    return html

# 1. Global CSS section
theme_resets = """
<style>
/* =========================================================
   Asim SEO Wala PRO - Master Elementor Theme Compatibility Resets
   ========================================================= */
.elementor-section.elementor-section-boxed > .elementor-container {
  max-width: 100% !important;
  width: 100% !important;
  padding: 0 !important;
}
.elementor-widget-html {
  width: 100% !important;
}
.elementor-widget-container {
  width: 100% !important;
}
.elementor-column-gap-default > .elementor-column > .elementor-element-populated {
  padding: 0 !important;
}
.elementor-widget-wrap {
  padding: 0 !important;
}
html {
  scroll-behavior: smooth;
}
body {
  background-color: #060911 !important;
  color: #cbd5e1 !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
  margin: 0 !important;
  padding: 0 !important;
  overflow-x: hidden;
}
.site-header a, .hero-section a, .section a, .card a, .site-footer a, .nav-menu a {
  text-decoration: none !important;
}
*, *::before, *::after {
  box-sizing: border-box;
}

""" + css_min + """
</style>
"""

sections = []

# Section 1: Stylesheet
sections.append(make_elementor_section("🎨 01. Global CSS & Design System", theme_resets))

# Section 2: Header / Nav
header_match = re.search(r'(<header class="site-header".*?</header>)', index_html, re.DOTALL)
if header_match:
    header_html = clean_urls(header_match.group(1))
    sections.append(make_elementor_section("📌 02. Header & Sticky Navigation", header_html))

# Section 3: Hero Section
hero_match = re.search(r'(<section class="hero-section".*?</section>)', index_html, re.DOTALL)
if hero_match:
    hero_html = hero_match.group(1)
    hero_html = re.sub(r'<section class="hero-section"', '<section class="hero-section" id="top"', hero_html)
    hero_html = clean_urls(hero_html)
    sections.append(make_elementor_section("🚀 03. Hero Showcase & Availability", hero_html))

# Extract all sections from index.html
index_sections = re.findall(r'(<section[^>]*>.*?</section>)', index_html, re.DOTALL)

# Sec 2 in index.html is About / Bento
about_html = clean_urls(index_sections[1])
about_html = re.sub(r'<section class="bg-alt"', '<section class="bg-alt" id="about"', about_html)
sections.append(make_elementor_section("👨‍💻 04. About Asim & Hands-on Experience", about_html))

# Sec 3 in index.html is Services
services_html = clean_urls(index_sections[2])
services_html = re.sub(r'<section>', '<section id="services">', services_html)
sections.append(make_elementor_section("⚡ 05. Three Core SEO Services", services_html))

# Sec 4 in index.html is Case Studies / Results
results_html = clean_urls(index_sections[3])
results_html = re.sub(r'<section class="bg-alt"', '<section class="bg-alt" id="results"', results_html)
sections.append(make_elementor_section("📈 06. Verified Case Studies & Traffic Gains", results_html))

# Sec 5 in index.html is Reviews
reviews_html = clean_urls(index_sections[4])
reviews_html = re.sub(r'<section>', '<section id="reviews">', reviews_html)
sections.append(make_elementor_section("⭐ 07. International Client Reviews", reviews_html))

# Sec 6 in index.html is Academy Spotlight
academy_html = clean_urls(index_sections[5])
academy_html = re.sub(r'<section class="bg-academy-glow"', '<section class="bg-academy-glow" id="courses"', academy_html)
sections.append(make_elementor_section("🎓 08. Free Learning Academy", academy_html))

# Sec 7 in index.html is Sunday Zoom
zoom_html = clean_urls(index_sections[6])
zoom_html = re.sub(r'<section id="zoom-registration-form"', '<section id="zoom"', zoom_html)
sections.append(make_elementor_section("📆 09. Weekly Sunday Live Zoom Classes", zoom_html))

# Sec 9 in index.html is Video Tutorials Showcase
videos_html = clean_urls(index_sections[8])
videos_html = re.sub(r'<section>', '<section id="videos">', videos_html)
sections.append(make_elementor_section("🎥 10. Screen-Share Video Tutorials", videos_html))

# From contact.html: FAQ Accordion
faq_match = re.search(r'(<section class="bg-alt" id="faq">.*?</section>)', contact_html, re.DOTALL)
if faq_match:
    faq_html = clean_urls(faq_match.group(1))
    sections.append(make_elementor_section("❓ 11. Frequently Asked Questions (FAQ)", faq_html))

# From contact.html: Contact Information & Client Inquiry Form
contact_match = re.search(r'(<section style="padding-top: 20px;">.*?</section>)', contact_html, re.DOTALL)
if contact_match:
    contact_html_chunk = contact_match.group(1)
    # Add Section header for contact
    full_contact_html = f"""
    <section class="hero-section" id="contact" style="padding: 70px 0 20px; text-align: center;">
      <div class="container">
        <span class="pill-badge">GET IN TOUCH</span>
        <h2 style="max-width: 800px; margin: 0 auto 16px;">Ready to Scale Your Organic Search Growth?</h2>
        <p class="section-subtext" style="margin: 0 auto 20px;">
          Send your website URL and project goals below, or message me directly on WhatsApp for an immediate response.
        </p>
      </div>
    </section>
    """ + contact_html_chunk
    full_contact_html = clean_urls(full_contact_html)
    sections.append(make_elementor_section("📬 12. Contact Form & WhatsApp CTA", full_contact_html))

# From contact.html: Legal Policies & Disclaimer
legal_match = re.search(r'(<section id="privacy".*?</section>)', contact_html, re.DOTALL)
if legal_match:
    legal_html = clean_urls(legal_match.group(1))
    sections.append(make_elementor_section("📜 13. Legal Policies, Terms & Disclaimer", legal_html))

# Master Footer
footer_match = re.search(r'(<footer class="site-footer".*?</footer>)', index_html, re.DOTALL)
if footer_match:
    footer_html = clean_urls(footer_match.group(1))
    sections.append(make_elementor_section("⚓ 14. Master Footer & Copyright", footer_html))

# Interactive JavaScript Engine
js_script = """
<script>
document.addEventListener('DOMContentLoaded', () => {
  // Mobile Nav Toggle
  const mobileToggle = document.querySelector('.mobile-toggle');
  const navMenu = document.querySelector('.nav-menu');
  const menuSvg = '<svg class="icon" viewBox="0 0 24 24"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>';
  const closeSvg = '<svg class="icon" viewBox="0 0 24 24"><line x1="18" x2="6" y1="6" y2="18"/><line x1="6" x2="18" y1="6" y2="18"/></svg>';

  if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', (e) => {
      e.stopPropagation();
      navMenu.classList.toggle('open');
      const isOpen = navMenu.classList.contains('open');
      mobileToggle.innerHTML = isOpen ? closeSvg : menuSvg;
      mobileToggle.setAttribute('aria-expanded', isOpen);
    });

    document.querySelectorAll('.nav-link, .nav-menu .btn-primary').forEach(link => {
      link.addEventListener('click', () => {
        if (navMenu.classList.contains('open')) {
          navMenu.classList.remove('open');
          mobileToggle.innerHTML = menuSvg;
        }
      });
    });
  }

  // Sticky Header Scroll
  const siteHeader = document.querySelector('.site-header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      siteHeader?.classList.add('scrolled');
    } else {
      siteHeader?.classList.remove('scrolled');
    }
  });

  // Dynamic Year
  const yearElement = document.getElementById('current-year');
  if (yearElement) {
    yearElement.textContent = new Date().getFullYear();
  }

  // Toast Notification System
  function showToast(title, message) {
    let container = document.querySelector('.toast-container');
    if (!container) {
      container = document.createElement('div');
      container.className = 'toast-container';
      document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    toast.className = 'toast-card';
    toast.innerHTML = `
      <svg class="toast-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
        <polyline points="22 4 12 14.01 9 11.01"/>
      </svg>
      <div class="toast-content">
        <div class="toast-title">${title}</div>
        <div class="toast-desc">${message}</div>
      </div>
      <button class="toast-close" aria-label="Close notification">
        <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2">
          <line x1="18" y1="6" x2="6" y2="18"/>
          <line x1="6" y1="6" x2="18" y2="18"/>
        </svg>
      </button>
    `;

    container.appendChild(toast);
    requestAnimationFrame(() => toast.classList.add('show'));

    const removeToast = () => {
      toast.classList.remove('show');
      setTimeout(() => toast.remove(), 350);
    };

    toast.querySelector('.toast-close').addEventListener('click', removeToast);
    setTimeout(removeToast, 5000);
  }

  // Form Submissions
  document.querySelectorAll('form[id="client-inquiry-form"]').forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const submitBtn = form.querySelector('button[type="submit"]');
      const originalText = submitBtn ? submitBtn.innerHTML : 'Submit';
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = 'Sending Inquiry...';
      }
      setTimeout(() => {
        showToast(
          'Inquiry Received Successfully!',
          'Thank you! Asim will review your campaign goals and reply via email within 12–24 business hours.'
        );
        form.reset();
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = originalText;
        }
      }, 600);
    });
  });

  document.querySelectorAll('form[id="zoom-registration-form"]').forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const submitBtn = form.querySelector('button[type="submit"]');
      const originalText = submitBtn ? submitBtn.innerHTML : 'Register';
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = 'Reserving Seat...';
      }
      setTimeout(() => {
        showToast(
          'Seat Reserved Successfully!',
          'You are registered for our upcoming Free Sunday Zoom Class. Check your email and WhatsApp for login credentials.'
        );
        form.reset();
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = originalText;
        }
      }, 600);
    });
  });
});
</script>
"""
sections.append(make_elementor_section("⚙️ 15. Interactive Scripts Engine", js_script))

elementor_template = {
    "version": "0.4",
    "title": "Asim SEO Wala - All-in-One Master Template",
    "type": "page",
    "content": sections,
    "page_settings": {}
}

output_path = "asim-seowala-elementor-template.json"
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(elementor_template, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {output_path} with {len(sections)} sections.")
