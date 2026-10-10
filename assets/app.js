'use strict';
(() => {
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const activeAnimations = new Set();
  let motionEnabled = true;
  try { motionEnabled = localStorage.getItem('portfolio-motion') !== 'off'; } catch { /* Storage is optional. */ }
  const allowMotion = () => motionEnabled && !reducedMotion.matches;
  const animate = (element, frames, options = {}) => {
    if (!allowMotion() || !element.animate) return null;
    const animation = element.animate(frames, { duration: 240, easing: 'cubic-bezier(.16,1,.3,1)', ...options });
    activeAnimations.add(animation);
    animation.finished.catch(() => {}).finally(() => activeAnimations.delete(animation));
    return animation;
  };
  const motionToggle = document.querySelector('.motion-toggle');
  function syncMotion() {
    const enabled = allowMotion();
    document.documentElement.dataset.motion = enabled ? 'on' : 'off';
    motionToggle.setAttribute('aria-checked', String(enabled));
    motionToggle.querySelector('[data-motion-label]').textContent = enabled ? 'on' : 'off';
    motionToggle.disabled = reducedMotion.matches;
    motionToggle.title = reducedMotion.matches ? 'Reduced motion is enabled in your device settings.' : 'Turn page animations on or off';
    if (!enabled) activeAnimations.forEach(animation => animation.finish());
  }
  motionToggle.hidden = false;
  motionToggle.addEventListener('click', () => {
    motionEnabled = !motionEnabled;
    try { localStorage.setItem('portfolio-motion', motionEnabled ? 'on' : 'off'); } catch { /* Preference still works for this visit. */ }
    syncMotion();
  });
  reducedMotion.addEventListener('change', syncMotion);
  syncMotion();

  // A single, finite sequence connects the three parts of the approach diagram.
  animate(document.querySelector('.map-route'), [{ strokeDashoffset: 1 }, { strokeDashoffset: 0 }], { duration: 1000 });
  document.querySelectorAll('.map-node').forEach((node, index) => {
    animate(node, [{ opacity: .35 }, { opacity: 1 }], { duration: 400, delay: index * 170 });
  });
  const approachCopy = {
    people: ['Build the team behind the technology.', 'Coaching, clear ownership and shared engineering practices help people deliver with confidence.'],
    architecture: ['Make the trade-offs clear.', 'Architecture boards and documented decisions align modernisation, resilience and cost with the needs of the service.'],
    delivery: ['Carry decisions through to production.', 'Delivery ownership connects engineering quality, client relationships and the continuity of critical services.']
  };
  const approach = document.querySelector('.approach');
  const approachPanel = document.querySelector('.approach-panel');
  document.querySelector('.approach-controls').hidden = false;
  document.querySelectorAll('[data-approach]').forEach(button => {
    button.addEventListener('click', () => {
      if (button.getAttribute('aria-pressed') === 'true') return;
      const selected = button.dataset.approach;
      document.querySelectorAll('[data-approach]').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
      approach.dataset.selected = selected;
      approachPanel.getAnimations().forEach(animation => animation.cancel());
      approachPanel.querySelector('h3').textContent = approachCopy[selected][0];
      approachPanel.querySelector('p').textContent = approachCopy[selected][1];
      animate(approachPanel, [{ opacity: .4, transform: 'translateY(5px)' }, { opacity: 1, transform: 'translateY(0)' }]);
    });
  });

  const header = document.querySelector('.site-header');
  const menuToggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.site-nav');
  header.dataset.enhanced = 'true';
  menuToggle.hidden = false;
  function closeMenu(returnFocus = false) {
    nav.classList.remove('is-open');
    menuToggle.setAttribute('aria-expanded', 'false');
    if (returnFocus) menuToggle.focus();
  }
  menuToggle.addEventListener('click', () => {
    const open = menuToggle.getAttribute('aria-expanded') !== 'true';
    menuToggle.setAttribute('aria-expanded', String(open));
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
    if (wasOpen) {
      const section = document.querySelector(link.getAttribute('href'));
      if (section) {
        section.setAttribute('tabindex', '-1');
        section.focus({ preventScroll: true });
      }
    }
  }));
  const narrowViewport = window.matchMedia('(max-width: 760px)');
  narrowViewport.addEventListener('change', () => closeMenu());

  const filterButtons = [...document.querySelectorAll('[data-filter]')];
  const cards = [...document.querySelectorAll('[data-category]')];
  const status = document.getElementById('filter-status');
  let selectedFilter = 'all';
  document.querySelector('.filters').hidden = false;
  function filterProjects(filter) {
    if (filter === selectedFilter) return;
    selectedFilter = filter;
    const before = new Map();
    cards.forEach(card => {
      card.getAnimations().forEach(animation => animation.cancel());
      if (!card.hidden) before.set(card, card.getBoundingClientRect());
    });
    filterButtons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.filter === filter)));
    cards.forEach(card => { card.hidden = filter !== 'all' && !card.dataset.category.split(' ').includes(filter); });
    const visible = cards.filter(card => !card.hidden);
    status.textContent = `${visible.length} ${visible.length === 1 ? 'project' : 'projects'}`;
    // FLIP: read positions together, then animate transforms without driving layout.
    const after = new Map(visible.map(card => [card, card.getBoundingClientRect()]));
    visible.forEach(card => {
      const previous = before.get(card);
      const next = after.get(card);
      if (previous) {
        const x = previous.left - next.left;
        const y = previous.top - next.top;
        if (x || y) animate(card, [{ transform: `translate(${x}px, ${y}px)` }, { transform: 'translate(0, 0)' }], { duration: 280 });
      } else {
        animate(card, [{ opacity: .25, transform: 'translateY(8px)' }, { opacity: 1, transform: 'translateY(0)' }], { duration: 240 });
      }
    });
  }
  filterButtons.forEach(button => button.addEventListener('click', () => filterProjects(button.dataset.filter)));
  document.querySelectorAll('[data-filter-jump]').forEach(link => link.addEventListener('click', () => filterProjects(link.dataset.filterJump)));

  // Native details remain usable without JavaScript. Animation is an enhancement.
  document.querySelectorAll('details').forEach(details => {
    const summary = details.querySelector('summary');
    let animation;
    let intendedOpen = details.open;
    summary.addEventListener('click', event => {
      if (!allowMotion() || !details.animate) return;
      event.preventDefault();
      const start = details.getBoundingClientRect().height;
      intendedOpen = animation ? !intendedOpen : !details.open;
      if (animation) animation.cancel();
      details.open = true;
      const end = intendedOpen ? details.getBoundingClientRect().height : summary.getBoundingClientRect().height + 1;
      details.style.overflow = 'hidden';
      animation = animate(details, [{ height: `${start}px` }, { height: `${end}px` }], { duration: intendedOpen ? 260 : 190 });
      const current = animation;
      if (!current) { details.open = intendedOpen; details.style.overflow = ''; return; }
      current.onfinish = () => {
        if (animation !== current) return;
        details.open = intendedOpen;
        details.style.overflow = '';
        animation = undefined;
      };
    });
  });

  const copyButton = document.querySelector('.copy-email');
  const copyStatus = document.querySelector('.copy-status');
  copyButton.hidden = false;
  copyButton.addEventListener('click', async () => {
    copyButton.disabled = true;
    try {
      if (!navigator.clipboard?.writeText) throw new Error('Clipboard unavailable');
      await navigator.clipboard.writeText('paulo.sanch3s@gmail.com');
      copyStatus.textContent = 'Email address copied.';
    } catch {
      copyStatus.textContent = 'Copy unavailable. Select the email address above, or use the email link.';
    } finally {
      copyButton.disabled = false;
    }
  });
  if ('IntersectionObserver' in window) {
    const sectionObserver = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        nav.querySelectorAll('a').forEach(link => {
          if (link.getAttribute('href') === `#${entry.target.id}`) link.setAttribute('aria-current', 'location');
          else link.removeAttribute('aria-current');
        });
      });
    }, { rootMargin: '-15% 0px -65% 0px' });
    document.querySelectorAll('#about, #projects, #expertise, #experience, #contact').forEach(section => sectionObserver.observe(section));
  }
  // Preserve links shared from the original Portuguese portfolio.
  const legacyAnchors = { inicio: 'main', conteudo: 'main', sobre: 'about', projetos: 'projects', percurso: 'experience', contacto: 'contact' };
  const replacement = legacyAnchors[location.hash.slice(1)];
  if (replacement) { history.replaceState(null, '', `#${replacement}`); document.getElementById(replacement).scrollIntoView(); }
  document.getElementById('year').textContent = new Date().getFullYear();
})();
