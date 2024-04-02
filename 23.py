from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_dict = defaultdict(list)
    play_dict = defaultdict(int)
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        genre_dict[genre].append((i, play))
        play_dict[genre] += play
    
    sorted_genres = sorted(play_dict.items(), key=lambda x: x[1], reverse=True)
    
    for genre, _ in sorted_genres:
        sorted_songs = sorted(genre_dict[genre], key=lambda x: (-x[1], x[0]))
        answer.extend([idx for idx, _ in sorted_songs[:2]])
    
    return answer
