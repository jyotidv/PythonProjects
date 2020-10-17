from cx_Freeze import *

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
        "[TARGETDIR]\smartCalculator.exe",   #target
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
    description="Calculator",
    author="Jyoti Yadav",
    name="Calculator",
    options={'build_exe':{'include_files':includefiles}, "bdist_msi":bdist_msi_options},
    executables=[
        Executable(
            script="smartCalculator.py",
            base=base,
            icon='cali.ico'
        )

    ]
)


