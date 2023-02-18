# PHSX815 Spring 2023 Week 5

## Monte Carlo Integration.

Awwww yeahhh baby! Do you like spending a lot of time at smokey lounges and throwing darts? Are you also a sleep deprived mathematician who just can't figure out how to analytically integrate that crazy function? No need. Now we can solve both of your problems with one technique: Monte Carlo Integration. 

Let's head over to the 'Python' Folder and see what I'm talking about. 

**Calculating Pi**

First we take a look at some code that Professor Rogan supplied to see what the whole idea of Monte Carlo integration is. 

Let's run the **CalculatePi.py** file with the following line in the terminal.
>python3 CalculatePi.py -Nsample 100000

This produces two graphs which are **CalculatePipy.pdf** and **circleQuadPy.pdf**. The first shows the error between the Monte Carlo integration and the actual value of Pi as a function of how many sample points we take (darts we throw). More sample points leads to a more accurate answer! The second graph shows the whole idea of Monte Carlo integration: we only accept the dart throw if it falls within the region we are interested in calculating the area under a curve. In this case, within a quarter circle contained in the 1st quadrant. This means that each dart that we throw is either accepted or rejected in our calculation. And the area is given by Naccepted/Ntotal. 

![calculatedPiPy.pdf](https://github.com/DJDdawg/PHSX815_Week5/blob/master/python/calculatedPiPy.pdf)

![circleQuadPy.pdf](https://github.com/DJDdawg/PHSX815_Week5/blob/master/python/circleQuadPy.pdf)


**Integrating Any Function**

Seeing the above idea, we can expand this simply be defining any function we like. I chose the simple case of y = x^2. 

You can see the code at **CalculateXsquared.py** and it can be run with:
>python3 CalculateXsquared.py -Nsample 100000

It also produces the exact same graphs **calculatedxsquared.pdf** and **xsquaredPy.pdf**, but now for our new area. 

![calculatedxsquared.pdf](https://github.com/DJDdawg/PHSX815_Week5/blob/master/python/xsquaredPy.pdf)

![xsquaredPy.pdf](https://github.com/DJDdawg/PHSX815_Week5/blob/master/python/xsquaredPy.pdf)
