from models import album
from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository


#Creating artists and albums
artist1 = Artist("Green Day")
artist_repository.save(artist1)

artist2 = Artist("Built to Spill")
artist_repository.save(artist2)

album1 = Album("Warning", "Pop-Punk", artist1.id)
album_repository.save(album1)

album2 = Album("Perfect From Now On", "Indie-Rock", artist2.id)
album_repository.save(album2)

album3 = Album("Keep It Like a Secret", "Indie-Rock", artist2.id)
album_repository.save(album3)




# album_repository.delete(1)
# artist_repository.delete(1)

# album_repository.delete_all()
# artist_repository.delete_all()


#Updating artist and album names
artist1.name = 'Foxboro Hot Tubs'
artist_repository.update(artist1)

album1.title = 'Stop, Drop and Roll!'
album_repository.update(album1)


#Returning all albums by artist
results = artist_repository.select_albums_by_artist(artist2)
print (artist2.name)
for result in results:
    print (result.__dict__)


#Returning single artist and single album
result = artist_repository.select(1)
print (result.__dict__)

result = album_repository.select(1)
print (result.__dict__)


#Returning all artists and all albums
results = artist_repository.select_all()
for result in results:
    print (result.__dict__)

results = album_repository.select_all()
for result in results:
    print (result.__dict__)