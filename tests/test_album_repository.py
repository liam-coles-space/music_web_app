from lib.album import Album
from lib.album_repository import AlbumRepository

#when all method is called i get a list of album objects back that represents all records in the albums table
def test_all_returns_records(db_connection):
    db_connection.seed("seeds/music_store.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new BookRepository

    albums = repository.all() # Get all books

    # Assert on the results
    assert albums == [
        Album(1, "Thriller", 1982, 19),
        Album(2, "Back In Black", 1980, 345),
        Album(3, "The Bodyguard", 1992, 32),
    ]


#when add methods is called a new record is added to the albums table whose data matches the arguements passed into the method
def test_add_method(db_connection):
    db_connection.seed("seeds/music_store.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new BookRepository

    repository.add('Silent Alarm', 2008, 784)

    albums = repository.all() # Get all books

    # Assert on the results
    assert albums == [
        Album(1, "Thriller", 1982, 19),
        Album(2, "Back In Black", 1980, 345),
        Album(3, "The Bodyguard", 1992, 32),
        Album(4, "Silent Alarm", 2008, 784),
    ]