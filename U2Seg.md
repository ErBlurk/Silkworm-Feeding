
### Ensure required packages are already installed
E.g. be sure to already have torch installed for conda environments

### Environment and prerequisites
> # CUDA 12.x system (or adapt the conda line)
> conda create -n u2seg python=3.11 -y
> conda activate u2seg
> 
> # PyTorch (latest stable; pick the right cudatoolkit)
> conda install -c pytorch -c nvidia pytorch torchvision torchaudio cudatoolkit=12.1 -y

### Install detectron2
> # Add u2seg as a submodule
> git submodule add -b main https://github.com/u2seg/U2Seg.git U2Seg
> git commit -m "Add U2Seg as a git submodule"
> 
> # or clone it
> git clone https://github.com/u2seg/U2Seg.git
>
> # builds Detectron2 that ships inside the repo
> cd U2Seg
> pip install -e .
>
> export PYTHONPATH=$(pwd)/../U2Seg:$PYTHONPATH

### Prepare the dataset

> # Generate pseudo panoptics annotations:
> python ../U2Seg/datasets/prepare_ours/generate_pseudo_panoptic.py \
>        -class_num 3 \          #  silkworm / leaf / background
>        -split train \
>        -data_root datasets/silkworm
> 
> # Create stuff-class mask
> python datasets/prepare_ours/prepare_stuff_panoptic_fpn.py --cluster_num 3
