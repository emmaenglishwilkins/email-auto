def get_class_specs(class_name):  
    class_specs = {  
        "roblox": """<h2>Roblox Studio Setup Instructions</h2>
                     <p>Download and install Roblox Studio from <a href='https://www.roblox.com/create' target='_blank'>this link</a>.</p>
                     <p>Click "Start Creating" to download and install the app.</p>
                     <p>Log in with the provided Penguin Coding School account.</p>""",  

        "scratch": """<h2>Scratch Setup Instructions</h2>
                      <p>Use the online coding platform at <a href='https://scratch.mit.edu' target='_blank'>Scratch</a>.</p>
                      <p>Log in with the provided Penguin Coding School account.</p>
                      <p><strong>Important Note:</strong> Please do not change the password as this account belongs to Penguin Coding School.</p>""",  

        "minecraft": """<h2>Minecraft Education Edition Setup</h2>
                        <p>Download Minecraft Education Edition from <a href='https://education.minecraft.net/get-started/download' target='_blank'>this link</a>.</p>
                        <p>Install it on Windows, Mac, or Chromebook, and ensure it opens before class.</p>
                        <p>Students will receive instructions to connect to the Teacher's Minecraft Server during class.</p>""",  

        "remote_desktop": """<h2>Azure Remote Desktop Setup</h2>
                             <p>Access Azure Remote Desktop at <a href='https://client.wvd.microsoft.com/arm/webclient/index.html' target='_blank'>this link</a>.</p>
                             <p>Log in with the provided Microsoft account.</p>
                             <p><strong>Important Note:</strong> Please do not change the password as this account belongs to Penguin Coding School.</p>""",  

        "other": """<h2>Other Class Setup</h2>
                    <p>Check with the instructor for any additional setup requirements.</p>""",  
    }  
    return class_specs.get(class_name.lower(), "")  


# The main function that Zapier will call
def generate_email(input_data):
    class_name = input_data['class_name']

    if "Python" in class_name:
        general_class = 'remote_desktop'
    elif "Scratch" in class_name:
        general_class = 'scratch'
    elif "Minecraft" in class_name:
        general_class = 'minecraft'
    elif "Roblox" in class_name:
        general_class = 'roblox'
    elif "Java" in class_name:
        general_class = 'remote_desktop'
    else:
        general_class = 'other'
    
    # Get the class specifications
    class_specs = get_class_specs(general_class)
    
    # Build the email body
    email_body = {
        'semester': "Winter 2 2025",
        'class_specs': class_specs if class_specs else '',
    }
    
    return email_body
# for zapier
output = generate_email(input_data)
return output