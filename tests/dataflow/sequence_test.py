import json
from types import SimpleNamespace

import relogic.utils.crash_on_ipy
from relogic.logickit.base.constants import SEQUENCE_LABELING_TASK
from relogic.logickit.dataflow import TASK_TO_DATAFLOW_CLASS_MAP, SequenceDataFlow
from relogic.logickit.tokenizer.tokenization import BertTokenizer

config = SimpleNamespace(
  **{
    "buckets": [(0, 15), (15, 40), (40, 450)],
    "max_seq_length": 450,
    "label_mapping_path": "data/preprocessed_data/ner_BIOES_label_mapping.json"
  })

tokenizers = {
  "BPE": BertTokenizer.from_pretrained("bert-base-multilingual-cased", do_lower_case=False),
}

dataflow: SequenceDataFlow = TASK_TO_DATAFLOW_CLASS_MAP[SEQUENCE_LABELING_TASK](
  task_name=SEQUENCE_LABELING_TASK,
  config=config,
  tokenizers=tokenizers,
  label_mapping=json.load(open(config.label_mapping_path)))

examples = [{
  "tokens": ["I", "visited", "China", "yesterday", "."],
  "labels": ["O", "O", "S-LOC", "O", "O"]
},{
  "tokens": ["Barack", "Obama", "went", "to", "Paris", "."],
  "labels": ["B-PER", "E-PER", "O", "O", "S-LOC", "O"]
}]

dataflow.update_with_jsons(examples)

for mb in dataflow.get_minibatches(minibatch_size=2):
  print(mb)

raise NotImplementedError("You can start to play with data")