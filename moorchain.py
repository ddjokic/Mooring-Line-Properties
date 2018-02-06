#!/bin/env python
import math

#update 07-Feb-2017: added calc equiv. dia element (cylinder); removed inout reference

def get_integer(message, default):
#get integer number - error check included
	try:
		f=input (message)
		st=type(f)
		if f==0:
			f=default
			return int(f)
		elif f==" ":
			f=default
			return int(f)
		else:
			return int(f)
	except:
		print("Wrong Input! Try again")
		return(get_integer(message, default))
        
def get_float(message, default):
#get float number - error check included
	try:
		f=input (message)
		st=type(f)
		if f==0:
			f=default
			return float(f) ##dodo
		elif f==" ":
			f=default
			return float(f)  ##dodo
		else:
			return float(f)
	except:
		print("Wrong Input! Try again")
		return(get_float(message, default))

def write_file (file, description, var):
#write to file
	file.write ("\n")
	file.write (str(description))
	file.write ("\t")
	file.write (str(var))

def BL(c):
	BL=c*Dmm**2*(44-0.08*Dmm)
	return (BL)
def VL(a):
	VL=1.1346*10**(-5)*Dmm**2
	return VL

print("Calculating Properties of Mooring Chain")
print("Use results as preliminary data, only! Wherever possible use manufacturer's data instead.")
Dmm=get_float("Input Diameter of chain link in mm or '0' for default of 90mm: ", 90.0)
D=Dmm/1000
print("1 - Studless Chain")
print("2 - Studlink Chain")
choice1=get_integer("Choose option 1 or 2: ", 1)
if choice1==1:
	print ("Calculating properties of Studless Chain")
	#Outer Diameter
	ODmm=1.80*Dmm
	OD=ODmm/1000
	#Contact Diameter
	CDmm=3.35*Dmm
	#mass per length [te/m]
	ML=19.9*D**2  
	#Submerged weight of chain [te/m]:
	SW=0.87*ML
	#Axial Stiffness [kN]
	AS=0.854*10**8*D**2 
	#Bending Stiffness
	BS=0
	#Normal Drag Coef
	NDC=1
	#Normal Drag Diameter in mm
	NDD=2.1*Dmm
	#Axial Drag Coeficient
	ADC=0.4
	#Axial Drag Diameter in mm
	ADD=0.54*Dmm/math.pi
	#Normal Added mass Coeff
	NAMC=1.0
	#Axial added mass Coeff
	AADMC=0.08
	#Calculating Minimum Breaking Load (MBL) of the Chain in kN
	# BL for ORQ Chain BLORQ[kn]
	BLORQ=BL(0.0211)
	# BL for R3
	BLR3=BL(0.0223)
	#BL for R3s
	BLR3S=BL(0.0249)
	#BL for R4
	BLR4=BL(0.0274)
	#BL for R4S
	BLR4S=BL(0.0304)
	#BL for R5
	BLR5=BL(0.032)
	#Calculating Proof Load (PL)
	#PL for ORQ
	PLORQ=BL(0.014)
	#PL for R3
	PLR3=BL(0.0148)
	#PL for R3S
	PLR3S=BL(0.0174)
	#PL for R4
	PLR4=BL(0.0192)
	#PL for R4S
	PLR4S=BL(0.0213)
	#PL for R5
	PLR5=BL(0.0223)
	#Allowable twist of 90-foot (27.432m) length of chain
	twist=61875/Dmm
	twist360=twist/360
	#Effective Elastic Modulus (EEM) [kN/sqm]
	# R3 chain
	EEMR3=(5.40-0.0040*Dmm)*10**7
	# R4 chain
	EEMR4=(5.45-0.0025*Dmm)*10**7
	# R5 chain
	EEMR5=(6.0-0.0033*Dmm)*10**7
	# calculating equivalent element dia - cylinder of equal volume
	eDia = (4*ML/(math.pi*7.8*1))**0.5
	#locker volume in cum per m of chain
	locker=VL(Dmm)
	#writing results-studless chain
	fname="studless.txt"
	fn=open(fname, 'a')
	write_file(fn, "Link Diameter of Studless Chain [mm]: ", Dmm)
	write_file(fn, "Outer Diameter [mm]: ", ODmm)
	write_file(fn, "Contact Diameter [mm]: ", CDmm)
	write_file(fn, "Mass per unit length [t/m]: ", ML)
	write_file(fn, "Submerged weight of chain [t/m]: ", SW)
	write_file(fn, "Axial Stiffness [kN]: ", AS)
	write_file(fn, "Bending Stiffness [kN*sqm]: ", BS)
	write_file(fn, "Normal Drag Coefficient: ", NDC)
	write_file(fn, "Normal Drag Diameter [mm]: ", NDD)
	write_file(fn, "Axial Drag Coefficient: ",ADC)
	write_file(fn, "Axial Drag Diameter [mm]: ", ADD)
	write_file(fn, "Normal Added mass Coeff: ", NAMC)
	write_file(fn, "Axial Added mass Coeff: ", AADMC)
	fn.write("\n")
	write_file(fn, "Breaking Load - ORQ Chain [kN]: ", BLORQ)
	write_file(fn, "Breaking Load - R3 Chain [kN]: ", BLR3)
	write_file(fn, "Breaking Load - R3S Chain [kN]: ", BLR3S)
	write_file(fn, "Breaking Load - R4 Chain [kN]: ", BLR4)
	write_file(fn, "Breaking Load - R4S Chain [kN]: ", BLR4S)
	write_file(fn, "Breaking Load - R5 Chain [kN]: ", BLR5)
	fn.write("\n")
	write_file(fn, "Proof Load - ORQ Chain [kN]: ", PLORQ)
	write_file(fn, "Proof Load - R3 Chain [kN]: ", PLR3)
	write_file(fn, "Proof Load - R3S Chain [kN]: ", PLR3S)
	write_file(fn, "Proof Load - R4 Chain [kN]: ", PLR4)
	write_file(fn, "Proof Load - R4S Chain [kN]: ", PLR4S)
	write_file(fn, "Proof Load - R5 Chain [kN]: ", PLR5)
	fn.write("\n")
	write_file(fn, "Effective Elastic Modulus - R3 Chain [kN/sqm]: ", EEMR3)
	write_file(fn, "Effective Elastic Modulus - R4 Chain [kN/sqm]: ", EEMR4)
	write_file(fn, "Effective Elastic Modulus - R5 Chain [kN/sqm]: ", EEMR5)
	fn.write("\n")
	write_file(fn, "Allowable maximum twist of 90-foot (27.432m) length of chain [deg]: ", twist)
	write_file(fn, "Allowable maximum twist of 90-foot (27.432m) length of chain in 360deg turns: ", twist360)
	fn.write("\n")
	write_file(fn, "Equivalent element Dia [m]", eDia)
	fn.write("\n")
	write_file(fn, "Chain locker volume for 1m of Chain [cum]: ", locker)
	fn.write("\n")
	fn.write("\n")
	fn.close()
	print("Results file 'studless.txt' had been written")

