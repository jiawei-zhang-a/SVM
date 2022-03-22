echo -n > train/dev.results.txt
for F in train/dev.*.log.txt; do
    echo $F $(cat $F) | \
        sed 's;.*\.\(.*\)\.\(.*\)\.\(.*\)\.log.* = \(.*\)%.*;\1 \2 \3 \4;' \
        | grep -v 'classification' \
        >> train/results.txt;
done

