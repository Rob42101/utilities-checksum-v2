# utilities-checksum-v2

Announcing version 2 of my 'File Checksum' app, which is a complete rework of the V1 app. As with V1, V2 was developed using the PAGE GUI design application, but since PAGE V8 has now been released, I've used that version of PAGE to develop the GUI for this project. You'll find some details about that in the `README.md` page for my `utilities` repository, of which this is a sub-section.

Although PGP signature files are becoming more popular, you'll still come across this kind of file verification (such as for files hosted on `pypi.org`, for example) and this app is an easy and pleasant way to use this time honoured process.

As before, this application provides an easy to use GUI for checking the hash values of any file. The use case is for when you download a file for which the author has provided a checksum value: this app will generate the hash values of the downloaded file (on the local host machine) and allows you to simply paste in the published hash values. It will then compare the two values and indicate if they are a match, or not a match. The main difference between my two apps is that V2 generates all four supported hash digests (MD5, SHA-1, SHA-256 and SHA-512), in parallel, and displays all four in the GUI at once, rather than one at a time, which is what V1 did.

In order to support that new feature, the GUI needed to be completely redesigned. While doing that, I decided to add a new function: V2 has the option to save the generated hash digests, as a report, making it useful for not only checking the published hash values of a downloaded file, but also for uploading the hash digests of your published files. You will be able to see what that report looks like further down this page.

As with V1, this version has been written in Python3 code, using the Tkinter library for the GUI. I have again kept the dependencies to the minimum and used standard Python libraries, so there should be no `pip install` requirements. As for the app itself, again, there are no install requirements, per se, but a working Python3 environment is a given, along with Tkinter.

Apps written using the PAGE GUI designer, have two `.py` files; both of which are required in order for said app to run.

For this app, the two files are:

`checksum.py`

`checksum_support.py`

Either can be used to run the app, but `checksum.py` should be considered as the 'application' file: it creates the GUI front end, while the `_support.py` file can be considered as the 'driver', so to speak.

The application can be launched as is, by granting the `checksum.py` file 'executable' permission, or it can be launched from a command line, via your `python3` interpreter, without elevated privileges.

As a part of this application, there is not only a `icons` folder (as before), but also a `themes` folder, which is a new requirement for all PAGE V8 developed applications. All four of these objects should reside in the same location of your file system, where said location does not need, again, any elevated user privileges. Gone is the need for a `config.ini` file (which V1 used) and along with it, gone is the need for the in-app editor of V1.

As a replacement for that system, you'll see a 'Red/Green - Off/On' flip switch to the top RH side of the GUI, for which there is a 'tool tip'. Flipping that switch, you'll notice, changes the text of the 'Exit' button. In the 'Off' position, the app will simply exit, but in the 'On' position, the app will create a small text file (a 'cookie', if you will), which is placed in the same file location in which this app resides. It's simply a pointer to the current working directory, which is selected and selectable, from the 'File path' drop down. I'll explain that operation further down this page.

Although PAGE V8 supports the option for user selectable 'GUI themes', I have chosen not to implement that feature with this version of my app, which has next to no outside interest (as of the time of writing this), so going to the time and trouble of implementing a feature that nobody is going to see or use, seems a little redundant. I may very well update this app with a series of `.` releases, which will implement user selectable GUI Themes, should I receive any encouragement to do so.

### Controls & Usage

Rather than the file selector widget, that V1 used, the file for which a user needs the hash digests is selected via two `TCombobox` widgets. These widgets combine a Tk Entry widget with a Tk Listbox (that drops down on demand) all in one.

1. `File path:`

As its name suggests, one can navigate the file directory tree via this widget. The list of directories has been sorted in ascending order, with the current directory as the **second** one listed (the first being the 'parent' directory, so that one can navigate in either direction) and is pre-selected for you.

2. `File name:`

This 'drop down Combobox' is empty by default, but under it, one will find a list of files that pertain to the 'File path'. Again, the list is sorted in ascending order.

Once a file has been selected, the hash generation is initiated right away and the four hash digests (along with the file creation data and file size) will be displayed as soon as the process has been completed (please read the notes below, **BEFORE** you load any file for the hash generation). Also, the two 'Hash Values' buttons will become active and the status message will change from `Waiting...` to `Hash values unsaved.`

As before, the boxes below the hash digests is where you enter the published hash value(s), which you should obtain from the same location from which you downloaded the file that you are now checking. You can enter any of, or all four hash values, with a C&P, or (for Linux uses), the centre mouse button will simply paste a 'source selected' hash value.

The 'Save Hash Values' button will save a report file to the same directory location from which the file was selected and if clicked, the button will once again become inactive and the status message updated, while the 'Verify Hash Values' button will compare the generated values with the ones entered into the GUI box areas. There are three possible outcomes to this action:

1. The values match and you'll see the 'Hash Names' flip Green.
2. The values do not match and you'll see the 'Hash Names' flip Red.
 - This is done on an individual bases, but if you're entering multiple hash values, for the same file, you should be seeing all Greens **or** all Reds. A mix of Red and Green names means that there's an issue with the published values (assuming that you've entered the correct published hash value, in the correct entry box), which, in turn, could mean that an unauthorised change has been made to the file that you have downloaded and on which you are now (and should) be checking.
3. The 'Hash Names' will flip Grey, meaning that no comparison could be made.

So, Red 'Hash Names' means that there's a mismatch between the generated value and the one that you've entered: be **VERY** wary about that, because it could mean that an unauthorised change has been made to the file that you have downloaded. Check that you have not made an error before contacting the files's author, to let them know of the issue.

If all is well, the 'Hash Names' will be Green and you will know that the file that you have just checked has not been changed since the published hash values were generated.

The file hashing engine that I developed for V1 has been repurposed for use with my V2 application and carries the same caveat:

 - **Please note:** With larger files (size > 100 MB) it will take a noticeable amount of time to generate the hash digests. There is no known (by me) file size limit (computer RAM/swap space not withstanding) but logically, the larger the file for which you need the hash values, the more time it's going to take to generate said hash values. This app will freeze while the hash digests are being created, which it does in buffered, 1024 byte, chunks. This has been done as a system load management measure, so that if one does need to create the hash values for a large file, the RAM/swap file space requirements are minimised, so please be patient if you intend to generate hash values for relatively large files: it may take five seconds or more, to process a gigabyte of data, depending on how quickly your computer can carry out the process.

Thank you for your interest in this and I trust that you will not only find my tool of use, but also a joy to use.

The following report was generated with and for this application:

```
#====<GENERATED BY FILE CHECKSUM V2>====#

Hash values for /home/rob/checksum/v2/rc1/rc1.tar.gz

MD5
90a740a0a50bcc0ce05067518e8092a8

SHA-1
82e29ba2d55330feafbebdf67d26a7401e0ec021

SHA-256
e4c51162fcb474daa98eedaf4663a43a5c6f794dc177e35ef3dea404a6e6febb

SHA-512
2bb840fca81e37f4bcee8bca6c57a90fa4684222fecab70e5de862beaf97311e5100f7f112adb7db2b5d75c61b86bfa0d4a795afca0ecd3215fc97484255a177
```
