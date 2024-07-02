let slideIndex = 0;
const slides = document.querySelectorAll('.slides img');
const totalSlides = slides.length;

function showSlides() {
  slides.forEach(slide => slide.style.display = 'none');
  slides[slideIndex].style.display = 'block';
}

function nextSlide() {
  slideIndex++;
  if (slideIndex >= totalSlides) {
    slideIndex = 0;
  }
  showSlides();
}

function prevSlide() {
  slideIndex--;
  if (slideIndex < 0) {
    slideIndex = totalSlides - 1;
  }
  showSlides();
}

showSlides();
setInterval(nextSlide, 3000); // Cambia la imagen cada 3 segundos
