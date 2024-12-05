# RAG Chat System

Welcome to the **RAG Chat System**! 
This project is a **Retrieval-Augmented Generation (RAG)** chat application built with Streamlit and OpenAI's GPT models. 
It allows you to query a datastore of documents and get contextually relevant responses, with sources provided when available.

![Screenshot](https://github.com/ahmedashraffcih/rag-chat-system/blob/main/assets/Screenshot%202024-12-05%20193013.png)

## Features

- **Regenerate Data Store**: Easily refresh the document datastore.
- **Interactive Chat**: Engage in a conversational interface for asking questions.
- **Customizable Settings**:
  - Adjust model response temperature for diverse outputs.
- **Download Chat History**: Save your conversations as a text file.
- **Expandable Responses**: View long responses in collapsible sections for cleaner UI.

## Installation

### Prerequisites
- Python 3.8 or higher
- OpenAI API Key
- Streamlit installed

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/ahmedashraffcih/rag-chat-system.git
   cd rag-chat-system
   ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your environment variables:
    - Create a .env file in the project root directory.
    - Add the following line to your .env file:
        ```bash
        OPENAI_API_KEY=your_openai_api_key
        ```

4. Run the application:
    ```bash
    streamlit run app.py
    ```

## Project Structure
```bash
├── app.py                     # Main Streamlit app
├── 📂 src
│   ├── 📂 modules
│   │   ├── extraction.py      # Handles document ingestion and storage
│   │   ├── query.py           # Handles querying and response generation
│   │   └── __init__.py
│   └── 📂 utils
│       ├── constants.py       # Stores global constants
│       └── __init__.py
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (not included in repo)
└── README.md                  # Project documentation
```

## Usage

1. **Start the App**: Run the Streamlit app using:
   ```bash
   streamlit run app.py
   ```

2. Interact with the Chat:

    - Type your query in the input box and receive contextually relevant answers.
    - Use the sidebar to regenerate the datastore or adjust model settings.

3. Download Chat History:
    - Click on "Download Chat History" to save the conversation.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.