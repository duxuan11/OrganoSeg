from models.sam_predict import SAM_ONNX, show_anns
from PIL import Image
import numpy as np
import threading
import argparse
from ultralytics import YOLO


def read_image(img_path: str):
    image = Image.open(img_path)
    image = image.convert("RGB")
    return image


def object_detection_inference(
    image_path,
    weight_path,
):

    # Load a model
    model = YOLO(weight_path)  # pretrained YOLO11n model

    # Run batched inference on a list of images
    results = model([image_path])  # return a list of Results objects

    # Process results list
    yolo_bboxes = []
    for result in results:
        boxes = result.boxes  # Boxes object for bounding box outputs
        yolo_bboxes.append(boxes)
        # save detection boxes and filter bubbles
    boxes = np.array(yolo_bboxes)

    return boxes


def sam_inference(image_path, boxes, sam):
    image = read_image(image_path)
    thread1 = threading.Thread(target=sam.set_image(image))
    thread1.start()
    mask_process = SAM_ONNX.predict_mask_from_bboxes(boxes)
    show_anns(
        mask_process.masks_list,
        mask_process.coord_list,
        mask_process.resized_width,
        mask_process.resized_height,
        image,
    )


def main():
    parser = argparse.ArgumentParser(description="test (and eval) a model")
    parser.add_argument(
        "--yolo_weight",
        default=None,
        type=str,
        required=True,
        help="test config file path.",
    )
    parser.add_argument(
        "--seg_encoder_weight",
        default=None,
        type=str,
        required=True,
        help="checkpoint file.",
    )
    parser.add_argument(
        "--seg_decoder_weight",
        default=None,
        type=str,
        required=True,
        help="checkpoint file.",
    )
    parser.add_argument("--img_path", help="The inference image path.")
    parser.add_argument(
        "--slice_height",
        default=1024,
        type=int,
        help="Height of the image slice for inference.",
    )
    parser.add_argument(
        "--slice_width",
        default=1224,
        type=int,
        help="Width of the image slice for inference.",
    )
    parser.add_argument(
        "--overlap_height_ratio",
        default=0.15,
        type=float,
        help="Overlap height ratio for image slicing.",
    )
    parser.add_argument(
        "--overlap_width_ratio",
        default=0.15,
        type=float,
        help="Overlap width ratio for image slicing.",
    )
    parser.add_argument(
        "--device",
        default="cuda:0",
        type=str,
        help="Device to run the inference on, e.g., 'cuda:0' or 'cpu'.",
    )
    args = parser.parse_args()
    image_path = args.img_path
    yolo_weight = args.yolo_weight
    seg_encoder_weight = args.seg_encoder_weight
    seg_decoder_weight = args.seg_decoder_weight
    device = args.device if args.device else "cuda:0"

    boxes = object_detection_inference(image_path, yolo_weight)
    sam_onnx = SAM_ONNX(
        encoder_path=seg_encoder_weight,
        decoder_path=seg_decoder_weight,
    )
    sam_inference(image_path, boxes, sam_onnx)


if __name__ == "__main__":
    # Parameter from command line
    main()
