function odosliText() {
    let napisanyText = document.getElementById("vstupnyText").value;

    if (napisanyText.trim() === "") {
        alert("Najprv niečo napíš do políčka!");
        return;
    }

    document.getElementById("nadpis").textContent = "Ahoj, " + napisanyText + "!";

    document.getElementById("vstupnyText").value = "";
}