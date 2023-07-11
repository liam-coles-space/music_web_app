import os
from flask import Flask, request
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist import Artist
from lib.artist_repository import ArtistRepository
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/albums', methods = ['POST'])
def post_albums():
    if 'title' not in request.form or 'release_year' not in request.form or 'artist_id' not in request.form:
        return 'Please provide a album title, release year and artist ID', 400
    connection = get_flask_database_connection(app)      
    repository = AlbumRepository(connection)
    repository.add(request.form['title'], request.form['release_year'], request.form['artist_id'])
    return 'Album Added'

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)      
    repository = AlbumRepository(connection)
    albums = str(repository.all())
    albums = albums.replace('[','')
    albums = albums.replace(']','')
    return albums
    
@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app) 
    repository = ArtistRepository(connection)
    artists = str(repository.all())
    artists = artists.replace('[','')
    artists = artists.replace(']','')
    return artists

@app.route('/artists', methods=['POST'])
def post_artists():
    if 'name' not in request.form or 'genre' not in request.form:
        return 'Please provide a name and genre', 400
    connection = get_flask_database_connection(app) 
    repository = ArtistRepository(connection)
    repository.add(request.form['name'], request.form['genre'])
    return 'Artist added'


# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

