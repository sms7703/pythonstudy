@echo off
powershell -c "(Get-AudioDevice -PlaybackLevel).Volume = 1.0"