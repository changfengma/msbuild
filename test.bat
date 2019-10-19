C:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe  "E:\cprogram\cmake_test\test1\HELLO.sln" /property:Configuration=Release /t:build /p:VisualStudioVersion=12.0

e:
cd cprogram\cmake_test\test1\Release

hello.exe

pause

rem @echo off
rem echo Delete the output directory!
rem rd Release /s/q
rem rd Debug  /s/q
rem echo Building Entities.sln, please wait a minute...
rem "C:\WINDOWS\Microsoft.NET\Framework\v2.0.50727\MsBuild.exe" Entities\Entities.sln  
rem /t:rebuild 
rem /p:configuration=Debug  >Entities.log
rem echo Building Entities.sln Complete!
rem 
rem echo Building Business.sln, please wait a minute...
rem "C:\WINDOWS\Microsoft.NET\Framework\v2.0.50727\MsBuild.exe" Business\Business.sln  
rem /t:rebuild 
rem /p:configuration=Debug  >Business.log
rem echo Building Business.sln Complete!
rem 
rem echo Building UI.sln, please wait a minute...
rem "C:\WINDOWS\Microsoft.NET\Framework\v2.0.50727\MsBuild.exe" UI\UI.sln  
rem /t:rebuild 
rem /p:configuration=Debug  >UI.log
rem echo Building UI.sln Complete!
rem 
rem 到这里就结束了
rem 前面三行是清空输入路径。
rem 需要解释的是MsBuild后面的参数/t是taget ：可以是Rebuild。
rem  /property:<n>=<v>  设置或重写这些项目级属性。<n> 为
rem                     属性名，<v> 为属性值。请使用
rem                     分号或逗号分隔多个属性，或者
rem                     分别指定每个属性。(缩写为: /p)
rem                     示例:
rem                       /p:configuration=Debug;OutDir=bin\Debug\
rem OutDir就是指明了Release或者Debug的输出路径，如果不设置就是用IDE中给该项目设置的路径。
rem >Business.log是输入日志。在里面可以看到项目编译成功或者失败的信息。