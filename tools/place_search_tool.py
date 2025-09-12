import os
from utils.place_info_search import GooglePlaceSearchTool, TavilyPlaceSearchTool
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv

class PlaceSearchTool:
    def __init__(self):
        load_dotenv()
        self.google_api_key = os.environ.get("GPLACES_API_KEY")
        
        # Only initialize Google Places if API key looks valid
        if self.google_api_key and not self.google_api_key.startswith('your_') and len(self.google_api_key) > 10:
            try:
                self.google_places_search = GooglePlaceSearchTool(self.google_api_key)
            except Exception as e:
                print(f"Google Places initialization failed: {e}")
                self.google_places_search = None
        else:
            print("Google Places API key not configured, using Tavily search only")
            self.google_places_search = None
            
        self.tavily_search = TavilyPlaceSearchTool()
        self.place_search_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """Setup all tools for the place search tool"""
        @tool
        def search_attractions(place:str) -> str:
            """Search attractions of a place"""
            if self.google_places_search:
                try:
                    attraction_result = self.google_places_search.google_search_attractions(place)
                    if attraction_result:
                        return f"Following are the attractions of {place} as suggested by google: {attraction_result}"
                except Exception as e:
                    print(f"Google Places search failed: {e}")
            
            # Fallback to Tavily search
            tavily_result = self.tavily_search.tavily_search_attractions(place)
            return f"Following are the attractions of {place}: {tavily_result}"
        
        @tool
        def search_restaurants(place:str) -> str:
            """Search restaurants of a place"""
            if self.google_places_search:
                try:
                    restaurants_result = self.google_places_search.google_search_restaurants(place)
                    if restaurants_result:
                        return f"Following are the restaurants of {place} as suggested by google: {restaurants_result}"
                except Exception as e:
                    print(f"Google Places search failed: {e}")
            
            # Fallback to Tavily search
            tavily_result = self.tavily_search.tavily_search_restaurants(place)
            return f"Following are the restaurants of {place}: {tavily_result}"
        
        @tool
        def search_activities(place:str) -> str:
            """Search activities of a place"""
            if self.google_places_search:
                try:
                    activities_result = self.google_places_search.google_search_activity(place)
                    if activities_result:
                        return f"Following are the activities in and around {place} as suggested by google: {activities_result}"
                except Exception as e:
                    print(f"Google Places search failed: {e}")
            
            # Fallback to Tavily search
            tavily_result = self.tavily_search.tavily_search_activity(place)
            return f"Following are the activities of {place}: {tavily_result}"
        
        @tool
        def search_transportation(place:str) -> str:
            """Search transportation of a place"""
            if self.google_places_search:
                try:
                    transport_result = self.google_places_search.google_search_transportation(place)
                    if transport_result:
                        return f"Following are the modes of transportation available in {place} as suggested by google: {transport_result}"
                except Exception as e:
                    print(f"Google Places search failed: {e}")
            
            # Fallback to Tavily search
            tavily_result = self.tavily_search.tavily_search_transportation(place)
            return f"Following are the modes of transportation available in {place}: {tavily_result}"
        
        return [search_attractions, search_restaurants, search_activities, search_transportation]