import random
import time
# import org.sikuli.script.*

# Set the location you want to click on
location = Location(1016, 991)




input_list = [
"can you get prices for Laundromat website in Newtown, Wellington and please provide the results in json format. Can you please start the first node of the json as the website url",
"can you get prices for Liquid Laundromats Kilbirnie website in Kilbirnie, Wellington and please provide the results in json format. Can you please start the first node of the json as the website url",
"can you get prices for Newtown Laundry and Dryclean website in Newtown, Wellington and please provide the results in json format. Can you please start the first node of the json as the website url",
"can you get prices for Spinfresh Laundromat KARORI website in Karori, Wellington and please provide the results in json format. Can you please start the first node of the json as the website url",
"can you get prices for Liquid Laundromats Newlands website in Newlands, Wellington and please provide the results in json format. Can you please start the first node of the json as the website url",
"can you get prices for Liquid Laundromats Johnsonville website in Johnsonville, Wellington and please provide the results in json format. Can you please start the first node of the json as the website url",
"can you get prices for Laundry Drop website in Johnsonville, Wellington and please provide the results in json format. Can you please start the first node of the json as the website url",
"can you get prices for Q Laundromat website in Tawa, Wellington and please provide the results in json format. Can you please start the first node of the json as the website url",
"can you get prices for Janice Laundry - Tawa website in Tawa, Wellington and please provide the results in json format. Can you please start the first node of the json as the website url",
"can you get prices for Liquid Laundromat Porirua CBD website in CBD, Wellington and please provide the results in json format. Can you please start the first node of the json as the website url",
"can you get prices for Spinfresh Laundromat EPUNI website in Epuni, Lower Hutt and please provide the results in json format. Can you please start the first node of the json as the website url",
"can you get prices for Liquid Laundromat Moera website in Moera, Lower Hutt and please provide the results in json format. Can you please start the first node of the json as the website url",
"can you get prices for Laundromat - Easy Key Self Service Laundromats (Wainuiomata) website in Wainuiomata, Wellington and please provide the results in json format. Can you please start the first node of the json as the website url"
]

# Iterate over the input list and its index
for index, value in enumerate(input_list):
    # Randomize the x,y by -20 and +20 range
    x_offset = random.randint(-80, 80)
    y_offset = random.randint(-10, 10)
    new_location = Location(location.getX() + x_offset, location.getY() + y_offset)
    
    # Click on the new location
    # click(new_location)
    
    # Type the value at the new location
    type(new_location, value)
    type(Key.ENTER)
    wait(90)

