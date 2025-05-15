document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                const navbarHeight = document.querySelector('.navbar').offsetHeight;
                let additionalOffset = 0;
                
                // Специальная корректировка для секции services
                if (targetId === '#services') {
                    additionalOffset = -navbarHeight;
                }
                // Для секции about
                else if (targetId === '#about') {
                    additionalOffset = -navbarHeight - 5; // Уменьшаем смещение до -5px для поднятия секции выше
                }
                // Для секции contact
                else if (targetId === '#contact') {
                    additionalOffset = -70; // Уменьшаем смещение до -70px (было -60px)
                }
                
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset + additionalOffset;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Анимация появления элементов при скролле
    const animateOnScroll = function() {
        const elements = document.querySelectorAll('.card, .section-title');
        elements.forEach(element => {
            const elementPosition = element.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            if (elementPosition < windowHeight - 100) {
                element.classList.add('animate__animated', 'animate__fadeInUp');
            }
        });
    };

    window.addEventListener('scroll', animateOnScroll);
    animateOnScroll(); // Вызываем при загрузке страницы

    // Scroll to top button functionality
    const scrollToTopButton = document.getElementById('scrollToTop');

    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            scrollToTopButton.style.display = 'flex';
        } else {
            scrollToTopButton.style.display = 'none';
        }
    });

    scrollToTopButton.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
});

function previewImages(input) {
    const preview = document.getElementById('imagePreview');
    
    if (input.files) {
        Array.from(input.files).forEach((file, index) => {
            const reader = new FileReader();
            reader.onload = function(e) {
                const col = document.createElement('div');
                col.className = 'col-md-3';
                
                const card = document.createElement('div');
                card.className = 'card h-100';
                
                const img = document.createElement('img');
                img.src = e.target.result;
                img.className = 'card-img-top';
                img.style.height = '150px';
                img.style.objectFit = 'cover';
                
                const cardBody = document.createElement('div');
                cardBody.className = 'card-body p-2';
                
                const deleteBtn = document.createElement('button');
                deleteBtn.className = 'btn btn-danger btn-sm w-100';
                deleteBtn.innerHTML = 'Löschen';
                deleteBtn.onclick = function() {
                    // Создаем новый FileList без удаленного файла
                    const dt = new DataTransfer();
                    const files = input.files;
                    
                    for (let i = 0; i < files.length; i++) {
                        if (i !== index) {
                            dt.items.add(files[i]);
                        }
                    }
                    
                    input.files = dt.files;
                    col.remove(); // Удаляем превью
                };
                
                cardBody.appendChild(deleteBtn);
                card.appendChild(img);
                card.appendChild(cardBody);
                col.appendChild(card);
                preview.appendChild(col);
            };
            reader.readAsDataURL(file);
        });
    }
} 