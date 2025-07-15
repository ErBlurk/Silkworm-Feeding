# Efficient Computer Vision Models for Silkworm Feeding Prediction and Habitat Analysis

## Abstract

Efficient silkworm rearing is essential for sustainable silk production, relying heavily on accurate monitoring of feeding conditions. Traditional methods of observation are labor-intensive and subject to human error, highlighting the need for automated solutions. Advances in computer vision, particularly lightweight convolutional neural networks, offer promising approaches for interpreting complex visual scenes such as silkworm rearing beds. Differentiating between silkworms, mulberry leaves, and background areas is a critical step in automating feeding management and optimizing farm operations. The increasing availability of visual data from rearing environments further supports the development of robust, efficient monitoring systems tailored to the needs of modern silk production.

## Dataset

Silkworm rearing data (provided)

## Task

The project focuses on two complementary objectives:

1. **Binary Classification**
   Implement lightweight neural network architectures to determine whether the silkworms need feeding.

2. **Unsupervised Segmentation**
   Use non-supervised methods to distinguish and separate the three key elements in each image—silkworms, mulberry leaves, and background—without requiring pixel-wise annotations.

Both tasks will be complemented by data augmentation strategies to improve generalization across different conditions and increase robustness to environmental variations.

## Main Objectives

* **Rearing Classification**
  Use lightweight architectures for binary classification (feeding vs. no feeding).
* **Unsupervised Segmentation of Rearing Beds**
  Implement unsupervised methods to segment silkworms, mulberry leaves, and background without ground truth.
* **Performance Evaluation**
  Assess classification models and segmentation outputs using quantitative metrics and qualitative analysis to determine their effectiveness in real-world conditions.

## References

1. Zhao, M., Luo, Y., & Ouyang, Y. (2024). *RepNeXt: A Fast Multi-Scale CNN using Structural Reparameterization*. arXiv.
2. Tan, M., & Le, Q. V. (2021). *EfficientNetV2: Smaller Models and Faster Training*. arXiv.
3. Mehta, S., & Rastegari, M. (2022). *MobileViT: Light-weight, General-purpose, and Mobile-friendly Vision Transformer*. arXiv.
4. Rossetti, S., Samà, N., & Pirri, F. (2023). *Removing supervision in semantic segmentation with local-global matching and area balancing*. arXiv.
5. Niu, D., Wang, X., Han, X., Lian, L., Herzig, R., & Darrell, T. (2023). *Unsupervised Universal Image Segmentation*. arXiv.
