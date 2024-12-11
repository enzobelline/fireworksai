from fireworks.client import Fireworks
import fireworks.client
import os
import fireworks_api
import base64
import json

IMAGES_FOLDER_FILE_PATH = "sample_inputs"
IMAGE_LIST_JSON_FILE_PATH = "image_list.json"

if __name__ == "__main__":
    # fireworks_api.test()
    
    # Save file list to JSON
    file_list=fireworks_api.get_file_list(IMAGES_FOLDER_FILE_PATH)
    fireworks_api.save_list_to_json(file_list,"image_list.json")

    # Load file list from JSON
    print("Loading file list from JSON...")
    loaded_image_file_paths = fireworks_api.load_list_from_json(IMAGE_LIST_JSON_FILE_PATH)


    # #run code basic text output
    # fireworks_api.run_all_images_chat_completions_api_VLM(loaded_image_file_paths)

    #run code basic json output
    print(loaded_image_file_paths[0])
    fireworks_api.run_all_images_chat_completions_api_VLM_json_output(loaded_image_file_paths)