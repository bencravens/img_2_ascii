# img_2_ascii
Convert images to ascii text files

Example usage:

```shell
python3 img_2_ascii.py fern.jpg 2 ramp.txt
gedit out.txt
```

Here the first arg is the file to be converted, the second arg is the vertical downscaling, and the 
third argument is the ascii scale to use (a range of ascii characters which correspond to lighter->darker pixels)
