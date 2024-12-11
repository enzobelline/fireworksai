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

For the project, I initially started working with the phi-3-vision model, testing output text format first before transitioning to JSON output format. The JSON output proved more consistent and structured, making it easier to parse and extract the necessary data for the identity verification process.

To ensure usability and efficiency, I developed a basic front-end interface. This interface allows users to select images and compare extracted JSON data with correct information side-by-side. I also incorporated visual indicators for discrepancies, which promotes ease of handling mismatches and verifying data.

On the backend, I implemented pre-checks and exception handling mechanisms to validate inputs, such as ensuring the correctness of URLs and filenames for images. These measures help maintain data integrity and ensure smooth processing during API calls.
