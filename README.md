# RP2040-Zero-simple-blink-with-Micropython-function
As using the RGB led of RP2040 Zero as a simple led with a function
In this sketch i create a function to use the rgb led in tho ways:
First is possible switch on and off the led in white color with the function call
neo_pixel (1) and neo_pixel(0).
Second you can switch on the led not as white led but as a colored led with the function call
neo_pixel(color_red, color_green, color_blue)
where color_ is between 0 and 255.
The function return 1 if everything goes ok otherwise return 0.
