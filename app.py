import tkinter as tk
import data, fetchMetadata, io
import requests
from PIL import ImageTk, Image
def getdata():
    response = fetchMetadata.getdata(box4.get())
    name = response[0]
    artist = response[1]
    cover = response[2]
    recordname.delete(0, tk.END)
    artistname.delete(0, tk.END)
    recordname.insert(0, name)
    artistname.insert(0, artist)
    raw_data = requests.get(cover)
    img = ImageTk.PhotoImage(Image.open(io.BytesIO(raw_data.content)).resize((255,255)))
    image.configure(image=img)
    image.image=img
    

# In total the entries that should be here are the following:
# "tier": which tier the album should enter
# "link"|"bandcamp": a link to the bandcamp page of the album
# the cover, artist and name should also be gotten but have to be editable
# so add a button to "get metadata" and then edit
# the cover should also be previewed
# "comment": quick comment on the record
# "tags": which tags should be added
# "realartist": which artist(s) the alias applies to

# The program should be similar to the design.jpg file
# The designLayout.jpg file is meant so that I don't get confused with which div is called what.

# Moving objects up and down is not a priority
# That should do for enough documentation

window = tk.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=5)
window.rowconfigure(0, weight=10)
window.rowconfigure(1, weight=2)
window.rowconfigure(3, weight=6)

box1 = tk.Frame(
    borderwidth=3,
    master=window,
    relief=tk.RAISED
)
box1.grid(
    column=0,
    row=0,
)
box2 = tk.Frame(
    borderwidth=3,
    master=window,
    relief=tk.RAISED
)
box2.grid(
    column=1,
    row=0
)
box3 = tk.Button(
    borderwidth=3,
    master=window,
    relief=tk.RAISED,
    text="Submit",
    command=getdata
)
box3.grid(
    column=0,
    row=1
)
box4 = tk.Entry(
    borderwidth=3,
    master=window,
    relief=tk.RAISED,
    width=69
)
box4.grid(
    column=1,
    row=1
)
box5 = tk.Frame(
    borderwidth=3,
    master=window,
    relief=tk.RAISED
)
box5.grid(
    column=0,
    row=2,
    columnspan=2
)
namebox = tk.Frame(
    borderwidth=3,
    master=box5,
    relief=tk.RAISED
)
namebox.grid(
    column=2,
    row=0
)
tageditor = tk.Frame(
    borderwidth=3,
    master=box5,
    relief=tk.RAISED
)
tageditor.grid(column=1, row=0)

tag1 = tk.Entry(
    borderwidth=3,
    master=tageditor,
    relief=tk.RAISED
)
tag1.pack()
tag2 = tk.Entry(
    borderwidth=3,
    master=tageditor,
    relief=tk.RAISED
)
tag2.pack()
tag3 = tk.Entry(
    borderwidth=3,
    master=tageditor,
    relief=tk.RAISED
)
tag3.pack()
tag4 = tk.Entry(
    borderwidth=3,
    master=tageditor,
    relief=tk.RAISED
)
tag4.pack()

commentbox = tk.Text(
    borderwidth=3,
    master=box5,
    relief=tk.RAISED,
    width=25,
    height=10
)
commentbox.grid(row=0, column=0)

def clearInfo():
    box4.delete(0, tk.END)
    commentbox.delete("1.0", tk.END)
    recordname.delete(0, tk.END)
    artistname.delete(0, tk.END)
    image.image=""
    tag1.delete(0,tk.END)
    tag2.delete(0,tk.END)
    tag3.delete(0,tk.END)
    tag4.delete(0,tk.END)
    realartist.delete(0, tk.END)
    realartist2.delete(0, tk.END)

def sendInfo():
    tags = []
    if tag1.get() != "":
        tags.append(tag1.get())   
    if tag2.get() != "":
        tags.append(tag2.get())    
    if tag3.get() != "":
        tags.append(tag3.get())   
    if tag4.get() != "":
        tags.append(tag4.get())

    realartists = []
    if realartist != "":
        realartists.append(realartist.get())
    if realartist2 != "":
        realartists.append(realartist2.get())
    data.insertNewRecord(recordname.get(),artistname.get(),
                        fetchMetadata.getdata(box4.get())[2],
                        box4.get(), 
                        commentbox.get("1.0", tk.END),
                        tags, realartists)

recordname = tk.Entry(
    borderwidth=3,
    master=namebox,
    relief=tk.RAISED,
    width=35,
    bg="pink"
)
recordname.pack()
artistname = tk.Entry(
    borderwidth=3,
    master=namebox,
    relief=tk.RAISED,
    width=35,
    bg="pink"
)
artistname.pack()
realartist = tk.Entry(
    borderwidth=3,
    master=namebox,
    relief=tk.RAISED,
    width=35
)
realartist.pack()
realartist2 = tk.Entry(
    borderwidth=3,
    master=namebox,
    relief=tk.RAISED,
    width=35
)
realartist2.pack()
# https://dreamcatalogue.bandcamp.com/album/upgrade-yourslf 
# used for testing
image = tk.Label(master=box5)
image.grid(column=3, row=0)

label = tk.Button(master=box1, text="Clear", command=clearInfo, bg="red")  
label2 = tk.Button(master=box2, text="Save", command=sendInfo, bg="green")
label.pack() 
label2.pack()

window.title("tkinter is hell!")
  
window.mainloop()