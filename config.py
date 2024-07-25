# config.py
from omegaconf import OmegaConf

default_config = {
    "model_cache_dir": "/tmp/model_cache",
    "download_timeout": 600,  # 10 minutes
    "max_retries": 3,
    "chunk_size": 8192,
}

config = OmegaConf.create(default_config)

def update_config(new_config):
    global config
    config = OmegaConf.merge(config, new_config)