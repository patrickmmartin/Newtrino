filename=$(basename "$1")
root=${filename%.*}

echo $root.png ...
dot -Tpng  -Ggpi-96 -O $1
mv $1.png $root.png 

echo $root-small.png ...
dot -Tpng -Gdpi=72 -O $1
mv $1.png $root.png 

echo $root.pdf ...
dot -Tpdf  -O $1
mv $1.pdf $root.pdf 

echo $root.svg ...
dot -Tsvg  -O $1

