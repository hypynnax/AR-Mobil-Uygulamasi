let language = document.getElementById('language-select').checked ? 'en' : 'tr';

document.getElementById('language-select').addEventListener('change', function () {
    const selectedLanguage = this.checked ? 'en' : 'tr';

    let url = '';
    if (selectedLanguage === 'tr') {
        url = '/tr';
    } else if (selectedLanguage === 'en') {
        url = '/en';
    }

    window.location.href = window.location.href.slice(0, -3) + url;
});

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById('sign-in').addEventListener('click', function () {
        window.location.href = "http://127.0.0.1:8000/login/" + language;
    });

    document.getElementById('sign-up').addEventListener('click', function () {
        window.location.href = "http://127.0.0.1:8000/register/" + language;
    });
});

function logout() {
    fetch("http://127.0.0.1:8000/logout/", {
        method: "GET",
    });
    location.reload();
}

function startDownload(lang, device) {
    const downloadUrl = "http://127.0.0.1:8000/download/" + lang + "/" + device;
    window.location.href = downloadUrl;
}

let text = "";

let i = 0;
const speed = 50;

window.onload = function () {
    const lastTwoChars = window.location.href.slice(-2);

    if (lastTwoChars === "tr") {
        text = "Dünyanın her yerinde çocuklar, dijital keşiflere çıkmaya hazır! Bilge Korkut, teknolojinin yeni sınırlarını AR yardımıyla keşfetmeye odaklanıyor.Her seviyede, çocuklar birer maceraperest olarak farklı bilişim zorluklarını aşacak, kodlama bilmecelerini çözecek ve kendi dijital projelerini inşa edecekler.Her başarı onları daha büyük bir teknoloji kahramanı yaparken,dünyaya katkıda bulunmaya bir adım daha yaklaşıyorlar.Bilge Korkut, teknoloji yolculuğunda lider olmayı hedefleyen çocuklar için dijital bir macera dünyası...";
    } else if (lastTwoChars === "en") {
        text = "Children around the world are ready to embark on digital discoveries! Korkut the Wise focuses on exploring the new frontiers of technology with the help of AR.At each level, children will become adventurers, overcoming different computing challenges, solving coding riddles and building their own digital projects.As each success makes them a bigger tech hero, they are one step closer to contributing to the world.Korkut the Wise, a leader in the technology journey a world of digital adventure for children who aspire to be...";
    }

    typeWriter();
};

function typeWriter() {
    const typewriterElement = document.getElementById("typewriter");

    if (i < text.length) {
        typewriterElement.innerHTML += text.charAt(i);
        i++;
        setTimeout(typeWriter, speed);
    } else {
        typewriterElement.innerHTML += '<span></span>';
    }
}
