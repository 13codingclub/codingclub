

Students initially take photos using take_pictures.py

They will then use the photos to train a tensorflow model using Teachable machine: https://teachablemachine.withgoogle.com/train 

Once the trained model is downloaded, they can import it into cozmo_ai.py to control Cozmo's actions.

Python setup:

https://www.anaconda.com/distribution/#download-section
conda create -n tensorflow_env tensorflow python=3.6
conda activate tensorflow_env
python -m pip install --user cozmo[camera]
python -m pip install --user --upgrade cozmo
python -m pip install tensorflow
python -m pip install Pillow
pip install -U tensorflow
pip install -U keras

Setup of Cozmo:

https://developer.anki.com/blog/learn/tutorial/getting-started-with-the-cozmo-sdk/index.html

Cozmo API:

http://cozmosdk.anki.com/docs/api.html

