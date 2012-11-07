@echo off

::echo %~1
::echo %~2

set dri=%~d1
set dir=%~p1
set fname=%~1

::echo %dri%
::echo %dir%
%dri%
cd %dir%

git add %fname%
git commit -m %2 %fname%
