#!/usr/bin/env gnuplot

set title 'Heighway sequence'

set terminal x11
#set style line 1 lc rgb '#0060ad' lt 1 lw 2 pt 7 ps 1.5
set style line 1 lc rgb '#0060ad' lt 1 lw 1 pt 7 ps 0.1

set xzeroaxis lt 3 lw 1
set yzeroaxis lt 3 lw 1

#set xrange [-200:100]
#set yrange [-100:200]
set xrange [-30:80]
set yrange [-80:30]

N=system("wc -l data.txt") 
do for [i=1:N] {
  plot 'data.txt' every ::1::i notitle with linespoints ls 1; #pause 0.0001
}
