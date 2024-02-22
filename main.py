from PIL import Image as Img, ImageFont, ImageDraw, ImageTk
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog, colorchooser
from tkinter.colorchooser import askcolor
from tkinter import messagebox
from tkinter import ttk

FONT = ("Arial", 10)
OPTION_LIST = ["top left", "top centre", "top right", "centre left", "centre", "centre right",
               "bottom left", "bottom centre", "bottom right"]


# ---- Functions ---------


def browse_files():
    filename = filedialog.askopenfilename(initialdir="C:/Desktop", title="Select Img",
                                          filetypes=[("image files", ".jpg"), ("image files", ".jpeg"),
                                                     ("image files", ".png")])

    # Change label contents
    entry_file_explorer.delete(0, END)
    entry_file_explorer.insert(0, filename)


def choose_color():
    # variable to store hexadecimal code of color
    color_code = colorchooser.askcolor(title="Choose color")

    label_RGB_colour_r.configure(text=f"{color_code[0][0]}")
    label_RGB_colour_g.configure(text=f"{color_code[0][1]}")
    label_RGB_colour_b.configure(text=f"{color_code[0][2]}")


def get_position():
    position = position_selected.get()
    if position == "top left":
        text_anchor = (0, 0)
    elif position == "top centre":
        text_anchor = (1500, 0)
    elif position == "top left":
        text_anchor = (3000, 0)
    elif position == "centre left":
        text_anchor = (0, 1000)
    elif position == "centre":
        text_anchor = (1500, 1000)
    elif position == "centre right":
        text_anchor = (3000, 1000)
    elif position == "bottom left":
        text_anchor = (0, 2000)
    elif position == "bottom centre":
        text_anchor = (1500, 2000)
    elif position == "bottom right":
        text_anchor = (3000, 2000)
    else:
        text_anchor = (0, 0)
    return text_anchor


def font_size():
    font_size_selected = entry_font_size.get()
    return int(font_size_selected)


def get_opacity():
    opacity_selected = scale_opacity_selector.get()
    return int(opacity_selected)


def show_preview():

    image = Img.open(entry_file_explorer.get())

    watermark_image = image.copy()

    base_image = watermark_image.convert("RGBA")

    txt_img = Img.new("RGBA", base_image.size, (255, 255, 255, 0))

    text_font = ImageFont.truetype("arial.ttf", font_size())

    draw = ImageDraw.Draw(txt_img)

    # draw text at half opacity
    draw.text(get_position(), entry_text_watermark.get(), font=text_font, align="center",
              fill=(int(label_RGB_colour_r.cget("text")), int(label_RGB_colour_g.cget("text")),
                    int(label_RGB_colour_b.cget("text")), get_opacity()))

    composite = Img.alpha_composite(base_image, txt_img)

    plt.imshow(composite)
    plt.show()


def save_file():
    image = Img.open(entry_file_explorer.get())

    watermark_image = image.copy()

    base_image = watermark_image.convert("RGBA")

    txt_img = Img.new("RGBA", base_image.size, (255, 255, 255, 0))

    text_font = ImageFont.truetype("arial.ttf", font_size())

    draw = ImageDraw.Draw(txt_img)

    # draw text at half opacity
    draw.text(get_position(), entry_text_watermark.get(), font=text_font, align="center",
              fill=(int(label_RGB_colour_r.cget("text")), int(label_RGB_colour_g.cget("text")),
                    int(label_RGB_colour_b.cget("text")), get_opacity()))

    composite = Img.alpha_composite(base_image, txt_img)
    composite.save("watermark_image.png")
    open("watermark_image.png")


# ---------------------------- GUI SETUP ------------------------------- #

# Creating tkinter window
root = Tk()
root.title("Image Watermarker 1.0")
root.config(pady=10, padx=10)
# PC Screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Center coordinates of screen
center_x = int(screen_width/2 - 250)
center_y = int(screen_height/2 - 300)
# Set position in center of screen
root.geometry(f"500x350+{center_x}+{center_y}")


