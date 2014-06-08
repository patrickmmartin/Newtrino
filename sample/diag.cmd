@if "%1"=="" echo need input file & exit /b

@echo %~n1.png ...
@"c:\Program Files (x86)\Graphviz2.36\bin\dot" -Tpng  -Ggpi=96 -O %1
@move /Y %1.png %~n1.png > nul

@echo %~n1-small.png ...
@"c:\Program Files (x86)\Graphviz2.36\bin\dot" -Tpng -Gdpi=72  -O %1
@move /Y %1.png %~n1-small.png > nul

@echo %~n1.pdf ...
@"c:\Program Files (x86)\Graphviz2.36\bin\dot" -Tpdf  -O -s12 %1 
@move /Y %1.pdf %~n1.pdf > nul

@echo %~n1.svg ...
@"c:\Program Files (x86)\Graphviz2.36\bin\dot" -Tsvg  -O %1 
