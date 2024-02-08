function suggestGift() {
    // Get values from the form
    var occasion = document.getElementById('occasion').value;
    var recipient = document.getElementById('recipient').value;
    var favoriteThing = document.getElementById('favoriteThing').value;
    var budget = document.getElementById('budget').value;

    // You can implement your logic here to suggest gifts based on the input

    // For now, displaying a simple message
    var suggestionsContainer = document.getElementById('giftSuggestions');
    suggestionsContainer.innerHTML = `<p>Based on your inputs, we suggest a thoughtful gift for ${recipient} on ${occasion} related to ${favoriteThing} within your budget of $${budget}.</p>`;
}

// Add an event listener to remove the fade-in class after the animation completes
document.getElementById('container').addEventListener('animationend', function() {
    document.getElementById('container').classList.remove('fade-in');
});