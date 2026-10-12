'use strict';
const year = document.getElementById('year');
if (year) year.textContent = String(new Date().getFullYear());
const language = document.documentElement.lang;
const carouselRole = language === 'it' ? 'carosello' : language === 'pt-BR' ? 'carrossel' : 'carousel';
const counterJoin = language === 'it' ? 'di' : language === 'pt-BR' ? 'de' : 'of';
document.querySelectorAll('.language-switcher a').forEach(link => {
  link.addEventListener('click', () => {
    if (!window.location.hash) return;
    const destination = new URL(link.href);
    destination.hash = window.location.hash;
    link.href = destination.href;
  });
});

const experienceDisclosures = Array.from(document.querySelectorAll('#journey details'));
if (experienceDisclosures.length) {
  const desktop = window.matchMedia('(min-width: 1024px)');
  const mobileState = new Map(experienceDisclosures.map(detail => [detail, false]));
  const applyExperienceLayout = () => {
    experienceDisclosures.forEach(detail => {
      detail.open = desktop.matches || mobileState.get(detail);
    });
  };
  desktop.addEventListener('change', () => {
    if (desktop.matches) {
      experienceDisclosures.forEach(detail => mobileState.set(detail, detail.open));
    }
    applyExperienceLayout();
  });
  applyExperienceLayout();
}

document.querySelectorAll('.carousel').forEach(carousel => {
  const track = carousel.querySelector('.carousel-track');
  const controls = carousel.querySelector('.carousel-controls');
  const previous = controls.querySelector('.carousel-previous');
  const next = controls.querySelector('.carousel-next');
  const position = controls.querySelector('.carousel-position');
  const buttons = controls.querySelector('.carousel-buttons');
  const hint = carousel.querySelector('.carousel-hint');
  const cards = Array.from(track.children);
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const helpId = track.getAttribute('aria-describedby');
  let settleTimer;

  const updateControls = () => {
    const maximum = track.scrollWidth - track.clientWidth;
    const scrollable = maximum > 1;
    controls.hidden = !scrollable;
    buttons.hidden = !scrollable;
    hint.hidden = !scrollable;
    track.tabIndex = scrollable ? 0 : -1;
    if (scrollable) {
      carousel.setAttribute('aria-roledescription', carouselRole);
      if (helpId) track.setAttribute('aria-describedby', helpId);
    } else {
      carousel.removeAttribute('aria-roledescription');
      track.removeAttribute('aria-describedby');
      track.scrollLeft = 0;
    }
    previous.setAttribute('aria-disabled', String(track.scrollLeft <= 1));
    next.setAttribute('aria-disabled', String(track.scrollLeft >= maximum - 1));
    const viewport = track.getBoundingClientRect();
    const visible = cards.map((card, index) => {
      const rect = card.getBoundingClientRect();
      const overlap = Math.min(rect.right, viewport.right) - Math.max(rect.left, viewport.left);
      return overlap >= rect.width / 2 ? index + 1 : null;
    }).filter(Boolean);
    if (visible.length) {
      const first = visible[0];
      const last = visible[visible.length - 1];
      const label = `${first === last ? first : `${first}–${last}`} ${counterJoin} ${cards.length}`;
      if (position.textContent !== label) position.textContent = label;
    }
  };

  const move = (direction) => {
    const button = direction < 0 ? previous : next;
    if (cards.length < 2 || button.getAttribute('aria-disabled') === 'true') return;
    const nextColumn = cards.find(card => card.offsetLeft > cards[0].offsetLeft + 1);
    if (!nextColumn) return;
    const step = nextColumn.offsetLeft - cards[0].offsetLeft;
    track.scrollBy({ left: direction * step, behavior: reducedMotion.matches ? 'auto' : 'smooth' });
  };
  previous.addEventListener('click', () => move(-1));
  next.addEventListener('click', () => move(1));
  track.addEventListener('keydown', event => {
    if (event.target !== track) return;
    if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
      event.preventDefault();
      move(event.key === 'ArrowLeft' ? -1 : 1);
    } else if (event.key === 'Home' || event.key === 'End') {
      event.preventDefault();
      track.scrollTo({ left: event.key === 'Home' ? 0 : track.scrollWidth, behavior: reducedMotion.matches ? 'auto' : 'smooth' });
    }
  });
  const scheduleUpdate = () => {
    clearTimeout(settleTimer);
    settleTimer = setTimeout(updateControls, 160);
  };
  track.addEventListener('scroll', scheduleUpdate, { passive: true });
  window.addEventListener('resize', scheduleUpdate);
  if ('ResizeObserver' in window) {
    const observer = new ResizeObserver(scheduleUpdate);
    observer.observe(track);
    cards.forEach(card => observer.observe(card));
  }
  updateControls();
});
