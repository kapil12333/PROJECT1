// Get references to the button and output div
const button = document.getElementById('clickMeButton');
const output = document.getElementById('output');

// Define the function to run when the button is clicked
function handleClick() {
    const currentTime = new Date().toLocaleTimeString();
    output.textContent = `Button clicked at ${currentTime}`;
}

// Add an event listener to the button
button.addEventListener('click', handleClick);
