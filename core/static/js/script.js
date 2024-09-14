// Seleciona o botão de toggle do menu e a lista de links de navegação
const menuToggle = document.querySelector(".menu-toggle");
const navLinks = document.querySelector(".nav-links");

// Adiciona um event listener para o clique no botão de toggle
menuToggle.addEventListener("click", () => {
  // Alterna a classe 'active' na lista de links de navegação e no botão de toggle
  navLinks.classList.toggle("active");
  menuToggle.classList.toggle("active");
});

// Adiciona animação de entrada para os itens do menu
const menuItems = document.querySelectorAll('.menu-item');
menuItems.forEach((item, index) => {
  item.style.animationDelay = `${index * 0.1}s`;
  item.classList.add('animate__animated', 'animate__fadeInUp');
});

// Adiciona efeito de parallax na seção hero
window.addEventListener('scroll', () => {
  const heroSection = document.querySelector('.hero-section');
  const scrollPosition = window.pageYOffset;
  heroSection.style.backgroundPositionY = `${scrollPosition * 0.5}px`;
});

// Adiciona contador de itens no carrinho (exemplo)
let cartCount = 0;
const cartCountElement = document.createElement('span');
cartCountElement.classList.add('cart-count');
document.querySelector('header').appendChild(cartCountElement);

document.querySelectorAll('.cta-button').forEach(button => {
  button.addEventListener('click', (e) => {
    e.preventDefault();
    cartCount++;
    cartCountElement.textContent = cartCount;
    cartCountElement.classList.add('animate__animated', 'animate__rubberBand');
    setTimeout(() => {
      cartCountElement.classList.remove('animate__rubberBand');
    }, 1000);
  });
});

// Adiciona rolagem suave para links internos
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();

    document.querySelector(this.getAttribute('href')).scrollIntoView({
      behavior: 'smooth'
    });
  });
});

// Adiciona funcionalidade ao botão de toggle do menu mobile
const navbarToggler = document.querySelector('.navbar-toggler');
const navbarCollapse = document.querySelector('.navbar-collapse');

navbarToggler.addEventListener('click', () => {
  navbarCollapse.classList.toggle('show');
});

// Adicione esta função para rolagem suave
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();

    document.querySelector(this.getAttribute('href')).scrollIntoView({
      behavior: 'smooth'
    });
  });
});

// Adicione funcionalidades JavaScript personalizadas aqui

// Funcionalidade do acordeão para a página de Política de Privacidade
document.addEventListener('DOMContentLoaded', function() {
    const accordionItems = document.querySelectorAll('.accordion-item');
    
    accordionItems.forEach(item => {
        const header = item.querySelector('h3');
        const content = item.querySelector('.accordion-content');
        
        header.addEventListener('click', () => {
            // Fecha todos os outros itens
            accordionItems.forEach(otherItem => {
                if (otherItem !== item) {
                    otherItem.querySelector('.accordion-content').style.display = 'none';
                    otherItem.querySelector('h3').classList.remove('active');
                }
            });
            
            // Alterna o estado do item clicado
            content.style.display = content.style.display === 'block' ? 'none' : 'block';
            header.classList.toggle('active');
        });
    });
});

// Código existente...
