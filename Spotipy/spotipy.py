from artist import Artist,Album,Song
class SpotiPy:

    def __init__(self):
        self.__artists = []

    def getArtists (self):
        return self.__artists

    def addArtists (self, *artists):
        added = 0
        if(self.__artists == []):
            self.__artists.append(Artist("default", "default", 0, [], []))
            for index1 in range(len(artists)):
                t = True
                for index2 in range(len(self.__artists)):
                    if (artists[index1].getFirstName() == self.__artists[index2].getFirstName()
                            and artists[index1].getLastName() == self.__artists[index2].getLastName()
                            and artists[index1].getBirthYear() == self.__artists[index2].getBirthYear()):
                        t = False
                if (t):
                    self.__artists.append(artists[index1])
                    added += 1
            self.__artists = self.__artists[1:]
            return added
        for index1 in range(len(artists)):
            t = True
            for index2 in range(len(self.__artists)):
              if (artists[index1].getFirstName() == self.__artists[index2].getFirstName()
              and artists[index1].getLastName() == self.__artists[index2].getLastName()
              and artists[index1].getBirthYear() == self.__artists[index2].getBirthYear()):
                t = False
            if(t):
                self.__artists.append(artists[index1])
                added += 1
        return added

    def getTopTrendingArtist (self):
        artists = sorted(self.__artists, key=lambda artist: artist.totalLikes(), reverse=True)
        return (artists[0].getFirstName(),artists[0].getLastName())

    def getTopTrendingAlbum (self):
        Max = 0
        ansAlbum = Album("default",0)
        for artist in self.__artists:
            for album in artist.getAlbums():
                likes = 0
                for song in album.getSongs():
                    likes += song.getLikes()
                if(likes > Max):
                    ansAlbum = album
                    Max = likes

        return ansAlbum

    def getTopTrendingSong (self):
        songs = sorted(self.__artists, key=lambda artist: artist.mostLikedSong(), reverse=True)
        return songs[0].getTitle()

    @staticmethod
    def loadfromfile (newFile):
        file = open(newFile,"r")
        str = file.read()
        spotipy = SpotiPy()
        index = -1
        temp = ""
        for char in str:
            index += 1
            if (char != "\n"):
                if (not ((char == " "
                          and index >= 1
                          and index <= len(str) - 2
                          and (not (str[index - 1].isalpha()
                                    and str[index + 1].isalpha())))
                )):
                    temp += char
        str = temp
        str = str[9:]
        str = str[:-1]
        artists = str.split("#")

        def prefixRemover(string, key):
             index = 0
             while (string[index] != key and index < len(string) - 1):
                    index += 1

             return (string[index + 1:], string[:index])

        def takeAlbums(str, albums):
             str = str[8:]
             str = str[:-1]
             strAlbums = str.split("%")

             def takeSongs(str, songs):
                     str = str[7:]
                     str = str[:-1]
                     strSongs = str.split("|")

                     def formatmaker(minutes):
                             if (minutes.is_integer()):
                                    return int(minutes)
                             return minutes

                     for song in strSongs:
                                title = prefixRemover(song, ",")[1]
                                song = prefixRemover(song, ",")[0]
                                strDuration = prefixRemover(song, ",")[1]
                                strDuration = strDuration[:-7]
                                duration = formatmaker(float(strDuration))
                                print(duration)
                                song = prefixRemover(song, ",")[0]
                                releaseYear = int(prefixRemover(song, ",")[1])
                                song = prefixRemover(song, ",")[0]
                                likes = int(song)
                                newSong = Song(title, releaseYear, duration, likes)
                                songs.append(newSong)

                     return songs

             for album in strAlbums:
                            name = prefixRemover(album, ",")[1]

                            album = prefixRemover(album, ",")[0]
                            releaseYear = int(prefixRemover(album, ",")[1])

                            album = prefixRemover(album, ",")[0]
                            songs = []
                            songs = takeSongs(album, songs)

                            newAlbum = Album(name, releaseYear)
                            for song in songs:
                               newAlbum.addSongs(song)
                            albums.append(newAlbum)


             return albums

        def takeSingles(str, songs):
                str = str[:-1]
                strSongs = str.split("|")

                def formatmaker(minutes):
                         if (minutes.is_integer()):
                                return int(minutes)
                         return minutes

                for song in strSongs:
                            title = prefixRemover(song, ",")[1]
                            song = prefixRemover(song, ",")[0]
                            strDuration = prefixRemover(song, ",")[1]
                            strDuration = strDuration[:-7]
                            duration = formatmaker(float(strDuration))
                            song = prefixRemover(song, ",")[0]
                            releaseYear = int(prefixRemover(song, ",")[1])
                            song = prefixRemover(song, ",")[0]
                            likes = int(song)
                            newSong = Song(title, releaseYear, duration, likes)
                            songs.append(newSong)

                return songs

        for artist in artists:
                        firstname = prefixRemover(artist, ",")[1]

                        artist = prefixRemover(artist, ",")[0]
                        lastname = prefixRemover(artist, ",")[1]

                        artist = prefixRemover(artist, ",")[0]
                        birthYear = int(prefixRemover(artist, ",")[1])

                        artist = prefixRemover(artist, ",")[0]
                        lst = artist.split(",singles:{")
                        albums = takeAlbums(lst[0], [])

                        singles = takeSingles(lst[1], [])
                        newArtist = Artist(firstname, lastname, birthYear, albums, singles)

                        spotipy.__artists.append(newArtist)

        return spotipy

    def __str__(self):
        ans = ""
        for artist in self.__artists:
            ans += artist.__str__() + "\n"
        return ans









































