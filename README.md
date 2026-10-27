
Computer Components Real-Time Recognition

Real-time PC hardware classification using OpenCV and a pre-trained machine learning model. This repository contains a production-ready Python script that captures a live webcam feed, processes frames on the fly, and displays real-time predictions of 14 distinct computer components with their confidence scores.

🚀 Features

• Live Webcam Inference: Process continuous frames seamlessly from your default camera.
• 14 Hardware Classes: Pre-configured to recognize essential computer parts.
• Visual Overlay: Renders dynamic, real-time text indicators directly on the video window.
• Safe Resource Handling: Automatically releases hardware and window contexts on exit.

📊 Supported Classes

The underlying model is trained to classify the following computer components:

Component Category	Included Items
Peripherals	Headset, Microphone, Speakers, Mouse, Keyboard, Webcam
Core Hardware	CPU, GPU, Motherboard, RAM
Storage & Structure	HDD, Case
Infrastructure	Monitors, Cables


🛠️ Prerequisites & Installation


1. Clone the Repository

bash
git clone https://github.com
cd pc-parts-recognition
Используйте код с осторожностью.

2. Install Dependencies

Install the required base libraries using pip:
bash
pip install opencv-python numpy
Используйте код с осторожностью.
⚠️ Important Framework Note: Because the script uses pickle to load model.pkl, you must install the specific deep learning framework used to train your model (such as tensorflow, keras, or scikit-learn) in your environment so the architecture unpacks successfully.

3. Add Your Model

Ensure your trained model file is named model.pkl and placed directly in the root directory of this project.

💻 Usage

To launch the real-time recognition system, run:
bash
python main.py
Используйте код с осторожностью.
• How to Exit: Press the Q key on your keyboard while focusing on the video feed window to stop recording and close the application safely.

🔄 Pipeline Workflow

[Webcam Feed] ➔ [Convert BGR to RGB] ➔ [Resize to 128x128] ➔ [Normalize (0-1)] ➔ [Model Prediction] ➔ [UI Overlay]
If you want to make this repository stand out to recruiters or contributors, let me know:
• What deep learning library (TensorFlow, Keras, etc.) should be added to the installation steps?
• Would you like an added section explaining how to collect data and retrain the model?
• Do you want to include a License section (e.g., MIT, Apache)?
