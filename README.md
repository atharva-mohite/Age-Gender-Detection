# Bosch's Age And Gender Detection Submission - Team 17

<!-- TABLE OF CONTENTS -->
## Table of Contents
  <ol>
    <li>
      <a>Project overview and Introduction</a>
    </li>
    <li>
      <a>Models</a>
      <ul>
        <li><a>SRGAN</a></li>
        <li><a>Facial Age Gender Detection</a></li>
        <li><a>Best Approach: YOLO Age and Gender Detection</a></li>
      </ul>
    </li>
    <li>
      <a>Inference</a>
    </li>
    
  </ol>



<!-- ABOUT THE PROJECT -->
## Project Overview and Introduction


In the wake of recent advancements in the field of machine learning and artificial intelligence, there is a need for models to accurately classify, summarize, extract and analyze information from massive amounts of data. The problem statement’s task involves estimating age and gender of a person from surveillance footages. This task not only requires huge amount of data but also thorough investigation and analysis. Surveillance footages are usually of low resolution which poses a hurdle for models to learn and extract important features. Hence, to tackle this problem a mechanism to convert the low resolution videos into their corresponding high definition counterparts needs to be developed. Subsequently, a deep learning model capable of predicting the age and gender of multiple people in the said high definition video should be implemented to create a robust pipeline. 

Need and relevance of the project are as follows:
* Most existing digital video surveillance systems rely on human observers for detecting specific activities in a real-time video scene. However, there are limitations in the human capability to monitor simultaneous events in surveillance displays.
* Estimating age and gender from a footage can help companies and organisations in keeping a track of their clientele base. It can also serve as a backup information with demographic details of the customer in case of theft or robbery. 
* Surveillance footages are usually of low resolution which poses a hurdle for models to learn and extract important features. 

How to tackle this problem Statement?
* A mechanism to convert the low resolution videos into their corresponsing high definition counterparts needs to be developed. 
* Subsequently, a deep learning model capable of predicting the age and gender of multiple people in the said high definition video should be implemented to create a robust pipeline. 






## Proposed models
### Super Resolution:
#### What is Super Resolution?

A super-resolution algorithm is trained to generate a Super-Resolution (SR) image for a corresponding Low Resolution (LR) image obtained by adding noise and downsampling a High Resolution (HR) ground truth image. 
The drawback of most of the super resolution techniques is low perceptual quality of the output image. To overcome this, we have employed SRGAN based algorithms.
### SRGAN
SRGAN based algorithms can upsample an image with an upsampling factor of x4. SRGAN is trained to minimize a unique perceptual loss function - a combination of the content loss and an adversarial loss.We have fine tuned the SRGAN pretrained model according to our use case. 

#### Please refer the SRGAN folder for detailed instructions of fine tuning and inference 
Run the FineTune.ipynb notebook in the SRGAN folder for running the finetuning algorithm
For inference of our trained model, run the inference.ipynb file in the SRGAN folder

### FAST-SRGAN
This approach follows the existing SRGAN architecture but replaces the residual blocks with inverted residual blocks for faster operation and higher efficiency.
We have used the official pretrained weights of FAST SRGAN for our use case.
#### Please refer the FAST SRGAN folder and run inference.ipynb notebook in this folder for getting the inference of FAST SRGAN on an input video. All the instructions are provided in the notebook itself.

### ESRGAN
We have used the official pretrained weights of FAST SRGAN for our use case. 
#### Please refer the ESRSRGAN folder and run inference.ipynb notebook in this folder for getting the inference of FAST SRGAN on an input video.All the instructions are provided in the notebook itself.

### Age and Gender Detection:

### Facial based CNN model
The benefit of using CNNs is their ability to develop an internal representation of a two-dimensional image . This allows the model to learn position and scale in variant structures in the data which is important when working with images.
We have used a deep convolutional neural network to train our model from scratch on the UTK Face dataset. Please refer to the technical report for the architecture and dataset information.
#### Please refer the Face Age gender folder for the training and inference notebook of the model. All instructions are provided in the said notebook.


## FINAL PROPOSED APPROACH : YOLOV4 with DARKNET BACKBONE 
You only look once (YOLO) is a state-of-the-art, real-time object detection system. 
YOLO was written in a custom framework called Darknet. Darknet is a very flexible research framework written in low level languages and has produced a series of the best realtime object detectors in computer vision: YOLO, YOLOv2, YOLOv3, and now, YOLOv4.
We have created a cutom dataset with corresponding annotations for training. 
Please refer the technical report for detailed architecture.

### YOLO AGE MODEL:
#### Please refer the YOLO age folder for complete instructions regarding the training notebook and dataset downloading procedure.

### YOLO GENDER MODEL:
#### Please refer the YOLO gender folder for complete instructions regarding the training notebook and dataset downloading procedure.


## Final Inference
#### Please follow the inference starter guide to perform complete end-to-end inference on an input video or image.
This end to end pipeline consists of the following steps:

**"yolov4_age" Age Model Folder link** - https://drive.google.com/drive/folders/1gPdRqUNFdJ6CstIByH_Dtcm-oAQGBP-4?usp=sharing

**"yolov4" Gender Model Folder link** - https://drive.google.com/drive/folders/1uVlIRWDI12TKFdsIjUaMoEJHRo-62Ege?usp=sharing

* Open these two links and then 'Add Shortcut to My Drive'. 
* Then open the "END_TO_END_inference_final_video.ipynb" in Google colab for video input and  "END_TO_END_inference_final_img.ipynb" for images inference
* Connect to Standard GPU.
* Rull all the cells one by one following the instructions given in each sections. 

FAST Srgan generates a high resolution video output of the input video. YOLO age and gender models then predict age and gender of multiple people in the high resolution video. If you wish to check a intermediate video, check the output directory mentioned after each model.

