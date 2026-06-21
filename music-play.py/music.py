class playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.songs = []
        print(f"playlist '{self.name}' of genre '{self.genre}' created.")
    def add_song(self, song):
        self.songs.append(song)
        print(f"song '{song}' added to playlist '{self.name}'.")
    def remove_song(self, song):
            if song in self.songs:
                self.songs.remove(song)
                print(f"song '{song}' removed from playlist '{self.name}'.")
            else:
                print(f"song '{song}' not found in playlist '{self.name}'.")
    def display(self):
        print(f"\n---{self.name} ({self.genre})---")
        if self.songs:
            for i, song in enumerate(self.songs, 1):
                print(f"{i}. {song}")
        else:
            print("No songs in this playlist.")
    def __delete__(self):
        print(f"playlist '{self.name}' deleted.")
my_playlist = playlist("Chill Vibes", "Pop")
while True:
    print("\n1. Add song 2. Remove song 3. Display playlist 4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        song = input("Enter song name to add: ")
        my_playlist.add_song(song)
    elif choice == '2':
        song = input("Enter song name to remove: ")
        my_playlist.remove_song(song)
    elif choice == '3':
        my_playlist.display()    
    elif choice == '4':
        my_playlist.__delete__()
        break