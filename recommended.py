import pickle 
import pandas as pd

def recommended_songs_id(song_id_list):
    
    # Load the model from disk
    filename = './model/finalized_model.sav'
    model    = pickle.load(open(filename, 'rb'))
    df_recommended = pd.DataFrame()
    flag = 0
    
    # Identyfiying the recommendation based on Individual Songs and then summing from all the options
    for song_id in song_id_list:
        similars = model.similar_items(song_id, N)
        df_rec   = pd.DataFrame(similars, columns=['id',song_id])    
        df_rec   = df_rec.sort_values(by=['id'])
        if flag == 0:
            df_recommended['id']    = df_rec['id']
            df_recommended['total'] = df_rec[song_id]
            flag = 1
        else:
            df_recommended['total'] = df_rec[song_id] + df_recommended['total']

    df_recommended = df_recommended.sort_values(by = ['total'],ascending=0)

    for song_id in song_id_list:
        df_recommended = df_recommended[df_recommended['id'] != song_id]

    top_5_ids = df_recommended.id[0:5]
    return top_5_ids