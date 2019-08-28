from relogic.logickit.dataflow import SRLDataFlow
from types import SimpleNamespace
import json
from relogic.logickit.tokenizer.fasttext_tokenization import FasttextTokenizer
from relogic.logickit.tokenizer.tokenization import BertTokenizer
from relogic.structures.sentence import Sentence
import relogic.utils.crash_on_ipy


config = SimpleNamespace(**{
    "buckets": [(0, 15), (15, 40), (40, 450)],
    "max_seq_length": 450,
    "label_mapping_path": "data/preprocessed_data/srl_conll05_label_mapping.json",
    "srl_label_format": "srl_label_span_based"})


tokenizers = {
  "BPE": BertTokenizer.from_pretrained("bert-large-cased"),
  "Fasttext": FasttextTokenizer.from_pretrained("wiki-news-300d-1M")}

dataflow = SRLDataFlow(task_name="joint_srl",
                       config = config,
                       tokenizers=tokenizers,
                       label_mapping=json.load(open(config.label_mapping_path)))

structures = [Sentence(text="I went to Paris yesterday .")]
dataflow.update_with_structures(structures)

examples = [{"tokens": ["I", "went", "to", "Paris", "yesterday", "."],
           "labels": [(1, 2, "went", 0, 1, "I", "A0"), (1, 2, "went", 3, 4, "Paris", "A1")],
           "label_candidates": [[0], [0, 1, 2, 3], [0], [0], [0], [0]]},
            {"tokens": ["But", "I", "didn't", "find", "you", "lol", "."],
            "labels": [(3, 4, "find", 0, 1, "But", "AM-DIS")],
            "label_candidates": [[0], [0], [0], [5, 6, 7, 8, 9],[0], [0], [0]]}]
dataflow.update_with_jsons(examples)

for mb in dataflow.get_minibatches(minibatch_size=2):
  print(mb)

raise NotImplementedError("You can start to play with data")


