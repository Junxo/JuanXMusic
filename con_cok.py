import json

# Baca file JSON
with open('cookies.json', 'r') as f:
    cookies = json.load(f)

# Buka file untuk menulis dalam format Netscape
with open('youtube_cookies.txt', 'w') as f:
    # Tulis header file Netscape
    f.write("# Netscape HTTP Cookie File\n")
    f.write("# This is a generated file! Do not edit.\n\n")
    
    # Konversi setiap cookie ke format Netscape
    for cookie in cookies:
        f.write("\t".join([
            cookie.get('domain', ''),
            'TRUE' if cookie.get('hostOnly', False) else 'TRUE',
            cookie.get('path', '/'),
            'TRUE' if cookie.get('secure', False) else 'TRUE',
            str(int(cookie.get('expirationDate', 0))),
            cookie.get('name', ''),
            cookie.get('value', ''),
        ]) + "\n")
