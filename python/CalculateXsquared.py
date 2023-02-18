import numpy as np
import sys
import matplotlib.pyplot as plt

sys.path.append(".")
import Random as rng

if __name__ == "__main__":

	#set default number of samples
	Nsample = 1000

	# read the user-provided seed from the command line (if there)
	if '-Nsample' in sys.argv: #How many random numbers you want to sample
		p = sys.argv.index('-Nsample')
		Nsample = int(sys.argv[p+1])
	if '-h' in sys.argv or '--help' in sys.argv:
		print ("Usage: %s -Nsample [number]" % sys.argv[0])
		print
		sys.exit(1) 

	nAccept = 0
	nTotal = 0
	
	# accepted values
	Xaccept = []
	Yaccept = []

	# reject values
	Xreject = []
	Yreject = []

	# sample number
	isample = []
	# calculated values of Pi (per sample)
	calcArea = []

	random = rng.Random()

	idraw = max(1,int(Nsample)/100000)
	for i in range(0,Nsample):
		X = random.rand()
		Y = random.rand()

		nTotal += 1
		if(Y - X*X <= 0): #accept if under the curve y = x^2
			nAccept += 1
			if(i % idraw == 0):
				Xaccept.append(X)
				Yaccept.append(Y)
				
		else: # reject if above curve
			if(i % idraw == 0):
				Xreject.append(X)
				Yreject.append(Y)
				
		if(i % idraw == 0):
			isample.append(nTotal)
			calcArea.append(nAccept/nTotal) #nAccept/nTotal = area under the curve 

	#plot calculated area vs sample number
	fig1 = plt.figure()
	
	plt.plot(isample,calcArea)
	
	plt.ylabel(r'Approximate Integral')
	plt.xlabel("Sample number")
	plt.xlim(0,isample[len(isample)-1])
	
	ax = plt.gca()
	ax.axhline(y=1/3,color='green',label=r'true area') #line at true value of indefinite integral
	
	plt.title(r'Approximation of $\int_{0}^{\inf} x^2 dx$ as a function of number of samples')
	plt.legend()

	fig1.savefig("calculatedxsquared.pdf")


	#plot accept/reject points
	fig2 = plt.figure()
	
	plt.plot(Xaccept,Yaccept,marker='o',linestyle='',color='green',label='accept')
	plt.plot(Xreject,Yreject,marker='o',linestyle='',color='red',label='reject')
	
	plt.ylabel("Y")
	plt.xlabel("X")
	plt.legend()

	x_curve = np.arange(min(min(Xaccept),min(Xreject)),max(max(Xaccept),max(Xreject)),0.001)
	y_curve = [i*i for i in x_curve]
	
	plt.plot(x_curve,y_curve,color='blue',label=r'$y = x^2$')
	
	plt.legend()
	plt.title('Sampled points')
	fig2.savefig("xsquaredPy.pdf")
