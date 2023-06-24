from tkinter import Canvas
def make_home_view(parent_frame:str, imgs:dict)-> None:
    home_canvas = Canvas(
        parent_frame,
        bg = "#FFFFFF",
        height = 600,
        width = (1000-277),
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    home_canvas.pack()

    home_canvas.create_text(
        (1000-277)/2-100,
        170,
        anchor="nw",
        text="Waste Management System",
        fill="#2F3061",
        font=("Lato SemiBold", 20 * -1)
    )

    # home_canvas.create_image(
    #     (1000-277)/2-100,
    #     200,
    #     image = imgs["logo"],
    # )

    home_canvas.create_text(
        (1000-277)/2-330,
        223.0,
        anchor="nw",
        text="Welcome to the waste management system, a technological solution for efficiently\nmanaging and reducing waste in our communities. Our system utilizes sensors\nto detect when dustbins are full, allowing for more efficient and timely\ncollection of waste. By using this system, we can not only improve sanitation\nand reduce litter, but also help to protect the environment and conserve\nresources.Thank you for using the waste management system and doing your\npartto create a cleaner, healthier world for all.",
        fill="#343434",
        font=("Lato Italic", 18 * -1)
    )
