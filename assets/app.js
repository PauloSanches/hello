'use strict';
const year = document.getElementById('year');
if (year) year.textContent = String(new Date().getFullYear());

const certificationTrack = document.getElementById('certification-track');
if (certificationTrack) {
  const carousel = certificationTrack.closest('.certification-carousel');
  const controls = carousel.querySelector('.certification-controls');
  const previous = controls.querySelector('.certification-previous');
  const next = controls.querySelector('.certification-next');
  const position = controls.querySelector('.certification-position');
  const cards = Array.from(certificationTrack.children);
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let settleTimer;

  const updateControls = () => {
    const maximum = certificationTrack.scrollWidth - certificationTrack.clientWidth;
    previous.setAttribute('aria-disabled', String(certificationTrack.scrollLeft <= 1));
    next.setAttribute('aria-disabled', String(certificationTrack.scrollLeft >= maximum - 1));
    const viewport = certificationTrack.getBoundingClientRect();
    const visible = cards.map((card, index) => {
      const rect = card.getBoundingClientRect();
      const overlap = Math.min(rect.right, viewport.right) - Math.max(rect.left, viewport.left);
      return overlap >= rect.width / 2 ? index + 1 : null;
    }).filter(Boolean);
    if (visible.length) {
      const first = visible[0];
      const last = visible[visible.length - 1];
      const label = `${first === last ? first : `${first}–${last}`} of ${cards.length}`;
      if (position.textContent !== label) position.textContent = label;
    }
  };

  const move = (direction) => {
    const button = direction < 0 ? previous : next;
    if (button.getAttribute('aria-disabled') === 'true') return;
    const step = cards[1].offsetLeft - cards[0].offsetLeft;
    certificationTrack.scrollBy({ left: direction * step, behavior: reducedMotion.matches ? 'auto' : 'smooth' });
  };
  previous.addEventListener('click', () => move(-1));
  next.addEventListener('click', () => move(1));
  certificationTrack.addEventListener('keydown', event => {
    if (event.target !== certificationTrack) return;
    if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
      event.preventDefault();
      move(event.key === 'ArrowLeft' ? -1 : 1);
    } else if (event.key === 'Home' || event.key === 'End') {
      event.preventDefault();
      certificationTrack.scrollTo({ left: event.key === 'Home' ? 0 : certificationTrack.scrollWidth, behavior: reducedMotion.matches ? 'auto' : 'smooth' });
    }
  });
  const scheduleUpdate = () => {
    clearTimeout(settleTimer);
    settleTimer = setTimeout(updateControls, 160);
  };
  certificationTrack.addEventListener('scroll', scheduleUpdate, { passive: true });
  window.addEventListener('resize', scheduleUpdate);
  controls.hidden = false;
  updateControls();
}
