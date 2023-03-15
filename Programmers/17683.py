def solution(m, musicinfos):
    def change_hash(str):
        if 'C#' in str:
            str = str.replace('C#', 'c')
        if 'D#' in str:
            str = str.replace('D#', 'd')
        if 'F#' in str:
            str = str.replace('F#', 'f')
        if 'G#' in str:
            str = str.replace('G#', 'g')
        if 'A#' in str:
            str = str.replace('A#', 'a')
        return str
    
    m = change_hash(m)
    len_musicinfos = len(musicinfos)
    candidates = []
    for i in range(len_musicinfos):
        start, end, title, melody = map(str, musicinfos[i].split(','))
        melody = change_hash(melody)
        
        s_h, s_m = map(int, start.split(':'))
        e_h, e_m = map(int, end.split(':'))
        duration = (e_h * 60 + e_m) - (s_h * 60 + s_m)
            
        played_music = ""
        played_music += melody * (duration // len(melody))
        played_music += melody[:duration % len(melody)]
        
        if m in played_music:
            candidates.append((duration, i, title))
    
    if len(candidates) == 0:
        return "(None)"
    elif len(candidates) == 1:
        return candidates[0][2]
    else:
        candidates = sorted(candidates, key=lambda x: (-x[0], x[1]))
        return candidates[0][2]
        
            