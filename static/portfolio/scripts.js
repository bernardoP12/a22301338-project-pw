function formatTime(time) {
    return time < 10 ? `0${time}` : time;
}

function updateClock() {
    const agora = new Date();
    const horas = agora.getHours();
    const minutos = agora.getMinutes();
    const segundos = agora.getSeconds();
    const tempoFormatado = `${formatTime(horas)}:${formatTime(minutos)}:${formatTime(segundos)}`;
    document.getElementById('contador').innerText = tempoFormatado;
}

setInterval(updateClock, 1000);
updateClock();

var backgrounds = [
    "url('/media/portfolio/background.jpg')",
    "url('https://img.freepik.com/fotos-gratis/fundo-abstrato-escuro_1048-1920.jpg?size=338&ext=jpg&ga=GA1.1.2116175301.1717718400&semt=ais_user')"
];

document.getElementById('dark-mode').addEventListener('click', function() {
    if (this.dataset.mode === "OFF") {
        this.dataset.mode = "ON";
        document.body.style.backgroundImage = backgrounds[1]; // Modo ON (dark mode)
        this.classList.remove('fa-moon');
        this.classList.add('fa-sun');
    } else {
        this.dataset.mode = "OFF";
        document.body.style.backgroundImage = backgrounds[0]; // Modo OFF (light mode)
        this.classList.remove('fa-sun');
        this.classList.add('fa-moon');
    }
});