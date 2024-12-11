const RESPONSES_JSON = "./cleaned_responses.json";
const IMAGE_LIST_JSON = "./image_list.json";
const CORRECT_JSON = "./correct_information.json";

document.addEventListener("DOMContentLoaded", async () => {
    const imageSelect = document.getElementById("image-select");
    const selectedImage = document.getElementById("selected-image");
    const extractedJsonPre = document.getElementById("extracted-json");
    const correctJsonPre = document.getElementById("correct-json");

    let responses = [];
    let imageList = [];
    let correctInfo = {};

    // Load JSON files
    async function loadJson(url) {
        const response = await fetch(url);
        if (!response.ok) {
            console.error(`Failed to load ${url}: ${response.statusText}`);
            return {};
        }
        return await response.json();
    }

    // Populate image dropdown
    function populateImageSelect(images) {
        const defaultOption = document.createElement("option");
        defaultOption.value = "";
        defaultOption.textContent = "Choose an image...";
        imageSelect.appendChild(defaultOption);

        images.forEach((image, index) => {
            const option = document.createElement("option");
            option.value = image; // Use the full image path
            option.textContent = image.replace(/sample_inputs[\\/]/, "").replace(/-/g, " "); // Make human-readable
            imageSelect.appendChild(option);
        });
    }
// Highlight differences for extracted JSON and correct JSON
function highlightDifferences(extracted, correct) {
    const extractedDiffHtml = [];
    const correctDiffHtml = [];

    // Iterate over all keys in the correct JSON
    for (const key in correct) {
        if (extracted[key] !== correct[key]) {
            // If the values are different, show red for extracted and green for correct
            extractedDiffHtml.push(
                `<span class="mismatch">${key}: ${extracted[key] || "N/A"}</span>`
            );
            correctDiffHtml.push(
                `<span class="correct">${key}: ${correct[key]}</span>`
            );
        } else {
            // If values match, show normally
            extractedDiffHtml.push(`${key}: ${extracted[key]}`);
            correctDiffHtml.push(`${key}: ${correct[key]}`);
        }
    }

    // Handle any extra keys in extracted JSON not present in correct JSON
    for (const key in extracted) {
        if (!(key in correct)) {
            extractedDiffHtml.push(
                `<span class="mismatch">${key}: ${extracted[key]}</span>`
            );
        }
    }

    return {
        extractedHtml: extractedDiffHtml.join("<br>"),
        correctHtml: correctDiffHtml.join("<br>")
    };
}

// Handle dropdown change
imageSelect.addEventListener("change", (e) => {
    const selectedImagePath = e.target.value; // Full path from dropdown
    const placeholder = document.querySelector(".placeholder");

    if (!selectedImagePath) {
        selectedImage.src = "";
        selectedImage.alt = "No image selected";
        selectedImage.style.display = "none"; // Hide the image element
        placeholder.style.display = "flex";  // Show the placeholder

        extractedJsonPre.innerHTML = "No JSON data available. Please select an image.";
        correctJsonPre.innerHTML = "No JSON data available. Please select an image.";
        return;
    }

    // Hide the placeholder and show the selected image
    selectedImage.src = selectedImagePath;
    selectedImage.alt = selectedImagePath;
    selectedImage.style.display = "block"; // Show the image element
    placeholder.style.display = "none";   // Hide the placeholder

    // Match the extracted JSON using the selected image path
    const extractedInfo = responses[imageList.indexOf(selectedImagePath)] || {};
    const correctInfoForImage = correctInfo[selectedImagePath] || {}; // Ensure matching logic

    // Highlight differences
    const { extractedHtml, correctHtml } = highlightDifferences(extractedInfo, correctInfoForImage);

    // Display highlighted JSON
    extractedJsonPre.innerHTML = extractedHtml || "No extracted JSON available.";
    correctJsonPre.innerHTML = correct

    // Initialize app
    async function init() {
        // Load JSON data
        responses = await loadJson(RESPONSES_JSON);
        imageList = await loadJson(IMAGE_LIST_JSON);
        correctInfo = await loadJson(CORRECT_JSON);

        // Populate the dropdown
        populateImageSelect(imageList);
    }

    init();
});
