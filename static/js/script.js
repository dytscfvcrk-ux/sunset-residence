
const menuToggle = document.getElementById("menuToggle");
const mainNav = document.getElementById("mainNav");

if (menuToggle && mainNav) {
    menuToggle.addEventListener("click", () => {
        mainNav.classList.toggle("active");
    });
}

const contactForm = document.getElementById("contactForm");
const formMessage = document.getElementById("formMessage");

if (contactForm && formMessage) {
    contactForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const submitButton = contactForm.querySelector("button[type='submit']");

        submitButton.disabled = true;
        submitButton.textContent = "ОТПРАВКА...";

        formMessage.className = "form-message";
        formMessage.textContent = "";

        try {
            const response = await fetch("/send-message", {
                method: "POST",
                body: new FormData(contactForm)
            });

            const result = await response.json();

            if (!response.ok) {
                throw new Error(result.error || "Не удалось отправить заявку.");
            }

            contactForm.reset();
            formMessage.textContent = "Спасибо! Ваша заявка успешно принята.";
            formMessage.className = "form-message show";

        } catch (error) {
            formMessage.textContent = error.message || "Ошибка отправки. Попробуйте ещё раз.";
            formMessage.className = "form-message show error";

        } finally {
            submitButton.disabled = false;
            submitButton.textContent = "ОТПРАВИТЬ ЗАЯВКУ ↗";
        }
    });
}
