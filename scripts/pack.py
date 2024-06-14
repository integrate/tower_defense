import PyInstaller.__main__ as pi

pi.run([
    "../source/main.pyw", #w need to prevent console window #path to main python file. relatively to this script itself.
    "-y", #remove old files without confirmation
    "--windowed",
    # "--onedir", #pack as file+folder pack
    "--onefile", #pack as one-file dist

    "--specpath=../temp/spec", #folder that will be created and where .spec file will be placed. Relative to main.py
    "--distpath=../temp/dist", #folder that will be created and where final .EXE file will be placed. Relative to main.py
    "--workpath=../temp/build", #folder that will be created and where temporary building files will be placed. Relative to main.py

    "--name=Tower Defense",
    "--icon=../../source/assets/icon.ico",

    "--add-data=../../source/assets:assets" #path to folder with assets. Relative to "spec" folder
])

