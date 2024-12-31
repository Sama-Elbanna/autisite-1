const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs'); // For file system operations (saving to file)
const path = require('path');

const app = express();
const port = 5000;

app.use(bodyParser.json());

// Define the path to your data file (adjust as needed)
const dataFilePath = path.join(__dirname, 'registrations.json');

// Function to read existing data from the file
function readDataFromFile() {
    try {
        const data = fs.readFileSync(dataFilePath, 'utf8');
        return JSON.parse(data);
    } catch (error) {
        // If the file doesn't exist or there's an error parsing it, return an empty array
        return [];
    }
}

// Function to write data to the file
function writeDataToFile(data) {
    fs.writeFileSync(dataFilePath, JSON.stringify(data, null, 2), 'utf8'); // Use null, 2 for formatted JSON
}

app.post('/register', (req, res) => {
    const formData = req.body;
    console.log('Received form data:', formData);

    if (!formData.guardian_name || !formData.patient_name || !formData.email || !formData.password || !formData.register_date || !formData.patient_birth_date) {
        return res.status(400).json({ error: "Missing required fields" });
    }

    // Read existing data
    const existingData = readDataFromFile();

    // Add the new form data
    existingData.push(formData);

    // Write the updated data back to the file
    writeDataToFile(existingData);

    res.json({ message: 'Registration successful!' });
});

app.get('/registrations', (req, res) => {
    const registrations = readDataFromFile();
    res.json(registrations);
});

app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
});