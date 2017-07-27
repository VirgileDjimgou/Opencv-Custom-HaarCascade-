opencv_createsamples -img 3hearts.png -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 1.1 -maxyangle 1.1 -maxzangle 0.5 -num 1950

opencv_createsamples -info info/info.lst -num 1950 -w 50 -h 75 -vec positives.vec

opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 400 -numNeg 200 -numStages 3 -w 50 -h 75 &

