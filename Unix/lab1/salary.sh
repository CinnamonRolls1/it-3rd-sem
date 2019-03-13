#1/bin/sh
echo "Basic:"
read basic
dp=$(echo "scale=3; 50 / 100 * $basic" | bc)
da=$(echo "scale=3; 35 / 100 * ($basic + $dp)" | bc)
hra=$(echo "scale=3; 8 / 100 * ($basic + $dp)" | bc)
ma=$(echo "scale=3; 3 / 100 * ($basic + $dp)" | bc)
pf=$(echo "scale=3; 10 / 100 * ($basic + $dp)" | bc)
sal=$(echo "scale=3; $basic + $dp + $da + $hra + $ma - $pf" | bc)
echo "sal: $sal"