elif choice1==2:
	print ("Calculating properties of Studlink Chain")
	#Outer Diameter
	ODmm=1.89*Dmm
	OD=ODmm/1000
	#Contact Diameter
	CDmm=3.6*Dmm
	#mass per length [te/m]
	ML=21.9*D**2  
	#Submerged weight of chain [te/m]:
	SW=0.87*ML
	#Axial Stiffness [kN]
	AS=1.01*10**8*D**2 
	#Bending Stiffness
	BS=0
	#Normal Drag Coef
	NDC=1
	#Normal Drag Diameter in mm
	NDD=2.26*Dmm
	#Axial Drag Coeficient
	ADC=0.4
	#Axial Drag Diameter in mm
	ADD=0.60*Dmm/math.pi
	#Normal Added mass Coeff
	NAMC=1.0
	#Axial added mass Coeff
	AADMC=0.07
	#Calculating Minimum Breaking Load (MBL) of the Chain in kN
	BLORQ=BL(0.0211)
	# BL for R3
	BLR3=BL(0.0223)
	#BL for R3s
	BLR3S=BL(0.0249)
	#BL for R4
	BLR4=BL(0.0274)
	#BL for R4S
	BLR4S=BL(0.0304)
	#BL for R5
	BLR5=BL(0.032)
	#Calculating Proof Load (PL)
	PLORQ=BL(0.014)
	#PL for R3
	PLR3=BL(0.0148)
	#PL for R3S
	PLR3S=BL(0.018)
	#PL for R4
	PLR4=BL(0.0216)
	#PL for R4S
	PLR4S=BL(0.024)
	#PL for R5
	PLR5=BL(0.0251)
	#Allowable twist of 90-foot (27.432m) length of chain
	twist=61875/Dmm
	twist360=twist/360
	##Effective Elastic Modulus [kn/sqm]
	EEM=5.6*10**7
	#locker volume in cum per m of chain
	locker=VL(Dmm)
	# calculating equivalent element dia - cylinder of equal volume
	eDia = (4*ML/(math.pi*7.8*1))**0.5
	#writing results- stud chain
	fname="studlink.txt"
	fn=open(fname, 'a')
	write_file(fn, "Link Diameter of Studlink Chain [mm]: ", Dmm)
	write_file(fn, "Outer Diameter [mm]: ", ODmm)
	write_file(fn, "Contact Diameter [mm]: ", CDmm)
	write_file(fn, "Mass per unit length [t/m]: ", ML)
	write_file(fn, "Submerged weight of chain [t/m]: ", SW)
	write_file(fn, "Axial Stiffness [kN]: ", AS)
	write_file(fn, "Bending Stiffness [kN*sqm]: ", BS)
	write_file(fn, "Normal Drag Coefficient: ", NDC)
	write_file(fn, "Normal Drag Diameter [mm]: ", NDD)
	write_file(fn, "Axial Drag Coefficient: ",ADC)
	write_file(fn, "Axial Drag Diameter [mm]: ", ADD)
	write_file(fn, "Normal Added mass Coeff: ", NAMC)
	write_file(fn, "Axial Added mass Coeff: ", AADMC)
	fn.write("\n")
	write_file(fn, "Breaking Load - ORQ Chain [kN]: ", BLORQ)
	write_file(fn, "Breaking Load - R3 Chain [kN]: ", BLR3)
	write_file(fn, "Breaking Load - R3S Chain [kN]: ", BLR3S)
	write_file(fn, "Breaking Load - R4 Chain [kN]: ", BLR4)
	write_file(fn, "Breaking Load - R4S Chain [kN]: ", BLR4S)
	write_file(fn, "Breaking Load - R5 Chain [kN]: ", BLR5)
	fn.write("\n")
	write_file(fn, "Proof Load - ORQ Chain [kN]: ", PLORQ)
	write_file(fn, "Proof Load - R3 Chain [kN]: ", PLR3)
	write_file(fn, "Proof Load - R3S Chain [kN]: ", PLR3S)
	write_file(fn, "Proof Load - R4 Chain [kN]: ", PLR4)
	write_file(fn, "Proof Load - R4S Chain [kN]: ", PLR4S)
	write_file(fn, "Proof Load - R5 Chain [kN]: ", PLR5)
	fn.write("\n")
	write_file(fn, "Effective Elastic Modulus - all grades of studlink chain [kn/sqm]: ", EEM)
	fn.write("\n")
	write_file(fn, "Allowable maximum twist of 90-foot (27.432m) length of chain [deg]: ", twist)
	write_file(fn, "Allowable maximum twist of 90-foot (27.432m) length of chain in 360deg turns: ", twist360)
	fn.write("\n")
	write_file(fn, "Equivalent element Dia [m]", eDia)
	fn.write("\n")
	write_file(fn, "Chain locker volume for 1m of Chain [cum]: ", locker)
	fn.write("\n")
	fn.write("\n")
	fn.close()
	print("Results file 'studlink.txt' had been written")
	
else:
	print ("Invalid input - try again")