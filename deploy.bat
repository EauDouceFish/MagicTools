@echo off
call hexo clean
call hexo g
call hexo d

echo.
echo Deploy complete. Starting local server...
start cmd /k "hexo s"
start http://localhost:4000
echo.
echo Server started in new window. Press any key to exit...
pause > nul