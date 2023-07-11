from lib.album import *

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection 

#Get all albums stored in the albums table as a list
    def all(self):
    # Sql Used:
    #   SELECT id, title, release_year, artist_id FROM albums
    # Returns:
        #list of Album objects
        rows = self._connection.execute('SELECT id, title, release_year, artist_id FROM albums')
        albums = []
        for row in rows:
            albums.append(Album(row['id'], row['title'], row['release_year'], row['artist_id']))
        return albums
    
    


#add new album to albums table 
    def add(self,title, release_year, artist_id):
    # Parameters:
    #   title: string
    #   release_year: int
    #   artist_id: int
    # Side effects:
    #   Adds record to album table
    # Sql used:
    #   INSERT INTO albums(title, release_year, artist_id) VALUES(%s,%s,%s)

        self._connection.execute('INSERT INTO albums(title, release_year, artist_id) VALUES(%s,%s,%s)', [title, release_year, artist_id])

    


