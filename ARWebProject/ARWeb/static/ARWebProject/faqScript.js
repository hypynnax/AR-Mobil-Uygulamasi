const faqItems = document.querySelectorAll('.faq-item');
const itemsPerPage = 10;
let currentPage = 1;
let filteredItems = Array.from(faqItems);

function displayPage(page) {
    currentPage = page;
    const start = (page - 1) * itemsPerPage;
    const end = start + itemsPerPage;

    filteredItems.forEach((item, index) => {
        item.style.display = (index >= start && index < end) ? 'block' : 'none';
    });

    updatePagination();
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function updatePagination() {
    const totalPages = Math.ceil(filteredItems.length / itemsPerPage);
    const pagination = document.getElementById('pagination');
    pagination.innerHTML = '';

    for (let i = 1; i <= totalPages; i++) {
        const pageNumber = document.createElement('span');
        pageNumber.textContent = i;
        pageNumber.classList.add('page-number');
        if (i === currentPage) pageNumber.classList.add('active');
        pageNumber.onclick = () => displayPage(i);
        pagination.appendChild(pageNumber);
    }
}

function filterQuestions() {
    const query = document.querySelector('.search-box').value.toLowerCase();

    filteredItems = Array.from(faqItems).filter(item => {
        const question = item.querySelector('.faq-question').textContent.toLowerCase();
        const isMatch = question.includes(query);
        item.style.display = isMatch ? 'block' : 'none';
        return isMatch;
    });

    displayPage(1);
}

document.querySelectorAll('.faq-question').forEach(question => {
    question.addEventListener('click', () => {
        const answer = question.nextElementSibling;
        answer.classList.toggle('open');
        question.querySelector('span').textContent = answer.classList.contains('open') ? '-' : '+';
    });
});

displayPage(currentPage);
