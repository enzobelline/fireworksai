from fireworks.client import Fireworks
import fireworks.client
import re
import base64
import os
import json
import requests
from pathlib import Path
import mimetypes

#-------------------------
#--LOCAL VARAIBLES--------
#-------------------------
DEFAULT_PROMPT="Can you describe this image?"
DEFAULT_LICENSE_PROMPT="Parse the relevant license data in JSON format"
DOG_IMAGE_PATH="https://images.squarespace-cdn.com/content/v1/54822a56e4b0b30bd821480c/45ed8ecf-0bb2-4e34-8fcf-624db47c43c8/Golden+Retrievers+dans+pet+care.jpeg?format=750w"

#-------------------------
#--JSON Functions---------
#-------------------------
def get_file_list(directory, extension_filter=None):
    """
    Generate a list of full file paths in a specified directory.
    Handles paths consistently across operating systems.
    
    Args:
        directory (str): The directory to scan for files.
        extension_filter (list, optional): A list of file extensions to include (e.g., ['png', 'jpg']).
                                           If None, includes all files.
    
    Returns:
        list: A list of full file paths in the specified directory.
    """
    try:
        # Check if the directory exists
        if not os.path.exists(directory):
            raise FileNotFoundError(f"The directory {directory} does not exist.")
        
        # Convert directory to Path object for cross-platform handling
        directory = Path(directory)
        
        # List files in the directory
        files = []
        for file in directory.iterdir():
            if file.is_file():  # Ensure it's a file, not a directory
                if extension_filter:
                    # Check if the file's extension matches the filter
                    if file.suffix.lower().strip('.') in extension_filter:
                        files.append(str(file))
                else:
                    files.append(str(file))
        
        return files
    except Exception as e:
        print(f"Error: {e}")
        return []
        
def save_list_to_json(file_list, output_path):
    """
    Save a list of file names to a JSON file.
    
    Args:
        file_list (list): The list of file names to save.
        output_path (str): The path to save the JSON file.
    """
    try:
        with open(output_path, 'w') as json_file:
            json.dump(file_list, json_file, indent=4)
        print(f"File list saved to {output_path}")
    except Exception as e:
        print(f"Error saving JSON file: {e}")

def load_list_from_json(json_path):
    """
    Load a list of file names from a JSON file.
    
    Args:
        json_path (str): The path to the JSON file.
    
    Returns:
        list: The list of file names loaded from the JSON file.
    """
    try:
        with open(json_path, 'r') as json_file:
            file_list = json.load(json_file)
        print(f"File list loaded from {json_path}")
        return file_list
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return []


#-------------------------
#--Image Functions--------
#-------------------------
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
    
def create_base64_image_url(image_path):
    """
    Converts a local image file to a base64-encoded data URL based on its file extension.
    
    Args:
        image_path (str): Path to the local image file.
    
    Returns:
        str: A base64-encoded data URL for the image.
    
    Raises:
        FileNotFoundError: If the image file does not exist.
        ValueError: If the file is not a recognized image format.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")
    
    # Detect MIME type from the file extension
    mime_type, _ = mimetypes.guess_type(image_path)
    if not mime_type or not mime_type.startswith("image/"):
        raise ValueError(f"Unsupported or unrecognized image format: {image_path}")
    
    # Read and encode the image in base64
    image_base64 = encode_image(image_path)
    
    # Return the data URL
    return f"data:{mime_type};base64,{image_base64}"


def validate_image_path(input_path):
    """
    Validates if the given image path is a valid local file or a reachable URL.
    
    Args:
        image_path (str): Path to the local image file or URL to an online image.
    
    Raises:
        FileNotFoundError: If the local file does not exist.
        ValueError: If the URL is not reachable or does not point to a valid image.
    """

    if not input_path:
        raise ValueError("Input path cannot be empty or None.")

    url_pattern = re.compile(
        r'^(https?://)'                  # Starts with http:// or https://
        r'((([A-Za-z0-9-]+\.)+[A-Za-z]{2,6})|localhost)'  # Domain (e.g., example.com) or localhost
        r'(:[0-9]{1,5})?'                # Optional port (e.g., :80)
        r'(/.*)?$'                       # Optional path (e.g., /index.html)
    )
        
    # Validate if it's an HTTP/HTTPS URL
    if url_pattern.match(input_path):
        # Check if the URL is reachable and valid
        try:
            response = requests.head(input_path, timeout=5)
            if response.status_code != 200:
                raise ValueError(f"URL is not reachable: {input_path}")
            
            # Verify content type is an image
            content_type = response.headers.get("Content-Type", "")
            if not content_type.startswith("image/"):
                raise ValueError(f"URL does not point to a valid image: {input_path}")
            
            print(f"Valid image URL: {input_path}")
            return "http_url"
        except requests.RequestException as e:
            raise ValueError(f"Error accessing URL: {e}")
    
    # Validate if it's a local file path
    elif os.path.exists(input_path):
        print(f"Local file found: {input_path}")
        return "local_path"
    
    # If neither, raise an error
    else:
        raise FileNotFoundError(f"Path does not exist and is not a valid URL: {input_path}")
    

    
#-------------------------
#--API Functions--------
#-------------------------

def test():
    # API request test
    # Initialize client with API key
    client = Fireworks(api_key=os.getenv("FIREWORKS_API_KEY"))

    response = client.chat.completions.create(
        model="accounts/fireworks/models/llama-v3p1-8b-instruct",
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            },
        ],
    )

    # Print the response
    print("Response from Fireworks API:")
    print(response.choices[0].message.content)

def chat_completions_api_VLM(text=DEFAULT_PROMPT,image_path=DOG_IMAGE_PATH):
    if validate_image_path(image_path)=="local_path":
        image_path=create_base64_image_url(image_path)

    fireworks.client.api_key = os.getenv("FIREWORKS_API_KEY")
    response = fireworks.client.ChatCompletion.create(
    model = "accounts/fireworks/models/phi-3-vision-128k-instruct",
    messages = [{
        "role": "user",
        "content": [{
        "type": "text",
        "text": text,
        }, {
        "type": "image_url",
        "image_url": {
            "url": image_path
        },
        }, ],
    }],
    )
    return(response.choices[0].message.content)

def completions_api_VLM(client):
    fireworks.client.api_key = os.getenv("FIREWORKS_API_KEY")
    response = fireworks.client.Completion.create(
    model = "accounts/fireworks/models/phi-3-vision-128k-instruct",
    prompt = "SYSTEM: Hello\n\nUSER:<image>\ntell me about the image\n\nASSISTANT:",
    images = ["https://images.unsplash.com/photo-1582538885592-e70a5d7ab3d3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80"],
    )
    print(response.choices[0].text)






