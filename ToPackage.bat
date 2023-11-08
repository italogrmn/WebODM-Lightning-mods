@echo off

:: Cria a pasta Plugin Revit e limpa possíveis lixos
for %%I in ("%cd%") do set PastaAtual=%%~fI

if exist "%PastaAtual%\package" (
    rmdir /s /q "%PastaAtual%\package"
    Mkdir "%PastaAtual%\package"
) else (
    Mkdir "%PastaAtual%\package"
)

copy potree.js "%PastaAtual%\package"
copy projects.py "%PastaAtual%\package"
copy sidebar.html "%PastaAtual%\package"

:: Cria o instalador
cd %PastaAtual%
pyinstaller --onefile --add-data="package;package" WebODM_mods.py

:: Move o executável para pasta atual
move %PastaAtual%\dist\WebODM_mods.exe %PastaAtual%

:: Limpa o lixo
rmdir /s /q %PastaAtual%\build
rmdir /s /q %PastaAtual%\dist
rmdir /s /q "%PastaAtual%\package"
del WebODM_mods.spec

pause