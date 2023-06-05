
import os
from text_summarizer.entity import DataTransformationConfig
from text_summarizer.logging import logger
from text_summarizer.constants import PROJECT_DIR
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    
    def convert_example_to_features(self,example_batch):
        # print("*"*10,"FROM ex to feat , example_ba", example_batch)
        input_encoding = self.tokenizer(example_batch['dialogue'],max_length=1024,truncation=True)
        # print("*"*10,"FROM ex to feat , input_encoding", input_encoding)
        with self.tokenizer.as_target_tokenizer():
            target_encoding = self.tokenizer(example_batch['summary'],max_length=128,truncation=True)
        # print("*"*10,"FROM ex to feat target_encoding", target_encoding)
        
        return {
            'input_ids':input_encoding['input_ids'],
            'attention_mask':input_encoding['attention_mask'],
            'labels':target_encoding['input_ids']
        }

    def convert(self):
        dataset_samsum = load_from_disk(PROJECT_DIR.joinpath( self.config.data_path))
        dataset_samsum_pt = dataset_samsum.map(self.convert_example_to_features,batched=True)
        dataset_samsum_pt.save_to_disk(os.path.join(PROJECT_DIR,self.config.root_dir,"samsum_dataset" ))