from typing import Optional
from fastapi import FastAPI
from recommended import recommended_songs_id

app = FastAPI()


@app.get("/")
def read_root():
    return {"Status": "Working"}


# Input Type : GET /recommendations?songs=3,6,12
# Output Type: { "recommended": [ 30749, 48439, 82784, 144942, 176568 ] }

@app.get("/recommendations")
def read_item(songs: str):
    
    numbers      = songs.split(',')
    song_id_list = []
    for number in numbers:
        song_id_list.append(int(number))
    
    top_5_ids  = recommended_songs_id(song_id_list)
    top_5_ids  = list(top_5_ids)
    top_5_json = {"recommended":top_5_ids}
    
    return top_5_json

