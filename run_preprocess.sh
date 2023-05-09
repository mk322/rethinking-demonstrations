
for i in direct
do
    python create_data.py \
    --dataset poem_sentiment,glue-rte,sick,glue-mrpc,tweet_eval-hate \
    --variant attr \
    --method $i
done