
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

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contactForm');
    const submitBtn = document.getElementById('submitBtn');
    const formMessage = document.getElementById('formMessage');

    if (!form) return;

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Показать состояние загрузки
        submitBtn.disabled = true;
        submitBtn.innerHTML = `
            <span class="spinner-border spinner-border-sm me-2"></span>
            Отправка...
        `;
        
        try {
            // Сбор данных формы
            const formData = new FormData(form);
            
            // Отправка на сервер
            const response = await fetch(form.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                    'Accept': 'application/json'
                }
            });

            const data = await response.json();
            
            if (!response.ok) {
                throw new Error(data.message || 'Ошибка сервера');
            }

            // Успешная отправка
            showMessage('success', '✔️ Сообщение успешно отправлено!');
            form.reset();
            
        } catch (error) {
            console.error('Ошибка:', error);
            showMessage('danger', `❌ ${error.message}`);
        } finally {
            // Восстановить кнопку
            submitBtn.disabled = false;
            submitBtn.textContent = 'Отправить';
        }
    });

    function showMessage(type, text) {
        formMessage.className = `mt-3 alert alert-${type}`;
        formMessage.textContent = text;
        formMessage.classList.remove('d-none');
        
        // Автоматическое скрытие через 5 сек
        setTimeout(() => {
            formMessage.classList.add('d-none');
        }, 5000);
    }
});

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

