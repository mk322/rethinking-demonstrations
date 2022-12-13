
for i in direct channel
do
    python create_data.py \
    --dataset poem_sentiment,glue-rte,sick,glue-mrpc,tweet_eval-hate \
    --variant gold_w_template \
    --method $i
done