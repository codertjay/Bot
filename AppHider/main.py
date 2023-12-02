
def hide_exe_in_image(image_path, exe_path, output_path):
    with open(image_path, 'rb') as img:
        img_data = img.read()
    with open(exe_path, 'rb') as exe:
        exe_data = exe.read()
    with open(output_path, 'wb') as out:
        out.write(img_data)
        out.write(exe_data)



hide_exe_in_image("input.png","input.xlsx","output.png")