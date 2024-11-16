import requests
from serpapi import GoogleSearch
import time
from typing import List, Dict
import streamlit as st
from config.config import SERPAPI_API_KEY, MAX_RESULTS_PER_SEARCH, RATE_LIMIT_DELAY

class SearchEngine:
    def __init__(self):
        self.api_key = SERPAPI_API_KEY

    def search(self, query: str) -> List[Dict]:
        """
        Perform a web search using SerpAPI
        Returns a list of search results
        """
        try:
            search_params = {
                "api_key": self.api_key,
                "engine": "google",
                "q": query,
                "num": MAX_RESULTS_PER_SEARCH,
            }
            
            search = GoogleSearch(search_params)
            results = search.get_dict()
            
            # Extract organic results
            if "organic_results" in results:
                processed_results = []
                for result in results["organic_results"]:
                    processed_results.append({
                        "title": result.get("title", ""),
                        "link": result.get("link", ""),
                        "snippet": result.get("snippet", "")
                    })
                
                time.sleep(RATE_LIMIT_DELAY)  # Respect rate limits
                return processed_results
            
            return []
            
        except Exception as e:
            st.error(f"Search error: {str(e)}")
            return []

    def batch_search(self, queries: List[str], progress_bar=None) -> List[Dict]:
        """
        Perform batch searches for multiple queries
        Returns a list of search results for each query
        """
        all_results = []
        
        for i, query in enumerate(queries):
            results = self.search(query)
            all_results.append(results)
            
            if progress_bar:
                progress_bar.progress((i + 1) / len(queries))
                
        return all_results