import os
from setuptools import setup, find_packages

from torch.utils.cpp_extension import BuildExtension, CUDAExtension

with open('README.md') as f:
    long_description = f.read()

base_dir = os.path.dirname(os.path.abspath(__file__))
sources = [
        os.path.join(base_dir, path)
        for path in ['torch_efficient_distloss/cuda/segment_cumsum.cpp', 
                     'torch_efficient_distloss/cuda/segment_cumsum_kernel.cu']]

setup(
    name='torch_efficient_distloss',
    packages=find_packages(),
    package_data={'': ['torch_efficient_distloss/cuda/segment_cumsum.cpp', 'torch_efficient_distloss/cuda/segment_cumsum_kernel.cu']},
    include_package_data=True,
    version='0.1.3',
    license='MIT',
    description='Efficient distortion loss with O(n) realization.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Cheng Sun',
    author_email='chengsun@gapp.nthu.edu.tw',
    url='https://github.com/sunset1995',
    ext_modules=[ CUDAExtension('segment_cumsum_cuda', sources) ],
    cmdclass={"build_ext": BuildExtension}
)

