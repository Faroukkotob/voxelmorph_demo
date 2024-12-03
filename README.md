I have a venv setup on my machine with all the requiremtns install
- running on python 3.8 and tensorflow 2.10.1

What i did first is to install neurite and voxelmorph through these commands:
- pip install https://github.com/adalca/neurite/archive/refs/heads/dev.zip
- pip install https://github.com/voxelmorph/voxelmorph/archive/refs/heads/dev.zip

And that images have to be normalized between 0 and 1

Using this the register.py script from here: 
- https://github.com/voxelmorph/voxelmorph/blob/dev/scripts/tf/register.py
  
and the weights from here:
- https://github.com/voxelmorph/voxelmorph/blob/dev/data/readme.md#models

I'm running it with this command with my data (in the images folder .nii) :

python register.py     --moving normalized_moving.nii.gz --fixed normalized_fixed.nii.gz --moved warped.nii.gz --model models/pvxm_dense_brain_T1_3D_mse.h5 --gpu 0

But im getting errors, im not sure if this is the correct way to do or if i'm missing some steps. If you could please help me to try to register on my images, like what commands,steps etc to do.
