pydragon
========

[Heighway dragon](https://en.wikipedia.org/wiki/Dragon_curve#Heighway_dragon) with Python and gnuplot.

Usage
-----

Static version:
```shell
$ ./dragon.py 12 | gnuplot -p plot.gp
```

Animated plot:
```shell
$ ./dragon.py 12 > data.txt && gnuplot -p plot_anim.gp
```

License
-------

Licensed under the GNU General Public License. (see LICENSE.txt)
