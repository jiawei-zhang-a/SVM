mkdir results
echo -n > output/dev.results.txt
for F in output/dev.*.log.txt; do
    echo $F $(cat $F) | \
        sed 's;.*\.\(.*\)\.\(.*\)\.\(.*\)\.log.* = \(.*\)%.*;\1 \2 \3 \4;' \
        | grep -v 'classification' \
        >> results/results.txt;
done

