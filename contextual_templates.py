import string

CONTEXT_TEMP = {
    "instr": "Instruction: answer a question based on the provided context.\n "
}

TEMPLATES = {
    "financial_phrasebank": {
        "direct" : ("{}", "The sentiment is: {}"),
        "channel": ("{}", "The sentiment is: {}")
    },
    "poem_sentiment": {
        "direct" : {
            "base": ("{}", "The sentiment is: {}"),
            "attr": ("{} Based on the poem, ", "the sentiment is: {}."),
            "opin": ("Bob wrote the poem, \"{}\" In Bob’s poem, ", "the sentiment is: {}"),
            "instr": ("Instruction: give the sentiment based on the provided poem.\n{}", "The sentiment is: {}"),
            "instr+opin": ("Instruction: give the sentiment based on the provided poem.\nBob wrote the poem, \"{}\" In Bob’s poem, ", "the sentiment is: {}")
            },
        "channel": ("{}", "The sentiment is: {}")
    },
    "glue-mrpc": {
        "direct" : {
            "base": ("{}\nThe question is: {} True or False?", "The answer is: {}"),
            "attr": ("Context:{}\nThe question is: {} True or False? Based on the context, ", "the answer is: {}"),
            "opin": ("Bob said, \"{}\"\nThe question is: {} True or False? In Bob’s opinion, ", "the answer is: {}"),
            "instr": ("Instruction: answer the question based on the provided context.\nContext:{}\nThe question is: {} True or False?", "The answer is: {}"),
            "instr+opin": ("Instruction: answer the question based on Bob's opinion.\nBob said, \"{}\"\nThe question is: {} True or False? In Bob’s opinion, ", "the answer is: {}"),
        },
        "channel": ("The question is: {} True or False?\n{}", "The answer is: {}")
    },
    "glue-rte": {
        "direct" : {
            "base": ("{}\nThe question is: {} True or False?", "The answer is: {}"),
            "attr": ("{}\nThe question is: {} True or False? Based on the context, ", "the answer is: {}"),
            "opin": ("Bob said, \"{}\"\nThe question is: {} True or False? In Bob’s opinion, ", "the answer is: {}"),
            "instr": ("Instruction: answer the question based on the provided context.\nContext:{}\nThe question is: {} True or False?", "The answer is: {}"),
            "instr+opin": ("Instruction: answer the question based on the Bob's opinion.\nBob said, \"{}\"\nThe question is: {} True or False? In Bob’s opinion, ", "the answer is: {}"),
        },
        "channel": ("The question is: {} True or False?\n{}", "The answer is: {}")
    },
    "sick": {
        "direct" : {
            "base": ("{}\nThe question is: {} True or False?", "The answer is: {}"),
            "attr": ("{}\nThe question is: {} True or False? Based on the context, ", "the answer is: {}"),
            "opin": ("Bob said, \"{}\"\nThe question is: {} True or False? In Bob’s opinion, ", "the answer is: {}"),
            "instr": ("Instruction: answer the question based on the provided context.\nContext:{}\nThe question is: {} True or False?", "The answer is: {}"),
            "instr+opin": ("Instruction: answer the question based on Bob's opinion.\nBob said, \"{}\"\nThe question is: {} True or False? In Bob’s opinion, ", "the answer is: {}"),
        },
        "channel": ("The question is: {} True or False?\n{}", "The answer is: {}")
    },
    "tweet_eval-hate": {
        "direct" : {
            "base": ("Tweet: {}", "Sentiment: {}"),
            "attr": ("Tweet: {} Based on the tweet,", "sentiment: {}"),
            "opin": ("Bob wrote the tweet: , \"{}\"\nIn Bob’s tweet, ", "sentiment: {}"),
            "instr": ("Instruction: give the sentiment based on the provided tweet.\nTweet: {}", "sentiment: {}"),
            "instr+opin": ("Instruction: give the sentiment based on Bob's tweet.\nBob wrote the tweet, \"{}\"\nIn Bob’s tweet, ", "sentiment: {}")
            },
        #"direct" : ("Tweet: {}", "Sentiment: {}"),
        "channel": ("Tweet: {}", "Sentiment: {}"),
    },
    "openbookqa": {
        "direct" : ("The question is: {}", "The answer is: {}"),
        "channel": ("The question is: {}", "The answer is: {}")
    },
    "ai2_arc": {
        "direct" : ("The question is: {}", "The answer is: {}"),
        "channel": ("The question is: {}", "The answer is: {}")
    },
    "codah": {
        "direct" : ("The question is: {}", "The answer is: {}"),
        "channel": ("The question is: {}", "The answer is: {}")
    },
    "commonsense_qa": {
        "direct" : ("The question is: {}", "The answer is: {}"),
        "channel": ("The question is: {}", "The answer is: {}")
    }
}

def apply_template(dp, dataset, method, prompt):
    if dataset.startswith("glue") or dataset.startswith("sick"):
        def map_option(option):
            if option in ["equivalent", "entailment"]:
                return "True"
            if option in ["not_equivalent", "not_entailment", "contradiction"]:
                return "False"
            if option in ["neutral"]:
                return "Not sure"
            raise NotImplementedError(option)
        dp["input"] = dp["input"].replace("sentence 1: ", "").replace("sentence 2: ", "")
        splits = dp["input"].split(" [SEP] ")
        if method=="channel":
            splits = [splits[1], splits[0]]
        splits = [split if split[-1] in string.punctuation else split+"." for split in splits]
        dp["input"] = TEMPLATES[dataset][method][prompt][0].format(splits[0], splits[1])
        dp["output"] = TEMPLATES[dataset][method][prompt][1].format(map_option(dp["output"]))
        for i, options in enumerate(dp["options"]):
            dp["options"][i] =TEMPLATES[dataset][method][prompt][1].format(map_option(dp["options"][i]))
    else:
        def map_option(option):
            if dataset=="tweet_eval-hate":
                return {"hate": "against", "non-hate": "favor"}[option]
            return option
        dp["input"] = TEMPLATES[dataset][method][prompt][0].format(dp["input"])
        dp["output"] = TEMPLATES[dataset][method][prompt][1].format(map_option(dp["output"]))
        for i, options in enumerate(dp["options"]):
            dp["options"][i] =TEMPLATES[dataset][method][prompt][1].format(map_option(dp["options"][i]))





