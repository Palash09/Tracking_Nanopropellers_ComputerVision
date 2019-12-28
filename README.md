# Tracking_Nanopropellers_ComputerVision
In this repository, I have included the code for tracking magnetic nanopropellers which was implemented through computer vision.

The tracking of magnetic nanopropellers was a research project during my internship @ Indian Institute of Science in the 
Nanoscience Department.

There is a ongoing research in the Nanoscience field on magnetic nano propellers. They are expected to be used in healthcare 
sector with specific tasks like drug delivery, blockage removal and for determing the viscosity of fluids.

The process for this project involved an apparatus which was known as microfludic chamber. This apparatus was used to carry
the fluid consisting of nanopropellers over a very short distance and the movement was tracked by a powerful thorlabs camera.

The computer vision technique which was used for this was background subtraction algorithm, this helped in removing the static
objects from the captured part, thus enabling the algorithm to focus on the motile nano propellers itself. The movement was detected with the help of a box which was built around any kind of mobile objects.

It had the flexibility of using either live stream videos or pre-recorded videos as input to the algorithm for prediction. 

![Fig-1](https://github.com/Palash09/Tracking_Nanopropellers_ComputerVision/blob/master/Tracking_1.png)

Output generated from a live-stream video. As we can see, there is regtangular box around the moving magnetic nanopropellers.

<p align="center">
  <img width="460" height="300" src="https://github.com/Palash09/Tracking_Nanopropellers_ComputerVision/blob/master/Tracking_3.png">
</p>

The above output is of pre-recorded video of the experiment.

The algorithm performed satisfactorily good, with an accuracy of around 70%. 



