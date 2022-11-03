@echo off
setlocal enabledelayedexpansion

set language=python
set subKeyFile=%1
set basepath=%~dp0
set input=%basepath%..
set output=%basepath%..\output
set keyDir=%basepath%..\key

if not defined JAVA_HOME (
    echo "No JAVA_HOME"
    goto end
)

if not defined subKeyFile if exist "!keyDir!" (
    for /F "delims=#" %%i in ('dir "!keyDir!" /a/s/b/on') do (set subKeyFile="%%i")
)

if not defined subKeyFile (
	"%JAVA_HOME%\bin\java" -jar pkg-tool.jar -i "!input!" -o "!output!" -t "!language!" -c
) else (
    "%JAVA_HOME%\bin\java" -jar pkg-tool.jar -i "!input!" -o "!output!" -k %subKeyFile% -t "!language!" -c
)

:end
