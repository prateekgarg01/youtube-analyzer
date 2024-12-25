from googleapiclient.discovery import build
import streamlit as st
import ollama

api_key = "api_key"

youtube = build('youtube','v3',developerKey=api_key)

def fetch_top_trending_videos(region_code="IN", max_results=2):
    request = youtube.videos().list(
        part="snippet,statistics",
        chart="mostPopular",
        regionCode=region_code,
        maxResults=max_results
    )

    response=request.execute()
    videos=[]

    for item in response['items']:
        title = item['snippet']['title']
        video_id = item['id']
        description = item['snippet']['description']
        channel_title = item['snippet']['channelTitle']
        views = item['statistics']['viewCount']

        video_data={
            "title":title,
            "video_id":video_id,
            "description":description,
            "channel_title":channel_title,
            "views":views
        }
        videos.append(video_data)
    return videos

def analyze_video_content(title, description):
    prompt =f"""Analyze the following Youtube video and provide insights:\n\nTitle:{title}\n
    Description: {description}\n\n provide a brief summary, key topics and any trend or insights about 
    the video."""
    response = ollama.chat(model="llama3.1:8b", messages=[{"role":"user","content":prompt}])

    return response['message']['content']


if st.button("Fetch Top trending Videos in India:"):
    videos=fetch_top_trending_videos()

    for video in videos:
        st.subheader(video['title'])
        st.write(f"**Channel**:{video['channel_title']}")
        st.write(f"**Views**: {video['views']}")
        st.write(f"**Description** : {video['description']}")
        analysis = analyze_video_content(video['title'],video['description'] )
        st.write(f"**Analysis**:{analysis}")
        st.write("-------------------------------")