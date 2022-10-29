from song import Song
class Album:


    def __init__(self,title,releaseYear):
        self.__title = title
        self.__releaseYear = releaseYear
        self.__songs = []

    def getTitle (self):
        return self.__title

    def getReleaseYear (self):
        return self.__releaseYear

    def getSongs (self):
        return self.__songs

    def sortBy (self,byKey,reverse):
        if(reverse):
            self.__songs = sorted(self.__songs, key=byKey, reverse=False)
        else:
            self.__songs = sorted(self.__songs, key=byKey, reverse=True)
        return self.__songs

    def sortByNames (self,reverse):
        self.sortBy(lambda song: song.getTitle().lower(), reverse)

    def sortByLikes (self, reverse):
        self.sortBy(lambda song: song.getLikes(), reverse)

    def sortByDuration (self,reverse):
        self.sortBy(lambda song: song.getDuration(),reverse)

    def sortByReleaseYear (self,reverse):
        self.sortBy(lambda song: song.getReleaseYear(),reverse)



    def addSongs (self,*songs):
        added = 0
        if(self.__songs == []):
            self.__songs.append(Song("default", 0, 0, 0))
            for index1 in range(len(songs)):
                t = True
                for index2 in range(len(self.__songs)):
                    if ((songs[index1].getTitle() == self.__songs[index2].getTitle()
                         and songs[index1].getDuration() == self.__songs[index2].getDuration()
                         and songs[index1].getReleaseYear() == self.__songs[index2].getReleaseYear())):
                        t = False
                if (t):
                    self.__songs.append(songs[index1])
                    added += 1
            self.__songs = self.__songs[1:]
            return added
        for index1 in range(len(songs)):
            t = True
            for index2 in range(len(self.__songs)):
              if ((songs[index1].getTitle() == self.__songs[index2].getTitle()
              and songs[index1].getDuration() == self.__songs[index2].getDuration()
              and songs[index1].getReleaseYear() == self.__songs[index2].getReleaseYear())):
                t = False
            if(t):
                self.__songs.append(songs[index1])
                added += 1
        return added

    def __str__(self):
        def strSongs (songs):
            anstr = ""
            for song in songs:
                anstr += song.__str__()
                anstr += "|"
            anstr = anstr.removesuffix("|")
            return '{' + anstr + '}'
        return f'Title:{self.__title},Release year:{self.__releaseYear},songs:{strSongs(self.__songs)}'





