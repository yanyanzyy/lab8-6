document.addEventListener("DOMContentLoaded", () => {
    const inputMessage = document.getElementById("inputMessage");
    const sendMessageButton = document.getElementById("sendMessageButton");
    const messagesContainer = document.getElementById("messages");

    // Function to send a message
    function sendMessage() {
        const messageText = inputMessage.value.trim();

        if (messageText) {
            // Create a new message element
            const newMessage = document.createElement("div");
            newMessage.classList.add("message", "to");

            const profileDiv = document.createElement("div");
            profileDiv.classList.add("profile");

            const img = document.createElement("img");
            img.src = "https://lh3.googleusercontent.com/a/ACg8ocK0_IEiBum5fdzAh439e_1u_1-aRonEW_MwD5ay17MbeZ9rlw=s64";
            profileDiv.appendChild(img);

            const contentDiv = document.createElement("div");
            contentDiv.classList.add("content");
            contentDiv.textContent = messageText;

            // Append profile and content to the message
            newMessage.appendChild(profileDiv);
            newMessage.appendChild(contentDiv);

            // Add the new message to the messages container
            messagesContainer.appendChild(newMessage);

            // Clear the input
            inputMessage.value = '';

            // Scroll to the bottom of the messages container
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }
    }

    // Send message on button click
    sendMessageButton.addEventListener("click", sendMessage);

    // Allow sending the message with the Enter key
    inputMessage.addEventListener("keypress", (event) => {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });

    // Handle button clicks for options
    document.querySelectorAll('.option-button').forEach(button => {
        button.addEventListener('click', () => {
            inputMessage.value = button.textContent; // Set the input message to the button text
            sendMessage(); // Send the message
        });
    });
});
