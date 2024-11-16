KanluAI - AI Information Retrieval Agent
KanluAI is an AI-powered tool that allows you to upload a dataset (CSV or Google Sheets), perform web searches, and extract specific information for each entity in the dataset. The tool leverages a large language model (LLM) to process search results and generate structured, usable data based on your queries.

This project includes a simple Streamlit dashboard where users can upload files, define search queries, and view or download the results.

Key Features
Data Source Flexibility: Upload CSV files or connect to Google Sheets directly.
Entity-based Search: Automatically searches the web for information related to entities in a specific column of your dataset.
Prompt Configuration: Customize the search query using placeholders for dynamic querying.
LLM Integration: Leverage large language models to process search results and structure data.
Progress Tracking: Track progress for search execution and data processing.
Results Download: Download the processed data as a CSV file.
Setup Instructions
Prerequisites
To run KanluAI, ensure you have the following installed:

Python 3.7+
Streamlit: For creating the web dashboard.
Pandas: For data manipulation and processing.
Required Libraries: Other libraries required for web scraping, LLM processing, and Google Sheets integration.
You can install these dependencies using pip:

bash
Copy code
pip install streamlit pandas openai google-auth google-auth-oauthlib google-auth-httplib2
If you're using a custom LLM provider or any additional dependencies, be sure to install them as well (e.g., asyncio, or any libraries for web scraping or searching).

Setting Up API Keys
To enable web searching and LLM processing, you'll need API keys for services like OpenAI (or Azure OpenAI). Make sure to store the necessary keys in environment variables or a configuration file:

OpenAI API Key: If using OpenAI's API, you will need to set your API key:

bash
Copy code
export OPENAI_API_KEY="your-openai-api-key"
Google Sheets API Credentials: If you want to connect to Google Sheets, you will need to authenticate via the Google API. Follow the Google Sheets API setup guide to create and download your credentials.json.

Clone the Repository
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/kanluai.git
cd kanluai
Running the Application
Once you've set up the dependencies and API keys, you can run the KanluAI web application using Streamlit:

bash
Copy code
streamlit run main.py
This will launch the web app in your browser where you can upload your CSV file, configure search queries, and process your data.

Usage Instructions
Upload Data:

Choose between uploading a CSV file or connecting to Google Sheets by providing the spreadsheet ID and range (e.g., Sheet1!A1:B10).
Select Entity Column:

After the dataset is uploaded, select the column that contains the entities (e.g., company names, product names, etc.).
Define Search Query:

In the "Search Query Configuration" section, define a prompt template for how you'd like the web search to be performed. You can use placeholders like {name} for dynamic queries. For example: "Get me the last name for {name}".
Start Processing:

Click Start Processing to initiate the process. The application will:
Extract relevant content for each entity.
Perform web searches based on your query.
Process the search results with a language model (LLM).
Display the results in a structured format.
View Results:

The processed results will be displayed in a table format, where you can inspect the information gathered.
Download Results:

After the processing is complete, you can download the results as a CSV file by clicking the Download Results button.
Code Overview
main.py
extract_relevant_csv_content(df: pd.DataFrame, entity: str, selected_column: str): Extracts relevant rows from the dataset for a given entity in the selected column.
main(): The main function initializes the Streamlit dashboard, handles file uploads, configures prompts, and processes the data via web searches and LLM.
Key Components:
FileHandler: Handles reading and exporting data from CSV files or Google Sheets.
SearchEngine: Performs web searches based on the defined query template.
LLMProcessor: Processes the search results using a language model (e.g., OpenAI) to extract structured data.
Progress Bars:
Search Progress: Displays progress while performing web searches for each entity.
LLM Progress: Displays progress while processing the search results with the LLM.
Customization
Search Query Template: You can customize the prompt template to suit your specific needs. For example:

"What is the last name of {name}?"
"Find details for {company} including its industry and CEO name."
Just replace {name} or {company} with the entity from the selected column.

LLM Integration: The project is designed to work with Azure OpenAI, but you can easily replace this with another LLM provider if needed.

Future Improvements
Support for Other Data Formats: Adding support for Excel files, JSON, or other data sources.
Advanced Search Options: Allowing users to refine search criteria (e.g., filtering by keywords or adding additional fields).
Better Error Handling: Improve error handling for missing data or failed API requests.
Caching: Implement caching to reduce repeated processing for the same entity.
Contributing
If you'd like to contribute to this project, feel free to submit a pull request with any improvements or bug fixes. Make sure to follow the contribution guidelines and write tests where applicable.

