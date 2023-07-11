DROP TABLE IF EXISTS albums;

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title text,
    release_year int,
    artist_id int
);

INSERT INTO albums(title, release_year, artist_id) values
    ('Thriller', 1982, 19), 
    ('Back In Black', 1980, 345),
    ('The Bodyguard', 1992, 32);