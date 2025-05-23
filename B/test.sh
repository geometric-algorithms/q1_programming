#!/bin/bash


points1=( 0 0   1 2   2 1   3 3   4 0   3 -2   1 -1   2 -3   5 2   2 2 )

points2=( 0 0   1 1   2 2   3 3 )

points3=( 0 0   0 1   1 1   1 0 )

points4=( 0 0   1 3   2 0 )

points5=( 1 1 )

points6=( 0 0   4 0   4 4   0 4   1 1   2 2   3 3 )

points7=( 0 0   4 0   4 4   0 4   1 1   2 2   3 3   1 0   2 0   3 0 )

points8=( 0 0   1 0   0 1   -1 0   0 -1   2 2   -2 2   2 -2   -2 -2   3 0   -3 0   0 3   0 -3   4 4   -4 4   4 -4   -4 -4   5 0   -5 0   0 5 )

points9=( 0 0   1 2   2 1   3 3   4 2   5 0   4 -2   3 -3   2 -2   1 -3   0 -1   1 0   2 0   3 0   4 0   1 1   2 2   3 1   2 -1   3 -1 )

points10=( 1 8   3 10   6 9   8 7   7 4   6 2   3 1   1 2   2 5   4 5   5 6   4 7   0 3   2 3   3 2   1 1   1.5 4.5   5 3.5   3.5 6   6.5 5 )

points11=( 100 100   200 50   350 200   450 300   400 450   250 400   150 300   250 150   200 250   300 350   350 250   100 200   200 300   250 250   350 400   300 100   125 250   175 150   325 300   275 375 )

points12=( 1 3   4 7   6 2   8 9   0 5   3 1   7 6   2 8   5 0   9 4   4 4   6 6   1 9   8 2   0 0   2 3   7 1   9 9   3 5   5 7 )

points13=( 1 2   3 5   6 1   8 7   2 9   4 4   7 3   0 6   5 2   9 8   3 0   6 6   1 8   7 9   2 0   8 3   4 7   0 1   5 5   9 2   3 3   6 9   1 6   7 0   2 2   8 5   4 0   0 9   5 7   9 1   3 8   6 0   1 0   7 5   2 6 )

points14=( 0 0   1 2   2 4   3 1   4 3   5 0   6 5   7 2   8 6   9 1   10 4   11 0   12 3   13 5   14 2   15 6   16 1   17 3   18 0   19 5   20 2   21 4   22 1   23 3   24 0   25 6   26 2 )

points15=( 0 1   1 4   2 0   3 3   4 2   5 5   6 1   7 6   8 2   9 4   10 0   11 3   12 5   13 1   14 6   15 2   16 4   17 0   18 3   19 1   20 5   21 2   22 6   23 0   24 4   25 3   26 1 )

points16=( 1 1   2 4   3 2   4 6   5 3   6 7   7 1   8 5   9 2   10 6   11 3   12 7   13 4   14 0   15 5   16 1   17 6   18 2   19 4   20 0   21 3   22 7   23 1   24 6   25 2   26 5   27 0 )

points17=( 0 0   5 0   10 0   10 5   10 10   5 10   0 10   0 5   1 1   2 2   3 3   4 4   5 5   6 6   7 7   8 8   9 9   5 2   5 8   2 5   8 5   0 2   10 2   0 0   10 10   10 10   5 5   6 4   6 5  6 6   7 5   5 6   3 7   7 3   4 6   6 2   2 6   0 0.1   9.9 0 )

points18=( 0 0   1 1   2 2   3 3   4 4 )

points19=( 0 0   1 1   2 2   1 1   2 2   0 0 )

points20=( 0 0   1 2   3 3   4 2   5 0   3 -2   1 -2 )

points21=( 0 3   1 1   2 2   3 1   4 3   2 0 )

points22=( 0 0   5 0   10 0   5 5   0 10   10 10 )

points23=( 0 0   1e-9 1e-9   2e-9 2e-9   1 1 )

points24=( 0 0   5 0   10 0   10 5   0 5   5 2 )

#points25=( 0 0   10 0   10 10   0 10 )+( 5+1e-8*i 5+1e-8*j foriinrange 3 forjinrange 3 )

points26=( 0 0   5 0   2.5 4   2.5 4   5 0 )

#points27=( 10**9 10**9   -10**9 10**9   -10**9 -10**9   10**9 -10**9   0 0 )

points28=( 43 27   50 67   34 5   72 60   39 18   15 10   17 63   22 25   64 28   55 24   3 58   19 26   0 11   41 33   32 21   37 48   12 7   59 31   16 13   73 52   68 1   38 35   9 44   36 40   2 20   8 46   29 42   6 62   70 61   66 49   30 23   54 47   14 45   57 53   56 4   71 69   51 0 )

points29=( 17 60   66 9   59 23   18 12   31 42   8 68   22 6   58 25   16 43   72 36   3 45   55 35   73 48   62 26   30 1   32 28   50 69   63 37   41 19   14 39   7 4   20 13   27 44   47 0   2 11   29 5   38 51   10 21   24 33   64 15   61 70   56 40   53 57   46 34   52 67   49 54   71 0 )

points30=( 29 71   67 48   5 1   3 40   63 18   41 34   0 27   20 16   68 25   43 17   55 21   26 37   28 11   62 7   60 9   24 19   56 53   31 36   23 59   66 6   4 42   33 15   22 32   44 14   46 13   12 50   35 38   10 70   69 73   45 52   2 30   8 47   57 49   39 64   58 51   61 72   65 0 )

points31=( 0 0   1 0   0 1   -1 0   0 -1   2 2   -2 2   2 -2   -2 -2   3 0   -3 0   0 3   0 -3   4 5   -4 3   3 -3   -3 -5   5 0   -5 0   0 5 )


python3 b.py "${points28[@]}"
