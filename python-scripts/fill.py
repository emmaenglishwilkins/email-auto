# Parking info for Newton location
def parking_info(location):
    if location.lower() == "newton":
        return '<p>There is public street parking, as well as the lot directly across from our school.</p>'
    return ""

# Drop-off information based on location
def dropoff_info(location):
    dropoff_details = {
        "cobble hill": """
        <p>Drop-off:</p>
        <ul>
            <li>Weekdays:
                <ul>
                    <li>3:30 classes: Drop-off no earlier than 15 minutes before start.</li>
                    <li>4:30 and 5:30 classes: Drop-off no earlier than 5 minutes before start.</li>
                </ul>
            </li>
            <li>Weekends: Drop-off no earlier than 5 minutes before class starts.</li>
        </ul>
        <p>Upon arrival, students will be greeted at the front door, marked present, and directed to their classroom.</p>
        """,
        "park slope": """
        <p><b>Drop-off:</b></p>
        <ul>
            <li>Drop-off occurs at our <b>7th avenue front entrance</b>.</li>
            <li>Drop-off should not be occurring more than <b>5 minutes before class begins</b>. If you are dropping off more than 5 minutes early, it will be a charge of <b>$25 for the day</b>.</li>
        </ul>
        """,
        "newton": """
        <p>Drop-off should not be occurring more than <b>5 minutes before class begins</b>. If you are dropping off more than 5 minutes early, it will be a charge of <b>$25 for the day</b>. For special circumstances or requests, please talk to us beforehand and we can try to accommodate your needs.</p>
        """,
        "lexington": """
        <p>Drop-off should not be occurring more than <b>5 minutes before class begins</b>. If you are dropping off more than 5 minutes early, it will be a charge of <b>$25 for the day</b>. For special circumstances or requests, please talk to us beforehand and we can try to accommodate your needs.</p>
        """
    }
    return dropoff_details.get(location.lower(), "")

# Pickup information based on location
def pickup_info(location):
    pickup_details = {
        "cobble hill": """
        <p>Pickup:</p>
        <ul>
            <li>All Classes: Students pack up 3-5 minutes before pickup and gather by the art wall.</li>
        </ul>
        <p>Parents meet a teacher outside to confirm pickup. Students not yet picked up will wait calmly in the pickup area. If you pick up more than 15 minutes late it will be a charge of $25 for the day</p>
        """,
        "park slope": """
        <p><b>Pickup:</b></p>
        <ul>
            <li>Pickup occurs at our <b>14th street side entrance</b>.</li>
            <li>Classes are one hour long. Please try to be on time for pick up as we have other classes that come in right after.</li>
            <li>Please call us at <a href="tel:3392351605">339-235-1605</a> if you cannot pick up by the designated end time. If you pick up more than <b>15 minutes late</b>, it will be a charge of <b>$25 for the day</b>.</li>
        </ul>
        """,
        "newton": """
        <p>Each class is one hour long. Please try to be on time for pick-up as we have other classes that come in right after. Please give us a call at <a href="tel:7813549732">781-354-9732</a> if you cannot pick up by the designated end time. If you pick up more than <b>15 minutes late</b>, it will be a charge of <b>$25 for the day</b>.</p>
        """,
        "lexington": """
        <p>Each class is one hour long. Please try to be on time for pick-up as we have other classes that come in right after. Please give us a call at <a href="tel:7812772755">781-277-2755</a> if you cannot pick up by the designated end time. If you pick up more than <b>15 minutes late</b>, it will be a charge of <b>$25 for the day</b>.</p>
        """
    }
    return pickup_details.get(location.lower(), "")

# Class-specific details
def get_class_specs(class_name):
    class_specs = {
        "roblox": '<p>During the class we will use Roblox Studio. You can go to <a href="https://www.roblox.com" target="_blank">roblox.com</a> to download.</p>',
        "scratch": '<p>During the class we will use an online coding platform called Scratch. To log in at home you can go to <a href="https://scratch.mit.edu" target="_blank">scratch.mit.edu</a> and use the following login information.</p>',
        "minecraft": '''
        <p>During the class, we will use the education edition of Minecraft. If you want to log in at home, you will need to download Minecraft Education Edition here: <a href="https://education.minecraft.net/en-us/get-started/download" target="_blank">education.minecraft.net/en-us/get-started/download</a></p>
        <p>Please keep in mind this is not the same as regular Minecraft and you cannot log into regular Minecraft with your Penguin Coding account.</p>
        ''',
        "python": '''
        <p>During the class, we code on Python IDLE, which you can download here: <a href="https://www.python.org/downloads/" target="_blank">python.org/downloads</a>.</p>
        <p>We have uploaded our code to OneDrive. If you are interested in accessing your child’s code at home, please use the login information below to access Outlook.</p>
        ''',
        "robotics": ''
    }
    return class_specs.get(class_name.lower(), "")

def phone_fill(location){
    phoneNumbers = {
        "Newton" : "(617) 608-4757",
        "Lexington" : "(781) 277-2755" , 
        "Acton" : "(781) 277-2956", 
        "Park Slope" : "(347) 620-9235",
        "Cobble Hill" : "(917) 813-1007",
        "Online" : "(917) 813-1007",
        "No Location" : "MA Phone: (781) 277-2755\t\tNY Phone: (347) 620-9235"
    }
    return phoneNumbers.get(location, "Phone number not available")
}

def address_fill(location){
    LocationAddresses = {
        "Newton" : "1223 Centre St. Newton Centre, MA",
        "Lexington" : "Suite 101 (Bottom Floor) of 5 Militia Drive, Lexington MA 02421" , 
        "Acton" : "411 Massachusetts Ave. Suite 101 Acton, MA 01720", 
        "Park Slope" : "424 7th Ave, Brooklyn, NY, 11215 (Corner of 14th street and 7th Ave)",
        "Cobble Hill" : "156 Smith Street, Brooklyn, NY 11201",
        "Online" : "N/A",
        "No Location" : ""
    }
    return LocationAddresses.get(location, "")
}

# Replacing placeholders in the email template
email_body = email_template.replace("{location_address}", address_fill(location))
email_body = email_template.replace("{location_phone}", phone_fill(location))
email_body = email_template.replace("{class_specs}", get_class_specs(class_name))
email_body = email_body.replace("{dropoff_info}", dropoff_info(location))
email_body = email_body.replace("{pickup_info}", pickup_info(location))
email_body = email_body.replace("{parking_info}", parking_info(location))

print(email_body)
