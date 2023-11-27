# Chat-with-PDF
This repository uses OpenAI and LangChain that creates a simple app to chat with your PDF's</p>

## Indroduction 

This is a Python Application that allows user to chat with PDF's. The user can ask relevant questions about the given PDF's and it would provide relevant repsonses by searching the content of the dcoument.

## Install and Usage 

To install to local system:

1. Use the Git command Line for either macOS, Linux or Windows to fork this repository to your Local Machine

2. In the `App.py` look at all the packages and install them.
```
pip install PyPDF2
pip install python-dotenv
pip install langchain
pip install streamlit
pip install openai
pip install faiss-cpu
pip install huggingface-hub
pip install InstructorEmbedding
```

3. Obtain the API key from OpenAI and as well as Hugging Face and add it to the `.env` file in the project directory


To use the given app follow the below given steps: 

1. If you have already installed Python using Anaconda , then firstly Launch Anaconda Prompt CLI.

2. Go the directory where the `main.py` file is stored and then execute the folloeing command:
   ```
   streamlit run app.py

   ```
3. The app will run on local host:   `http://localhost:8501`

4. In the browser load the PDF documents and then click on the `process button`.

5. In the Chat box ask question's related to the PDF and get its response.

