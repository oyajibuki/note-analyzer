
import requests
import json
import urllib.parse
from datetime import datetime, timedelta

def test_note_api(keyword, params=None):
    encoded_word = urllib.parse.quote(keyword)
    url = f"https://note.com/api/v3/searches?context=note&q={encoded_word}&size=10&sort=like"
    
    if params:
        for k, v in params.items():
            url += f"&{k}={v}"
    
    print(f"\nTesting URL: {url}")
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        if "data" in data and "notes" in data["data"]:
            notes_data = data["data"]["notes"]
            if isinstance(notes_data, dict) and "contents" in notes_data:
                notes_list = notes_data["contents"]
                print(f"Found {len(notes_list)} notes.")
                
                for i, note in enumerate(notes_list[:3]):
                    title = note.get('name')
                    publish_at = note.get('publish_at')
                    print(f"  [{i+1}] Title: {title[:20]}..., Date: {publish_at}")
                return notes_list
            else:
                print("Unexpected structure.")
        else:
            print("No notes found.")
            
    except Exception as e:
        print(f"Error: {e}")
        return []

print("--- Control: No filters ---")
test_note_api("#Python")

print("--- Test 1: duration=24h ---")
test_note_api("#Python", {"duration": "24h"})

print("--- Test 2: duration=week ---")
test_note_api("#Python", {"duration": "week"})

print("--- Test 3: since/until (Last 24h) ---")
now = datetime.now()
yesterday = now - timedelta(days=1)
params = {
    "since": yesterday.strftime("%Y-%m-%dT%H:%M:%S"),
    "until": now.strftime("%Y-%m-%dT%H:%M:%S")
}
test_note_api("#Python", params)

print("--- Test 4: created_at_from (Last 24h) ---")
test_note_api("#Python", {"created_at_from": yesterday.strftime("%Y-%m-%d")})
