# Passports & Drivers License Identity Verification

A web-based application to view and validate JSON data extracted from images (e.g., licenses and passports). This project enables users to select an image, view its associated JSON data, compare it with the correct JSON, and highlight differences for easy validation.

---

- [Passports \& Drivers License Identity Verification](#passports--drivers-license-identity-verification)
  - [Features](#features)
  - [Demo](#demo)
  - [Installation](#installation)

---
## Features
- **Image Selection**: Choose images from a dropdown menu.
- **JSON Display**: View extracted JSON and the correct JSON side-by-side.
- **Highlight Differences**: Mismatched values between the extracted and correct JSON are displayed in red.
- **Responsive Design**: Works across devices with clean and user-friendly visuals.

---

## Demo

Check out the live version on [GitHub Pages](https://github.com/enzobelline/fireworksai).

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-github-username/json-viewer-validator.git
   cd json-viewer-validator
2. Set up a local environment:
   ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    .\venv\Scripts\activate   # Windows

3. Install dependencies:
   ```bash
    pip install -r requirements.txt

4. Start a local server:
   ```bash
    python -m http.server

5. Open the application in your browser:
   ```bash
    http://localhost:8000

---

fireworksai/
├── app.js                    # JavaScript logic for the application
├── style.css                 # Styling for the application
├── index.html                # Main HTML file
├── sample_inputs/            # Folder containing the images
│   ├── License-1.png
│   ├── License-2.jpg
│   ├── ...
│   ├── Passport-3.jpeg
├── cleaned_responses.json   # Extracted JSON data
├── correct_information.json # Correct JSON for comparison
├── image_list.json          # List of images in order
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
