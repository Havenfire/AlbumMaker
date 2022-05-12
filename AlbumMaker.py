import http
import json
from turtle import clear
from urllib import request
from webbrowser import get
import requests
from googleapiclient.discovery import build


api_key = "AIzaSyDbnpuTMh7AvUkgCaNwlbYnVqREHCzTVVE"
my_channel_id = "UC4X59r0SHRRNSlzL424O3EA"
                
youtube = build('youtube', 'v3', developerKey=api_key)

def get_channel_id(channel_name):
    search_request = youtube.search().list(
        part="snippet",
        maxResults=1,
        q=channel_name
    )
    response = search_request.execute()

    return(response["items"][0]["snippet"]["channelId"])
def get_channel_playlists(channel_id):
    request = youtube.playlists().list(
            part="snippet,contentDetails",
            channelId= channel_id,
            maxResults=10
    )
    response = request.execute()
    playlist_title_list = [{"titleName": t["snippet"]["title"]} for t in response["items"]]
    return playlist_title_list

def playlist_items():
    request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            playlistId="OLAK5uy_kL8dOOJh8D35rvkHIfmmEKZZIx69OH87w"
        )
    response = request.execute()
    print(response)



playlist_id = "OLAK5uy_nvbTquFDU0b9h9pKmzVSQ3GqGBENxnQsk"

userInput = input("Artist Name:")
x = get_channel_id(userInput)
print(get_channel_playlists(x))