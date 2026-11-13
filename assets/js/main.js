/**
 * Asim SEO Wala PRO - "Profound" Architectural Interactive Engine
 * Reverse-Engineered from https://www.tryprofound.com/
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Mobile Menu Toggle
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

    document.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => {
        if (navMenu.classList.contains('open')) {
          navMenu.classList.remove('open');
          mobileToggle.innerHTML = menuSvg;
        }
      });
    });
  }

  // 2. Interactive Tabbed Execution Showcase ("Prompt-to-Execution" Tabs)
  const executionTabBtns = document.querySelectorAll('.execution-tab-btn');
  const tabPanes = document.querySelectorAll('.tab-pane');

  if (executionTabBtns.length && tabPanes.length) {
    executionTabBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const targetTab = btn.getAttribute('data-tab');

        executionTabBtns.forEach(b => b.classList.remove('active'));
        tabPanes.forEach(p => p.classList.remove('active'));

        btn.classList.add('active');
        const activePane = document.getElementById(`tab-${targetTab}`);
        if (activePane) {
          activePane.classList.add('active');
        }
      });
    });
  }

  // 3. Workspace Sidebar Interactive Filter
  const workspaceSidebarItems = document.querySelectorAll('.sidebar-item');
  if (workspaceSidebarItems.length) {
    workspaceSidebarItems.forEach(item => {
      item.addEventListener('click', () => {
        workspaceSidebarItems.forEach(i => i.classList.remove('active'));
        item.classList.add('active');
      });
    });
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

  // 5. Dynamic Year in Footer
  const yearElement = document.getElementById('current-year');
  if (yearElement) {
    yearElement.textContent = new Date().getFullYear();
  }

  // 6. Contact & Zoom Form Feedback
  const contactForm = document.getElementById('client-inquiry-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      alert('Inquiry received! Asim will review your search performance metrics and respond within 12–24 business hours.');
      contactForm.reset();
    });
  }

  const zoomForm = document.getElementById('zoom-registration-form');
  if (zoomForm) {
    zoomForm.addEventListener('submit', (e) => {
      e.preventDefault();
      alert('Confirmed! Your seat for the Free Sunday Live Zoom Class is reserved. Check your email and WhatsApp for the direct session link.');
      zoomForm.reset();
    });
  }

  // 7. Smooth Scroll for Workspace Anchor
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href').substring(1);
      if (!targetId) return;
      const targetElement = document.getElementById(targetId);
      if (targetElement) {
        e.preventDefault();
        window.scrollTo({
          top: targetElement.offsetTop - 85,
          behavior: 'smooth'
        });
      }
    });
  });
});
