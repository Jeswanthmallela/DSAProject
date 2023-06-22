class Song:
    def init(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.next = None  

class Playlist:
    def init(self):
        self.head = None  
        self.tail = None  # Pointer to the last song in the playlist

    def addSong(self, title, artist, duration):
        newSong = Song(title, artist, duration)
        if not self.head:
            # If the playlist is empty, set the new song as the head and tail
            self.head = newSong
            self.tail = newSong
        else: 
            # Otherwise, add the new song to the end of the playlist
            self.tail.next = newSong
            self.tail = newSong

    def removeSong(self, title):
        current = self.head
        prev = None
        while current:
            if current.title == title:
                # If the current song matches the title, remove it from the playlist
                if current == self.head:
                    # If the song is the head of the playlist, update the head pointer
                    self.head = current.next
                elif current == self.tail:
                    # If the song is the tail of the playlist, update the tail pointer
                    self.tail = prev
                    self.tail.next = None
                else:
                    # Otherwise, update the previous song's pointer to skip over the current song
                    prev.next = current.next
                return True  # Return True to indicate that the song was successfully removed
            prev = current
            current = current.next
        return False  # Return False to indicate that the song was not found in the playlist

    def shufflePlaylist(self):
        # Convert the linked list to an array
        songsArray = []
        current = self.head
        while current:
            songsArray.append(current)
            current = current.next

        import random
        # Fisher-Yates shuffle algorithm
        for i in range(len(songsArray) - 1, 0, -1):
            j = random.randint(0, i)
            songsArray[i], songsArray[j] = songsArray[j], songsArray[i]

        # Convert the shuffled array back to a linked list
        self.head = songsArray[0]
        self.tail = songsArray[-1]
        for i in range(len(songsArray) - 1):
            songsArray[i].next = songsArray[i + 1]
        self.tail.next = None

playlist = Playlist()
playlist.addSong("Bohemian Rhapsody", "Queen", "5:55")
playlist.addSong("Stairway to Heaven", "Led Zeppelin", "8:02")
playlist.addSong("Hotel California", "Eagles", "6:30")
print(playlist)

playlist.removeSong("Stairway to Heaven")
print(playlist)

playlist.shufflePlaylist()
print(playlist)

class Song:
    def _init_(self, title, artist, duration, genre):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.genre = genre
        self.prev = None
        self.next = None

class PlaylistManager:
    def _init_(self):
        self.head = None
        self.tail = None
        self.graph = {}

    def addSong(self, title, artist, duration, genre):
        new_song = Song(title, artist, duration, genre)
        if not self.head:
            self.head = new_song
            self.tail = new_song
        else:
            self.tail.next = new_song
            new_song.prev = self.tail
            self.tail = new_song

        self.graph[new_song] = []
        
        current = self.head
        
        while current != new_song:
            if current.genre == new_song.genre or current.artist == new_song.artist:
                self.addConnection(current, new_song)
            current = current.next

    def removeSong(self, title):
        current = self.head
        while current:
            if current.title == title:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev

     
                del self.graph[current]

                return True

            current = current.next
        return False

    def addConnection(self, song1, song2):
        if song1 in self.graph and song2 in self.graph:
            if song2 not in self.graph[song1]:
                self.graph[song1].append(song2)
            if song1 not in self.graph[song2]:
                self.graph[song2].append(song1)

    def removeConnection(self, song1, song2):
        if song1 in self.graph and song2 in self.graph:
            self.graph[song1].remove(song2)
            self.graph[song2].remove(song1)

    def getPlaylist(self):
        playlist = []
        current = self.head
        while current:
            playlist.append(current.title)
            current = current.next
        return playlist

    def getRecommendedSongs(self, song):
        if song in self.graph:
            return [adj_song.title for adj_song in self.graph[song]]
        return []
        
playlistManager = PlaylistManager()
playlistManager.addSong("Bohemian Rhapsody", "Queen", "5:55","Rock")
playlistManager.addSong("Stairway to Heaven", "Led Zeppelin", "8:02","Rock")
playlistManager.addSong("Hotel California", "Eagles", "6:30","Country")
playlistManager.addSong("Da club", "50 Cent", "6:30","Rock")
playlistManager.addConnection(playlistManager.head, playlistManager.head.next)
playlistManager.addConnection(playlistManager.head.next, playlistManager.tail)
print(playlistManager.getPlaylist())
print(playlistManager.getRecommendedSongs(playlistManager.head))

class BSTNode:
    def _init_(self, song):
        self.song = song
        self.left = None
        self.right = None

class BST:
    def _init_(self):
        self.root = None

    def insert(self, song):
        if self.root is None:
            self.root = BSTNode(song)
        else:
            current = self.root
            while True:
                if song.title < current.song.title:
                    if current.left is None:
                        current.left = BSTNode(song)
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = BSTNode(song)
                        break
                    else:
                        current = current.right

    def search(self, title):
        current = self.root
        while current is not None:
            if title == current.song.title:
                return current.song
            elif title < current.song.title:
                current = current.left
            else:
                current = current.right
        return None

    def inorder_traversal(self, current):
        if current is not None:
            self.inorder_traversal(current.left)
            print(current.song)
            self.inorder_traversal(current.right)

    def remove_song(self, title):
        self.root = self._delete_recursive(title, self.root)

    def _delete_recursive(self, title, current):
        if current is None:
            return current
        if title < current.song.title:
            current.left = self._delete_recursive(title, current.left)
        elif title > current.song.title:
            current.right = self._delete_recursive(title, current.right)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            temp = self._find_min(current.right)
            current.song = temp.song
            current.right = self._delete_recursive(temp.song.title, current.right)
        return current

    def _find_min(self, current):
        while current.left is not None:
            current = current.left
        return current

class HashTable:
    def _init_(self):
        self.size = 100
        self.table = [None] * self.size

    def _hash_function(self, song_id):
        return song_id % self.size

    def insert(self, song):
        key = self._hash_function(song.id)
        if self.table[key] is None:
            self.table[key] = [song]
        else:
            self.table[key].append(song)

    def search(self, song_id):
        key = self._hash_function(song_id)
        if self.table[key] is not None:
            for song in self.table[key]:
                if song.id == song_id:
                    return song
        return None

class Song:
    def _init_(self, id, title, artist, duration, genre):
        self.id = id
        self.title = title
        self.artist = artist
        self.duration = duration
        self.genre = genre

    def _str_(self):
        return f"ID: {self.id}, Title: {self.title}, Artist: {self.artist}, Duration: {self.duration}, Genre: {self.genre}"

class PlaylistManager:
    def _init_(self):
        self.bst = BST()
        self.hash_table = HashTable()

    def add_song(self, song):
        self.bst.insert(song)
        self.hash_table.insert(song)

    def remove_song(self, title):
        song = self.bst.search(title)
        if song:
            del self.hash_table.table[self.hash_table._hash_function(song.id)]
            self.bst.remove_song(title)
            print("Song removed from the playlist.")
        else:
            print("Song not found in the playlist.")

    def search_song(self, title):
        return self.bst.search(title)

    def display_playlist(self):
        self.bst.inorder_traversal(self.bst.root)

class PM:
    def _init_(self):
        self.playlist_manager = PlaylistManager()

    def add_song(self):
        print("Add a Song")
        id = int(input("Enter song ID: "))
        title = input("Enter song title: ")
        artist = input("Enter artist name: ")
        duration = int(input("Enter song duration: "))
        genre = input("Enter song genre: ")
        song = Song(id, title, artist, duration, genre)
        self.playlist_manager.add_song(song)
        print("Song added to the playlist.")

    def remove_song(self):
        print("Remove a Song")
        title = input("Enter song title: ")
        self.playlist_manager.remove_song(title)

    def search_song(self):
        print("Search for a Song")
        title = input("Enter song title: ")
        song = self.playlist_manager.search_song(title)
        if song:
            print(song)
        else:
            print("Song not found in the playlist.")

    def display_playlist(self):
        print("Playlist")
        self.playlist_manager.display_playlist()

    def run(self):
        while True:
            print("Menu:")
            print("1. Add a Song")
            print("2. Remove a Song")
            print("3. Search for a Song")
            print("4. Display Playlist")
            print("0. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_song()
            elif choice == "2":
                self.remove_song()
            elif choice == "3":
                self.search_song()
            elif choice == "4":
                self.display_playlist()
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")
ui = PM()
ui.run()