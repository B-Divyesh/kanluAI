from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI
import time
from typing import List, Dict
import streamlit as st
from config.config import AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY, AZURE_OPENAI_DEPLOYMENT_NAME, DEFAULT_MODEL, MAX_TOKENS, TEMPERATURE

st.write("AZURE_OPENAI_API_KEY", st.secrets["AZURE_OPENAI_API_KEY"])
st.write("AZURE_OPENAI_ENDPOINT", st.secrets["AZURE_OPEN_ENDPOINT"])

class LLMProcessor:
    def __init__(self):
        self.client = AzureOpenAI(
            api_key=AZURE_OPENAI_API_KEY,
            api_version='2024-08-01-preview',
            azure_endpoint=AZURE_OPENAI_ENDPOINT
        )
        self.model = DEFAULT_MODEL

    async def process_search_results(self, entity: str, search_results: List[Dict], csv_content: str, prompt_template: str) -> Dict:
        """
        Process search results and CSV content using Azure OpenAI to extract relevant information
        Returns extracted information based on the prompt template
        """
        try:
            # Prepare the context from search results
            search_context = "\n\n".join([
                f"Title: {result['title']}\nURL: {result['link']}\nContent: {result['snippet']}"
                for result in search_results
            ])

            # Combine search context and CSV content
            combined_context = f"Search Results:\n{search_context}\n\nCSV Content:\n{csv_content}"

            # Prepare the system message
            system_message = """
            You are an AI assistant that extracts specific information from web search results and CSV content.
            You will be provided with search results, CSV content, and a prompt template.
            Extract the requested information accurately and concisely.
            If the information is not found, respond with "Not found".
            """

            # Replace placeholder in prompt template
            specific_prompt = prompt_template.replace("{company}", entity)

            # Make API call to Azure OpenAI
            response = self.client.chat.completions.create(
                model=self.model,  # Use the deployment name here
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": f"Context:\n{combined_context}\n\nTask:\n{specific_prompt}"}
                ],
                temperature=TEMPERATURE,
                max_tokens=MAX_TOKENS
            )

            return {
                "entity": entity,
                "extracted_info": response.choices[0].message.content,
                "status": "success"
            }

        except Exception as e:
            st.error(f"LLM processing error for {entity}: {str(e)}")
            return {
                "entity": entity,
                "extracted_info": f"Error during processing: {str(e)}",
                "status": "error"
            }

    async def batch_process(self, entities: List[str], search_results: List[List[Dict]], csv_content: List[str], prompt_template: str, progress_bar=None) -> List[Dict]:
        """
        Process multiple entities and their search results and CSV content
        Returns a list of results for each entity
        """
        all_results = []
        
        for i, (entity, results, content) in enumerate(zip(entities, search_results, csv_content)):
            result = await self.process_search_results(entity, results, content, prompt_template)
            all_results.append(result)
            
            if progress_bar:
                progress_bar.progress((i + 1) / len(entities))
                
        return all_results