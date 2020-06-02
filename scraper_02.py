import requests

response = requests.get("https://en.wikipedia.org/robots.txt")  #enter the link here to download the text
response.raise_for_status()                                     #always raise_for_status for the error in download
f = open("test.txt",'bw')
for chunk in response.iter_content(1000):                       #Divide the content in chunks
    f.write(chunk)

f.close()
