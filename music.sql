-- music.sql

-- Table to store information about artists
CREATE TABLE artists (
    artist_id INTEGER PRIMARY KEY AUTOINCREMENT,
    artist_name TEXT NOT NULL UNIQUE
);

-- Table to store information about albums
CREATE TABLE albums (
    album_id INTEGER PRIMARY KEY AUTOINCREMENT,
    album_name TEXT NOT NULL,
    artist_id INTEGER NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
);

-- Table to store information about songs
CREATE TABLE songs (
    song_id INTEGER PRIMARY KEY AUTOINCREMENT,
    song_name TEXT NOT NULL,
    album_id INTEGER NOT NULL,
    track_number INTEGER NOT NULL,
    song_length_seconds INTEGER NOT NULL,
    FOREIGN KEY (album_id) REFERENCES albums(album_id),
    UNIQUE (album_id, track_number)
);

-- Optional Indexes
CREATE INDEX idx_artist_name ON artists (artist_name);
CREATE INDEX idx_album_name ON albums (album_name);
CREATE INDEX idx_album_id ON songs (album_id);
