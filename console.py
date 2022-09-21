from models import album
from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository



artist1 = Artist("Green Day")
artist_repository.save(artist1)

album1 = Album("Warning", "Pop-Punk", artist1.id)
album_repository.save(album1)

# album_repository.delete_all()
# artist_repository.delete_all()

result = artist_repository.select(1)
print (result.__dict__)

result = album_repository.select(1)
print (result.__dict__)

results = artist_repository.select_all()
for result in results:
    print (result.__dict__)

results = album_repository.select_all()
for result in results:
    print (result.__dict__)