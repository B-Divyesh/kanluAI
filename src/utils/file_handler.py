import pandas as pd
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from googleapiclient.discovery import build
import streamlit as st
from typing import Union, Tuple
import io

class FileHandler:
    @staticmethod
    def read_csv(file_obj: Union[str, io.BytesIO]) -> pd.DataFrame:
        """Read CSV file and return pandas DataFrame"""
        try:
            df = pd.read_csv(file_obj)
            return df
        except Exception as e:
            st.error(f"Error reading CSV file: {str(e)}")
            return None

    @staticmethod
    def connect_google_sheets(spreadsheet_id: str, range_name: str) -> pd.DataFrame:
        """Connect to Google Sheets and return data as pandas DataFrame"""
        try:
            # Load credentials from the stored JSON
            credentials = service_account.Credentials.from_service_account_info(
                st.secrets["gcp_service_account"],
                scopes=['https://www.googleapis.com/auth/spreadsheets.readonly']
            )

            # Build the Sheets API service
            service = build('sheets', 'v4', credentials=credentials)
            sheet = service.spreadsheets()
            
            # Request data from the sheet
            result = sheet.values().get(
                spreadsheetId=spreadsheet_id,
                range=range_name
            ).execute()
            
            # Convert to DataFrame
            values = result.get('values', [])
            if not values:
                st.error('No data found in the sheet.')
                return None
                
            df = pd.DataFrame(values[1:], columns=values[0])
            return df
            
        except Exception as e:
            st.error(f"Error connecting to Google Sheets: {str(e)}")
            return None

    @staticmethod
    def export_results(df: pd.DataFrame, filename: str = "results.csv") -> Tuple[io.BytesIO, str]:
        """Export results to CSV file"""
        try:
            output = io.BytesIO()
            df.to_csv(output, index=False)
            output.seek(0)
            return output, filename
        except Exception as e:
            st.error(f"Error exporting results: {str(e)}")
            return None, None