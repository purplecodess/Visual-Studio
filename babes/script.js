function showAnswers(event) {
    event.preventDefault(); // Prevent form submission

    // Get form values
    var memory = document.getElementById("memory").value;
    var destination = document.getElementById("destination").value;
    var gift = document.getElementById("gift").value;
    var met = document.getElementById("met").value;
    var date = document.getElementById("date").value;
    var dream = document.getElementById("dream").value;

    // Display the answers in a new section
    document.getElementById("answers").innerHTML = `
        <h2>Your Responses:</h2>
        <p><strong>Favorite Memory Together:</strong> ${memory}</p>
        <p><strong>Dream Destination:</strong> ${destination}</p>
        <p><strong>Favorite Gift:</strong> ${gift}</p>
        <p><strong>How We Met:</strong> ${met}</p>
        <p><strong>Favorite Date Activity:</strong> ${date}</p>
        <p><strong>Future Dream:</strong> ${dream}</p>
    `;
}
