'use strict';
(() => {
  const header = document.querySelector('.site-header');
  const menu = document.querySelector('.menu-toggle');
  const nav = document.getElementById('site-nav');
  const mobile = window.matchMedia('(max-width: 760px)');

  function closeMenu(restoreFocus = false) {
    nav.classList.remove('is-open');
    menu.setAttribute('aria-expanded', 'false');
    if (restoreFocus) menu.focus();
  }

  menu.hidden = false;
  header.dataset.enhanced = 'true';
  menu.addEventListener('click', () => {
    const open = menu.getAttribute('aria-expanded') !== 'true';
    menu.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('is-open', open);
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && nav.classList.contains('is-open')) closeMenu(true);
  });
  document.addEventListener('click', event => {
    if (!header.contains(event.target)) closeMenu();
  });
  nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
    const wasOpen = nav.classList.contains('is-open');
    closeMenu();
    if (wasOpen && mobile.matches) {
      const section = document.querySelector(link.getAttribute('href'));
      if (section) {
        section.setAttribute('tabindex', '-1');
        section.focus({ preventScroll: true });
      }
    }
  }));
  mobile.addEventListener('change', () => closeMenu());
  document.getElementById('year').textContent = new Date().getFullYear();
})();
