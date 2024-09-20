from flask import Flask, render_template, url_for, request, redirect, send_file
import requests
import csv
import os

app = Flask(__name__, template_folder='templates')

# Function to write results to CSV
def write_to_csv(data, username):
    """
    Writes the results to a CSV file.

    Args:
        data (list): A list of dictionaries containing the results.
        username (str): The username to be used in the filename.

    Returns:
        str: The path to the generated CSV file.
    """
    file_path = f"{username}_check_results.csv"
    keys = data[0].keys()
    with open(file_path, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
    return file_path

# Function to check username across platforms
def check_username(username):
    """
    Checks the availability of a username across various social media platforms.

    Args:
        username (str): The username to be checked.

    Returns:
        tuple: A tuple containing the results and the path to the generated CSV file.
    """
    results = []

    def add_result(platform, found, url):
        """
        Adds a result to the list.

        Args:
            platform (str): The platform name.
            found (bool): Whether the username is found or not.
            url (str): The URL of the platform.
        """
        results.append({
            'Platform': platform,
            'Username': username,
            'Found': found,
            'URL': url if found else 'Not Found'
        })

    def check_url(platform, url_format):
        """
        Checks the availability of a username on a platform.

        Args:
            platform (str): The platform name.
            url_format (str): The URL format of the platform.
        """
        try:
            url = url_format.format(username)
            response = requests.get(url, headers={"Accept-Language": "en"})
            found = response.status_code == 200
            add_result(platform, found, url)
        except Exception as e:
            print(f"Error checking {platform}: {e}")
            add_result(platform, False, 'Error')

    platforms = {
        "Instagram": "https://www.instagram.com/{}",
        "Facebook": "https://www.facebook.com/{}",
        "Twitter": "https://www.twitter.com/{}",
        "YouTube": "https://www.youtube.com/{}",
        "Blogger": "https://{}.blogspot.com",
        "Reddit": "https://www.reddit.com/user/{}",
        "Wordpress": "https://{}.wordpress.com",
        "GitHub": "https://www.github.com/{}",
        "Pinterest": "https://www.pinterest.com/{}",
        "SoundCloud": "https://soundcloud.com/{}",
    }

    for platform, url_format in platforms.items():
        check_url(platform, url_format)

    file_path = write_to_csv(results, username)
    return results, file_path

@app.route("/")
def index():
    """
    The index route.

    Returns:
        str: The rendered HTML template.
    """
    return render_template("tools.html")

@app.route("/username", methods=["GET", "POST"])
def username():
    """
    The username route.

    Returns:
        str: The rendered HTML template.
    """
    if request.method == "POST":
        username_input = request.form.get('username')
        results, file_path = check_username(username_input)
        return render_template("username_results.html", results=results, file_path=file_path)
    return render_template("username.html")

@app.route("/download/<path:filename>")
def download_file(filename):
    """
    The download route.

    Args:
        filename (str): The filename to be downloaded.

    Returns:
        str: The downloaded file.
    """
    return send_file(filename, as_attachment=True)

@app.route("/email")
def email():
    """
    The email route.

    Returns:
        str: The rendered HTML template.
    """
    return render_template("Email.html")

@app.route("/ip_mac")
def ip_mac():
    """
    The IP/MAC route.

    Returns:
        str: The rendered HTML template.
    """
    return render_template("IP MAC.html")

@app.route("/telephone")
def telephone():
    """
    The telephone route.

    Returns:
        str: The rendered HTML template.
    """
    return render_template("phoneno.html")

if __name__ == "__main__":
    app.run(debug=True)
