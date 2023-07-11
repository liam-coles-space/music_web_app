from lib.album_repository import AlbumRepository

# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===


"""
Scenario 1:
# POST /albums
#  Parameters:
#    title: Silent Alarm
#    release_year: 2008
#    artist_id: 857
#  Expected response (200 OK):
# Album added

# GET /albums
# Expected response (200 OK):
#   'Album(1, Thriller, 1982, 19), Album(2, Back In Black, 1980, 345), Album(3, The Bodyguard, 1992, 32), Album(4, Silent Alarm, 2008, 857)' 
"""

def test_post_albums_adds_record(db_connection, web_client):
    db_connection.seed("seeds/music_store.sql") # Seed our database with some test data
    response = web_client.post('/albums', data = {'title':'Silent Alarm','release_year': 2008, 'artist_id':857})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == 'Album Added'
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == 'Album(1, Thriller, 1982, 19), Album(2, Back In Black, 1980, 345), Album(3, The Bodyguard, 1992, 32), Album(4, Silent Alarm, 2008, 857)' 

    
"""    
Scenario 2:

# POST /albums
#  Parameters:
#    None
#  Expected response (400 Bad request):
#  Please provide a album title, release year and artist ID
"""
def test_post_errors_if_wrong_form_passed(db_connection, web_client):
    db_connection.seed("seeds/music_store.sql") # Seed our database with some test data
    response = web_client.post('/albums', data = {'goat':'Silent Alarm','release_year': 2008, 'artist_id':857})
    assert response.status_code == 400
    assert response.data.decode("utf-8") == 'Please provide a album title, release year and artist ID'