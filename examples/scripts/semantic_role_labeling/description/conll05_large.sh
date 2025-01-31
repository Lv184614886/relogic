python -u -m relogic.main  \
--task_name srl \
--mode train \
--output_dir saves/semantic_role_labeling/conll05_large_description_4 \
--bert_model bert-large-cased \
--raw_data_path data/raw_data/srl/json/conll05/propbank \
--train_file train.json \
--dev_file dev.json \
--test_file test.json \
--label_mapping_path data/preprocessed_data/srl_conll05_BIOES_label_mapping.pkl \
--model_name default \
--local_rank $1 \
--train_batch_size 16 \
--test_batch_size 16 \
--learning_rate 3e-5 \
--epoch_number 3 \
--eval_dev_every 1000 \
--hidden_size 1024 \
--no_bilstm \
--gradient_accumulation_steps 2 \
--srl_module_type description_aware \
--use_description \
--external_embeddings data/embeddings/wiki-news-300d-1M.npy \
--use_span_candidates \
--two_stage_optim \
--adam_learning_rate 0.005 \