
REM @ECHO OFF


REM SET SAGA_MLB=C:\SAGA\Modules
REM SET PATH=%PATH%;C:\SAGA

REM *****************POTI***********************************

REM Pot do delovnega okolja
set WORK=D:\LIDARucenje\UvoziVecListov\UvozSAGAvGRID\SGRD 

REM *******************POTI NASTAVLJENE*************************

REM ****************** PROCESIRAM ******************************
FOR /F %%i IN ('dir /b %WORK%\*.sgrd') DO (

saga_cmd io_grid "Export ESRI Arc/Info Grid" ^
-GRID=%WORK%\%%i ^
-FILE=%WORK%\ASCII\%%~ni.asc ^
-FORMAT=1 -GEOREF=0 -PREC=4 -DECSEP=0

)

PAUSE
