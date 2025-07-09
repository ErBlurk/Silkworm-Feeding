# Silkworm_Feeding Annotation Pipeline

This guide shows how to automatically generate **COCO-style instance** and **panoptic** annotations for your raw images using **CutLER (MaskCut)** and **U2Seg**.

---

## 📁 Project Structure

~~~text
Silkworm_Feeding/
├── data/
│   └── images/                          # raw .jpg images
│       ├── IMG_0001.jpg
│       ├── IMG_0002.jpg
│       └── …
├── CutLER/                              # MaskCut repository (git clone)
│   ├── maskcut.py
│   ├── merge_jsons.py
│   ├── requirements.txt
│   └── third_party/TokenCut/
└── U2Seg/                               # U2Seg repository (git clone)
    └── datasets/
        ├── coco/
        │   └── train2017/
        │       └── images/              # symlink or copy of data/images
        ├── panoptic_anns/
        │   └── panoptic_train2017.json  # ← to be generated
        └── prepare_ours/
            └── u2seg_annotations/
                ├── ins_annotations/      # MaskCut + merge_jsons output
                ├── semantic_annotations/ # (if available)
                └── panoptic_annotations/ # generate_pseudo_panoptic output
~~~

---

## 1. Environment Setup

~~~bash
# 1.1 create & activate Python 3.10 env
conda create -n cutler_env python=3.10 -y
conda activate cutler_env

# 1.2. install CutLER dependencies
cd ~/Desktop/Silkworm_Feeding/CutLER
git submodule update --init --recursive
pip install -r requirements.txt
pip install pydensecrf
pip install torch torchvision --extra-index-url https://download.pytorch.org/whl/cu121

# 1.3. clone U2Seg (if not yet)
cd ~/Desktop/Silkworm_Feeding
git submodule init
git submodule update

# 1.4. link or copy images into COCO train2017
mkdir -p U2Seg/datasets/coco/train2017/images
ln -s ../../data/images/*.jpg U2Seg/datasets/coco/train2017/images/
~~~

---

## 2. Generate Instance Masks with MaskCut

~~~bash
cd ~/Desktop/Silkworm_Feeding/CutLER/maskcut
export PYTHONPATH="$(pwd)/..:$PYTHONPATH"

python maskcut.py \
  --dataset-path /home/leo/Desktop/Silkworm_Feeding/data \
  --out-dir      /home/leo/Desktop/Silkworm_Feeding/U2Seg/datasets/prepare_ours/u2seg_annotations/ins_annotations \
  --vit-arch     base \
  --patch-size   8 \
  --tau          0.15 \
  --fixed_size   480 \
  --N            3 \
  --num-folder-per-job 1 \
  --job-index         0
~~~

* `--dataset-path` → **parent** of `images/` (`data/`)  
* `--out-dir`      → where per-folder JSONs are written

---

## 3. [Skip] Merge into a Single COCO Instances JSON

~~~bash
python merge_jsons.py \
  --base-dir       ../U2Seg/datasets/prepare_ours/u2seg_annotations/ins_annotations \
  --num-folder-per-job 1 \
  --fixed-size     480 \
  --tau            0.15 \
  --N              3 \
  --save-path      ../U2Seg/datasets/prepare_ours/u2seg_annotations/ins_annotations/instances_train2017.json
~~~

Resulting file:

- U2Seg/datasets/prepare_ours/u2seg_annotations/ins_annotations/instances_train2017.json


---

## 4. Generate Pseudo-Panoptic Annotations

~~~bash
mkdir -p datasets/prepare_ours/u2seg_annotations/semantic_annotations

ls datasets/datasets/coco/train2017/images/*.jpg | xargs -n 1 basename > \
datasets/prepare_ours/u2seg_annotations/semantic_annotations/coco_train_img_file_names.txt
~~~

~~~bash
cd ~/Desktop/Silkworm_Feeding/U2Seg

python datasets/prepare_ours/generate_pseudo_panoptic.py \
  --class_num 800 --split train

mv datasets/prepare_ours/u2seg_annotations/panoptic_annotations/cocotrain_800_ins_panoptic.json \
   datasets/datasets/panoptic_anns/panoptic_train2017.json
~~~

Final file created:

- U2Seg/datasets/panoptic_anns/panoptic_train2017.json

---

## Outputs Ready for Training

* `instances_train2017.json` → `U2Seg/datasets/prepare_ours/u2seg_annotations/ins_annotations/`
* `panoptic_train2017.json`  → `U2Seg/datasets/panoptic_anns/`
