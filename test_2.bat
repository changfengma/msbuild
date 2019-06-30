@echo off

echo "enviroment set........"
call "D:\\VS2013\\Common7\\Tools\\VsDevCmd.bat"

echo "building hello.exe ...."
MSBuild E:\cprogram\cmake_test\test1\HELLO.sln /t:build /p:VisualStudioVersion=12.0 /property:Configuration=Release

echo "starting run..."
E:\cprogram\cmake_test\test1\Release\hello.exe

rem MSBuild /help

pause

