# -*- coding: utf-8 -*-
import logging
import subprocess
import time
from itertools import product
from torch.optim import AdamW

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)  # 配置日志记录器
    #train(预测出的数据，正负样本)， shot,
    # l = ['JDDC']
    # l = ['DuDialRec']
    l = ['inspired']
    batch_sizes = [16]
    # batch_sizes = [4,8,16,32,64]
    learning_rates = ['5e-5']
    # learning_rates = ['2e-5','3e-5','4e-5','5e-5']
    # learning_rates = ['3e-1','3e-2','3e-3','3e-4','3e-5','3e-6','3e-7','3e-8']
    # shots = [10,20,30,40,50,60,70]
    shots = [50]    #
    # seeds = [i for i in range(100,151)]
    # seeds = [146,137,109,123,144]
    seeds = [146]
    template_id = [0]#换模板时候pipeline_base里面的title = wrapped_example[0][3]['text']也要把3换掉
    # verbalizer = ['kpt','kpt1','kpt2','kpt3','kpt4','kpt5']
    verbalizer = ['kpt']            #'kpt','manual'
    max_epochs = [15]
    for n, t, j, i, k, v, m, e in product(l,template_id, seeds, batch_sizes, learning_rates, verbalizer,shots, max_epochs):
        cmd = (
            f"python fewshot.py --result_file ./result/ch_result.txt "
            # f"--label_result ./i_label/shot{m}bs{i}seed{j}lr{k}.txt "
            f"--dataset {n} --template_id {t} --seed {j} "
            f"--batch_size {i} --shot {m} "
            f"--learning_rate {k} --verbalizer {v} "
            f"--max_epochs {e}"
        )

        logging.info(f"Executing command: {cmd}")
        print(cmd)
        try:
            subprocess.run(cmd, shell=True, check=True)
            logging.info(f"Command executed successfully: {cmd}")
        except subprocess.CalledProcessError as e:
            # logging.error(f"Command failed: {cmd}. Error: {e.stderr.decode().strip()}")
            logging.error(f"Command failed: {cmd}. Error: {e}")

        time.sleep(1)
