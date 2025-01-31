output_dir=saves/ner/conll2002/en/test

python -u -m relogic.main \
--task_name ner \
--mode train \
--output_dir ${output_dir} \
--encoder_type xlmr \
--bert_model xlmr.base.v0  \
--raw_data_path tests/datasets/conll2002/en/ \
--label_mapping_path data/preprocessed_data/ner_BIOES_label_mapping.json \
--model_name default \
--no_cuda \
--learning_rate 1e-5 \
--train_batch_size 3 \
--test_batch_size 3 \
--epoch_number 3 \
--eval_dev_every 5 \
--pretokenized \
--metrics f1 \
--early_stop_at 5 \
--config_file configurations/ner_configuration.json

python -u -m relogic.main \
--mode eval \
--restore_path ${output_dir} \
--no_cuda

rm -r ${output_dir}