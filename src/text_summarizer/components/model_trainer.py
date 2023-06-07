import os
import torch
from datasets import load_dataset, load_from_disk
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from text_summarizer.entity import ModelTrainerConfig
from text_summarizer.constants import PROJECT_DIR

class ModelTrainer:
    def __init__(self, config:ModelTrainerConfig):
        self.config = config
    
    def train(self):
        # check cuda 
        device = "cuda" if torch.cuda.is_available() else "cpu"
        print("Using device:", device)
        torch.cuda.empty_cache()
        print('Memory Usage Befor load model to device:')
        print('Allocated:', round(torch.cuda.memory_allocated(0)/1024**3,1), 'GB')
        print('Cached:   ', round(torch.cuda.memory_reserved(0)/1024**3,1), 'GB')
        # loading tokenizer
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        # loading model
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer,model=model_pegasus)

        print('Memory Usage After load model to device:')
        print('Allocated:', round(torch.cuda.memory_allocated(0)/1024**3,1), 'GB')
        print('Cached:   ', round(torch.cuda.memory_reserved(0)/1024**3,1), 'GB')

        # loading dataset
        dataset_samsum_pt = load_from_disk(PROJECT_DIR.joinpath(self.config.data_path))

        # set training parameters
        trainer_args = TrainingArguments(
            output_dir=PROJECT_DIR.joinpath(self.config.root_dir),
            num_train_epochs=self.config.num_train_epochs,
            
            warmup_steps=self.config.warmup_steps,

            per_device_train_batch_size=self.config.per_device_train_batch_size,
            per_device_eval_batch_size=self.config.per_device_eval_batch_size,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy,
              eval_steps=self.config.eval_steps, save_steps=self.config.save_steps,
            gradient_accumulation_steps=self.config.gradient_accumlation_steps,
            # optim=self.config.optim,
            # optim="adamw_torch",
        )
        # train model
        trainer = Trainer(model=model_pegasus,args=trainer_args,
                          tokenizer=tokenizer, data_collator=seq2seq_data_collator,
                          train_dataset=dataset_samsum_pt["train"],
                          eval_dataset=dataset_samsum_pt["validation"])
        
        trainer.train()
        # save model
        model_pegasus.save_pretrained(os.path.join(PROJECT_DIR,
                                                   self.config.root_dir,
                                                   "pegasus_model_samsum"))
        # save tokenizer
        tokenizer.save_pretrained(os.path.join(PROJECT_DIR,
                                               self.config.root_dir,
                                               "tokenizer"))
