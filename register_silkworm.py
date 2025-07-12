from detectron2.data.datasets import register_coco_instances

def register_silkworm_dataset():
    register_coco_instances(
        "silkworm_unsup", {},
        "../data/annotations.json",
        "../data/images"
    )
