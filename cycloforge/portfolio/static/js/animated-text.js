document.addEventListener('DOMContentLoaded', function() {
    let texts = ["Back-end developer.", "Front-end developer.", "Fullstack developer.", "Python developer.", "JavaScript developer.", "Django developer.", "NodeJS developer.", "Electron developer.", "DevOps", "Michael Verbroekken."];

    // Function to shuffle the array
    function shuffle(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
    }

    shuffle(texts); // Shuffle the texts array

    let index = 0;
    let charIndex = 0;
    const typingSpeed = 50;
    const erasingSpeed = 10;
    const delayBetweenTexts = 2000;
    const delayForLastText = 90000; // 1.5 minutes
    const animatedTextElement = document.getElementById('animated-text');

    function type() {
        if (charIndex < texts[index].length) {
            animatedTextElement.textContent += texts[index].charAt(charIndex);
            charIndex++;
            setTimeout(type, typingSpeed);
        } else {
            if (texts[index] === "Michael Verbroekken.") {
                setTimeout(erase, delayForLastText);
            } else {
                setTimeout(erase, delayBetweenTexts);
            }
        }
    }

    function erase() {
        if (charIndex > 0) {
            animatedTextElement.textContent = texts[index].substring(0, charIndex - 1);
            charIndex--;
            setTimeout(erase, erasingSpeed);
        } else {
            index = (index + 1) % texts.length;
            setTimeout(type, typingSpeed);
        }
    }

    type();
});