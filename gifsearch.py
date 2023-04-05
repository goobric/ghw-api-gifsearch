import requests
import tkinter as tk
from PIL import Image, ImageTk

# Set up parameters for API request
api_key = '<AIzaSyBcZJR24IegQGSVyeWF2Hz5FlRg9Ojp7lU>'
search_term = 'cat'  # Change this to the search term you want

params = {
    'key': api_key,
    'q': search_term,
    'limit': 10
}

# Make API request to search for GIFs
response = requests.get('https://api.tenor.com/v1/search', params=params)

# Check if request was successful
if response.status_code == 200:
    # Get list of GIFs from response JSON
    gifs = response.json()['results']

    # Create GUI window
    root = tk.Tk()
    root.title(f'Search Results for "{search_term}"')

    # Create grid of GIFs
    row = 0
    column = 0
    for gif in gifs:
        # Download GIF image
        gif_url = gif['media'][0]['gif']['url']
        gif_data = requests.get(gif_url).content

        # Convert image data to Tkinter PhotoImage
        img = Image.open(BytesIO(gif_data))
        photo = ImageTk.PhotoImage(img)

        # Add PhotoImage to GUI window
        label = tk.Label(root, image=photo)
        label.photo = photo
        label.grid(row=row, column=column)

        # Increment row/column indices
        column += 1
        if column == 5:
            row += 1
            column = 0

    root.mainloop()
else:
    print('Error: API request failed.')