#!/bin/sh

for k in base instr+opin instr opin attr
do
    for i in gpt2-large gpt-j-6B
    do
        for j in direct
        do
            python test.py \
                --dataset poem_sentiment_$k\_$j,glue-rte_$k\_$j,sick_$k\_$j,glue-mrpc_$k\_$j,tweet_eval-hate_$k\_$j \
                --gpt2 $i \
                --method $j \
                --out_dir out-icl-cap/$i \
                --do_zeroshot \
                --use_demonstrations \
                --k 16 \
                --seed 21,87 \
                --test_batch_size 4
        done
    done
done

#,13,21,42,87