# [CS231n: Convolutional Neural Networks for Visual Recognition](http://cs231n.stanford.edu)

[![Completion status](https://img.shields.io/badge/status-complete-brightgreen.svg)]()
[![Used TensorFlow](https://img.shields.io/badge/TensorFlow-yes-brightgreen.svg)]()
[![Used PyTorch](https://img.shields.io/badge/PyTorch-no-red.svg)]()
[![Did Extras](https://img.shields.io/badge/extras-no-red.svg)]()

My solutions to this computer vision course taught at Stanford University (spring 2017).
I am not a student of SU, I just do this out of curiosity and to help me in my current job.

The course is now complete.
As for now, exercises are done only in TensorFlow and it do not include any extra bonus tasks.

## Structure

* [**Assignment 1**](http://cs231n.github.io/assignments2017/assignment1)
    - Q1: k-Nearest Neighbor classifier ([solution](https://gitlab.com/me-learnz/CS231n/blob/master/assignment1/knn.ipynb))
    - Q2: Training a Support Vector Machine ([solution](https://gitlab.com/me-learnz/CS231n/blob/master/assignment1/svm.ipynb))
    - Q3: Implement a Softmax classifier ([solution](https://gitlab.com/me-learnz/CS231n/blob/master/assignment1/softmax.ipynb))
    - Q4: Two-Layer Neural Network ([solution](https://gitlab.com/me-learnz/CS231n/blob/master/assignment1/two_layer_net.ipynb))
    - Q5: Higher Level Representations: Image Features ([solution](https://gitlab.com/me-learnz/CS231n/blob/master/assignment1/features.ipynb))
    - Q6: Cool Bonus: Do something extra!
* [**Assignment 2**](http://cs231n.github.io/assignments2017/assignment2)
    - Q1: Fully-connected Neural Network ([solution](https://gitlab.com/me-learnz/CS231n/blob/master/assignment2/FullyConnectedNets.ipynb))
    - Q2: Batch Normalization ([solution](https://gitlab.com/me-learnz/CS231n/blob/master/assignment2/BatchNormalization.ipynb))
    - Q3: Dropout ([solution](https://gitlab.com/me-learnz/CS231n/blob/master/assignment2/Dropout.ipynb))
    - Q4: Convolutional Networks ([solution](https://gitlab.com/me-learnz/CS231n/blob/master/assignment2/ConvolutionalNetworks.ipynb))
    - Q5: PyTorch / TensorFlow on CIFAR-10 ([solution](https://gitlab.com/me-learnz/CS231n/blob/master/assignment2/TensorFlow.ipynb))
    - Q6: Do something extra!
* [**Assignment 3**](http://cs231n.github.io/assignments2017/assignment3)
    - Q1: Image Captioning with Vanilla RNNs ([solution](https://gitlab.com/me-learnz/CS231n/blob/master/assignment3/RNN_Captioning.ipynb))
    - Q2: Image Captioning with LSTMs ([solution](https://gitlab.com/me-learnz/CS231n/blob/master/assignment3/LSTM_Captioning.ipynb))
    - Q3: Network Visualization: Saliency maps, Class Visualization, and Fooling Images ([solution](https://gitlab.com/me-learnz/CS231n/blob/master/assignment3/NetworkVisualization-TensorFlow.ipynb))
    - Q4: Style Transfer ([solution](https://gitlab.com/me-learnz/CS231n/blob/master/assignment3/StyleTransfer-TensorFlow.ipynb))
    - Q5: Generative Adversarial Networks ([solution](https://gitlab.com/me-learnz/CS231n/blob/master/assignment3/GANs-TensorFlow.ipynb))
    
## Links

* Course homepage: http://cs231n.stanford.edu
* Course notes: http://cs231n.github.io
* GAN training tips: https://github.com/soumith/ganhacks

## Credits

* [CS231n staff](http://cs231n.stanford.edu) for creating this course, maintaining it and making it accessible to a public audience.
* [lightaime's solutions](https://github.com/lightaime/cs231n): I used these to verify my solutions and pull me out when stuck.
* [cthoreys's solutions](https://github.com/cthorey/CS231): dtto; Also, I directly copy-pasted some [backpropagations](https://gitlab.com/me-learnz/CS231n/blob/master/assignment2/cs231n/layers.py#L288) from it since I am not perfectly fluent with derivations and currently don't have enough time to do it myself.
* [madalinabuzau's solutions](https://github.com/madalinabuzau/CS231n-Convolutional-Neural-Networks-for-Visual-Recognition): Helped later in Assignment 3.

## Notes

* I used [Anaconda](https://www.anaconda.com/distribution/) Python distribution (3.6) on Windows.
* To run the assignments notebooks I used `jupyter notebook`.
* I manually resolved errors (xrange -> range, ...) and installed missing packages by `conda install ...`
* I didn't mess with virtualenvs and requitements.txt since I didn't manage to get it working.