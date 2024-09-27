// Select the necessary elements
const inputMessage = document.getElementById('inputMessage');
const sendMessageButton = document.getElementById('sendMessageButton');
const messagesContainer = document.getElementById('messages');

// Function to add a new message bubble
function addMessage() {
    // Get the text from the input field
    const messageText = inputMessage.value.trim();

    // Proceed only if the input is not empty
    if (messageText !== "") {
        // Create a new message div
        const newMessage = document.createElement('div');
        newMessage.classList.add('message', 'to'); // 'to' means it's the user's message
        
        // Create the profile image div
        const profileDiv = document.createElement('div');
        profileDiv.classList.add('profile');
        
        const profileImg = document.createElement('img');
        profileImg.src = "https://lh3.googleusercontent.com/a/ACg8ocK0_IEiBum5fdzAh439e_1u_1-aRonEW_MwD5ay17MbeZ9rlw=s64";
        profileImg.alt = "User Profile";
        
        profileDiv.appendChild(profileImg);
        
        // Create the content div
        const contentDiv = document.createElement('div');
        contentDiv.classList.add('content');
        contentDiv.textContent = messageText;

        // Append profile and content to the new message
        newMessage.appendChild(profileDiv);
        newMessage.appendChild(contentDiv);

        // Append the new message to the messages container
        messagesContainer.appendChild(newMessage);

        // Scroll to the bottom of the messages container
        messagesContainer.scrollTop = messagesContainer.scrollHeight;

        // Clear the input field after sending the message
        inputMessage.value = '';
    }
}

// Add event listener to the button
sendMessageButton.addEventListener('click', addMessage);

// Optionally, send the message when the user presses Enter
inputMessage.addEventListener('keypress', function (event) {
    if (event.key === 'Enter') {
        addMessage();
    }
});
hh