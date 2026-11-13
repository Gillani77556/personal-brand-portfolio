/**
 * Main JavaScript for Asim SEO Wala PRO - Personal Branding & Portfolio Website
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Mobile Menu Toggle with Lucide SVG Icons
  const mobileToggle = document.querySelector('.mobile-toggle');
  const navMenu = document.querySelector('.nav-menu');

  const menuSvg = '<svg class="icon" viewBox="0 0 24 24"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>';
  const closeSvg = '<svg class="icon" viewBox="0 0 24 24"><line x1="18" x2="6" y1="6" y2="18"/><line x1="6" x2="18" y1="6" y2="18"/></svg>';

  if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', () => {
      navMenu.classList.toggle('open');
      const isOpen = navMenu.classList.contains('open');
      mobileToggle.innerHTML = isOpen ? closeSvg : menuSvg;
      mobileToggle.setAttribute('aria-expanded', isOpen);
    });

    // Close mobile menu when regular nav links (not dropdown toggles) are clicked
    document.querySelectorAll('.nav-link:not(.dropdown-toggle), .dropdown-item a').forEach(link => {
      link.addEventListener('click', () => {
        if (navMenu.classList.contains('open')) {
          navMenu.classList.remove('open');
          mobileToggle.innerHTML = menuSvg;
        }
      });
    });
  }

  // 1B. Dropdown Click Toggle (Desktop & Mobile)
  document.querySelectorAll('.has-dropdown').forEach(dropdown => {
    const toggle = dropdown.querySelector('.dropdown-toggle');
    if (toggle) {
      toggle.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        const isOpen = dropdown.classList.contains('dropdown-open');
        
        // Close other dropdowns if any
        document.querySelectorAll('.has-dropdown').forEach(d => {
          if (d !== dropdown) d.classList.remove('dropdown-open');
        });

        dropdown.classList.toggle('dropdown-open', !isOpen);
        toggle.setAttribute('aria-expanded', !isOpen ? 'true' : 'false');
      });
    }
  });

  // Close dropdown when clicking outside
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.has-dropdown')) {
      document.querySelectorAll('.has-dropdown').forEach(d => {
        d.classList.remove('dropdown-open');
        const toggle = d.querySelector('.dropdown-toggle');
        if (toggle) toggle.setAttribute('aria-expanded', 'false');
      });
    }
  });

  // 2. Sticky Header Elevation on Scroll
  const siteHeader = document.querySelector('.site-header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      siteHeader?.classList.add('scrolled');
    } else {
      siteHeader?.classList.remove('scrolled');
    }
  });

  // 3. Dynamic Year in Footer
  const yearElement = document.getElementById('current-year');
  if (yearElement) {
    yearElement.textContent = new Date().getFullYear();
  }

  // 4. Portfolio Filterable Tabs (if on portfolio page)
  const filterButtons = document.querySelectorAll('.filter-btn');
  const portfolioItems = document.querySelectorAll('.portfolio-item');

  if (filterButtons.length && portfolioItems.length) {
    filterButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        filterButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const filterValue = btn.getAttribute('data-filter');

        portfolioItems.forEach(item => {
          if (filterValue === 'all' || item.getAttribute('data-category') === filterValue) {
            item.style.display = 'flex';
          } else {
            item.style.display = 'none';
          }
        });
      });
    });
  }

  // 5. Contact & Zoom Form Submission Handling (with visual feedback)
  const contactForm = document.getElementById('client-inquiry-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      alert('Thank you for your project inquiry! Asim will review your website details and reply via email within 12–24 business hours.');
      contactForm.reset();
    });
  }

  const zoomForm = document.getElementById('zoom-registration-form');
  if (zoomForm) {
    zoomForm.addEventListener('submit', (e) => {
      e.preventDefault();
      alert('Success! You have been registered for our upcoming Free Sunday Zoom Class. Check your email and WhatsApp for the meeting link.');
      zoomForm.reset();
    });
  }

  // 6. Smooth Scroll for Table of Contents
  document.querySelectorAll('.toc-list a').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const targetId = this.getAttribute('href').substring(1);
      const targetElement = document.getElementById(targetId);
      if (targetElement) {
        window.scrollTo({
          top: targetElement.offsetTop - 90,
          behavior: 'smooth'
        });
      }
    });
  });
});
