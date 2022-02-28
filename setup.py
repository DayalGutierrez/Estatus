import sys, os
from cx_Freeze import setup, Executable

files = ['main_view.py','mainwindow.py']

exe = Executable(script='Agenda.py',base='Win32GUI')

setup(
    name="Agenda de alumnos",
    version='1.0',
    description="Agenda para poder guardar contactos de alumnos",
    author="Dayal Gutierrez",
    options={'build_exe':{'include_files': files}},
    executables = [exe]
)