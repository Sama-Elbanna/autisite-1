// JavaScript to collect data and send it to the localhost server

// Select the checkboxes and add an event listener to a button (if needed)
document.addEventListener("DOMContentLoaded", () => {
    const checkboxes = document.querySelectorAll("input[type='checkbox']");

    // Create a button to send the data
    const sendButton = document.createElement("button");
    sendButton.textContent = "Submit Symptoms";
    sendButton.style.marginTop = "20px";
    document.body.appendChild(sendButton);

    // Add click event to send data
    sendButton.addEventListener("click", () => {
        const symptoms = [];

        // Loop through checkboxes to find checked ones
        checkboxes.forEach((checkbox, index) => {
            if (checkbox.checked) {
                symptoms.push(checkbox.nextSibling.textContent.trim());
            }
        });

        // Send the data to the server
        fetch("http://localhost:3000/symptoms", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ symptoms })
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error("Failed to send data to the server.");
            }
        })
        .then(data => {
            console.log("Server response:", data);
            alert("Symptoms submitted successfully!");
        })
        .catch(error => {
            console.error("Error:", error);
            alert("There was an error submitting the symptoms.");
        });
    });
});
