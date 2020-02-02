https://www.anaconda.com/distribution/#download-section

conda create -n tensorflow_env tensorflow python=3.6
conda activate tensorflow_env

python -m pip install --user cozmo[camera]
python -m pip install --user --upgrade cozmo
python -m pip install tensorflow
python -m pip install Pillow
pip install -U tensorflow
pip install -U keras
