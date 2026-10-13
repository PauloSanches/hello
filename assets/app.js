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
  const storageKey = 'paulo-easter-egg-mode';
  const legacyStorageKey = 'paulo-redbull-mode';
  const portrait = document.querySelector('.portrait-photo');
  const originalPortrait = portrait?.getAttribute('src');
  const originalAlt = portrait?.getAttribute('alt');
  const introduction = document.querySelector('.hero-introduction');
  const themeLine = document.querySelector('.hero-theme-line');
  const originalThemeLine = themeLine?.textContent;
  const themeSeparator = introduction?.textContent.trim().endsWith('.') ? ' ' : '. ';
  const portraitURL = file => originalPortrait && new URL(file, new URL(originalPortrait, document.baseURI)).href;
  const themeMeta = document.querySelector('meta[name="theme-color"]');
  const originalThemeColor = themeMeta?.getAttribute('content');
  const resetButtons = Array.from(document.querySelectorAll('.theme-reset'));
  const locale = root.lang === 'pt-BR' ? 'pt' : root.lang === 'it' ? 'it' : 'en';
  const originalNotice = {
    pt: 'Tema original restaurado.',
    it: 'Tema originale ripristinato.',
    en: 'Original theme restored.'
  };
  const modes = {
    redbull: {
      portrait: 'paulo-portrait-redbull.webp',
      colour: '#001e3c',
      phrase: 'It’s time to fly.',
      notice: {
        pt: 'Modo Red Bull. Digite redbull novamente ou pressione Esc para voltar.',
        it: 'Modalità Red Bull. Digita di nuovo redbull o premi Esc per tornare al tema originale.',
        en: 'Red Bull mode. Type redbull again or press Esc to reset.'
      },
      alt: {
        pt: 'Paulo Sanches segurando uma lata de Red Bull',
        it: 'Paulo Sanches con una lattina di Red Bull',
        en: 'Paulo Sanches holding a Red Bull can'
      }
    },
    gameday: {
      portrait: 'paulo-portrait-gameday.webp',
      colour: '#002244',
      phrase: 'Every day is game day.',
      notice: {
        pt: 'Modo GameDay. Digite gameday novamente ou pressione Esc para voltar.',
        it: 'Modalità GameDay. Digita di nuovo gameday o premi Esc per tornare al tema originale.',
        en: 'GameDay mode. Type gameday again or press Esc to reset.'
      },
      alt: {
        pt: 'Paulo Sanches segurando um capacete do Seattle Seahawks',
        it: 'Paulo Sanches con un casco dei Seattle Seahawks',
        en: 'Paulo Sanches holding a Seattle Seahawks helmet'
      }
    },
    dante: {
      portrait: 'paulo-portrait-dante.webp?v=f317aa6099ec',
      colour: '#111111',
      phrase: '& Dante Saggin - Enterprise Architect & FDE',
      separator: ' ',
      notice: {
        pt: 'Modo Dante. Digite dante novamente ou pressione Esc para voltar.',
        it: 'Modalità Dante. Digita di nuovo dante o premi Esc per tornare al tema originale.',
        en: 'Dante mode. Type dante again or press Esc to reset.'
      },
      alt: {
        pt: 'Paulo Sanches e Dante juntos',
        it: 'Paulo Sanches e Dante insieme',
        en: 'Paulo Sanches and Dante together'
      }
    },
    tubarao: {
      portrait: 'portrait-tubarao.webp?v=6fa8adedebf5',
      colour: '#111111',
      phrase: 'Vai TUBARÃO, vai TUBARÃO…',
      phraseLanguage: 'pt-BR',
      notice: {
        pt: 'Modo Tubarão. Digite tubarao novamente ou pressione Esc para voltar.',
        it: 'Modalità Tubarão. Digita di nuovo tubarao o premi Esc per tornare al tema originale.',
        en: 'Tubarão mode. Type tubarao again or press Esc to reset.'
      },
      alt: {
        pt: 'Criança com óculos de sol brancos e camiseta do Sonic, fazendo gestos com as mãos',
        it: 'Bambino con occhiali da sole bianchi e una maglietta di Sonic, mentre fa gesti con le mani',
        en: 'Child wearing white sunglasses and a Sonic T-shirt, making playful hand gestures'
      }
    },
    vietnam: {
      portrait: 'paulo-portrait-vietnam.webp?v=5895a8439be6',
      colour: '#283222',
      phrase: 'GOOOOD MOOORNING…',
      notice: {
        pt: 'Good Morning, Vietnam! Digite goodmorning novamente ou pressione Esc para voltar.',
        it: 'Good Morning, Vietnam! Digita di nuovo goodmorning o premi Esc per tornare al tema originale.',
        en: 'Good Morning, Vietnam! Type goodmorning again or press Esc to reset.'
      },
      alt: {
        pt: 'Paulo Sanches com sua camisa branca, segurando um microfone de rádio retrô',
        it: 'Paulo Sanches con la sua camicia bianca, mentre tiene un microfono radiofonico vintage',
        en: 'Paulo Sanches in his white shirt, holding a vintage radio microphone'
      }
    }
  };
  const codes = Object.keys(modes);
  const compactCodes = new Set(['redbull', 'gameday', 'goodmorning', 'vietnam', 'nfl', 'dante', 'tubarao', 'tubarão']);
  const aliases = new Map([
    ['redbull', 'redbull'], ['itstimetofly', 'redbull'],
    ['gameday', 'gameday'], ['nfl', 'gameday'],
    ['everydayisgameday', 'gameday'], ['everydayisgamedayletsgo', 'gameday'],
    ['vietnam', 'vietnam'], ['goodmorning', 'vietnam'], ['goodmorningvietnam', 'vietnam'],
    ['dante', 'dante'], ['tubarao', 'tubarao']
  ]);
  const orderedAliases = Array.from(aliases.keys()).sort((a, b) => b.length - a.length);
  const maximumCodeLength = orderedAliases[0].length;
  const normalizeCode = value => value.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[^a-z]/g, '')
    .replace(/go{2,}d/g, 'good').replace(/mo+rning/g, 'morning');
  const matchCode = value => {
    const compact = normalizeCode(value);
    const alias = orderedAliases.find(candidate => compact.endsWith(candidate));
    return alias ? { alias, mode: aliases.get(alias) } : null;
  };
  let active = '';
  let buffer = '';
  let lastKeyTime = 0;
  let previousAlias = '';
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

  const setMode = (mode, notify = true) => {
    active = mode;
    const theme = active && modes[active];
    if (active) root.dataset.theme = active;
    else delete root.dataset.theme;
    resetButtons.forEach(button => { button.hidden = !active; });
    if (portrait) {
      portrait.src = theme ? portraitURL(theme.portrait) : originalPortrait;
      portrait.alt = theme ? theme.alt[locale] : originalAlt;
    }
    if (themeLine) {
      if (theme?.phrase) {
        const phrase = document.createElement('span');
        phrase.lang = theme.phraseLanguage ?? 'en';
        phrase.textContent = theme.phrase;
        themeLine.replaceChildren(theme.separator ?? themeSeparator, phrase);
      } else {
        themeLine.textContent = originalThemeLine;
      }
    }
    if (themeMeta) themeMeta.content = theme ? theme.colour : originalThemeColor;
    try {
      if (active) sessionStorage.setItem(storageKey, active);
      else sessionStorage.removeItem(storageKey);
      sessionStorage.removeItem(legacyStorageKey);
    } catch { /* The Easter egg also works when browser storage is unavailable. */ }
    if (notify) announce(theme ? theme.notice[locale] : originalNotice[locale]);
  };
  const toggleMode = code => setMode(active === code ? '' : code);
  const clearSequence = () => {
    buffer = '';
    lastKeyTime = 0;
    previousAlias = '';
  };
  const recognizeCode = match => {
    // A longer greeting can complete a phrase that already activated the same mode.
    const continuation = active === match.mode && previousAlias &&
      match.alias.length > previousAlias.length && match.alias.startsWith(previousAlias);
    if (!continuation) toggleMode(match.mode);
    previousAlias = match.alias;
  };

  try {
    const saved = sessionStorage.getItem(storageKey);
    if (codes.includes(saved)) setMode(saved, false);
    else if (sessionStorage.getItem(legacyStorageKey) === 'on') setMode('redbull', false);
  } catch { /* Storage is optional. */ }

  portrait?.addEventListener('error', () => {
    if (active && portrait.src === portraitURL(modes[active].portrait)) {
      portrait.src = originalPortrait;
      portrait.alt = originalAlt;
    }
  });

  const keyboard = document.querySelector('.secret-keyboard');
  const keyboardToggle = keyboard?.querySelector('.secret-keyboard-toggle');
  const codeInput = keyboard?.querySelector('.secret-code-input');
  const keyboardPanel = keyboard?.querySelector('.secret-keyboard-panel');
  if (keyboardToggle && codeInput && keyboardPanel) {
    let lastInputValue = '';
    const closeKeyboard = (returnFocus = false) => {
      keyboardPanel.hidden = true;
      codeInput.value = '';
      lastInputValue = '';
      keyboardToggle.setAttribute('aria-expanded', 'false');
      if (returnFocus) keyboardToggle.focus({ preventScroll: true });
    };
    const checkCode = () => {
      const raw = codeInput.value.trim().toLowerCase();
      const compact = normalizeCode(raw);
      if (compact === lastInputValue) return;
      lastInputValue = compact;
      const match = matchCode(compact);
      if (!match) return;
      buffer = compact.slice(-maximumCodeLength);
      lastKeyTime = performance.now();
      recognizeCode(match);
      // Keep a phrase in the field until Done, so the rest can be typed safely.
      if (compactCodes.has(raw)) closeKeyboard(true);
    };
    keyboardToggle.addEventListener('click', () => {
      if (!keyboardPanel.hidden) {
        closeKeyboard(true);
        return;
      }
      clearSequence();
      keyboardPanel.hidden = false;
      keyboardToggle.setAttribute('aria-expanded', 'true');
      // Keep focus synchronous with the tap so iOS can open its software keyboard.
      codeInput.focus({ preventScroll: true });
    });
    codeInput.addEventListener('input', event => {
      if (!event.isComposing) checkCode();
    });
    codeInput.addEventListener('compositionend', checkCode);
    resetButtons.forEach(button => button.addEventListener('click', () => {
      clearSequence();
      setMode('');
      closeKeyboard(true);
    }));
    // Safari can blur the input with no relatedTarget before a button receives its click.
    // Dismiss only when a pointer or focus actually moves outside the controls.
    document.addEventListener('pointerdown', event => {
      if (!keyboardPanel.hidden && !keyboard.contains(event.target)) closeKeyboard();
    });
    document.addEventListener('focusin', event => {
      if (!keyboardPanel.hidden && !keyboard.contains(event.target)) closeKeyboard();
    });
    codeInput.addEventListener('keydown', event => {
      if (event.isComposing || (event.key !== 'Escape' && event.key !== 'Enter')) return;
      event.preventDefault();
      clearSequence();
      if (event.key === 'Escape' && active) setMode('');
      closeKeyboard(true);
    });
    keyboard.hidden = false;
  }

  document.addEventListener('keydown', event => {
    const editable = event.composedPath().some(target => target instanceof Element && (
      target.isContentEditable || target.matches('input, textarea, select, [role="textbox"]')
    ));
    if (editable) {
      if (event.target !== codeInput) clearSequence();
      return;
    }
    if (event.ctrlKey || event.metaKey || event.altKey || event.isComposing || event.repeat) {
      clearSequence();
      return;
    }
    if (event.key === 'Escape') {
      clearSequence();
      if (active) setMode('');
      return;
    }
    if (event.key === 'Shift' || event.key === 'CapsLock') return;
    if (event.key.length !== 1 || !/^[a-z]$/i.test(normalizeCode(event.key))) {
      if (/^[\s’'.,!?…-]$/.test(event.key)) return;
      clearSequence();
      return;
    }
    const now = performance.now();
    if (now - lastKeyTime > 2000) clearSequence();
    lastKeyTime = now;
    buffer = normalizeCode(buffer + event.key).slice(-maximumCodeLength);
    const match = matchCode(buffer);
    if (match) recognizeCode(match);
  });
  window.addEventListener('blur', clearSequence);
})();
