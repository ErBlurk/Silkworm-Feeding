# Efficient Computer Vision Models for Silkworm Feeding Prediction and Habitat Analysis

# !!! TODO: Improve README !!!

### Quick project informations

#### People:
> 1986191: Leonardo Mariut \
> 2190452: Mohamed Zakaria Benjelloun Tuimy

#### Tested segmentation models:
> DINO \
> STEGO \
> U2Seg \
> SegFormer

#### Tested classification models:
> EfficientNetV2 \
> RepNeXt \
> MobileViT \
> Linear regressor 

#### Link to dataset:
> https://drive.google.com/file/d/1FM-CnQ1NrRSv-CD7C0-gnsR63hlRXsUp/view?ts=68419e2bV

---

### Approach

Following the proposed literature, we've started with CutLER and STEGO to later test U2Seg, uninspired by the achieved results we've also tested DINO and developed our methods, like heavy image preprocesssing and color thresholding, linear regression on color ratios (binary classification) and SegFormer fine tuning (semantic segmentation)

---

### Results

Achieved good self-supervised semantic segmentation (heuristics used, but no manual labelling) both with color thresholding and SegFormer.

Achieved very good results on binary classification on raw images with all the tested models (feed / don't feed silkworms decision)

---


![Color_Threshold](examples/threshold_color.png)
*Heuristic self-supervised semantic segmentation example*

---
![SegFormer_Mask](examples/SegFormer.png)
*SegFormer generated semantic mask example*