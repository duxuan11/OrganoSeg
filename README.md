## Documentation 📑
> This is about the organoid/organ-on-a-chip intelligent segmentation algorithm.

## Usage
#### Environment Setup
```shell
conda create -n POST python==3.10.0
pip install -r requirements.txt
```
### Prediction

```shell
python inference.py
```
### Training
You can refer to the training process of [yolov8](https://github.com/ultralytics/ultralytics) and [yolov9](https://github.com/WongKinYiu/yolov9).Then use these trained models in this code.

### Download
Post models:[Google Drive](https://drive.google.com/drive/folders/1-Dd-zFxHM2GfprqbEv2Tv0_mLNu88SuW?usp=sharing)

## License
The code is released under the MIT License. It is a short, permissive software license. Basically, you can do whatever you want as long as you include the original copyright and license notice in any copy of the software/source.

## Acknowledgement
Our project is developed based on [yolov8](https://github.com/ultralytics/ultralytics),[yolov9](https://github.com/WongKinYiu/yolov9), and [TinySAM](https://github.com/xinghaochen/TinySAM).
