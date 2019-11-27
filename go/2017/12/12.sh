#! /bin/sh

echo "Part 1 :"
echo " graph day12 {
$(sed -e "s/<->/--/" 12.in)
}" | ccomps -X 0 | gc -n

echo "Part 2 :"
echo " graph day12 {
$(sed -e "s/<->/--/" 12.in)
}" | gc -c
