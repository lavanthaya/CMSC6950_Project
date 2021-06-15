import math
import os.path
from os import path
import pandas as pd

#Coefficients
C00 = 1402.388    ; A02 = 7.166E-5
C01 = 5.03830     ; A03 = 2.008E-6
C02 =-5.81090E-2  ; A04 =-3.21E-8
C03 = 3.3432E-4   ; A10 = 9.4742E-5
C04 = -1.47797E-6 ; A11 =-1.2583E-5
C05 = 3.1419E-9   ; A12 =-6.4928E-8
C10 = 0.153563    ; A13 = 1.0515E-8
C11 = 6.8999E-4   ; A14 =-2.0142E-10
C12 =-8.1829E-6   ; A20 =-3.9064E-7
C13 = 1.3632E-7   ; A21 = 9.1061E-9
C14 =-6.1260E-10  ; A22 = -1.6009E-10
C20 = 3.1260E-5   ; A23 = 7.994E-12
C21 =-1.7111E-6   ; A30 = 1.100E-10
C22 = 2.5986E-8   ; A31 = 6.651E-12
C23 =-2.5353E-10  ; A32 =-3.391E-13
C24 = 1.0415E-12  ; B00 =-1.922E-2
C30 =-9.7729E-9   ; B01 =-4.42E-5
C31 = 3.8513E-10  ; B10 = 7.3637E-5
C32 =-2.3654E-12  ; B11 = 1.7950E-7
A00 = 1.389       ; D00 = 1.727E-3
A01 =-1.262E-2    ; D10 =-7.9836E-6
                                                          

DataFile = "argo_data.csv"
                                     
def SoundSpeed(S,T,P):
    '''
       Function that Calculates the sound speend under ocean
       T = temperature in degrees Celsius
       S = salinity in Practical Salinity Units (parts per thousand)
       P = pressure in bar
       Equation adopted from: http://resource.npl.co.uk/acoustics/techguides/soundseawater/content.html
    '''
    
    
    D_p = D00 + (D10*P)
    
    B_t_p = B00 + (B01*T) + (B10 + (B11*T))*P
    
    A_t_p = ((A00 + (A01*T) + (A02*(T**2)) + (A03*(T**3)) + (A04*(T**4))) +
             (A10 + (A11*T) + (A12*(T**2)) + (A13*(T**3)) + (A14*(T**4)))*P + 
             (A20 + (A21*T) + (A22*(T**2)) + (A23*(T**3)))*(P**2) + 
             (A30 + (A31*T) + (A32*(T**2)))*(P**3))
    
    Cw_t_p = ((C00 + (C01*T) + (C02*(T**2)) + (C03*(T**3)) + (C04*(T**4)) + (C05*(T**5))) + 
              (C10 + (C11*T) + (C12*(T**2)) + (C13*(T**3)) + (C14*(T**4)))*P + 
              (C20 +(C21*T) + (C22*(T**2)) + (C23*(T**3)) + (C24*(T**4)))*(P**2) + 
              (C30 + (C31*T) + (C32*(T**2)))*(P**3))
    
    C_s_t_p =  Cw_t_p + (A_t_p*S) + B_t_p*(S**(3/2)) + D_p*(S**2) #Sound Speed
    
    
    return C_s_t_p

if path.exists(DataFile):
    data = pd.read_csv(DataFile) 
    data["PRESURE(bar)"] = data["PRESURE (db)"].values/10
    data = data.rename(columns={"PRESURE (db)":"DEPTH (m)"})
    sspead = SoundSpeed(data["PRACTICAL SALINITY (psu)"],data["TEMPERATURE (C)"],data["PRESURE(bar)"])
    data["SSPEED"] = sspead.values 
    data.to_csv('SSpeed_data.csv',index=False)

else:    
    print("The file Doesn't exist...!")