# KanluAI

**KanluAI** is an AI-powered information retrieval tool that enables automated web searching and data extraction for your datasets. Upload CSV files or connect to Google Sheets to process multiple entities efficiently using large language models. Try it out at 

<div align="center">

![KanluAI](https://img.shields.io/badge/KanluAI-Information%20Retrieval-blue)
![Python](https://img.shields.io/badge/Python-3.7%2B-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

</div>

## Key Features
- **Data Source Flexibility**: Support for CSV files and Google Sheets
- **Entity-based Search**: Automated web searches for entities in your dataset
- **Prompt Configuration**: Customizable search queries with dynamic placeholders
- **LLM Integration**: Process search results using large language models
- **Progress Tracking**: Real-time progress monitoring for searches and processing
- **Results Download**: Export processed data as CSV files

## Setup Instructions

### Prerequisites
```bash
#makes sure you setup a virtual enviroment before starting
source .venv/bin/activate
pip install -r requirements.txt
```

### API Configuration
Set up your API keys for required services:
first Preferable method, deploy to streamlit to use from any remote device and provide your keys in this format IN THE SECRETS SECTION OF YOUR APP SETTINGS or in your.streamlit.secrets.toml file:
```bash
AZURE_OPENAI_API_KEY="<API-KEY>"
SERPAPI_API_KEY="<API-KEY>"
GOOGLE_CREDENTIALS="<API-KEY>"
AZURE_OPENAI_ENDPOINT="<API-ENDPOINT>"
```
second Preferable method make an .env file in the root directory with the following format:
```bash
AZURE_OPENAI_API_KEY="<API-KEY>"
SERPAPI_API_KEY=<API-KEY>
GOOGLE_CREDENTIALS=<API-KEY>
AZURE_OPENAI_ENDPOINT="<API-ENDPOINT>"
AZURE_OPENAI_DEPLOYMENT_NAME=<MODEL-NAME> #optional
```
third preferance, hard code your api keys if you are not going to deploy into public domains:
```bash
self.client = AzureOpenAI(
            api_key=<AZURE_OPENAI_API_KEY>,
            api_version='2024-08-01-preview',
            azure_endpoint=<AZURE_OPENAI_ENDPOINT>
        )
```

For Google Sheets integration, follow the [Google Sheets API setup guide](https://developers.google.com/sheets/api/quickstart/python) to obtain your credentials.json.

### Installation
```bash
git clone https://github.com/your-username/kanluAI.git
cd kanluAI
streamlit run main.py
```

## Usage

### Data Upload
1. Choose between CSV upload or Google Sheets connection
2. Select the entity column from your dataset
3. Configure your search query template using placeholders (e.g., `{name}`)
4. Start processing to initiate web searches and LLM analysis
5. Download results in CSV format

### Example Query Templates
- `"What is the last name of {name}?"`
- `"Find details for {company} including its industry and CEO name."`

## Get Help

### Documentation
For detailed usage instructions, please refer to our documentation (coming soon).

### Updates
- Follow our GitHub repository for updates
- Star the repository to show support

### Discussions
- Open an issue for bug reports
- Start a discussion for feature requests

## Future Improvements
- Support for additional data formats (Excel, JSON)
- Advanced search options and filtering
- Enhanced error handling
- Result caching system
- API endpoint support

## Contributing
We welcome contributions! Please feel free to submit pull requests for:
- Bug fixes
- New features
- Documentation improvements
- Test coverage

## License
KanluAI is licensed under the MIT License. See [LICENSE](LICENSE) for more information.
