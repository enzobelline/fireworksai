from fireworks.client import Fireworks
import fireworks.client
import os
import fireworks_api
import base64
import json

IMAGES_FOLDER_FILE_PATH = "sample_inputs"
IMAGE_LIST_JSON_FILE_PATH = "image_list.json"
RAW_RESPONSES_FILE_PATH = "raw_responses.json"
CLEANED_RESPONSES_FILE_PATH = "cleaned_responses.json"
CLEANED_RESPONSES_FRONT_END_FILE_PATH="./front_end/cleaned_responses.json"

if __name__ == "__main__":
    # fireworks_api.test()
    
    # # Save file list to JSON
    # file_list=fireworks_api.get_file_list(IMAGES_FOLDER_FILE_PATH)
    # fireworks_api.save_list_to_json(file_list,"image_list.json")

    # Load file list from JSON
    print("Loading file list from JSON...")
    loaded_image_file_paths = fireworks_api.load_list_from_json(IMAGE_LIST_JSON_FILE_PATH)

    # #run code basic text output
    # fireworks_api.run_all_images_chat_completions_api_VLM(loaded_image_file_paths)

    # #run code basic json output
    responses_list=fireworks_api.run_all_images_chat_completions_api_VLM_json_output(loaded_image_file_paths)
    fireworks_api.save_list_to_json(responses_list,RAW_RESPONSES_FILE_PATH)

    #just attempt to clean old responses
    # responses_list=fireworks_api.load_list_from_json(RAW_RESPONSES_FILE_PATH)

    #actually doing the cleaning use on either active run or old run
    cleaned_response_list=fireworks_api.clean_responses(responses_list)
    fireworks_api.save_list_to_json(cleaned_response_list,CLEANED_RESPONSES_FILE_PATH)
    fireworks_api.save_list_to_json(cleaned_response_list,CLEANED_RESPONSES_FRONT_END_FILE_PATH)
    print(f"Cleaned responses saved to {CLEANED_RESPONSES_FILE_PATH},{CLEANED_RESPONSES_FRONT_END_FILE_PATH}")

