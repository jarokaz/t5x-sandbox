"""KFP components."""

from typing import Optional

from kfp.v2 import dsl
from kfp.v2.dsl import Artifact
from kfp.v2.dsl import Dataset
from kfp.v2.dsl import Input
from kfp.v2.dsl import Model
from kfp.v2.dsl import Output


@dsl.component()
def generate_output_dir(
    model_dir: Output[Artifact],
    tfds_dataset_dir: Output[Artifact]
):
    pass