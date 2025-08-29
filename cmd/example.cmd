@REM @echo off
call cd pathtofolder\steamtl
call conda activate base // or the env you got all the lib installed
call python ./main.py --exe_path "C:\Program Files (x86)\Steam\steamapps\common\Russian Subway Dogs\russian_subway_dogs.exe" --steam_app_id 762610
REM Keep the window open
PAUSE

