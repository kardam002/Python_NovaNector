document.addEventListener('DOMContentLoaded', function () {
    const output = document.getElementById('output');
    const commandInput = document.getElementById('commandInput');
    const submitBtn = document.getElementById('submitBtn');

    submitBtn.addEventListener('click', function () {
        const command = commandInput.value;
        fetch('/command', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ command: command })
        })
        .then(response => response.json())
        .then(data => {
            output.innerHTML += `<p>${data.response}</p>`;
            commandInput.value = '';
        });
    });

    // Start the game on page load
    fetch('/start', { method: 'POST' });
});
