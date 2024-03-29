# ProgressPrinter

![Code Examples](https://raw.githubusercontent.com/ElCap1tan/ProgressPrinter/master/docs/static/ProgressPrinterDemo_v0.1.1.gif)

## Progress Bar:

### For the full example see examples_progress_bar.py and examples_byte_progress_bar.py
#### A first really bare version of a html documentation is available [here](https://elcapitan.io/ProgressPrinter/index.html)
#### This will be edited in the next days to make things clearer.

### ProgressBar Examples

```Python
from time import sleep

from ProgressPrinter import ProgressBar
```
```Python
def ex1():
    pb1 = ProgressBar(100, '%', pre='Downloading file', post='Download finished', length=25)
    pb1.print_progress()  # Prints the initial empty progress bar
    for mb in range(1, 101):
        pb1.print_progress(mb)
        sleep(0.15)
```
```
Downloading file
[========================>] - Finished 100 % of 100 %
Download finished
```
```Python
def ex2():
    pb2 = ProgressBar(500, 'MB', pre='Downloading file', post='Download finished', head='#')
    pb2.print_progress()  # Prints the initial empty progress bar
    for mb in range(1, 501):
        pb2.print_progress(mb)
        sleep(0.02)
```
```
Downloading file
[=================================================#] - Finished 500 MB of 500 MB
Download finished
```
```Python
def ex3():
    pb3 = ProgressBar(1000.12, 'MB', pre='Downloading file', post='Download finished', length=100)
    pb3.print_progress()  # Prints the initial empty progress bar
    for mb in range(1, 1001):
        if mb != 1000 and mb % 2 == 0:
            mb = mb + 0.5
        elif mb != 1000:
            mb = mb + 0.25
        else:
            mb = mb + 0.12
        pb3.print_progress(mb)
        sleep(0.025)
```
```
Downloading file
[===================================================================================================>] - Finished 1000.12 MB of 1000.12 MB
Download finished
```
```Python
def ex4():
    pb4 = ProgressBar(5, 'files', pre='Deleting files', post='Finished!', length=25, empty='*', fill='#')
    pb4.print_progress()  # Prints the initial empty progress bar
    for file in range(1, 6):
        pp4.print_progress(file, pre="Deleting file file{}.txt".format(file))
        sleep(1)
```
```
Deleting files
Deleting file file1.txt
Deleting file file2.txt
Deleting file file3.txt
Deleting file file4.txt
Deleting file file5.txt
[########################>] - Finished 5 files of 5 files
Finished!
```
```Python
def ex5():
    with open('example.txt', 'r') as f:
        pb5 = ProgressBar(len(f.readlines()), 'lines', pre="Reading lines from file {}".format(f.name), post='Finished reading file!')
        f.seek(0)  # Return to start of line after obtaining line count
        pb5.print_progress()  # Prints the initial empty progress bar
        for lineno, line in enumerate(f, start=1):
            pb5.print_progress(lineno, pre=line.replace('\n', ''))
            sleep(1)
```
```
Reading lines from file example.txt
Line 1
Line 2
Line 3
Line 4
...
[=================================================>] - Finished 5 lines of 5 lines
Finished reading file!
```

### ByteProgressBar Example
```Python
import requests

from ProgressPrinter import ByteProgressBar

def ex1():
    # The ByteProgressBar is a extension of the normal progress bar that supports automatic unit conversion
    # from bytes, the base unit you will work with most of the time, to KB, MB, etc.
    # This for example is useful when downloading or working with a file (see example below)
    #
    # UNCOMMENT TO LINK YOU WANT TO USE FOR THE TEST DOWNLOAD
    # -------------------------------------------------------
    # 100MB.bin [100 MB] - Auto conversion to MB
    # link = 'https://speed.hetzner.de/100MB.bin'
    # -------------------------------------------------------------------------------------------
    # Linux Mint Cinnamon x64.iso [ca. 1.87 GB] - Auto conversion to GB
    link = 'http://mirrors.evowise.com/linuxmint/stable/19.2/linuxmint-19.2-cinnamon-64bit.iso'
    # -------------------------------------------------------------------------------------------

    file_name = link.split('/')[-1]
    with open(file_name, 'wb') as f:
        response = requests.get(link, stream=True)
        byte_size = int(response.headers.get('content-length'))
        if byte_size is None:
            f.write(response.content)
        else:
            # Set to ByteProgressBar.UNITS.AUTO to automatically interfere a fitting unit from the byte size
            # -----------------------------------------------------------------------------------------------
            # Supported values: ByteProgressBar.UNITS.{BYTES, KILOBYTES, MEGABYTES, GIGABYTES, TERABYTES, AUTO}

            bpb1 = ByteProgressBar(byte_size, ByteProgressBar.UNITS.AUTO, pre='Downloading {} from {}'
                                   .format(file_name, link), post='Finished download!')
            bpb1.print_progress()
            loaded_bytes = 0
            for chunk in response.iter_content(chunk_size=1048576):  # 1 MB
                loaded_bytes += len(chunk)
                f.write(chunk)
                bpb1.print_progress(loaded_bytes)
```
```
Downloading linuxmint-19.2-cinnamon-64bit.iso from http://mirrors.evowise.com/linuxmint/stable/19.2/linuxmint-19.2-cinnamon-64bit.iso
[======>                                           ] - Finished 0.27 GB of 1.87 GB
```
