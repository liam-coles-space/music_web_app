# Request:
POST /albums

# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK)
(No content)

Nouns:
albums, title, release_year, artist_id

Record || Properties
album     title, release_year, artist_id

Table:
albums
id: serial
title: text
release_year: int
artist_id: int

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int
);

Route design:
Scenario 1:
"""
# POST /albums
#  Parameters:
#    title: Silent Alarm
#    release_year: 2008
#    artist_id: 857
#  Expected response (200 OK):
# None
"""

"""
# GET /albums
# Expected response (200 OK):
#   'Album(1, Thriller, 1982, 19), Album(2, Back In Black, 1980, 345), Album(3, The Bodyguard, 1992, 32), Album(4, Silent Alarm, 2008, 857) 
"""

Scenario 2:
"""
# POST /albums
#  Parameters:
#    None
#  Expected response (400 Bad request):
#  Please provide a album title, release year and artist ID
"""

Model Design:

class Album:
  # User facing properties: 
  #   id: Int
  #   title: string
  #   release_year: int
  #   artist_id


Repository design:

class AlbumRepository:
  #No properties except database connection object      

#Get all albums stored in the albums table as a list
def all():
  # Sql Used:
  #   SELECT id, title, release_year, artist_id FROM albums
  # Returns:
      list of Album objects
  


#add new album to albums table 
def add(title, release_year, artist_id):
  # Parameters:
  #   title: string
  #   release_year: int
  #   artist_id: int
  # Side effects:
  #   Adds record to album table
  # Sql used:
  #   INSERT INTO albums(title, release_year, artist_id) VALUES(%s,%s,%s)

Tests:

Album:
#when album object is created it has the correct properties

AlbumRepository:
#when all method is called i get a list of album objects back that represents all records in the albums table

#when add methods is called a new record is added to the albums table whose data matches the arguements passed into the method




