from modelscope.hub.snapshot_download import snapshot_download
import os
os.environ['MODELSCOPE_CACHE'] ='/home/zy-4090-1/hqq/conversation_recommendation/models'
model_name = 'langboat/mengzi-t5-base'

snapshot_download(model_name)
