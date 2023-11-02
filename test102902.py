from email.mime import image
from lib2to3.pytree import convert
from PIL import Image

def main():
    jump = 1
    jump = int(input("png->icon?[1_Y\\0_N]"))
    if(jump == 0):
        input_file = input("*.png_file:")
        output_file = input("*.icon_file:")
        convert_to_icon(input_file,output_file)
    exe_file = input("*.exe_file:")
    icon_file = input("*.icon_file:")
    change_exe_icon(exe_file,icon_file)
    

def convert_to_icon(input_file,output_file,size=(32,32)):
    img = Image.open(input_file)
    imge = img.resize(size,Image.ADAPTIVE)
    img.save(output_file,'ICO')

def change_exe_icon(file_path,icon_path):
    with Image.open(icon_path) as img:
        img.save(file_path,'ICO')

if __name__ == '__main__':
    main()