#!/bin/sh

for k in base instr+opin instr opin attr
do
    for i in text-davinci-003
    do
        for j in direct
        do
            python test_gpt3.py \
                --dataset poem_sentiment_$k\_$j,glue-rte_$k\_$j,sick_$k\_$j,glue-mrpc_$k\_$j,tweet_eval-hate_$k\_$j \
                --gpt3 $i \
                --method $j \
                --out_dir out-icl-cap-gpt3/$i \
                --do_zeroshot \
                --use_demonstrations \
                --k 16 \
                --seed 21,87 \
                --test_batch_size 4
        done
    done
done

#,13,21,42,87