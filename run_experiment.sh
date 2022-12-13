#!/bin/sh

for i in gpt-j-6B gpt2-large
do
    for j in direct channel
    do
    python test.py \
        --dataset poem_sentiment_gold_w_template_$j,glue-rte_gold_w_template_$j,sick_gold_w_template_$j,glue-mrpc_gold_w_template_$j,tweet_eval-hate_gold_w_template_$j \
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