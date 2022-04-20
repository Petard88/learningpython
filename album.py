def make_album(artist_name, album_title, tracks=None):
    """Return a dictionary of information about an album"""
    album = {'Artist': artist_name, 'Album': album_title}
    if tracks:
        album['Tracks'] = tracks
    return album

skiva = make_album('nirvana', 'nevermore', tracks=12)
print(skiva)
skiva = make_album('soad', 'kurtans', tracks=2)
print(skiva)
skiva = make_album("Berit's svänggäng", 'leif', tracks=999)
print(skiva)