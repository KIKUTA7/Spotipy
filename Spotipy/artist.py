from album import Album, Song
class Artist:

    def __init__(self,firstName,lastName,birthYear,albums,singles):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__birthYear = birthYear
        self.__albums = albums
        self.__singles = singles

    def getFirstName (self):
        return self.__firstName

    def getLastName (self):
        return self.__lastName

    def getBirthYear (self):
        return self.__birthYear

    def getAlbums (self):
        return self.__albums

    def getSongs (self):
        return self.__singles

    def mostLikedSong (self):
        Max = 0
        ans = Song("default",0,0,0)
        singleLikes = lambda single: single.getLikes()
        newSingles = sorted(self.__singles, key=singleLikes, reverse=False)
        topSong = newSingles.pop(len(newSingles) - 1)
        if Max < topSong.getLikes():
            ans = topSong
        Max = max(Max, topSong.getLikes())

        for album in self.__albums:
            singleLikes = lambda single: single.getLikes()
            newSingles = sorted(album.getSongs(), key=singleLikes, reverse=False)
            topSong = newSingles.pop(len(newSingles) - 1)
            if Max < topSong.getLikes():
                ans = topSong
            Max = max(Max, topSong.getLikes())

        return ans

    def leastLikedSong (self):
        Max = 0
        ans = Song("default",0,0,0)
        singleLikes = lambda single: single.getLikes()
        newSingles = sorted(self.__singles, key=singleLikes, reverse=True)
        topSong = newSingles.pop(len(newSingles) - 1)
        if Max > topSong.getLikes():
            ans = topSong
        Max = max(Max, topSong.getLikes())

        for album in self.__albums:
            singleLikes = lambda single: single.getLikes()
            newSingles = sorted(album.getSongs(), key=singleLikes, reverse=True)
            topSong = newSingles.pop(len(newSingles) - 1)
            if Max > topSong.getLikes():
                ans = topSong
            Max = max(Max, topSong.getLikes())

        return ans

    def totalLikes (self):
        ans = 0
        for single in self.__singles:
            ans += single.getLikes()


        for album in self.__albums:
            for single in album.getSongs():
                 ans += single.getLikes()

        return ans

    def __str__(self):
        return f'Name: {self.__firstName} {self.__lastName},Birth year:{self.__birthYear},Total likes:{self.totalLikes()}'













