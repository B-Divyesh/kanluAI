import streamlit as st
import pandas as pd
from utils.file_handler import FileHandler
from utils.search import SearchEngine
from utils.llm import LLMProcessor
import asyncio

def extract_relevant_csv_content(df: pd.DataFrame, entity: str, selected_column: str) -> str:
    """
    Extract relevant content from the CSV file for the given entity.
    """
    relevant_rows = df[df[selected_column] == entity]
    if relevant_rows.empty:
        return "No relevant content found in the CSV."
    
    # Concatenate all relevant rows into a single string
    relevant_content = "\n".join(relevant_rows.apply(lambda row: row.to_string(), axis=1))
    return relevant_content

async def main():
    st.set_page_config(page_title="AI Information Retrieval Agent", layout="wide")
    
    # Initialize components
    file_handler = FileHandler()
    search_engine = SearchEngine()
    llm_processor = LLMProcessor()
    
    # Sidebar for uploading data
    st.title("KanluAI")
    st.sidebar.header("Data Source")
    source_type = st.sidebar.radio("Choose data source:", ["CSV Upload", "Google Sheets"])
    
    df = None
    
    if source_type == "CSV Upload":
        uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=['csv'])
        if uploaded_file:
            df = file_handler.read_csv(uploaded_file)
    else:
        spreadsheet_id = st.sidebar.text_input("Enter Google Sheets ID")
        range_name = st.sidebar.text_input("Enter Sheet Range (e.g., Sheet1!A1:B10)")
        if st.sidebar.button("Connect to Google Sheets"):
            df = file_handler.connect_google_sheets(spreadsheet_id, range_name)
    
    if df is not None:
        # Display data preview
        st.subheader("Data Preview")
        st.dataframe(df.head())
        
        # Column selection
        columns = df.columns.tolist()
        selected_column = st.selectbox(
            "Select the column containing entities:", columns,
            help="The column containing the entities to search for"
            )
        
        # Prompt template
        st.subheader("Search Query Configuration")
        prompt_template = st.text_area(
            "Enter your prompt template:",
            "Replace this text with what you want to ask to the csv file, Get me the Last name for {name}",
            help="Use {name} as a placeholder for each entity"
        )
    
    if st.button("Start Processing"):
        entities = df[selected_column].tolist()
        total_entities = len(entities)
        
        # Initialize progress bars
        st.subheader("Processing Status")
        search_progress = st.progress(0)
        llm_progress = st.progress(0)
        status_text = st.empty()
        
        # Extract relevant CSV content for each entity
        csv_contents = [extract_relevant_csv_content(df, entity, selected_column) for entity in entities]
        
        # Perform searches
        status_text.text("Performing web searches...")
        search_results = search_engine.batch_search(
            [prompt_template.replace("{company}", entity) for entity in entities],
            search_progress
        )
        
        # Process results with Azure OpenAI
        status_text.text("Processing search results with AI...")
        processed_results = await llm_processor.batch_process(
            entities,
            search_results,
            csv_contents,
            prompt_template,
            llm_progress
        )
        
        # Create results DataFrame
        results_df = pd.DataFrame(processed_results)
        
        # Display results
        st.subheader("Results")
        st.dataframe(results_df)
        
        # Download button
        output, filename = file_handler.export_results(results_df)
        if output and filename:
            st.download_button(
                label="Download Results",
                data=output,
                file_name=filename,
                mime="text/csv"
            )

if __name__ == "__main__":
    asyncio.run(main())