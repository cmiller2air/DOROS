# DOROS: Dataset of Road Object States

## Overview

DOROS (Dataset of Road Object States) is a novel vision dataset designed for advanced scene understanding in urban environments. It features **multi-level annotations** across three primary categories:

- **Agent**: Key traffic entities such as pedestrians, cars, buses, and traffic lights.
- **Location**: Logical spatial contexts like lanes, crosswalks, intersections, and parking lots.
- **Action**: Dynamic behaviors such as braking, signaling, and stopping, allowing multiple simultaneous actions through multi-hot encoding.

The dataset addresses gaps in existing resources by providing:
- Comprehensive multi-level annotations.
- Diverse environmental conditions (e.g., rain, snow, fog, nighttime).
- High-quality, assisted-manual annotations using **Segment Anything** and **Grounding-DINO**.

The dataset is particularly suitable for training and evaluating models capable of understanding complex urban traffic scenarios.

## Key Features

- **Dataset Size**: 49,296 high-resolution images (480×1280 RGB), sampled from over 1,000,000 raw frames.
- **Geographical Diversity**: Data collected from multiple South Korean cities including Seoul, Daejeon, Hwaseong, Sejong, and Ulsan.
- **Multi-Level Annotations**: Each object has exactly one ‘Agent’ and ‘Location’ label, with optional ‘Action’ labels.
- **Class Distribution**: Balanced class representation across training and validation splits, as shown in Figure 1 of the paper.
- **Assisted Annotation**: Initial annotations generated using **Segment Anything** and **Grounding-DINO**, refined by human annotators.

## Applications

DOROS is ideal for:
- Object detection and segmentation.
- Action recognition in traffic scenarios.
- Context-aware autonomous driving models.

## Download

The dataset is available for download:

[Download DOROS Dataset](https://nanum.etri.re.kr/share/kimjy/ObjectStateDetection2025)

## Training Code

The training code leverages the **Ultralytics YOLOv8** framework in segmentation mode. You can find detailed instructions and examples in the repository.


## Experimental Results
### Baseline Training Results

| Model Size | Params | Configuration          | mAP-comb(mask) (50 / 50:95) |
|------------|--------|------------------------|-----------------------------|
| n          | 3.27M  | Baseline               | 6.09 / 10.44               |
|            |        | + no flip aug          | 7.05 / 12.15               |
|            |        | + large img            | 7.29 / 12.35               |
| s          | 11.80M | Baseline               | 9.63 / 17.02               |
|            |        | + no flip aug          | 9.89 / 17.61               |
|            |        | + large img            | 10.66 / 18.76              |
| m          | 27.26M | Baseline               | 11.07 / 19.74              |
|            |        | + no flip aug          | 10.67 / 19.93              |
|            |        | + large img            | 12.22 / 21.81              |
| l          | 45.96M | Baseline               | 12.24 / 22.11              |
|            |        | + no flip aug          | 13.09 / 23.76              |
|            |        | + large img            | 13.95 / 24.44              |
| x          | 71.78M | Baseline               | 12.87 / 23.15              |
|            |        | + no flip aug          | 13.90 / 25.32              |
|            |        | + large img            | 14.54 / 25.55              |

### Experimental Setup
- **Hardware**: NVIDIA GeForce RTX 4090 GPU, AMD EPYC 9124 16-core CPU.
- **Framework**: Ultralytics YOLOv8.
- **Augmentations**: Mosaic and random HSV.
- **Optimizer**: Stochastic Gradient Descent (SGD).

### Key Findings
- **Baseline Configurations**: 
  - Standard training with default augmentations.
  - Training without flip augmentations showed a slight accuracy reduction.
  - Large image sizes improved performance by capturing finer spatial details.
- **Evaluation Metrics**: Combined mAP(mask), which evaluates predictions across multi-level annotations.

For detailed ablation studies, refer to the [full paper](#).

## Acknowledgments

This work builds on tools and resources from the computer vision community, including:
- **Ultralytics YOLOv8** for training code.
- **Segment Anything** and **Grounding-DINO** for assisted annotations.

We thank all contributors and collaborators for their support.
