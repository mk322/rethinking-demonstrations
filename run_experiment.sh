#!/bin/sh

for k in instructive irrelevant misleading_extreme null_temp
do
    for i in gpt2-large gpt-j-6B
    do
        for j in direct channel
        do
            python test.py \
                --dataset poem_sentiment_gold_w_template_$k\_$j,glue-rte_gold_w_template_$k\_$j,sick_gold_w_template_$k\_$j,glue-mrpc_gold_w_template_$k\_$j,tweet_eval-hate_gold_w_template_$k\_$j \
                --gpt2 $i \
                --method $j \
                --out_dir out/$i \
                --do_zeroshot \
                --use_demonstrations \
                --k 16 \
                --seed 100,13,21,42,87 \
                --test_batch_size 4
        done
    done
done