from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

artist1 = Artist("Green Day")
artist_repository.save(artist1)