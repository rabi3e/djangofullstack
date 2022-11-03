#1 you have to install the library 
# pip install git+https://github.com/Joeclinton1/google-images-download.git
#importing the google_image_dowload library
from google_images_download import google_images_download  
#creat object
obj = google_images_download.googleimagesdownload()
#creating list of arguments
key = input("pleas enter your search ------->    ")
lim= int(input(" how many pic you want dowload -----> "))
arg = {"keywords":key,"limit":lim}   
#passing the arguments to the function
code = obj.download(arg)   

