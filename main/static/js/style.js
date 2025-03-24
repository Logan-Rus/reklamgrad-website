window.addEventListener('pageshow', function(event) {
    if (event.persisted || (window.performance && window.performance.navigation.type === 2)) {
        document.body.classList.remove('fade-out');
    }
});

const words = ["Надежность", "Качество", "Эффективность"];
let currentIndex = 0;
const changingWordElement = document.getElementById("changing-word");

function changeWord() {
    changingWordElement.style.opacity = 0;
    setTimeout(() => {
        currentIndex = (currentIndex + 1) % words.length;
        changingWordElement.textContent = words[currentIndex];
        changingWordElement.style.opacity = 1;
    }, 500);
}

setInterval(changeWord, 3000);

window.addEventListener('load', () => {
const loadingScreen = document.getElementById('loading-screen');
const content = document.getElementById('content');

// Начать анимацию затухания
loadingScreen.style.opacity = '0';

setTimeout(() => {
loadingScreen.classList.add('hidden'); // Полностью скрыть экран загрузки
content.style.display = 'block'; // Показать основной контент
}, 1000); // Время должно совпадать с длительностью анимации
});;

document.querySelector('form').addEventListener('submit', function(event) {
event.preventDefault();
const email = document.getElementById('email').value;
const message = document.getElementById('message').value;

if (!email || !message) {
alert('Пожалуйста, заполните все поля.');
return;
}
alert('Ваше сообщение успешно отправлено!');
});
