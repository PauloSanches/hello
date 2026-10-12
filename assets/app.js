'use strict';
const year = document.getElementById('year');
if (year) year.textContent = String(new Date().getFullYear());

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
  let settleTimer;

  const updateControls = () => {
    const maximum = track.scrollWidth - track.clientWidth;
    const scrollable = maximum > 1;
    buttons.hidden = !scrollable;
    hint.hidden = !scrollable;
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
      const label = `${first === last ? first : `${first}–${last}`} of ${cards.length}`;
      if (position.textContent !== label) position.textContent = label;
    }
  };

  const move = (direction) => {
    const button = direction < 0 ? previous : next;
    if (cards.length < 2 || button.getAttribute('aria-disabled') === 'true') return;
    const step = cards[1].offsetLeft - cards[0].offsetLeft;
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
  controls.hidden = false;
  updateControls();
});


document.querySelectorAll('[data-story-card]').forEach(card => {
  const front = card.querySelector('.story-front');
  const back = card.querySelector('.story-back');
  const content = card.querySelector('.story-content');
  const open = card.querySelector('.story-open');
  const close = card.querySelector('.story-close');
  const scrollHint = card.querySelector('.story-scroll-hint');
  if (!front || !back || !content || !open || !close) return;

  const updateScrollHint = () => {
    if (!scrollHint) return;
    const scrollable = content.scrollHeight > content.clientHeight + 1;
    const atBottom = content.scrollTop + content.clientHeight >= content.scrollHeight - 2;
    scrollHint.hidden = !scrollable || atBottom;
  };

  const showSide = (showBack) => {
    card.classList.toggle('is-flipped', showBack);
    front.inert = showBack;
    back.inert = !showBack;
    front.setAttribute('aria-hidden', String(showBack));
    back.setAttribute('aria-hidden', String(!showBack));
    open.setAttribute('aria-expanded', String(showBack));
    if (showBack) {
      content.scrollTop = 0;
      updateScrollHint();
      content.focus({ preventScroll: true });
    } else {
      open.focus({ preventScroll: true });
    }
  };

  back.inert = true;
  back.setAttribute('aria-hidden', 'true');
  content.tabIndex = 0;
  card.classList.add('story-enhanced');
  open.hidden = false;
  close.hidden = false;
  open.addEventListener('click', () => showSide(true));
  close.addEventListener('click', () => showSide(false));
  content.addEventListener('scroll', updateScrollHint, { passive: true });
  window.addEventListener('resize', updateScrollHint);
  if ('ResizeObserver' in window) {
    new ResizeObserver(updateScrollHint).observe(content);
  }
  front.addEventListener('click', event => {
    if (event.target.closest('button, a, input, select, textarea, summary')) return;
    if (String(window.getSelection()).trim()) return;
    showSide(true);
  });
  card.addEventListener('keydown', event => {
    if (event.key === 'Escape' && card.classList.contains('is-flipped')) {
      event.preventDefault();
      showSide(false);
    }
  });
});
