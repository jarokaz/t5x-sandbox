# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google_cloud_pipeline_components.v1.custom_job import CustomTrainingJobOp

from kfp.v2 import dsl
import components

@dsl.pipeline(
    name='finetuning-export-t5x-model',
    description='Fine tuning and exporting a T5x model using Vertex Pipelines.'
)
def finetune_pipeline(
    worker_pool_specs: str,
    project_id: str,
    image_uri: str
):
  import json

  """T5x Pipeline."""
  output_dirs = components.generate_output_dir()

  model_dir = output_dirs.outputs['model_dir']
  tfds_dataset_dir = output_dirs.outputs['tfds_dataset_dir']

  # Updating worker_pool_specs specs
  specs = json.loads(worker_pool_specs)
  specs[0]['container_spec']['image_uri'] = image_uri
  specs[0]['container_spec']['args'].append(f'--gin.MODEL_DIR="{model_dir.uri}"')
  specs[0]['container_spec']['args'].append(f'--tfds_data_dir={tfds_dataset_dir.uri}')

  # Submit Vertex Ai training job
  CustomTrainingJobOp(
    project=project_id,
    display_name='t5x-finetune-small',
    worker_pool_specs=specs
  )
