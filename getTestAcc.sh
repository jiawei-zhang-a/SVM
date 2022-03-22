echo -n > test/dev.results.txt
for F in test/dev.*.log.txt; do
    echo $F $(cat $F) | \
        sed 's;.*\.\(.*\)\.\(.*\)\.\(.*\)\.log.* = \(.*\)%.*;\1 \2 \3 \4;' \
        | grep -v 'classification' \
        >> test/results.txt;
done

