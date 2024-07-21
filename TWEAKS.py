
# You can tweak the flow by adding a tweaks dictionary
# e.g {"OpenAI-XXXXX": {"model_name": "gpt-4"}}

TWEAKS={
    "Prompt-SYrJK": {
        "template": "Your goal is to create text and prompt for ultrarealistic image for an INSTAGRAM post based on the Information from User. Avoid using '*' character. \nThe text should be interesting and attract readers, whereas the image should be relevant to text and mesmerize people.\nStructure your answer in the following way : \n\ntext: \"your text for instagram\" \n\nprompt:\"your prompt for image generation\"\n\n\nInformation from User: {user}\n\n\n\n\n\n\n\n\n",
        "user": ""
    },
    #   "ChatInput-5umZ2": {
    #     "files": "",
    #     "input_value": "",
    #     "sender": "User",
    #     "sender_name": "User",
    #     "session_id": "",
    #     "should_store_message": True
    #   },
    "CustomComponent-zgHJ0": {
        "image_generation_MLAIapi_key": 'image_generation_MLAIapi_key',
        "input_value": "",
        "instagram_graph_api_token": 'instagram_graph_api_token',
        "instagram_user_id": 'instagram_user_id'
    },
    "GroqModel-gOn12": {
        "groq_api_base": "",
        "groq_api_key": 'groq_api_key',
        "input_value": "",
        "max_tokens": 2048,
        "model_name": "llama3-70b-8192",
        "n": 1,
        "stream": False,
        "system_message": "",
        "temperature": 0.1
    }
}
