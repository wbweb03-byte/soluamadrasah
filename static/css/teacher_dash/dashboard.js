const text = "WELCOME ADMIN!";

const title = document.getElementById("Htitle");

let index = 0;

function typeWriter() {

    if (index < text.length) {
        title.textContent += text.charAt(index);
        index++;
        setTimeout(typeWriter, 80);
    }

}

typeWriter();