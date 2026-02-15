
from app import get_note_ranking
import json

def verify_ranking():
    print("Verifying get_note_ranking with keyword '#Python'...")
    results = get_note_ranking("#Python")
    
    if not results:
        print("No results found. Verification Failed.")
        return

    print(f"Found {len(results)} results.")
    
    is_sorted = True
    previous_likes = float('inf')
    
    for i, note in enumerate(results[:10]):
        likes = note['likes']
        print(f"[{i+1}] Likes: {likes}, Title: {note['title']}")
        
        if likes > previous_likes:
            is_sorted = False
        previous_likes = likes

    if is_sorted:
        print("\nSUCCESS: Results are sorted by likes in descending order.")
    else:
        print("\nFAILURE: Results are NOT sorted correctly.")

if __name__ == "__main__":
    verify_ranking()
