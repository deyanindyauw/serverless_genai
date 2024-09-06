@echo off
setlocal enabledelayedexpansion

REM Check if the number of times to call the command is provided
if "%1"=="" (
    echo Usage: %0 number_of_times
    exit /b 1
)

REM Set the number of times to call the AWS CLI command
set count=%1

REM Loop to call the AWS CLI command
for /L %%i in (1,1,%count%) do (
    echo Calling AWS CLI command %%i of %count%
    echo.
    echo Node
    aws lambda invoke --function-name Fibonaaci_GeneratorMethod_Node --cli-binary-format raw-in-base64-out response_node.json
    if errorlevel 1 (
        echo AWS CLI command failed at iteration %%i
        exit /b 1
    )
)

echo Completed calling AWS CLI command %count% times
endlocal