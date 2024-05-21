const allButtons = document.querySelectorAll(".topic button");
const title = document.getElementById('topic-title');

allButtons.forEach(button => {
    button.addEventListener('click', () => {
        allButtons.forEach(btn => {
            btn.classList.remove('active');
        });
        button.classList.add('active');
        title.innerText = button.textContent + " courses";
    })
});

