from googleapiclient.discovery import build
import streamlit as st

api_key = "api_key"

youtube = build('youtube','v3',developerKey=api_key)

def fetch_top_trending_videos(region_code="IN", max_results=1):
    request = youtube.videos().list(
        part="snippet,statistics",
        chart="mostPopular",
        regionCode=region_code,
        maxResults=max_results
    )

    response=request.execute()
    st.write(response)

fetch_top_trending_videos()