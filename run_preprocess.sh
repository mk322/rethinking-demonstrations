
for i in direct
do
for v in base instr opin attr instr+opin
do
    python create_data.py \
    --dataset poem_sentiment,glue-rte,sick,glue-mrpc,tweet_eval-hate \
    --variant $v \
    --method $i
    done
done