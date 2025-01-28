import re
from datetime import datetime

def generate_email(template_html, student_data):
    """
    Fills in the email template with student-specific data
    
    Args:
        template_html (str): HTML template with variables in {brackets}
        student_data (dict): Dictionary containing student-specific information
    
    Returns:
        str: Completed HTML email
    """
    # Make a copy of the template
    email_html = template_html
    
    # Replace each variable in the template
    for key, value in student_data.items():
        email_html = email_html.replace(f"{{{key}}}", str(value))
    
    return email_html

# Example student data
student_info = {
    "student_name": "Alex Smith",
    "class_name": "Python Advanced",
    "class_time": "Mondays at 3:30 PM",
    "parent_name": "Mr. and Mrs. Smith",
    "username": "penguin_student_123",
    "pwd": "SecurePass456"
}

# Function to save the generated email
def save_email(html_content, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)

# Example usage
if __name__ == "__main__":
    # Load the template (you would need to replace this with the actual template HTML)
    with open('email_template.html', 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Generate personalized email
    final_email = generate_email(template, student_info)
    
    # Save to a new file with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"generated_email_{timestamp}.html"
    save_email(final_email, output_filename)
    
    print(f"Email generated and saved as: {output_filename}")