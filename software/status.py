from tkinter import Canvas,Frame

def get_data():
    with open("data.txt", mode="r",encoding="utf-8") as data_file:
            code, status, time_of_full = data_file.read().replace('\n','').split(',')        
            with open("data_files/dust_bins_info.txt", mode="r", encoding="utf-8") as dust_bins:
                dust_bin_list = dust_bins.read().split('\n')[:-1]
                for each in dust_bin_list:
                    dust_bin_data = each.split(',,')
                    print(dust_bin_data)
                    if code in dust_bin_data:
                        code_to_show = dust_bin_data[1]
                        address = dust_bin_data[2]
                        location = dust_bin_data[3]

    if status == "FULL":
        status_text_color = "red"
    else:
        status_text_color = "green"
    return {"code":code_to_show,"address":address,"location": location, "status_text_color":status_text_color, "time_of_full":time_of_full,"status":status}

def make_status_view(parent_frame:str, images:dict, view_frame:Frame) ->None:
    canvas = Canvas(
        parent_frame,
        bg = "#FFFFFF",
        height = 600,
        width = 723,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)

    def update_content():   
        data = get_data()
        status_box = canvas.create_image(
            361.0,
            120.0,
            image=images['status_box_image'],
        )

        canvas.create_text(
            61.0,
            61.0,
            anchor="nw",
            text=data["code"],
            fill="#000000",
            font=("Lato Bold", 18 * -1)
        )

        canvas.create_text(
            61.0,
            83.0,
            anchor="nw",
            text=data["address"],
            fill="#5B5B5B",
            font=("Lato Medium", 14 * -1)
        )

        canvas.create_text(
            63.0,
            103.0,
            anchor="nw",
            text=f"Location: {data['location']}",
            fill="#5B5B5B",
            font=("Lato Medium", 14 * -1)
        )

        canvas.create_text(
            61.0,
            145.0,
            anchor="nw",
            text=f"Time: {data['time_of_full']}",
            fill="#5B5B5B",
            font=("Lato Medium", 14 * -1)
        )


        canvas.create_text(
            64.0,
            126.0,
            anchor="nw",
            text="Status :",
            fill="#5B5B5B",
            font=("Lato Medium", 14 * -1)
        )

        canvas.create_text(
            112.0,
            126.0,
            anchor="nw",
            text=data["status"],
            fill=data["status_text_color"],
            font=("Lato Bold", 15 * -1)
        )
        canvas.after(5000,update_content)

    update_content()