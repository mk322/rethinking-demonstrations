from accelerate import infer_auto_device_map, load_checkpoint_and_dispatch, init_empty_weights
from transformers import AutoConfig, AutoModelForCausalLM
import torch
import os

# Credit: Murray Kang

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

def init_opt_max_iml_30b(model_name):
    
    shortname = model_name.split("/")[1]
    weights_path = f"/gscratch/scrubbed/haoqik/{shortname}"
    if not os.path.exists(weights_path):
        os.makedirs(weights_path)
        model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="balanced_low_0")
        model.save_pretrained(weights_path)

    config = AutoConfig.from_pretrained(model_name)

    config.use_cache = False

    with init_empty_weights():
        model = AutoModelForCausalLM.from_config(config)

    device_map = infer_auto_device_map(model, no_split_module_classes=["OPTDecoderLayer"], dtype="float16")
    model = load_checkpoint_and_dispatch(
	    model,
	    weights_path,
	    device_map=device_map,
	    offload_folder=None,
	    offload_state_dict=False,
	    dtype="float16"
	)

    return model