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

// Recognise the secret code with hardware or mobile keyboards; leave other fields untouched.
(() => {
  const root = document.documentElement;
  const storageKey = 'paulo-redbull-mode';
  const portrait = document.querySelector('.portrait-photo');
  const originalPortrait = portrait?.getAttribute('src');
  const originalAlt = portrait?.getAttribute('alt');
  const themedPortrait = originalPortrait && new URL('paulo-portrait-redbull.webp', new URL(originalPortrait, document.baseURI)).href;
  const themeMeta = document.querySelector('meta[name="theme-color"]');
  const originalThemeColor = themeMeta?.getAttribute('content');
  const copy = root.lang === 'pt-BR' ? {
    enabled: 'Modo Red Bull. Digite redbull novamente ou pressione Esc para voltar.',
    disabled: 'Tema original restaurado.',
    portrait: 'Paulo Sanches segurando uma lata de Red Bull'
  } : root.lang === 'it' ? {
    enabled: 'Modalità Red Bull. Digita di nuovo redbull o premi Esc per tornare al tema originale.',
    disabled: 'Tema originale ripristinato.',
    portrait: 'Paulo Sanches con una lattina di Red Bull'
  } : {
    enabled: 'Red Bull mode. Type redbull again or press Esc to reset.',
    disabled: 'Original theme restored.',
    portrait: 'Paulo Sanches holding a Red Bull can'
  };
  let active = false;
  let buffer = '';
  let lastKeyTime = 0;
  let notice;
  let noticeTimer;

  const announce = text => {
    if (!notice) {
      notice = document.createElement('div');
      notice.className = 'easter-egg-notice';
      notice.setAttribute('role', 'status');
      notice.setAttribute('aria-live', 'polite');
      document.body.append(notice);
    }
    clearTimeout(noticeTimer);
    notice.hidden = false;
    notice.textContent = text;
    noticeTimer = setTimeout(() => { notice.hidden = true; }, 4000);
  };

  const setMode = (enabled, notify = true) => {
    active = enabled;
    if (active) root.dataset.theme = 'redbull';
    else delete root.dataset.theme;
    if (portrait) {
      portrait.src = active ? themedPortrait : originalPortrait;
      portrait.alt = active ? copy.portrait : originalAlt;
    }
    if (themeMeta) themeMeta.content = active ? '#001e3c' : originalThemeColor;
    try {
      if (active) sessionStorage.setItem(storageKey, 'on');
      else sessionStorage.removeItem(storageKey);
    } catch { /* The Easter egg also works when browser storage is unavailable. */ }
    if (notify) announce(active ? copy.enabled : copy.disabled);
  };

  try {
    if (sessionStorage.getItem(storageKey) === 'on') setMode(true, false);
  } catch { /* Storage is optional. */ }

  portrait?.addEventListener('error', () => {
    if (portrait.src === themedPortrait) {
      portrait.src = originalPortrait;
      portrait.alt = originalAlt;
    }
  });

  const keyboard = document.querySelector('.secret-keyboard');
  const keyboardToggle = keyboard?.querySelector('.secret-keyboard-toggle');
  const codeInput = keyboard?.querySelector('.secret-code-input');
  if (keyboardToggle && codeInput) {
    const closeKeyboard = (returnFocus = false) => {
      codeInput.hidden = true;
      codeInput.value = '';
      keyboardToggle.setAttribute('aria-expanded', 'false');
      if (returnFocus) keyboardToggle.focus({ preventScroll: true });
    };
    const checkCode = () => {
      if (!codeInput.value.trim().toLowerCase().endsWith('redbull')) return;
      buffer = '';
      setMode(!active);
      closeKeyboard(true);
    };
    keyboardToggle.addEventListener('click', () => {
      if (!codeInput.hidden) {
        closeKeyboard(true);
        return;
      }
      buffer = '';
      codeInput.hidden = false;
      keyboardToggle.setAttribute('aria-expanded', 'true');
      // Keep focus synchronous with the tap so iOS can open its software keyboard.
      codeInput.focus({ preventScroll: true });
    });
    codeInput.addEventListener('input', event => {
      if (!event.isComposing) checkCode();
    });
    codeInput.addEventListener('compositionend', checkCode);
    keyboard.addEventListener('focusout', event => {
      if (!keyboard.contains(event.relatedTarget)) closeKeyboard();
    });
    codeInput.addEventListener('keydown', event => {
      if (event.isComposing || (event.key !== 'Escape' && event.key !== 'Enter')) return;
      event.preventDefault();
      buffer = '';
      if (event.key === 'Escape' && active) setMode(false);
      closeKeyboard(true);
    });
    keyboard.hidden = false;
  }

  document.addEventListener('keydown', event => {
    const editable = event.composedPath().some(target => target instanceof Element && (
      target.isContentEditable || target.matches('input, textarea, select, [role="textbox"]')
    ));
    if (editable || event.ctrlKey || event.metaKey || event.altKey || event.isComposing || event.repeat) {
      buffer = '';
      return;
    }
    if (event.key === 'Escape') {
      buffer = '';
      if (active) setMode(false);
      return;
    }
    if (event.key === 'Shift' || event.key === 'CapsLock') return;
    if (event.key.length !== 1 || !/^[a-z]$/i.test(event.key)) {
      buffer = '';
      return;
    }
    const now = performance.now();
    if (now - lastKeyTime > 2000) buffer = '';
    lastKeyTime = now;
    buffer = (buffer + event.key.toLowerCase()).slice(-7);
    if (buffer === 'redbull') {
      buffer = '';
      setMode(!active);
    }
  });
  window.addEventListener('blur', () => { buffer = ''; });
})();
