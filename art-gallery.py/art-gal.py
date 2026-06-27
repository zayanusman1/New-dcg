class ArtGallery:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.artworks = []
        print(f"Art Gallery '{self.name}' located at '{self.location}' has been created.")
        print("Welcome to the Art Gallery Management System!")
        print("You can add, view, and manage artworks in the gallery.")
    
    def add_artwork(self, artwork):
        self.artworks.append(artwork)
        print(f"Artwork '{artwork}' has been added to the gallery.")
    def remove_artwork(self, artwork):
        if artwork in self.artworks:
            self.artworks.remove(artwork)
            print(f"Artwork '{artwork}' has been removed from the gallery.")
        else:
            print(f"Artwork '{artwork}' not found in the gallery.")
    def view_artworks(self):
        print(f"\n--- {self.name} Artworks ---")
        if self.artworks:
            for number, artwork in enumerate(self.artworks, start=1):
                print(f"{number}. {artwork}")
        else:
            print("No artworks available in the gallery.")
    def __delete__(self):
        print(f"\nClosing the Art Gallery '{self.name}'. Thank you for visiting!")
gallery = ArtGallery("Modern Art Gallery", "Downtown")
while True:
    print("\nOptions:")
    print("1. Add Artwork")
    print("2. Remove Artwork")
    print("3. View Artworks")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        artwork_name = input("Enter the name of the artwork to add: ")
        gallery.add_artwork(artwork_name)
    elif choice == '2':
        artwork_name = input("Enter the name of the artwork to remove: ")
        gallery.remove_artwork(artwork_name)
    elif choice == '3':
        gallery.view_artworks()
    elif choice == '4':
        gallery.__delete__()
        break
    else:
        print("Invalid choice. Please try again.")
        