# File Explorer
# Label
label_file_explorer = Label(text="Image", width=10, font=FONT, justify="left", anchor="w")
label_file_explorer.grid(row=1, column=0, columnspan=1, pady=5, padx=5)
# Entry
entry_file_explorer = Entry(root, width=30, font=FONT)
entry_file_explorer.grid(row=1, column=1, columnspan=3, pady=5, padx=5, sticky=W)
entry_file_explorer.insert(0, "File Directory")
# Button
button_explore = Button(text="Browse Files", width=10, command=browse_files)
button_explore.grid(row=1, column=4, columnspan=1, pady=5, padx=5, )


# Watermarker Text
# Label
label_text_watermark = Label(text="Text", width=10, font=FONT, justify="left", anchor="w")
label_text_watermark.grid(row=2, column=0, columnspan=1, pady=5, padx=5)
# Entry
entry_text_watermark = Entry(root, width=30, font=FONT)
entry_text_watermark.grid(row=2, column=1, columnspan=3, pady=5, padx=5, sticky=W)
entry_text_watermark.insert(0, "Sample Watermark")

# Watermarker Text Font Size
# Label
label_font_size = Label(text="Size", width=10, font=FONT, justify="left", anchor="w")
label_font_size.grid(row=3, column=0, columnspan=1, pady=5, padx=5)
# Entry
entry_font_size = Entry(root, width=5, font=FONT, justify="left")
entry_font_size.grid(row=3, column=1, pady=5, padx=5, sticky=W)
entry_font_size.insert(0, "10")

# Watermarker Opacity
# Label
label_opacity_selector = Label(text="Clarity", width=10, font=FONT, justify="left", anchor="w")
label_opacity_selector.grid(row=4, column=0, columnspan=1, pady=5, padx=5)
# Scale
scale_opacity_selector = Scale(root, from_=0, to=255, orient=HORIZONTAL, font=FONT, length=200)
scale_opacity_selector.grid(row=4, column=1, pady=5, padx=5, sticky=W)

# Position Selection
# Label
label_position = Label(text="Position", width=10, font=FONT, justify="left", anchor="w")
label_position.grid(row=5, column=0, columnspan=1, pady=5, padx=5)
# Option Menu
position_selected = StringVar(root)
position_selected.set(OPTION_LIST[3])  # default value
option_menu_widget = OptionMenu(root, position_selected, *OPTION_LIST)
option_menu_widget.config(font=FONT)
option_menu_widget.grid(row=5, column=1, columnspan=1, pady=5, padx=5, sticky=W)

# Colour Selection
# Label
label_color_option = Label(text="Colour", width=10, font=FONT, justify="left", anchor="w")
label_color_option.grid(row=7, column=0, columnspan=1, pady=5, padx=5)
label_RGB_colour_r = Label(text=int(255), width=5, font=FONT)
# label_RGB_colour_r.grid(row=7, column=2, columnspan=1, pady=5, padx=5)
label_RGB_colour_g = Label(text=int(255), width=5, font=FONT)
# label_RGB_colour_g.grid(row=7, column=3, columnspan=1, pady=5, padx=5)
label_RGB_colour_b = Label(text=int(255), width=5, font=FONT)
# label_RGB_colour_b.grid(row=7, column=4, columnspan=1, pady=5, padx=5)
# Button
button_RGB_colour = Button(text=f"R G B", width=20, command=choose_color)
button_RGB_colour.grid(row=7, column=1, columnspan=2, pady=5, padx=5, sticky=W)

# Preview
button_preview = Button(text="Preview", width=30, font=FONT, activebackground="yellow", command=show_preview)
button_preview.grid(row=8, column=1, columnspan=3, pady=10, padx=5)

# Save
button_save = Button(text="Save", width=30, font=FONT, activebackground="green", activeforeground="white",
                     command=save_file)
button_save.grid(row=9, column=1, columnspan=3, pady=10, padx=5)

root.mainloop()
