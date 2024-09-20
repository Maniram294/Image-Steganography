from tkinter import *
from tkinter import ttk
import tkinter.filedialog
from PIL import ImageTk, Image
from tkinter import messagebox
from io import BytesIO
import os

class Stegno:

    art = '''¯\_(ツ)_/¯'''
    art2 = '''
@(\/)
(\/)-{}-)@
@(={}=)/\)(\/)
(\/(/\)@| (-{}-)
(={}=)@(\/)@(/\)@
(/\)\(={}=)/(\/)
@(\/)\(/\)/(={}=)
(-{}-)""""@/(/\)
|:   |
/::'   \\
/:::     \\
|::'       |
|::        |
\::.       /
':______.'
`""""""`'''
    output_image_size = 0

    def main(self,root):
        root.title('ImageSteganography')
        root.geometry('500x600')
        root.resizable(width=False, height=False)
        f = Frame(root)

        title = Label(f, text='Image Steganography')
        title.config(font=('courier', 33))
        title.grid(pady=10)

        b_encode = Button(f, text="Encode", command=lambda: self.frame1_encode(f), padx=14)
        b_encode.config(font=('courier', 14))
        b_decode = Button(f, text="Decode", padx=14, command=lambda: self.frame1_decode(f))
        b_decode.config(font=('courier', 14))
        b_decode.grid(pady=12)

        ascii_art = Label(f, text=self.art)
        ascii_art.config(font=('courier', 60))

        ascii_art2 = Label(f, text=self.art2)
        ascii_art2.config(font=('courier', 12, 'bold'))

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        f.grid()
        title.grid(row=1)
        b_encode.grid(row=2)
        b_decode.grid(row=3)
        ascii_art.grid(row=4, pady=10)
        ascii_art2.grid(row=5, pady=5)

    def home(self, frame):
        frame.destroy()
        self.main(root)

    def frame1_decode(self, f):
        f.destroy()
        d_f2 = Frame(root)
        label_art = Label(d_f2, text='٩(^‿^)۶')
        label_art.config(font=('courier', 90))
        label_art.grid(row=1, pady=50)
        l1 = Label(d_f2, text='Select Image with Hidden text:')
        l1.config(font=('courier', 18))
        l1.grid()
        bws_button = Button(d_f2, text='Select', command=lambda: self.frame2_decode(d_f2))
        bws_button.config(font=('courier', 18))
        bws_button.grid()
        back_button = Button(d_f2, text='Cancel', command=lambda: self.home(d_f2))
        back_button.config(font=('courier', 18))
        back_button.grid(pady=15)
        d_f2.grid()

    def frame2_decode(self, d_f2):
        d_f3 = Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes=([('png', '*.png'), ('jpeg', '*.jpeg'), ('jpg', '*.jpg'), ('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error", "You have selected nothing!")
        else:
            myimg = Image.open(myfile, 'r')
            myimage = myimg.resize((300, 200))
            img = ImageTk.PhotoImage(myimage)
            l4 = Label(d_f3, text='Selected Image:')
            l4.config(font=('courier', 18))
            l4.grid()
            panel = Label(d_f3, image=img)
            panel.image = img
            panel.grid()
            hidden_data = self.decode(myimg)
            l2 = Label(d_f3, text='Hidden data is:')
            l2.config(font=('courier', 18))
            l2.grid(pady=10)
            text_area = Text(d_f3, width=50, height=10)
            text_area.insert(INSERT, hidden_data)
            text_area.configure(state='disabled')
            text_area.grid()
            back_button = Button(d_f3, text='Cancel', command=lambda: self.page3(d_f3))
            back_button.config(font=('courier', 11))
            back_button.grid(pady=15)
            show_info = Button(d_f3, text='More Info', command=self.info)
            show_info.config(font=('courier', 11))
            show_info.grid()
            d_f3.grid(row=1)
            d_f2.destroy()

    # Function to modify pixels to encode data
    def mod_pix(self, pixels, data):
        """Modifies pixels to encode data."""
        data_list = self.gen_data(data)
        data_len = len(data_list)
        img_pixels = iter(pixels)

        for i in range(data_len):
            # Get the next three pixels
            pixel = [value for value in next(img_pixels)[:3] +
                     next(img_pixels)[:3] +
                     next(img_pixels)[:3]]

            # Modify the pixel values
            for j in range(0, 8):
                if data_list[i][j] == '0' and pixel[j] % 2 != 0:
                    pixel[j] -= 1
                elif data_list[i][j] == '1' and pixel[j] % 2 == 0:
                    if pixel[j] != 0:
                        pixel[j] -= 1
                    else:
                        pixel[j] += 1

            # For the last pixel, if we have encoded the last bit of data, make it odd
            if i == data_len - 1:
                if pixel[-1] % 2 == 0:
                    pixel[-1] += 1
            else:
                if pixel[-1] % 2 != 0:
                    pixel[-1] -= 1

            # Yield the modified pixels
            yield tuple(pixel[:3])
            yield tuple(pixel[3:6])
            yield tuple(pixel[6:9])

    # Function to generate binary data from input
    def gen_data(self, data):
        """Generates binary data from the input string."""
        new_data = []
        for i in data:
            new_data.append(format(ord(i), '08b'))  # Convert to 8-bit binary representation
        return new_data

    # Decoding function
    def decode(self, img):
        """Decodes the hidden data from the image."""
        imgdata = iter(img.getdata())
        binary_data = ""

        while True:
            pixels = [value for value in next(imgdata)[:3] +
                      next(imgdata)[:3] +
                      next(imgdata)[:3]]

            bin_str = ""
            for i in range(8):
                if pixels[i] % 2 == 0:
                    bin_str += '0'
                else:
                    bin_str += '1'

            binary_data += bin_str
            if pixels[-1] % 2 != 0:  # Check if it's the end of data
                break

        # Convert binary data to the text
        decoded_data = ""
        for i in range(0, len(binary_data), 8):
            byte = binary_data[i:i + 8]
            decoded_data += chr(int(byte, 2))  # Convert binary to ASCII

        return decoded_data

    def frame1_encode(self, f):
        f.destroy()
        f2 = Frame(root)
        label_art = Label(f2, text='\'\(°Ω°)/\'')
        label_art.config(font=('courier', 70))
        label_art.grid(row=1, pady=50)
        l1 = Label(f2, text='Select the Image in which \nyou want to hide text:')
        l1.config(font=('courier', 18))
        l1.grid()

        bws_button = Button(f2, text='Select', command=lambda: self.frame2_encode(f2))
        bws_button.config(font=('courier', 18))
        bws_button.grid()
        back_button = Button(f2, text='Cancel', command=lambda: self.home(f2))
        back_button.config(font=('courier', 18))
        back_button.grid(pady=15)
        f2.grid()

    def frame2_encode(self, f2):
        ep = Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes=([('png', '*.png'), ('jpeg', '*.jpeg'), ('jpg', '*.jpg'), ('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error", "You have selected nothing!")
        else:
            myimg = Image.open(myfile)
            myimage = myimg.resize((300, 200))
            img = ImageTk.PhotoImage(myimage)
            l3 = Label(ep, text='Selected Image')
            l3.config(font=('courier', 18))
            l3.grid()
            panel = Label(ep, image=img)
            panel.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = myimg.size
            panel.grid()
            l2 = Label(ep, text='Enter the message')
            l2.config(font=('courier', 18))
            l2.grid(pady=15)
            text_area = Text(ep, width=50, height=10)
            text_area.grid()
            encode_button = Button(ep, text='Cancel', command=lambda: self.home(ep))
            encode_button.config(font=('courier', 11))
            back_button = Button(ep, text='Encode', command=lambda: [self.enc_fun(text_area, myimg), self.home(ep)])
            back_button.config(font=('courier', 11))
            back_button.grid(pady=15)
            encode_button.grid()
            ep.grid(row=1)
            f2.destroy()



    def mod_pix(self, pixels, data):
        """Modifies pixels to encode data."""
        data_list = self.gen_data(data)
        data_len = len(data_list)
        img_pixels = iter(pixels)

        for i in range(data_len):
            # Get the next three pixels
            pixel = [value for value in next(img_pixels)[:3] +
                     next(img_pixels)[:3] +
                     next(img_pixels)[:3]]

            # Modify the pixel values
            for j in range(0, 8):
                if data_list[i][j] == '0' and pixel[j] % 2 != 0:
                    pixel[j] -= 1
                elif data_list[i][j] == '1' and pixel[j] % 2 == 0:
                    if pixel[j] != 0:
                        pixel[j] -= 1
                    else:
                        pixel[j] += 1

            # For the last pixel, if we have encoded the last bit of data, make it odd
            if i == data_len - 1:
                if pixel[-1] % 2 == 0:
                    pixel[-1] += 1
            else:
                if pixel[-1] % 2 != 0:
                    pixel[-1] -= 1

            # Yield the modified pixels
            yield tuple(pixel[:3])
            yield tuple(pixel[3:6])
            yield tuple(pixel[6:9])

    def enc_fun(self, text_area, myimg):
        data = text_area.get("1.0", "end-1c")
        if len(data) == 0:
            messagebox.showinfo("Alert", "Kindly enter text in TextBox")
        else:
            newimg = myimg.copy()
            self.encode_enc(newimg, data)
            temp = os.path.splitext(os.path.basename(myimg.filename))[0]
            newimg.save(tkinter.filedialog.asksaveasfilename(initialfile=temp, filetypes=([('png', '*.png')]),
                                                             defaultextension=".png"))
            messagebox.showinfo("Success", "Encoding Successful\nFile is saved")

    def gen_data(self, data):
        """Generates binary data from the input string."""
        new_data = []

        for i in data:
            new_data.append(format(ord(i), '08b'))  # Convert to 8-bit binary representation
        return new_data

    def encode_enc(self, newimg, data):
        """Encodes the given data into the new image."""
        w = newimg.size[0]
        (x, y) = (0, 0)

        for pixel in self.mod_pix(newimg.getdata(), data):
            # Ensure the pixel is a tuple of three integers
            new_pixel = tuple(pixel)

            newimg.putpixel((x, y), new_pixel)  # Update the pixel value in the image

            if x == w - 1:
                x = 0
                y += 1
            else:
                x += 1

    def genData(self, data):
        newd = []
        for i in data:
            newd.append(format(ord(i), '08b'))
        return newd

    def modPix(self, pix, data):
        datalist = self.genData(data)
        lendata = len(datalist)
        imdata = iter(pix)
        for i in range(lendata):
            pixels = [value for value in next(imdata)[:3] +
                      next(imdata)[:3] +
                      next(imdata)[:3]]
            for j in range(8):
                if (datalist[i][j] == '0' and pixels[j] % 2 != 0):
                    pixels[j] -= 1
                elif (datalist[i][j] == '1' and pixels[j] % 2 == 0):
                    if pixels[j] != 0:
                        pixels[j] -= 1
                    else:
                        pixels[j] += 1
            if i == lendata - 1:
                if pixels[-1] % 2 == 0:
                    pixels[-1] += 1
            else:
                if pixels[-1] % 2 != 0:
                    pixels[-1] -= 1
            pixels = tuple(pixels)
            yield pixels

    def page3(self, frame):
        frame.destroy()
        self.main(root)

    def info(self):
        info_text = f'Original image size: {self.output_image_size.st_size} bytes\n' \
                    f'Width: {self.o_image_w}\nHeight: {self.o_image_h}'
        messagebox.showinfo("Info", info_text)

root = Tk()
app = Stegno()
app.main(root)
root.mainloop()
