---
title: Data storage for different AI dataset services
toc: true
tags:
  - dataset
date modified: Friday 27th September 2024, Fri
date created: Friday 27th September 2024, Fri
---

# Data Storage for Different AI Dataset Services
```toc
```
- [Analyze data sharing platforms](https://github.com/openml/meta/issues/13)
- HF : Folder of parquet files , with the occasional metadata csv
- Kaggle : Pretty much anything, but usually a folder with files and metadata
- NCBI (Bio tech info) : A tab delimited file : DataSet SOFT (but saved as a .gz archive)
- Fastai : tar.gz
- [COCO dataset](https://cocodataset.org/#overview) : good for checking image tasks - # [Detection](https://cocodataset.org/#detection-2020) | [DensePose](https://cocodataset.org/#densepose-2020) | [Keypoints](https://cocodataset.org/#keypoints-2020) | [Stuff](https://cocodataset.org/#stuff-2019) | [Panoptic](https://cocodataset.org/#panoptic-2020) | [Captions](https://cocodataset.org/#captions-2015)
	- folder with files and label splits
- [U.S. Department of Energy Office of Scientific and Technical Information](https://www.osti.gov/dataexplorer/)  (Physics): Images are in .zip, tabular in .csv and metadata as .xml