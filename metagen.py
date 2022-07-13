import time

# Meta Generator

__author__ = "@indradwi.25"

# Create Information about this tools

from multiprocessing.sharedctypes import Value


print("This is Tools For Meta Generator and use it in html")
print("This Tools is created by ", __author__)
print("Version 1.0")
print("Author: ", __author__)
print("Donate : https://Saweria.co/xnuvers007\n")


# Input name file from user
try:
    name_file = str(input("Enter name file: "))
except (Exception, KeyboardInterrupt, ValueError):
    print("Error")
    print("Will be exit in 3s")
    for i in range(3):
        print(3 - i)
        time.sleep(1)
    exit()
ext = name_file+".txt"

#create file from name_file
try :
    file = open(ext, "w", encoding="utf-8")
except (FileExistsError):
    pass
except (FileNotFoundError):
    file = open(ext, "w", encoding="utf-8")

description = str(input("Description Website: "))
name = str(input("Name: "))
title = str(input("Title: "))
image = str(input(" Url Image: "))
url = str(input("URL: "))

print("Insert the code into the <head> of your website")
try:
    input("enter to continue")
except (KeyboardInterrupt, ValueError):
    print("\n")
    print("Exiting...")
    exit()
print("\n")

print("<!-- HTML Meta Tags -->")
print("<!-- HTML Meta Tags -->",file=file)
print('<meta name="description" content="' + description + '">')
print('<meta name="description" content="' + description + '">',file=file)
print("\n\n",file=file)
print("\n\n")
print("<!-- Google / Search Engine Tags-->")
print("<!-- Google / Search Engine Tags-->",file=file)
print('<meta itemprop="name" content="' + name + '">')
print('<meta itemprop="description" content="' + description + '">')
print('<meta itemprop="image" content="' + image + '">')

print('<meta itemprop="name" content="' + name + '">',file=file)
print('<meta itemprop="description" content="' + description + '">',file=file)
print('<meta itemprop="image" content="' + image + '">',file=file)
print("\n\n",file=file)
print("\n\n")
print("<!-- Facebook Meta Tags-->")
print("<!-- Facebook Meta Tags-->",file=file)
print('<meta property="og:url" content="'+ url +'">')
print('<meta property="og:type" content="website">')
print('<meta property="og:title" content="'+ title +'">')
print('<meta property="og:description" content="'+ description +'">')
print('<meta property="og:image" content="'+ image +'">')

print('<meta property="og:url" content="'+ url +'">',file=file)
print('<meta property="og:type" content="website">',file=file)
print('<meta property="og:title" content="'+ title +'">')
print('<meta property="og:description" content="'+ description +'">')
print('<meta property="og:image" content="'+ image +'">')

print('\n\n')
print("\n\n",file=file)

print('<!-- Twitter Meta Tags-->')
print('meta name="twitter:card" content="summary_large_image">')
print('meta name="twitter:title" content="'+ title +'">')
print('meta name="twitter:description" content="'+ description +'">')
print('meta name="twitter:image" content="'+ image +'">')

print('<!-- Twitter Meta Tags-->',file=file)
print('meta name="twitter:card" content="summary_large_image">',file=file)
print('meta name="twitter:title" content="'+ title +'">',file=file)
print('meta name="twitter:description" content="'+ description +'">',file=file)
print('meta name="twitter:image" content="'+ image +'">',file=file)

print("<!-- Meta Tags Generated via https://github.com/Xnuvers007/Meta-Generator -->",file=file)

print("====================================")
print("Reference : https://ogp.me/".upper())
print("====================================")

file.close()