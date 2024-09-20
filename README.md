# Image Steganography Tool

This is a simple **Image Steganography** tool built using Python and Tkinter. The application allows users to hide text data inside images (encoding) and retrieve hidden text from images (decoding). The encoded image is saved as a new PNG file without noticeably altering the image quality.

## Features
- **Encode text into images**: Hide secret messages within an image using a simple steganography algorithm.
- **Decode text from images**: Extract hidden text from an image that has been encoded.
- Supports **PNG** image format.
- Displays hidden data directly in the app interface.

## Technologies Used
- **Python 3.x**
- **Tkinter**: Used for building the graphical user interface (GUI).
- **Pillow (PIL)**: A Python imaging library used for image processing.

## Usage

### Main Menu
When you open the application, you will see two options:
1. **Encode**: Hide a text message in an image.
2. **Decode**: Extract hidden text from an encoded image.

### Encode Text into an Image
1. Click the **Encode** button.
2. Select an image in which you want to hide a message.
3. Type the message you want to hide in the text area.
4. Click **Encode**, and then save the new image with the hidden message.

### Decode Text from an Image
1. Click the **Decode** button.
2. Select the image that contains the hidden message.
3. The hidden message will be displayed in a text area within the application.



## Example
1. **Encoding**:
   - Select an image (e.g., `before.png`).
     <p align="center">
     <img src="https://github.com/Maniram294/Image-Steganography/blob/master/Results/4.%20Select_the_Image_to_be_Encoded_with_Hidden_Message.png" alt="Selecting Image" width="500"/>
     </p>
   - Enter the message,in my example I've written "I'm BATMAN!!!".
     <p align="center">
     <img src="https://github.com/Maniram294/Image-Steganography/blob/master/Results/5.%20Type_Hidden_Message.png" alt="Writing hidden message" width="500"/>
     </p>
   - Save the new encoded image as `after.png`.

2. **Decoding**:
   - Select `after.png`.
     <p align="center">
     <img src="https://github.com/Maniram294/Image-Steganography/blob/master/Results/10.%20Select_the_Image_with_Hidden_Message.png" alt="Decoding" width="500"/>
     </p>
   - The hidden message "I'm BATMAN!!!" will be revealed in the text area.
   <p align="center">
   <img src="https://github.com/Maniram294/Image-Steganography/blob/master/Results/11.%20Displaying_Hidden_Message.png" alt="Result" width="500"/>
   </p>
