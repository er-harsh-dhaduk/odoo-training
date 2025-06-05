import base64

with open("iron-man.png", "rb") as img:
    print(base64.b64encode(img.read())).decode('utf-8')