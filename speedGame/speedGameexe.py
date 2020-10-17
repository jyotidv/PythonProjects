from cx_Freeze import *
 #for exe file hit cmd: python speedGameexe.py bdist_msi
includefiles =['cali.ico']
base = None

if sys.platform=='win64':
    base='win64GUI'

shortcut_table=[
    (
        "DesktopShortcut",  #shortcut
        "DesktopFolder",    #Directory
        "Calculator",       #name
        "TARGETDIR",        #component
        "[TARGETDIR]\speedGame.exe",   #target
        None,     #Arg
        None,     #Description
        None,     #Hotkey
        None,      #icon
        None,      #Iconindex
        None,      #showcmd
        "TARGETDIR",   #wkdir
    )
]

msi_data= {'Shortcut':shortcut_table}

#to change some default setting

bdist_msi_options={'data': msi_data}
setup(
    version="0.1",
    description="SpeedGame",
    author="Jyoti Yadav",
    name="SpeedGame",
    options={'build_exe':{'include_files':includefiles}, "bdist_msi":bdist_msi_options},
    executables=[
        Executable(
            script="typingSpeed.py",
            base=base,
            icon='cali.ico'
        )

    ]
)


