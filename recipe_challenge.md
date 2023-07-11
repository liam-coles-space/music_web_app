# Request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone

# Request:
POST /artists

# With body parameters:
name=Wild nothing
genre=Indie

# Expected response (200 OK)
(No content)

# Then subsequent request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing

Tests:
Scenario 1:
# GET /artists
#   Expected response(200 OK):
"""
'Artist(1, Pixies, Grunge), Artist(2, ABBA, Pop), Artist(3, Taylor Swift, Country), Artist(4, Nina Simone, Blues), Artist(5, Wild nothing, Rock)'
"""

Scenario 2:
# POST /artists 
# Parameters:
#   name: Bloc Party
#   genre: Indie
# Expected Response (200 OK)
"""
None   
"""

# GET /artists
#   Expected response(200 OK):
"""
'Artist(1, Pixies, Grunge), Artist(2, ABBA, Pop), Artist(3, Taylor Swift, Country), Artist(4, Nina Simone, Blues),Artist(5, Wild nothing, Rock), Artist(6, Bloc Party, Indie)'
"""

Post /artists
# Parameters
#   None
# Expected Response (400 Bad Request):
"""
Please provide a name and genre
"""

Table design:

Nouns:
artist, name, genre

Record  ||  Properties
artist      name, genre

table: artists
id:SERIAL
name:text
genre: text

Model class for artists:
class Artist:
    # Attributes:
    #   id: int
    #   name: string
    #   genre: string

Repository class for artists:
class ArtistRepository:
    # Attributes:
    #   connection: db_connection object

    def all(self):
        # SQL used: 
        #   SELECT id, name, genre FROM artists
        # Returns:
        #   A list of Artist Objects

    def add(self, name, genre):
        #SQL used:
        #   INSERT INTO artists(name, genre) values(name,genre)
        

Artist tests:
#when Artist object is created it initializes with the correct properties

#when str function is called on Artist object it formats correctly

#when two Artist objects have same properties they assert as equal

ArtistRepository tests:

#when all method is called a list of Artist objects are returned, with each objects properties representing the data of a record from the artists table, with an object per record

#when add method is called a new record is created in the artists table with the data passed into the add method







