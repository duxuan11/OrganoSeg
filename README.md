## Documentation 📑
> This is about the organoid/organ-on-a-chip intelligent segmentation algorithm.

## Usage
#### Environment Setup
**1. Create a Conda environment:**
```shell
conda create -n organoseg python==3.10.0
pip install -r requirements.txt
```
**2. Clone and Install this repository:**
```bash
git clone https://github.com/duxuan11/Precision-Organoid-Segmentation-Technique-POST.git
cd Precision-Organoid-Segmentation-Technique-POST
```
### Prediction

```shell
python predict.py --yolo_weight weights/yolon.pt --seg_encoder_weight weights/sam_encoder.onnx --seg_decoder_weight weights/sam_decoder.onnx --img_path img/example1.tiff
```
### Training
You can refer to the training process of [yolov11](https://github.com/ultralytics/ultralytics). Then use these trained models in this code.

### Download
Trained models:[Google Drive](https://drive.google.com/drive/folders/1-Dd-zFxHM2GfprqbEv2Tv0_mLNu88SuW?usp=sharing)

## License
The code is released under the MIT License. It is a short, permissive software license. Basically, you can do whatever you want as long as you include the original copyright and license notice in any copy of the software/source.

## Acknowledgement
Our project is developed based on [yolov11](https://github.com/ultralytics/ultralytics),[SAM](https://github.com/facebookresearch/segment-anything.git).
