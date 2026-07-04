const menuItems = document.querySelectorAll('.menu-item');
const pages = document.querySelectorAll('.page');
const pageTitle = document.getElementById('pageTitle');
const sidebar = document.querySelector('.sidebar');
const mobileMenu = document.getElementById('mobileMenu');
const modalButtons = document.querySelectorAll('[data-modal]');
const closeModalButtons = document.querySelectorAll('.close-modal');

const titles = {
  dashboard: 'Dashboard',
  produtos: 'Produtos',
  clientes: 'Clientes',
  pedidos: 'Pedidos de Venda'
};

menuItems.forEach((item) => {
  item.addEventListener('click', () => {
    const pageId = item.dataset.page;

    menuItems.forEach((button) => button.classList.remove('active'));
    pages.forEach((page) => page.classList.remove('active'));

    item.classList.add('active');
    document.getElementById(pageId).classList.add('active');
    pageTitle.textContent = titles[pageId];

    sidebar.classList.remove('open');
  });
});

mobileMenu.addEventListener('click', () => {
  sidebar.classList.toggle('open');
});

modalButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const modalId = button.dataset.modal;
    document.getElementById(modalId).classList.add('active');
  });
});

closeModalButtons.forEach((button) => {
  button.addEventListener('click', () => {
    button.closest('.modal').classList.remove('active');
  });
});

window.addEventListener('click', (event) => {
  if (event.target.classList.contains('modal')) {
    event.target.classList.remove('active');
  }
});
