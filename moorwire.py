#!/usr/bin/env 
import inout

print("Calculating Mooring Rope/Wire Charachteristics")
print("Use results as preliminary, only. Wherever possible, use maker's data!")
Dmm = inout.get_float("Input Rope/Wire Nominal Diameter [mm] or '0' for 90mm: ", 90)
D = Dmm/1000
# Weight in Air per meter of length[kN/m] and weight in water
#Nylon Rope - WLN 
WLN = 0.676*D**2*9.81
WLNw=WLN*(1.14-1.025)/1.14
#Polyester rope - WLP
WLP = 0.7978*D**2*9.81
WLPw=WLP*(1.38-1.025)/1.38
#Polypropylene -WLPp
WLPp = 0.4526*D**2*9.81
WLPpw=WLPp*(0.91-1.025)/0.91
#Wire rope with fibre core - WLWf
WLWf = 3.6109*D**2*9.81
WLWfw=WLWf*(6.81-1.025)/6.81
#Wire rope with wire core - WLWw
WLWw = 3.9897*D**2*9.81
WLWww=WLWw*(7.85-1.025)/7.85
#Nylon Rope - WLN
#Outer Diameter [mm]
#Nylon rope - ODN
ODN = 0.85*Dmm
#Polyester rope - ODP
ODP = 0.86*Dmm
#Polypropylene rope - ODPp
ODPp = 0.8*Dmm
#Wire rope with fibre core - ODWf
ODWf = 0.82*Dmm
#Wire rope with wire core - ODWw
ODWw = 0.8*Dmm
#Axial stiffness [kN]
#Nylon Ropes - ASN
ASN = D**2*1.18*10**5
#Polyester Ropes - ASP
ASP = D**2*1.09*10**6
#Polypropylene rope - ASPp
ASPp = D**2*1.06*10**6
#Wire rope with fibre core - ASWf
ASWf = D**2*3.67*10**7
#Wire rope with wire core - ASWw
ASWw = D**2*4.04*10**7
#Breaking Load [kN] - MBL
#Nylon Ropes dry - MBLNd
MBLNd = 163950*D**2
#Nylon rope wet - MBLNw
MBLNw = 139357*D**2
#Polyester ropes - MBLP
MBLP = 170466*D**2
#Polypropylene rope - MBLPp
MBLPp = 105990*D**2
#Wire ropes with fibre core - MBLWf
MBLWf = 584175*D**2
MBLWw = 633358*D**2
#writing results
fname = "ropes.txt"
fn = open(fname, 'a')
inout.write_file(fn, "Diameter of rope [mm]: ", Dmm)
fn.write("\nNylon Rope Data")
inout.write_file(fn, "Outer Diameter [mm]: ", ODN)
inout.write_file(fn, "Rope weight in Air [kN/m]: ", WLN)
inout.write_file(fn, "Rope weight in Water [kN/m]: ", WLNw)
inout.write_file(fn, "Axial stiffness [kN]: ", ASN)
inout.write_file(fn, "Minimum Breaking Load of Dry Nylon Rope [kN]: ", MBLNd)
inout.write_file(fn, "Minimum Breaking Load of Wet Nylon Rope [kN]: ", MBLNw)
fn.write("\n")
fn.write("\nPolyester rope Data")
inout.write_file(fn, "Outer Diameter [mm]: ", ODP)
inout.write_file(fn, "Rope weight in Air [kN/m]: ", WLP)
inout.write_file(fn, "Rope weight in Water [kN/m]: ", WLPw)
inout.write_file(fn, "Axial stiffness [kN]: ", ASP)
inout.write_file(fn, "Minimum Breaking Load of Polyester Rope [kN]: ", MBLP)
fn.write("\n")
fn.write("\nPolypropylene rope Data")
inout.write_file(fn, "Outer Diameter [mm]: ", ODPp)
inout.write_file(fn, "Rope weight in Air [kN/m]: ", WLPp)
inout.write_file(fn, "Rope weight in Water [kN/m]: ", WLPpw)
inout.write_file(fn, "Axial stiffness [kN]: ", ASPp)
inout.write_file(fn, "Minimum Breaking Load of Polypropylene Rope [kN]: ", MBLPp)
fn.write("\n")
fn.write("\nWire rope with fibre core Data")
inout.write_file(fn, "Outer Diameter [mm]: ", ODWf)
inout.write_file(fn, "Rope weight in Air [kN/m]: ", WLWf)
inout.write_file(fn, "Rope weight in Water [kN/m]: ", WLWf)
inout.write_file(fn, "Axial stiffness [kN]: ", ASWf)
inout.write_file(fn, "Minimum Breaking Load of Wire Rope with fibre core [kN]: ", MBLWf)
fn.write("\n")
fn.write("\nWire rope with wire core Data")
inout.write_file(fn, "Outer Diameter [mm]: ", ODWw)
inout.write_file(fn, "Rope weight in Air [kN/m]: ", WLWfw)
inout.write_file(fn, "Rope weight in Water [kN/m]: ", WLWw)
inout.write_file(fn, "Axial stiffness [kN]: ", ASWw)
inout.write_file(fn, "Minimum Breaking Load of Wire Rope with wire core [kN]: ", MBLWw)
fn.close()
print("Calculation results had been written.")