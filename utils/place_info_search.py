import os
import json
from langchain_tavily import TavilySearch
from langchain_google_community import GooglePlacesTool, GooglePlacesAPIWrapper 

class GooglePlaceSearchTool:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.places_wrapper = None
        self.places_tool = None
        
        # Only initialize Google Places if API key looks valid
        if api_key and not api_key.startswith('your_') and len(api_key) > 10 and 'your_' not in api_key:
            try:
                self.places_wrapper = GooglePlacesAPIWrapper(gplaces_api_key=api_key)
                self.places_tool = GooglePlacesTool(api_wrapper=self.places_wrapper)
            except Exception as e:
                print(f"Google Places API initialization failed: {e}")
                self.places_wrapper = None
                self.places_tool = None
        else:
            print("Google Places API key not configured, will use Tavily search as fallback")
            self.places_wrapper = None
            self.places_tool = None
    
    def google_search_attractions(self, place: str) -> dict:
        """
        Searches for attractions in the specified place using GooglePlaces API.
        """
        if self.places_tool:
            return self.places_tool.run(f"top attractive places in and around {place}")
        return None
    
    def google_search_restaurants(self, place: str) -> dict:
        """
        Searches for available restaurants in the specified place using GooglePlaces API.
        """
        if self.places_tool:
            return self.places_tool.run(f"what are the top 10 restaurants and eateries in and around {place}?")
        return None
    
    def google_search_activity(self, place: str) -> dict:
        """
        Searches for popular activities in the specified place using GooglePlaces API.
        """
        if self.places_tool:
            return self.places_tool.run(f"Activities in and around {place}")
        return None

    def google_search_transportation(self, place: str) -> dict:
        """
        Searches for available modes of transportation in the specified place using GooglePlaces API.
        """
        if self.places_tool:
            return self.places_tool.run(f"What are the different modes of transportations available in {place}")
        return None

class TavilyPlaceSearchTool:
    def __init__(self):
        pass

    def tavily_search_attractions(self, place: str) -> dict:
        """
        Searches for attractions in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"top attractive places in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_restaurants(self, place: str) -> dict:
        """
        Searches for available restaurants in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"what are the top 10 restaurants and eateries in and around {place}."})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_activity(self, place: str) -> dict:
        """
        Searches for popular activities in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"activities in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result

    def tavily_search_transportation(self, place: str) -> dict:
        """
        Searches for available modes of transportation in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"What are the different modes of transportations available in {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result