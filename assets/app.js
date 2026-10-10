'use strict';
const buttons = [...document.querySelectorAll('[data-filter]')];
const cards = [...document.querySelectorAll('[data-category]')];
buttons.forEach(button => {
  button.addEventListener('click', () => {
    const filter = button.dataset.filter;
    buttons.forEach(item => {
      const selected = item === button;
      item.classList.toggle('active', selected);
      item.setAttribute('aria-pressed', String(selected));
    });
    let visible = 0;
    cards.forEach(card => {
      card.hidden = filter !== 'all' && !card.dataset.category.split(' ').includes(filter);
      if (!card.hidden) visible++;
    });
    document.getElementById('filter-status').textContent = `${visible} projetos apresentados`;
  });
});
document.getElementById('year').textContent = new Date().getFullYear();
