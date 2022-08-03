import os
import math
import time
import matplotlib.pyplot as mp
import subprocess
import turtle
from sympy import symbols,solve
#os.system("cls")


def temp_density_cal(FlyingAltitude):
    if FlyingAltitude >= 20001:
        print("please enter with in 20 KM ")
    elif FlyingAltitude <= 11000 :
        tempatflyingalt=288.15-(0.0065*FlyingAltitude)
        pressureatflyingalt=(math.pow((tempatflyingalt/288.15),(5.2536437)))*1.01325
        speedofairatflyingalt=math.sqrt(1.402*287*tempatflyingalt)
        densityofairatflyingalt=(math.pow((tempatflyingalt/288.15),(5.2536437-1)))*1.2250
    else :
        tempatflyingalt=216.65
        pressureatflyingalt=0.226*math.exp(1.73-(0.00015777*FlyingAltitude))
        densityofairatflyingalt=0.364*math.exp(1.73-(0.00015777*FlyingAltitude))
        speedofairatflyingalt=math.sqrt(1.402*287*tempatflyingalt)
    return tempatflyingalt,pressureatflyingalt,speedofairatflyingalt,densityofairatflyingalt


def topicsinvolved():
    print("STEPS INVOLVED TO CREATE AN AIRCRAFT ARE : ")
    print("1.Preliminary Weight Estimation")
    print("2.Engine Selection")
    print("3.Second Weight Estimation")
    print("4.Selection Of Main Parameters")
    print("5.Selection Of Tip Chord And Root Chord ")
    print("6.Estimation Of Thickness To Chord Ratio")
    print("7.Estimation Of Cruise Lift Co-Efficient")
    print("8.Selection of Airfoil")
    print("9.Estimation Of Angle Of Attack")
    print("10.Estimation Of Landing Velocity Stalling Velocity")
    print("11.Estimation Of Additional Lift Co-Efficient")
    print("12.Flap Selection")
    print("13.Tyre Selection")
    print("14.Weight Breakage")
    print("15.Three View Diagram")
    print("16.Fuselage Balance Diagram")
    print("17.Wing Balance Diagram")
    print("18.Centre Of Gravity")
    print("19.Drag Estimation")
    print("20.Performance Calculation")
    print("21.Stability Calculation")


def PrilimaryWeightEstimation():
    print("\n\n1.Preiliminary Weight Estimation\n\n")
    time.sleep(2)
    
    global W_payload,W_crew,W_overall,W_fuel,W_empty,thrust_produced,thrust_produced_per_engine_inkgs
    
    print("     Wo = Wcrew + Wpayload + Wfuel + Wempty")
    print("     Wempty=Wfuselage + Wwing + WhorizontalTail + WverticalTail + Wwheels + Wfixedequipment + Wbaggage + Wengine") 
    W_payload=(Total_payload*9.81)
    W_crew=(Total_crew*110*9.81)
    
    print("     weight of crew(in newtons) :",W_crew)
    print("     weight of payload(in newtons) :",W_payload)    
    
    
    W_overall=(W_crew+W_payload)/(1-(fuel_MTW_ratio+empty_MTW_ratio))
    W_fuel=fuel_MTW_ratio*W_overall
    W_empty=empty_MTW_ratio*W_overall

    
    W_overall_in_newtons=W_overall  #in newtons
    W_overall_in_kg=W_overall/9.81   #in kilograms
    print("     the prilimary weight estimation Wo (in newtons) : ",W_overall_in_newtons)
    print("     the prilimary weight estimation Wo (in kilograms)    : ",W_overall_in_kg)

    
    #F/W=thrustloading
    print("     for design purpose 20% more is added")
    thrust_produced=thrustloading_ratio*W_overall_in_newtons*1.2  #in newtons
    
    #number of engines=e
    thrust_produced_per_engine_innewtons=thrust_produced/no_of_engines     # per engine in newtons
    thrust_produced_per_engine_inkgs=thrust_produced_per_engine_innewtons/9.81  #in kilograms
    print("     Thrust produced by one engine (in newtons) is : ",thrust_produced_per_engine_innewtons)
    print("     Thrust produced by one engine (in kilograms) is : ",thrust_produced_per_engine_inkgs)
    
    

def PowerPlantSelection():
    print("\n\n2.Engine Selection\n\n")
    time.sleep(2)
    
    global time_of_flight,Thrust_at_crusiealtitude,W_fuel_est,Density_ratio
    
    time_of_flight=key_Range/Cruise_Velocity
    
    Density_ratio=(20-Cruise_altitude)/(20+Cruise_altitude)
    print("     the density ratio is :",Density_ratio)
    Thrust_at_crusiealtitude=thrust_produced_per_engine_inkgs*Density_ratio
    print("     the thrust at cruise altitude is(in kg) : ",Thrust_at_crusiealtitude)

    print("\n     Fuel Weight Estimation\n\n")
    time.sleep(2)
    print('     considering 20% as reserver fuel ')
    W_fuel_est=1.2*time_of_flight*sfc_of_engine*Thrust_at_crusiealtitude*no_of_engines # in kilograms
    print("     the fuel weight(in kilograms) is : ",W_fuel_est)

    
    
def SecondWeightEstimation():
    print("\n\n3.Second Weight Estimation\n\n")
    time.sleep(2)
    
    global W_rtw
    
    #Wrtw=Wcrew+Wpayload+Wfuel+Wempty
    W_rtw=(W_crew+(W_fuel_est*9.81)+W_payload)/(1-empty_MTW_ratio)
    print("     the Wcrew is (in newtons) : ",W_crew)
    print("     the Wfuelest is (in newtons) : ",W_fuel_est*9.81)
    print("     the Wpayload is (in newtons): ",W_payload)
    print("     the refined takeoff weight (in newtons) is : ",W_rtw)
   

    

def KeyParameters():


    print("\n\n4.Selection Of Key Parameters\n\n")
    time.sleep(2)
    
    global wing_area,wing_span,L,Tr,Cr,Ct,TC,Cm,length_fuselage
    
    wing_area=W_rtw/(Wing_loading*9.81)
   
    print("     Wing area,S : ",wing_area)
    
    wing_span=(Aspect_ratio*wing_area)**0.5
    print("     Span length,B : ",wing_span)
    
    length_fuselage=wing_span/BL_Ratio
    print("     the length of fuselage is (in meters) :",length_fuselage)
    
    
    
    
def VolumeOfFuel():
    print("\n\n7.Selection Of Tip Chord And Root Chord\n\n")
    global Chord_root,Chord_tip,Cmean,volume_fuel
   
    Chord_root=(2*wing_area/(wing_span+Taper_ratio*wing_span))
    Chord_tip=Chord_root*Taper_ratio
    TC=(1+Taper_ratio+(Taper_ratio)**2)/(1+Taper_ratio)
    Cmean=0.667*Chord_root*TC
    print("     The Root chord lenght is(in meters) : ",Chord_root)
    print("     The tip chord lenght is (in meters) : ",Chord_tip)
    print("     The mean of the chord is(in meters) : ",Cmean)
    time.sleep(2)
    
    print('considering denisty of fuel is 0.8 kg/m**3')
    volume_fuel=W_fuel_est/(0.8*1000)
    print("     the volume of the fuel is (in metercube) : ",volume_fuel)
    

def ThicknessToChordratio():
    print("\n\n6.Estimation Of Thickness To Chord Ratio\n\n")
    time.sleep(2)
    
    global ThicknessToChordRatio
    
    ThicknessToChordRatio=volume_fuel/(wing_span*Cmean*Cmean*0.25)
    print("     the thickness of the chord ratio (t/c) is : ",ThicknessToChordRatio)
    time.sleep(2)
    

    

def CruiseLiftCoefficientCalucation():
    print("\n\n7.Etimation Of Cruise Lift Coefficient\n\n")
    #time.sleep(2)
    
    global Vcruise,FlyingAltitude,CruiseMacNumber,Density,CruiseLiftCoefficient,NEUo,To,NEU,Re
    
    #Vcruise is in m/s        
    Vcruise=Cruise_Velocity*1000/3600
    FlyingAltitude=Cruise_altitude*1000
 
    results_call=temp_density_cal(FlyingAltitude)
    tempatflyingalt=results_call[0]
    pressureatflyingalt=results_call[1]
    speedofairatflyingalt=results_call[2]
    densityofairatflyingalt=results_call[3]
    
    print("     temperature at flying altitude(in kelvin) is : ",tempatflyingalt)
    print("     pressure at flying altitude (bar) is : ",pressureatflyingalt)
    print("     speed of air at flying altitude(m/s) is : ",speedofairatflyingalt)
    print("     density of air at flying altitude (kg/m^3)is : ",densityofairatflyingalt) 

    CruiseMachNumber=Vcruise/speedofairatflyingalt
    MaximumMachNumber=CruiseMachNumber+0.04
    DensityOfAir=Density_ratio*1.225
    print("     The Cruise Mach Number is : ",CruiseMachNumber)
    print("     The Maximum Mach Number is :",MaximumMachNumber)
    CruiseLiftCoefficient=2*Wing_loading*9.81/(DensityOfAir*(Vcruise)**2)
    print("     Lift Coefficient at Cruise Velocity is : ",CruiseLiftCoefficient)

    #neu at cruise altitude
    #NEUo=sea level viscosity
    #To=Temperature at sealevel
    NEUo=1.789*10**(-5) #kg/m.s
    To=288.16 #K
    
    NEU=NEUo*(tempatflyingalt/To)**(3/4)


    #Reynolds number(in kg.S/m**2)
    Re=DensityOfAir*Vcruise*Cmean/NEU
    print("     The Reynolds Number for Provided Values Is :",Re)
    
    print("\n\n8.Selection Of Airfoil\n\n")
    Openbook=input("     Do You Want To Open Reference Book(Theory Of Wings) (y/n):")
    if Openbook=='y' or Openbook=='Y' :  # page no 415
        command=r"C:\Users\maruthi_chereddy\AbbottDoenhoff_TheoryOfWingSectionsIncludingASummaryOfAirfoilData.pdf"
        os.system(command)
    
     
def AOAcorrection():
    #AR correction for wing Airfoil
    print("\n\n9.Estimation Of Angle Of Attack\n\n")
    time.sleep(2)
    
    global Clofairfoil
    openjavafoil=input('      Do you want to open java airfoil software (y/n) : ')
    if openjavafoil=='y' or openjavafoil=='Y' :
        command=r"C:\Users\Public\Desktop\JavaFoil.lnk"
        os.system(command)
   
    Clofairfoil=float(input("please enter the maximum lift coeeficient of airfoil you selected : "))
    
    alphaStart=int(input("     Please enter the Angle of Attack To Start with : "))
    alphaEnd=int(input("     Please enter the Angle of Attack To End with : "))
    Step=int(input("     Please enter the step value : "))
    a=[] #for AOA
    b=[] #for Clift
    c=[] #for corrected AR
    d=[] #for Cd
    for i in range(alphaStart,alphaEnd+1,Step):
        a.append(i)
        i=+i
    print("     \nplease enter the lift coefficient values corresponding to your Angle Of Attacks\n : ")
    for i in a:
        Clift=float(input(f'     your Lift Coefficient for Angle of Attack {i} is : '))
       
        b.append(Clift)

    for p, q in zip(a, b):
    #alphaAR=alpha+(7*57.3*CruiseLiftCoefficientVar/(22*AR))
        alphaAR=p+(57.3*q/(3.14*Aspect_ratio))
        c.append(alphaAR)
        
    print("     \nPlease enter your drag coefficient for corresponding lift coefficients\n : ")
    for i in b:
        Clift=float(input(f'     your Drag Coefficient for corresponding lift coefficient is {i} : '))
        d.append(Clift)    
        i=i+1
        
    print("\n\nAngle Of Attack              Lift Coefficient                    Corrected AOA                   Drag Coefficient    ") 
    for m,n,o,l in zip(a, b, c, d):           
        print(m, n, o, l ,sep='\t\t\t\t')
    print("     \n\nYOUR ARE GOING TO EXECUTE GRAPH FOR THE ABOVE POINTS, !!!!! PLEASE CHECK YOUR POINTS !!!!!")
    correction=input("      \nDo you want to change any of the above points (y/n) : ")
    if correction=='y' or correction=='Y' :
        choice=int(input("      Please enter want you want to change \n1.lift coefficient\n2.drag coefficient\n3.BOTH\n Your Answer is : "))
        if choice==2:
            index=int(input("     please enter which Serial number you want to change : "))
            changedvalue=float(input("     please enter your new value : "))
            b.insert(index-1,changedvalue)
    print("PLOTTING GRAPHS FOR ABOVE MENTIONED DATA")    
 
    #collection of data for alphaAR and Cd
    time.sleep(2)
    #plotting for Cl vs alphaAR 
    print("\n************PLOTTING GRAPH FOR ANGLE OF ATTACK V/S LIFT COEFFICIENT**************")
    #for AOA x
    #for Cl y
     
    mp.scatter(a,b,label='stars',color='green', marker='*',s=30)
    mp.title('Lift Coefficient vs Angle Of Attack ')
    mp.xlabel('Angle Of Attack')
    mp.ylabel('Lift Coefficient')
    mp.plot(a,b)
    mp.show()        
            
    #plotting for Cl vs Cd
    print("\n************PLOTTING GRAP FOR LIFT COEFFICIENT V/S DRAG COEFFICIENT**************\n\n")


    mp.scatter(d,b,label='stars',color='green', marker='*',s=30)
    mp.title('Lift Coefficient vs Drag coefficient ')
    mp.ylabel('lift Coefficient')
    mp.xlabel('Drag coefficient')
    mp.plot(d,b)
    mp.show()    
    
    #plotting for Cl vs alphaAR
    print("\n************PLOTTING GRAP FOR LIFT COEFFICIENT V/S Corrected Angle Of Attack**************\n\n")


    mp.scatter(c,b,label='stars',color='green', marker='*',s=30)
    mp.title('Lift Coefficient vs Corrected Angle Of Attack ')
    mp.xlabel('Corrected Angle Of Attack')
    mp.ylabel('Lift coefficient')
    mp.plot(c,b)
    mp.show()         
    
    
    
def EstimationOfLandingVelocityAndStallingVelocity():
    #time.sleep(2)
    global CARFieldlength,g,deacclerating,LandingVelocity,StallingVelocity,Clmaxreq,diffClreq
           
    CARFieldlength=Runway_Length*0.6
    g=9.81
    deaccelerating=0.25*g
    LandingVelocity=math.sqrt(0.5*g*CARFieldlength)

    StallingVelocity=LandingVelocity/1.15

    Clmaxreq=2*Wing_loading*9.81/(1.225*(StallingVelocity)**2)
    
    print("\n\n11.Estimation Of Additional Lift Co-Efficient\n\n")
    print("     The coefficient lift maximum required is : ",Clmaxreq) 
    diffClreq=Clmaxreq-Clofairfoil    
    print("     The Calculated Delta Lift Coefficient Required is : ",diffClreq)    
    flapselection()
    #flap Selection open pdf
def flapselection():
    print("\n\n12.Flap Selection\n\n") 
    toopen=input("      Do you want to open flap selection pdf (y/n): ")
    if toopen=='y' or toopen=='Y' :
        command=r"C:\Users\maruthi_chereddy\FLAP_CHORD_data_pdf.pdf"
        os.system(command)
    flapCl=float(input("      please enter the Coefficient Of Lift Of Flap : "))
    tyreselection()
    #tyre selection
def tyreselection():
    print("\n\n13.Tyre Selection \n\n")
    global noofNLGtyres,dia_NLGtyres,width_NLGtyres,noofMLGtyres,dia_MLGtyres,width_MLGtyre
    
    noofNLGtyres=int(input("     please enter number of nose landing gear tyres : " ))
    dia_NLGtyres=float(input("     please enter the diameter of nose landing gear tyre(in inch) : "))
    width_NLGtyres=float(input("     please enter the width of nose landing gear tyre(in inch) : "))
    noofMLGtyres=int(input("     please enter number of main landing gear tyres : "))
    dia_MLGtyres=float(input("     please enter the diameter of main landing gear tyre(in inch) : "))
    width_MLGtyre=float(input("     please enter the width of main landing gear tyre(in inch) : "))
    R=float(input("     please enter radius of full tyre (R in inch) : "))
    r=float(input("     please enter radius of flated tyre (r in inch) : "))
    
    loadtakenbymainlandinggear=0.9*W_rtw
    loadtakenbynoselandinggear=0.1*W_rtw
    loadonMLG=loadtakenbymainlandinggear*0.225
    loadonNLG=loadtakenbynoselandinggear*0.225
    
    inflation=math.sqrt((R*R)-(r*r))
    contactarea=22*inflation*width_MLGtyre/(7*2*144) #ft^2 per wheel
    runwayload=(W_rtw/9.81)/(contactarea*noofMLGtyres)

    print("     load taken by main landing gear(in pounds) is : ",loadonMLG)
    print("     load taken by each tyre in main landing gear(in pounds) is : ",loadonMLG/noofMLGtyres)
    print("     load taken by nose landing gear(in pounds) is : ",loadonNLG)
    print("     the runway loading (in ton/ft^2) is : ",runwayload/1000)
    
    
def emphanage():
    global Area_horizontaltailwing,wingspan_horizontaltailwing,Chordroot_horizontaltailwing,Chordtip_horizontaltailwing,Area_verticaltailwing,wingspan_verticaltailwing,Chordroot_verticaltailwing,Chordtip_verticaltailwing

    print('estmation of horizontal tail parameters : ')
    S_Sw_ratio_horizontaltailwing=float(input('please enter the S/Swing ratio of horizontal tail wing : '))
    Area_horizontaltailwing=S_Sw_ratio_horizontaltailwing*wing_area
    AR_horizontaltailwing=float(input('please enter the aspect ratio of tail wing : '))
    wingspan_horizontaltailwing=(AR_horizontaltailwing*Area_horizontaltailwing)**0.5
    Taper_horizontaltailwing=float(input('please enter the taper ratio of tail wing : '))
    Chordroot_horizontaltailwing=2*Area_horizontaltailwing/(wingspan_horizontaltailwing*(1+Taper_horizontaltailwing))
    Chordtip_horizontaltailwing=Taper_horizontaltailwing*Chordroot_horizontaltailwing
    print('estmation of vertical tail parameters : ')
    S_Sw_ratio_verticaltailwing=float(input('please enter the S/Swing ratio of vertical tail wing : '))
    Area_verticaltailwing=S_Sw_ratio_verticaltailwing*wing_area
    AR_verticaltailwing=float(input('please enter the aspect ratio of vertical tail wing : '))
    wingspan_verticaltailwing=(AR_verticaltailwing*Area_verticaltailwing)**0.5
    Taper_verticaltailwing=float(input('please enter the taper ratio of vertical tail wing : '))
    Chordroot_verticaltailwing=2*Area_verticaltailwing/(wingspan_verticaltailwing*(1+Taper_verticaltailwing))
    Chordtip_verticaltailwing=Taper_verticaltailwing*Chordroot_verticaltailwing    
        
    print('area of horizontal tail wing : ',Area_horizontaltailwing)
    print('wing span of horizontal tail wing : ',wingspan_horizontaltailwing )
    print('chord root of horizontal tail wing : ',Chordroot_horizontaltailwing)
    print('chord tip of horizontal tail wing : ',Chordtip_horizontaltailwing)
    print('/narea of vertical tail wing : ',Area_verticaltailwing)
    print('wing span of vertical tail wing : ',wingspan_verticaltailwing )
    print('chord root of vertical tail wing : ',Chordroot_verticaltailwing)
    print('chord tip of vertical tail wing : ',Chordtip_verticaltailwing)    
    
    
    
    
def weightbreakage():
    
    global W_fusl,W_wing,W_verttail,W_horiztail,W_noselandinggear,W_mainlandinggear,W_engine,W_fixedequip,W_baggage,W_lavatory
    
    again2=True
    while again2==True :
        print("\n\n14.Weight Breakage\n\n")
        W_fusl=float(input("     please enter Wfuselage ratio : "))
        W_wing=float(input("     please enter Wwing ratio : "))
        W_horiztail=float(input("     please enter WhorizontalTail ratio : "))
        W_verttail=float(input("     please enter WverticalTail ratio : "))
        W_noselandinggear=float(input("     please enter Wnoselandinggear under carriage ratio : "))
        W_mainlandinggear=float(input("     please enter Wmainlandinggear under carriage ratio : "))
        W_engine=float(input("     please enter Wengine ratio(including all engines) : "))
        W_fixedequip=float(input("     please enter Wfixedequip ratio : "))
        W_baggage=float(input("     please enter Wbaggage ratio : "))
        W_lavatory=float(input('     please enter the Wlavatory ratio : '))
       
        W_emptytotal=W_fusl+W_wing+W_horiztail+W_verttail+W_noselandinggear+W_mainlandinggear+W_engine+W_fixedequip+W_baggage+W_lavatory
        if W_emptytotal <= empty_MTW_ratio :
            print(f'\n\n     weight of fuselage is {W_fusl*W_rtw} N')
            print(f'      weight of wing is {W_wing*W_rtw} N')
            print(f'      weight of horizantal tail is {W_horiztail*W_rtw} N')
            print(f'      weight of vertical tail is {W_verttail*W_rtw} N')
            print(f'      weight of nose landing gear under carriage is {W_noselandinggear*W_rtw} N')
            print(f'      weight of main landing gear under carriage is {W_mainlandinggear*W_rtw} N')
            print(f'      weight of power plant is {W_engine*W_rtw} N')
            print(f'      weight of fixed equipment is {W_fixedequip*W_rtw} N')
            print(f'      weight of baggage is {W_baggage*W_rtw} N')
            again2=False
        else :
            print("     please check the given values ### given values exculde the empty weight provided ")
            tryagain=input("Do you want to re-enter the weight breakage values (y/n) : ")
            if tryagain=='n' or tryagain == 'N' :
                again2=False
    #threedimview()
    
def CG_calculation():

    print('\n\n18.Center of gravity calculation of the airplane')
    print('\n   1. center of gravity calculation for fuselage')
    print('     CASE(1) : FULL PAYLOAD ')

    noof_galley=int(input('\n\n     please enter number of galley : '))
    noof_lavatory=int(input('     please enter number of lavatory : '))
    print('     assume like class(1)=business class , class(2)=first class ,class(3)=second class (or) economy class ')
    noof_classes=int(input('     please enter total number of classes : ')) 
    
    percent_of_instrument_weight=float(input('     please enter the percent of instrument weight at frontal part of wing : ')) 
    weight_instrumentsfront=(percent_of_instrument_weight/100)*W_fixedequip*W_rtw
    distance_instrumentsfront=float(input('     please enter distance of instruments(front) from nose of aircraft : '))
    weight_pilots_inkg=float(input('     please enter pilots weight ( in kgs) : '))
    weight_pilots=weight_pilots_inkg*9.81
    distance_pilots=float(input('     please enter distance of pilots from nose of aircraft : '))
    weight_nosegear=W_noselandinggear*W_rtw
    distance_nosegear=float(input('     please enter distance of nose gear from nose of aircraft : '))
    weight_crew=float(input('     please enter crew weight ( in Newtons) : '))
    distance_crew=float(input('     please enter distance of crew from nose of aircraft : '))
    weight_fuselagestructure=W_fusl*W_rtw
    distance_fuselagestructure=float(input('     please enter the distance of  fuselage structure from nose of aircraft : '))
    weight_instrumentsend=((100-percent_of_instrument_weight)/100)*W_fixedequip*W_rtw
    distance_instrumentsend=float(input('     please enter distance of instruments(end) from nose of aircraft : '))
    weight_verticalTail=W_verttail*W_rtw
    distance_verticalTail=float(input('     please enter distance of vertical Tail from nose of aircraft : '))
    weight_horizontalTail=W_horiztail*W_rtw
    distance_instruments=float(input('     please enter distance of horizontal Tail from nose of aircraft : '))
    weight_mainlandinggear=float(input('     please enter the weight of main landing gear ( if included in fuselage only) : '))
    distance_mainlandinggear=float(input('     please enter distance of main landing gear from nose of aircraft : '))
    weight_cargo_payload=Total_payload*9.81
    distance_cargo_payload=float(input('     please enter the distance of payload(if your category is cargo only else enter 0) : '))
    weight_engine_fuselage=float(input('     please enter the weight of engine (if attached to fuselage only )(in newtons) : '))
    distance_engine_fuselage=float(input('     please enter the distance of engine from nose of the aircraft (in meters) : '))
    
    fullpayload_weight=[weight_instrumentsfront,weight_pilots,weight_nosegear,weight_crew,weight_fuselagestructure,weight_instrumentsend,weight_verticalTail,weight_horizontalTail,weight_mainlandinggear,weight_cargo_payload,weight_engine_fuselage]
    object_distance=[distance_instrumentsfront,distance_pilots,distance_nosegear,distance_crew,distance_fuselagestructure,distance_instrumentsend,distance_verticalTail,distance_instruments,distance_mainlandinggear,distance_cargo_payload,distance_engine_fuselage]
    component_name=['instruments (front)','         pilots      ','nose landing gear','           crew      ','fuselage structure','instruments (end)','    vertical tail','    horizontal tail','main landing gear','      payload     ','      engine     ']
    
    #if weight_engine_fuselage!=0 :
    #    component_name.append('      engine ')
        
    for i in range(noof_galley):
        weight_galley_i=float(input('      please enter galley weight ( in Newtons) : '))
        distance_galley_i=float(input('     please enter distance of galley from nose of aircraft : '))
        fullpayload_weight.append(weight_galley_i)
        object_distance.append(distance_galley_i)
        if i==0:
            component_name.append('         galley_1    ')
        if i==1:
            component_name.append('         galley_2    ')
        if i==2:
            component_name.append('         galley_3    ')
        if i==3:
            component_name.append('         galley_4    ')

    for i in range(noof_lavatory):
        weight_lavatory_i=W_lavatory*W_rtw/noof_lavatory
        distance_lavatory_i=float(input('      please enter distance of lavatory from nose of aircraft : '))
        fullpayload_weight.append(weight_lavatory_i)
        object_distance.append(distance_lavatory_i)
        if i==0:
            component_name.append('     lavatory_1  ')
        if i==1:
            component_name.append('     lavatory_2  ')
        if i==2:
            component_name.append('     lavatory_3  ')
        if i==3:
            component_name.append('     lavatory_4  ')
        
    for i in range(noof_classes):    
        weight_classes_i=float(input('      please enter passengers first class weight ( in Newtons) : '))
        distance_classes_i=float(input('      please enter distance of passengers first class from nose of aircraft : '))
        fullpayload_weight.append(weight_classes_i)
        object_distance.append(distance_classes_i)
        if i==0:
            component_name.append('         class_1     ')
        if i==1:
            component_name.append('         class_2     ')
        if i==2:
            component_name.append('         class_3     ')
        if i==3:
            component_name.append('         class_4     ')
    

    
    
    fullpayload_WX= [x*y for x,y in zip(fullpayload_weight,object_distance)]
    sum_fullpayload_weight=sum(fullpayload_weight)
    sum_fullpayload_WX=sum(fullpayload_WX)
    fullpayload_Xfus=sum_fullpayload_WX/sum_fullpayload_weight
    print('\n       components               weight(N)          X (in meters)          WX\n')
    for m,n,o,l in zip(component_name, fullpayload_weight, object_distance,fullpayload_WX):           
        print(m, "{:.3f}".format(n), "{:.3f}".format(o),"{:.3f}".format(l)  ,sep='\t\t')
    print('\n     sum of fullpayload (W*X) : ',"{:.3f}".format(sum_fullpayload_WX))
    print('      X of fuselage (X fuselage) : ',"{:.3f}".format(fullpayload_Xfus))
    
    print('\n\n     CASE(2) : HALF PAYLOAD ')
    halfpayload_weight=fullpayload_weight
    if noof_classes==0:
        halfpayload_weight[9]=weight_cargo_payload/2
    if noof_classes==1:
        halfpayload_weight[10+noof_galley+noof_lavatory+1]=weight_classes_1/2
    if noof_classes==2:
        halfpayload_weight[10+noof_galley+noof_lavatory+1]=weight_classes_1/2
        halfpayload_weight[10+noof_galley+noof_lavatory+2]=weight_classes_2/2
    if noof_classes==3:
        halfpayload_weight[10+noof_galley+noof_lavatory+1]=weight_classes_1/2
        halfpayload_weight[10+noof_galley+noof_lavatory+2]=weight_classes_2/2
        halfpayload_weight[10+noof_galley+noof_lavatory+3]=weight_classes_3/2
    if noof_classes==4:
        halfpayload_weight[10+noof_galley+noof_lavatory+1]=weight_classes_1/2
        halfpayload_weight[10+noof_galley+noof_lavatory+2]=weight_classes_2/2
        halfpayload_weight[10+noof_galley+noof_lavatory+3]=weight_classes_3/2
        halfpayload_weight[10+noof_galley+noof_lavatory+4]=weight_classes_4/2
    
    
    #halfpayload_weight=[weight_instrumentsfront,weight_pilots,weight_nosegear,weight_galley,weight_lavatory,weight_crew,half_weight_passengersFC,weight_lavatory2,weight_crew2,weight_fuselagestructure,half_weight_passengerseconomy,weight_lavatory3,weight_instrumentsend,weight_verticalTail,weight_horizontalTail]
    halfpayload_WX= [x*y for x,y in zip(halfpayload_weight,object_distance)]
    sum_halfpayload_weight=sum(halfpayload_weight)
    sum_halfpayload_WX=sum(halfpayload_WX)
    halfpayload_Xfus=sum_halfpayload_WX/sum_halfpayload_weight
    
    print('\n       components               weight(N)           X (in meters)          WX\n')
    for m,n,o,l in zip( component_name,halfpayload_weight, object_distance,halfpayload_WX):           
        print(m, "{:.3f}".format(n), "{:.3f}".format(o),"{:.3f}".format(l)  ,sep='\t\t')
    print('\n     sum of halfpayload (W*X) : ',"{:.3f}".format(sum_halfpayload_WX))
    print('     X of fuselage (X fuselage) : ',"{:.3f}".format(halfpayload_Xfus))

    print('     CASE(3) : NULL PAYLOAD ')

    nullpayload_weight=fullpayload_weight
    if noof_classes==0:
        nullpayload_weight[9]=0
    if noof_classes==1:
        halfpayload_weight[10+noof_galley+noof_lavatory+1]=0
    if noof_classes==2:
        halfpayload_weight[10+noof_galley+noof_lavatory+1]=0
        halfpayload_weight[10+noof_galley+noof_lavatory+2]=0
    if noof_classes==3:
        halfpayload_weight[10+noof_galley+noof_lavatory+1]=0
        halfpayload_weight[10+noof_galley+noof_lavatory+2]=0
        halfpayload_weight[10+noof_galley+noof_lavatory+3]=0
    if noof_classes==4:
        halfpayload_weight[10+noof_galley+noof_lavatory+1]=0
        halfpayload_weight[10+noof_galley+noof_lavatory+2]=0
        halfpayload_weight[10+noof_galley+noof_lavatory+3]=0
        halfpayload_weight[10+noof_galley+noof_lavatory+4]=0
    
    #nullpayload_weight=[weight_instrumentsfront,weight_pilots,weight_nosegear,weight_galley,weight_lavatory,weight_crew,null_weight_passengersFC,weight_lavatory2,weight_crew2,weight_fuselagestructure,null_weight_passengerseconomy,weight_lavatory3,weight_instrumentsend,weight_verticalTail,weight_horizontalTail]
    nullpayload_WX= [x*y for x,y in zip(nullpayload_weight,object_distance)]
    sum_nullpayload_weight=sum(nullpayload_weight)
    sum_nullpayload_WX=sum(nullpayload_WX)
    nullpayload_Xfus=sum_nullpayload_WX/sum_nullpayload_weight
    
    print('\n       components               weight(N)          X (in meters)           WX\n')
    for m,n,o,l in zip( component_name,nullpayload_weight, object_distance,nullpayload_WX):           
        print(m, "{:.3f}".format(n), "{:.3f}".format(o),"{:.3f}".format(l)  ,sep='\t\t')
    print('\n     sum of nullpayload (W*X) : ',"{:.3f}".format(sum_nullpayload_WX))
    print('      X of fuselage (X fuselage) : ',"{:.3f}".format(nullpayload_Xfus))


    print('\n\n      center of gravity calculation of wing ')

    print('\n       case(1): full fuel weight')

    weight_wing_structure=W_wing*W_rtw/2
    x_distance_wingstructure=float(input('\n      please enter the X(m) of wing structure : '))
    y_distance_wingstructure=float(input('      please enter the Y(m) of wing structure : '))
    weight_main_landinggear=float(input('      please enter the weight of main landing gear(if in wing) (in newtons) : '))
    x_distance_maingear=float(input('      please enter the X(m) of main landing gear : '))
    y_distance_maingear=float(input('      please enter the Y(m) of main landing gear : '))
    weight_fuel_weight=W_fuel_est*9.81/2
    x_distance_fuelweight=float(input('      please enter the X(m) of fuel weight : '))
    y_distance_fuelweight=float(input('      please enter the Y(m) of fuel weight : '))

    component_name_wing=['wing structure    ','main landing gear','     fuel weight ']
    object_x_distance=[x_distance_wingstructure,x_distance_maingear,x_distance_fuelweight]
    object_y_distance=[y_distance_wingstructure,y_distance_maingear,y_distance_fuelweight]
    fullfuel_weight=[weight_wing_structure,weight_main_landinggear,weight_fuel_weight]
    
    weight_engine_1=weight_engine_2=weight_engine_3=W_engine*W_rtw/(no_of_engines/2)
    if (no_of_engines/2)==1:
        x_distance_engine_1=float(input('      please enter the X(m) of engine(if engine is attached to wing only): '))
        y_distance_engine_1=float(input('      please enter the Y(m) of engine (if engine is attached to wing only : '))
        component_name_wing.append('    engine_1    ')
        object_x_distance.append(x_distance_engine_1)
        object_y_distance.append(y_distance_engine_1)
        fullfuel_weight.append(weight_engine_1)
    if (no_of_engines/2)==2:
        x_distance_engine_1=float(input('      please enter the X(m) of engine(if engine is attached to wing only): '))
        y_distance_engine_1=float(input('      please enter the Y(m) of engine (if engine is attached to wing only : '))
        x_distance_engine_2=float(input('      please enter the X(m) of engine 2(if engine is attached to wing only): '))
        y_distance_engine_2=float(input('      please enter the Y(m) of engine 2(if engine is attached to wing only : '))
        component_name_wing.append('    engine_1    ')
        component_name_wing.append('    engine_2    ')
        object_x_distance.append(x_distance_engine_1)
        object_y_distance.append(y_distance_engine_1)
        fullfuel_weight.append(weight_engine_1)
        object_x_distance.append(x_distance_engine_2)
        object_y_distance.append(y_distance_engine_2)
        fullfuel_weight.append(weight_engine_2)
    if (no_of_engines/2)==3:
        x_distance_engine_1=float(input('      please enter the X(m) of engine(if engine is attached to wing only): '))
        y_distance_engine_1=float(input('      please enter the Y(m) of engine (if engine is attached to wing only : '))
        x_distance_engine_2=float(input('      please enter the X(m) of engine 2(if engine is attached to wing only): '))
        y_distance_engine_2=float(input('      please enter the Y(m) of engine 2(if engine is attached to wing only : '))
        x_distance_engine_3=float(input('      please enter the X(m) of engine 3(if engine is attached to wing only): '))
        y_distance_engine_3=float(input('      please enter the Y(m) of engine 3(if engine is attached to wing only : '))
        component_name_wing.append('    engine_1    ')
        component_name_wing.append('    engine_2    ')
        component_name_wing.append('    engine_3    ')
        object_x_distance.append(x_distance_engine_1)
        object_y_distance.append(y_distance_engine_1)
        fullfuel_weight.append(weight_engine_1)
        object_x_distance.append(x_distance_engine_2)
        object_y_distance.append(y_distance_engine_2)
        fullfuel_weight.append(weight_engine_2)
        object_x_distance.append(x_distance_engine_3)
        object_y_distance.append(y_distance_engine_3)
        fullfuel_weight.append(weight_engine_3)
    

    
    
    
    
    fullfuel_WX= [x*y for x,y in zip(fullfuel_weight,object_x_distance)]
    sum_fullfuel_weight=sum(fullfuel_weight)
    sum_fullfuel_WX=sum(fullfuel_WX)
    fullfuel_Xwing=sum_fullfuel_WX/sum_fullfuel_weight

    
    fullfuel_WY= [x*y for x,y in zip(fullfuel_weight,object_y_distance)]
    sum_fullfuel_WY=sum(fullfuel_WY)
    fullfuel_Ywing=sum_fullfuel_WY/sum_fullfuel_weight

    print('\n   components                  weight                    X(in meters)     Y(in meters)      WX                 WY\n')
    for m,n,o,p,q,r in zip( component_name_wing,fullfuel_weight, object_x_distance,object_y_distance,fullfuel_WX,fullfuel_WY):           
        print(m, "{:.3f}".format(n), "{:.3f}".format(o),"{:.3f}".format(p) ,"{:.3f}".format(q),"{:.3f}".format(r) ,sep='\t\t')
    print('\n      sum of nullpayload (W*X) : ',"{:.3f}".format(sum_fullfuel_weight))
    print('      X of fuselage (X fuselage) : ',"{:.3f}".format(fullfuel_Xwing))
    print('      Y of fuselage (Y fuselage) : ',"{:.3f}".format(fullfuel_Ywing))

    print('\n\n     case(2): half fuel weight')

    #half_fuelweight=weight_fuel_weight/2
    halffuel_weight=fullfuel_weight
    halffuel_weight[2]=weight_fuel_weight/2

    halffuel_WX= [x*y for x,y in zip(halffuel_weight,object_x_distance)]
    sum_halffuel_weight=sum(halffuel_weight)
    sum_halffuel_WX=sum(halffuel_WX)
    halffuel_Xwing=sum_halffuel_WX/sum_halffuel_weight

    halffuel_WY= [x*y for x,y in zip(halffuel_weight,object_y_distance)]
    sum_halffuel_WY=sum(halffuel_WY)
    halffuel_Ywing=sum_halffuel_WY/sum_halffuel_weight

    print('\n   components                  weight                    X(in meters)     Y(in meters)      WX                 WY\n')
    for m,n,o,p,q,r in zip( component_name_wing,halffuel_weight, object_x_distance,object_y_distance,halffuel_WX,halffuel_WY):           
        print(m, "{:.3f}".format(n), "{:.3f}".format(o),"{:.3f}".format(p),"{:.3f}".format(q),"{:.3f}".format(r)  ,sep='\t\t')
    print('\n      sum of nullpayload (W*X) : ',"{:.3f}".format(sum_halffuel_weight))
    print('      X of fuselage (X fuselage) : ',"{:.3f}".format(halffuel_Xwing))
    print('      Y of fuselage (Y fuselage) : ',"{:.3f}".format(halffuel_Ywing))


    print('\n\n     case(3): reserve fuel weight')

    print('\n     considering 20% of reserve fuel ')
    #reserve_fuelweight=weight_fuel_weight*0.2
    #reservefuel_weight=[weight_wing_structure,weight_main_landinggear,weight_engine,reserve_fuelweight]
    reservefuel_weight=fullfuel_weight
    reservefuel_weight[2]=weight_fuel_weight*0.2
    
    reservefuel_WX= [x*y for x,y in zip(reservefuel_weight,object_x_distance)]
    sum_reservefuel_weight=sum(reservefuel_weight)
    sum_reservefuel_WX=sum(reservefuel_WX)
    reservefuel_Xwing=sum_reservefuel_WX/sum_reservefuel_weight

    reservefuel_WY= [x*y for x,y in zip(reservefuel_weight,object_y_distance)]
    sum_reservefuel_WY=sum(reservefuel_WY)
    reservefuel_Ywing=sum_reservefuel_WY/sum_reservefuel_weight

    print('\n   components                  weight                  X(in meters)     Y(in meters)      WX                   WY\n')
    for m,n,o,p,q,r in zip( component_name_wing,reservefuel_weight, object_x_distance,object_y_distance,reservefuel_WX,reservefuel_WY):           
        print(m,"{:.3f}".format(n) , "{:.3f}".format(o),  "{:.3f}".format(p),"{:.3f}".format(q),  "{:.3f}".format(r),sep='\t\t')
    print('\n      sum of nullpayload (W*X) : ',"{:.3f}".format(sum_reservefuel_weight))
    print('      X of fuselage (X fuselage) : ',"{:.3f}".format(reservefuel_Xwing))
    print('      Y of fuselage (Y fuselage) : ',"{:.3f}".format(reservefuel_Ywing))

   
    print('AIRPLANE WITH FULL PAYLOAD + FULL FUEL ')

    _1_W_wing=2*sum_fullfuel_weight
    _1_W_fuselage=sum_fullpayload_weight
    _1_X_wing=fullfuel_Xwing
    _1_X_fuselage=fullpayload_Xfus
    X_final_1=float(input("please enter the distance of 0.3Cmean from leading edge of chordroot : "))
    
    X=(_1_W_fuselage*_1_X_fuselage+_1_W_wing*_1_X_wing-(_1_W_wing+_1_W_fuselage)*X_final_1)/_1_W_fuselage
    #_1_W_fuselage*_1_X_fuselage + _1_W_wing*(X+_1_X_wing)=(_1_W_fuselage+_1_W_wing)*(X+X_final_1)
    
    #_of_overall_length=overall_length/X
    print("the wing attachment point of airplane is : ",X )
    #print(X_final_1)

    print('AIRPLANE WITH FULL PAYLOAD + HALF FUEL ')

    _2_W_wing=2*sum_halffuel_weight
    _2_W_fuselage=sum_fullpayload_weight
    _2_X_wing=halffuel_Xwing
    _2_X_fuselage=fullpayload_Xfus
    
    
    X_final_2=-(_2_W_fuselage*X - _2_W_fuselage*_2_X_fuselage - _2_W_wing*_2_X_wing)/(_2_W_fuselage+_2_W_wing)

    X_2=(X_final_2 - X_final_1)/(Cmean)

    print(X_2)
    print(X_final_2)


    print('AIRPLANE WITH FULL PAYLOAD + RESERVE FUEL ')

    _3_W_wing=2*sum_reservefuel_weight
    _3_W_fuselage=sum_fullpayload_weight
    _3_X_wing=reservefuel_Xwing
    _3_X_fuselage=fullpayload_Xfus
    X_final_3=-((_3_W_fuselage)*X - _3_W_fuselage*_3_X_fuselage - _3_W_wing*_3_X_wing)/(_3_W_fuselage+_3_W_wing)

    X_3=(X_final_3 - X_final_1)/(Cmean)
    
    print(X_3)
    print(X_final_3)    
    

    print('AIRPLANE WITH HALF PAYLOAD + FULL FUEL ')


    _4_W_wing=2*sum_fullfuel_weight
    _4_W_fuselage=sum_halfpayload_weight
    _4_X_wing=fullfuel_Xwing
    _4_X_fuselage=halfpayload_Xfus
    X_final_4=-((_4_W_fuselage)*X - _4_W_fuselage*_4_X_fuselage - _4_W_wing*_4_X_wing)/(_4_W_fuselage+_4_W_wing)

    X_4=(X_final_4 - X_final_1)/(Cmean)

    print(X_4)
    print(X_final_4)



    print('AIRPLANE WITH HALF PAYLOAD + HALF FUEL ')



    _5_W_wing=2*sum_halffuel_weight
    _5_W_fuselage=sum_halfpayload_weight
    _5_X_wing=halffuel_Xwing
    _5_X_fuselage=halfpayload_Xfus
    X_final_5=-((_5_W_fuselage)*X - _5_W_fuselage*_5_X_fuselage - _5_W_wing*_5_X_wing)/(_5_W_fuselage+_5_W_wing)

    X_5=(X_final_5 - X_final_1)/(Cmean)

    print(X_5)
    print(X_final_5)


    print('AIRPLANE WITH HALF PAYLOAD + RESERVE FUEL ')


    _6_W_wing=2*sum_reservefuel_weight
    _6_W_fuselage=sum_halfpayload_weight
    _6_X_wing=reservefuel_Xwing
    _6_X_fuselage=halfpayload_Xfus
    X_final_6=-((_6_W_fuselage)*X - _6_W_fuselage*_6_X_fuselage - _6_W_wing*_6_X_wing)/(_6_W_fuselage+_6_W_wing)

    X_6=(X_final_6 - X_final_1)/(Cmean)

    print(X_6)
    print(X_final_6)



    print('AIRPLANE WITH NO PAYLOAD + FULL FUEL ')


    _7_W_wing=2*sum_fullfuel_weight
    _7_W_fuselage=sum_nullpayload_weight
    _7_X_wing=fullfuel_Xwing
    _7_X_fuselage=nullpayload_Xfus
    X_final_7=-((_7_W_fuselage)*X - _7_W_fuselage*_7_X_fuselage - _7_W_wing*_7_X_wing)/(_7_W_fuselage+_7_W_wing)

    X_7=(X_final_7 - X_final_1)/(Cmean)

    print(X_7)
    print(X_final_7)




    print('AIRPLANE WITH NO PAYLOAD + HALF FUEL ')


    _8_W_wing=2*sum_halffuel_weight
    _8_W_fuselage=sum_nullpayload_weight
    _8_X_wing=halffuel_Xwing
    _8_X_fuselage=nullpayload_Xfus
    X_final_8=-((_8_W_fuselage)*X - _8_W_fuselage*_8_X_fuselage - _8_W_wing*_8_X_wing)/(_8_W_fuselage+_8_W_wing)

    X_8=(X_final_8 - X_final_1)/(Cmean)

    print(X_8)
    print(X_final_8)



    print('AIRPLANE WITH NO PAYLOAD + RESERVE FUEL ')


    _9_W_wing=2*sum_reservefuel_weight
    _9_W_fuselage=sum_nullpayload_weight
    _9_X_wing=reservefuel_Xwing
    _9_X_fuselage=nullpayload_Xfus
    X_final_9=-((_9_W_fuselage)*X - _9_W_fuselage*_9_X_fuselage - _9_W_wing*_9_X_wing)/(_9_W_fuselage+_9_W_wing)

    X_9=(X_final_9 - X_final_1)/(Cmean)
    print(X_9)
    print(X_final_9)

    X_CG=X+Cmean
    print('      The center of gravity point of airplane is : ',X_CG) 
    
    
    
def drag_estimation():

    print('DRAG ESTIMATION')
    print('The various components of drag are : \n1. Parasite drag\n2. Induced drag\n3. Interference drag\n4. Drag due to compressibility correction')

    print('PROPER AREA METHOD')

    radius_of_fuselage=float(input('please enter the radius of fuselage : '))
    area_fuselage=3.14*radius_of_fuselage**2
    area_horizontalTail=Area_horizontaltailwing
    area_VerticalTail=Area_verticaltailwing
    area_powerplant_frontal=3.14*radius_engine*radius_engine*no_of_engines
    area_nosewheel=dia_NLGtyres*width_NLGtyres*noofNLGtyres*0.00064516   #from inch**2 to meter**2
    area_mainwheel=dia_MLGtyres*width_MLGtyre*noofMLGtyres*0.00064516  #from inch**2 to meter**2
    percent_of_aileron_wing_area=float(input('please enter the aileron area to wing area ratio : '))
    area_aileron=percent_of_aileron_wing_area*wing_area
    #L_aileron=float(input('please enter the length of aileron : '))
    L_aileron=area_aileron/(2*0.15*Cmean)
    L_flaps=(wing_span/2)-L_aileron-radius_of_fuselage
    area_flap=2*(0.3*Cmean)*L_flaps
        
       
    #drag coefficinet:
    Cf=0.427/(math.log(Re)-0.407)**2.64
    def wingdrag():
   
        
        Cdo=Cf*(4+2*(ThicknessToChordRatio)**(-1)+120*(ThicknessToChordRatio)**3)
        return Cdo
    
    def fuselagedrag():
    
        Cdo=Cf*(3*(length_fuselage/(2*radius_of_fuselage))+4.5*((2*radius_of_fuselage)/length_fuselage)**0.5+21*(2*radius_of_fuselage/length_fuselage)**2)
        return Cdo
    #horizontal and vertical tail : 90% of wing

    e=0.9#(for taper wing)
    #interfernce drag=5% of C do other service
    K=1/(3.14*e*Aspect_ratio)
    
    
    #drag_components=['canopy','fuselage','wing','vertical tail','horizontal tail','engine','nose landing gear','main landing gear','3/4th flap','full flap']
    #area_dragcomponents=[0.75*area_fuselage,area_fuselage,wing_area,area_VerticalTail,area_horizontalTail,area_powerplant_frontal,area_nosewheel,area_mainwheel,area_flap,area_flap]
    #CD_coefficient=[ 10*fuselagedrag(),fuselagedrag(),wingdrag(),0.9*wingdrag(),0.9*wingdrag(),fuselagedrag(),0.6,1,0.051,0.077    ]
    print('for cruise condition')
    cruise_drag_components=['       canopy','       fuselage','       wing','vertical tail','horizontal tail','         engine']
    cruise_area_dragcomponents=[0.75*area_fuselage,area_fuselage,wing_area,area_VerticalTail,area_horizontalTail,area_powerplant_frontal]
    cruise_CD_coefficient=[ 10*fuselagedrag(),fuselagedrag(),wingdrag(),0.9*wingdrag(),0.9*wingdrag(),fuselagedrag() ]
    cruise_dragarea= [x*y for x,y in zip(cruise_area_dragcomponents,cruise_CD_coefficient)]
    print('\n   components                  \n')
    for m,n,o,p in zip(cruise_drag_components,cruise_area_dragcomponents,cruise_CD_coefficient,cruise_dragarea ):           
        print(m, n,o,p  ,sep='\t\t')
    sum_cruise_dragarea=sum(cruise_dragarea)
    cruise_Cdo_others=sum_cruise_dragarea/wing_area
    cruise_interferencedrag=cruise_Cdo_others*1.05
    print('The interfernce drag for cruise condition is : ',cruise_interferencedrag)
    
    print('for landing condition')
    landing_drag_components=['      canopy','       fuselage','       wing','vertical tail','horizontal tail','        engine','nose landing gear','main landing gear','   full flap']
    landing_area_dragcomponents=[0.75*area_fuselage,area_fuselage,wing_area,area_VerticalTail,area_horizontalTail,area_powerplant_frontal,area_nosewheel,area_mainwheel,area_flap]
    landing_CD_coefficient=[ 10*fuselagedrag(),fuselagedrag(),wingdrag(),0.9*wingdrag(),0.9*wingdrag(),fuselagedrag(),0.6,1,0.077 ]
    landing_dragarea= [x*y for x,y in zip(landing_area_dragcomponents,landing_CD_coefficient)]
    print('\n   components                  \n')
    for m,n,o,p in zip(landing_drag_components,landing_area_dragcomponents,landing_CD_coefficient,landing_dragarea ):           
        print(m, n,o,p  ,sep='\t\t')
    sum_landing_dragarea=sum(landing_dragarea)
    landing_Cdo_others=sum_landing_dragarea/wing_area
    landing_interferencedrag=landing_Cdo_others*1.05
    print('The interfernce drag for landing condition is : ',landing_interferencedrag)
    
    print('for takeoff condition')
    takeoff_drag_components=['      canopy','       fuselage','        wing','vertical tail','horizontal tail','        engine','nose takeoff gear','main takeoff gear','  3/4th flap']
    takeoff_area_dragcomponents=[0.75*area_fuselage,area_fuselage,wing_area,area_VerticalTail,area_horizontalTail,area_powerplant_frontal,area_nosewheel,area_mainwheel,area_flap]
    takeoff_CD_coefficient=[ 10*fuselagedrag(),fuselagedrag(),wingdrag(),0.9*wingdrag(),0.9*wingdrag(),fuselagedrag(),0.6,1,0.051 ]
    takeoff_dragarea= [x*y for x,y in zip(takeoff_area_dragcomponents,takeoff_CD_coefficient)]
    print('\n   components                  \n')
    for m,n,o,p in zip(takeoff_drag_components,takeoff_area_dragcomponents,takeoff_CD_coefficient,takeoff_dragarea ):           
        print(m, n,o,p  ,sep='\t\t')
    sum_takeoff_dragarea=sum(takeoff_dragarea)
    takeoff_Cdo_others=sum_takeoff_dragarea/wing_area
    takeoff_interferencedrag=takeoff_Cdo_others*1.05
    print('The interfernce drag for takeoff condition is : ',takeoff_interferencedrag)
    
    
    print('DRAG POLAR')

    #Cd=Cdo+K*Cl**2
    #TAKEOFF : CD_TAKEOFF=takeoff_interferencedrag + K*CL**2)
    #CRUISE :CD_CRUISE=cruise_interferencedrag + K*CL**2)
    #LANDING :CD_LANDING=landing_interferencedrag + K*CL**2)

    CL_list=[]
    #print('drag polar for cruise')
    CD_CRUISE=[]
    for CL in range(-20,22,2):
       CD=cruise_interferencedrag + K*(CL/10)**2
       CD_CRUISE.append(CD)
       CL_list.append(CL/10)
    #print('drag polar for takeoff')
    CD_TAKEOFF=[]
    for CL in range(-20,22,2):
       CD=takeoff_interferencedrag + K*(CL/10)**2
       CD_TAKEOFF.append(CD)
    #print('drag polar for landing')
    CD_LANDING=[]
    for CL in range(-20,22,2):
       CD=landing_interferencedrag + K*(CL/10)**2
       CD_LANDING.append(CD)
       
    #graph for CL VS CD_TAKEOFF,CD_CRUISE,CD_LANDING

    #print(CL_list)
    #print(CD_LANDING)
    #print(CD_TAKEOFF)
    #print(CD_CRUISE)
    
    
    mp.plot(CD_TAKEOFF ,CL_list, label = "CD_TAKEOFF")
    mp.plot( CD_CRUISE,CL_list, label = "CD_CRUISE")
    mp.plot( CD_LANDING,CL_list, label = "CD_LANDING")
    mp.xlabel('CD')
    mp.ylabel('CL')
    mp.title('CL vs CD')
    mp.legend()
    mp.show()





'''
def performance_calculation():

    print('performance calculation')

    print('steady climb performance')
    #at sea level
    print('at sea level')
    result_atsealevel=temp_density_cal(0)
    speedofsound_atsealevel=result_atsealevel[2]
    density_atsealevel=result_atsealevel[3]
    
    mach_atsealevel=[]
    for CL in range(CL_list): 
        mach=((2*W_rtw/(wing_area*density_atsealevel*CL))**0.5)/speedofsound_atsealevel
        mach_atsealevel.append(mach)
    
    M
    CL
    CDT=kCL**2+(1/(1-M**2)**0.5)*Cdo_wing+cruise_Cdo_others
    D_drag=(CDT/CL)*W_rtw
    
    
    #at 3km altitude
    print('at 3km')
    result_at3km=temp_density_cal(3000)
    speedofsound_at3km=result_at3km[2]
    density_at3km=result_at3km[3]
    
    
    
    
    #at 6km altitude
    print('at 6km')
    result_at6km=temp_density_cal(6000)
    speedofsound_at6km=result_at6km[2]
    density_at6km=result_at6km[3]
    
    
    
    
    
    #at 9km altitude
    print('at 9km')
    result_at9km=temp_density_cal(9000)
    speedofsound_at9km=result_at9km[2]
    density_at9km=result_at9km[3]





    #at 12km altitude
    print('at 12km')
    result_at12km=temp_density_cal(12000)
    speedofsound_at12km=result_at12km[2]
    density_at12km=result_at12km[3]




    #at 14km altitude
    print('at 14km')
    result_at14km=temp_density_cal(14000)
    speedofsound_at14km=result_at14km[2]
    density_at14km=result_at14km[3]


    #rate of climb
    
    #at sea level
    V=M/330
    F=
    D_drag_atsealevel=
    R/C=(F-D_drag_atsealevel)*V*60*W_rtw
    
    
    
    
    
    
    #at 3km
    #at 6km
    #at 9km
    #at 12km
    #at 14km
    




    #graph for thrust(avaliable and required) Vs Velocity at each altitude
    #graph for power(avaliable and required) Vs Velocity at each altitude
    #graph for rate of climb Vs Velocity at each altitude
    #graph for rate of climb VS altitude
    print('absolute and servicing ceiling')

    print('estimation of range and endurance')

    endurance=(1/SFC)*(Cl/Cd)*loge(Wtotal/Wdry)
    range=endurance*Vcruise*3.6

    print('takeoff performance')

    StallingVelocity=LandingVelocity/1.15
    Clmaxreq=2*WL*9.81/(1.225*(StallingVelocity)**2)

    V_takeoff=stalling velocity*1.2
    Cl_takeoff=2*WL/(density at sealevel*V_takeoff)
    Cd_takeoff=Cdo_takeoff+K*Cl_takeoff**2
    D_takeoff=(Cd_takeoff*S*density at sea level * V_takeoff)/2

    Total thrust prodeuced by engine
    T_takeoff=

    angle of climb, sin(gammma) =(T_takeoff-D_takeoff)/W_total

    V_avg=0.7*V_takeoff
    L_avg=(Cl_takeoff*S*desnsity at sea level * V_avg**2)/2
    D_avg=(Cd_takeoff*S*desnsity at sea level * V_avg**2)/2
    S_groundroll=1.21*W_total**2/(g*densitysealevel*S*Cl_max*(T_takeoff-(D_takeoff-neu*r(W-L_avg)))) #assuming neu*r=0.02

    R_transistion=V_takeoff**2/(0.2*g)
    S_transistion=R_transistion*sin(gamma)
    H_transistion=R_transistion*(1-cos(gamma))
    S_climb=(H_obstacle-H_transition)/tan(gamma) #H_obstacle=15m
    S_takeoff=S_groundroll+S_transistion+S_climb

    print('landing performance')

    V_stall_approach=(2*W_landing/(densityatsealevel*S*Cl_max))**0.5
    V_approach=V_stall_approach*1.3
    Cd_landing=Cdo_landing*K*Cl_max**2
    V_avg=0.7*V_approach
    L_avg=(Cl_takeoff*S*desnsityatsealevel*V_avg**2)/2
    D_avg=(Cd_takeoff*S*desnsityatsealevel*V_avg**2)/2
    T_reverser=0.125*T_takeoff
    R_flare=V_approach**2/(0.2*g)
    S_flare=R_flare*sin(gamma_approach)
    H_flare=R_flare*(1-cos(gammma_approach))
    S_approach=(H_obstacle-Hflare)/tan(gamma_approach)
    S_ground_roll=1.69*W_landing**2/(g*densityatsealevel*S*Cl_max*(T_reverser+(D_avg+neu_brakes(W-0.1*L_avg))))  #gamma_approach=2.5 and neu_brakes=0.25

    print('turning performance')

    #maximum sustained turn rate  u,n,omega,R
    #sharpest sustained turn
    #maximum load factor turn
    Z=(T/W)*(Cl/Cd)max
    V_reference=240 m/s

    stability_control()

    def stability_control():
        print('analysis of stability and control of the aircraft')
        #longitudinal stick-fixed stability
    
  
   '''



loop=True
while loop==True:
    #os.system("cls")
    print("\n\n*******************************************************WELCOME TO AIRCRAFT DESIGN PROJECT**********************************************************\n\n")
    time.sleep(2)
    topicsinvolved()
    print("     Please Enter The Following Data To Start The Project\n")
    Total_crew=int(input("     1.please enter the total number of cabin crew(including pilots) :"))
    Total_payload=float(input("     2.please enter the payload (in kilograms): "))
    fuel_MTW_ratio=float(input("     3.please enter the (fuel/maximum takeoff weight) ratio : "))
    empty_MTW_ratio=float(input("     4.please enter the (empty weight/maximum takeoff weight) ratio : "))
    thrustloading_ratio=float(input("     5.please enter the thrust loading ratio : "))
    no_of_engines=int(input("     6.please enter the number of engines you prefer : "))
    radius_engine=float(input("     7.please enter the radius of engine frontal part : "))
    sfc_of_engine=float(input("     8.please enter the SFC of engine(in kg/kg-h) : "))
    key_Range=float(input("     9.please enter the key range(in kilometers) : "))
    Cruise_Velocity=float(input("     10.please enter the Crusie Velocity (in KM/HR) :"))
    Cruise_altitude=float(input("     11.please enter the crusie altitude(in Kilometers) : "))
    Wing_loading=float(input("     12.please enter the key wing loading(W/S)  : "))
    Aspect_ratio=float(input("     13.please enter the Aspect Ratio : "))
    BL_Ratio=float(input("     14.please enter the Wing Span/Fuselage (B/L) Ratio : "))
    Taper_ratio=float(input("     15.please enter the Taper ratio(assumed) : "))
    #DensityOfFuel=float(input("     15.please enter the density of Gasoline : "))
    Runway_Length=float(input("     16.Please enter the RunWay Length of Your Reference Airplane(in meters) : "))
    
    print("     \n\nThanks For Your Data Entry")
    
    
    DataChange=input("     \nDo You Want To Change Any Data You Entered (Y/N) : ")
    if DataChange=='y' or DataChange=='Y' :
        again=True
        while again==True:
            Rentry=int(input("      Please Enter The Serial.No You Want To Change : "))
            if Rentry==1 :  Toatal_crew=int(input("     1.please enter the total number of crew(including pilots) :"))
            elif Rentry==2 :Total_payload=float(input("     2.please enter the payload (in kilograms): "))
            elif Rentry==3 :fuel_MTW_ratio=float(input("     3.please enter the (fuel/maximum takeoff weight) ratio : "))
            elif Rentry==4 :empty_MTW_ratio=float(input("     4.please enter the (empty weight/maximum takeoff weight) ratio : "))
            elif Rentry==5 :thrustloading_ratio=float(input("     5.please enter the thrust loading ratio : "))
            elif Rentry==6 :no_of_engines=int(input("     6.please enter the number of engines you prefer : "))
            elif Rentry==7 :radius_engine=float(input("     7.please enter the radius of frontal part of engine(in meters) : "))
            elif Rentry==8 :sfc_of_engine=float(input("     8.please enter the SFC of engine(in kg/kg-h) : "))
            elif Rentry==9 :key_Range=float(input("     9.please enter the key range(in kilometers) : "))
            elif Rentry==10 :Cruise_Velocity=float(input("     10.please enter the Crusie Velocity (in KM/HR) :"))
            elif Rentry==11:Cruise_altitude=float(input("     11.please enter the crusie altitude(in Kilometers) : "))
            elif Rentry==12:Wing_loading=float(input("     12.please enter the key wing loading(W/S)  : "))
            elif Rentry==13:Aspect_ratio=float(input("     13.please enter the Aspect Ratio : "))
            elif Rentry==14:BL_Ratio=float(input("     14.please enter the Wing Span/Fuselage (B/L) Ratio : "))
            elif Rentry==15:Taper_ratio=float(input("     15.please enter the Taper ratio(assumed) : "))
            else :Runway_Length=float(input("     16.Please enter the RunWay Length of Your Reference Airplane : "))
        
            DataChange2=input("Do You Want To Change Any Other Data You Entered (Y/N) : ")
            if DataChange2=='n' or DataChange2=='N' :
                again=False
    print(("Continuing With The Data You Entered\n\n"))
    PrilimaryWeightEstimation()
    PowerPlantSelection()
    SecondWeightEstimation()
    KeyParameters()
    VolumeOfFuel()
    ThicknessToChordratio()
    CruiseLiftCoefficientCalucation()
    AOAcorrection()
    EstimationOfLandingVelocityAndStallingVelocity()
    emphanage()
    weightbreakage()
    CG_calculation()
    drag_estimation()
    










    result=input("Do you want to try one more(y/n) : ")
    if (result == 'n') or (result == 'N'):
        loop=False


'''

 #3d view
def threedimview():
    
    def draw(rad):
      for i in range(2):
        turtle.circle(rad,90)
        turtle.circle(rad//2,90)


    turtle.penup()  
    turtle.goto(-180,0) 
    turtle.pendown()
    turtle.left(90)
    turtle.forward(10)
    turtle.right(63)  
    turtle.forward(20)
    turtle.right(-15)  
    turtle.forward(20)
    turtle.right(42)
    turtle.forward(250)
    turtle.right(7)
    turtle.forward(30)
    turtle.right(83)
    turtle.forward(11)
    turtle.right(60)
    for i in range(50):
      turtle.forward(2)
      turtle.right(0.5)
      i=i+1
    turtle.right(5)  
    turtle.forward(160)  
    for i in range(33):
      turtle.forward(2)
      turtle.right(0.55)
      i=i+1  
    turtle.right(75) 
    for i  in range(9):
      turtle.forward(1.7)
      turtle.right(7)
      i=i+1
    #cock pit
    turtle.fillcolor("black")
    turtle.begin_fill()  
    turtle.penup()
    turtle.goto(-158,17)
    turtle.right(20)
    turtle.pendown()
    turtle.forward(13)
    turtle.left(85)
    turtle.forward(10)
    turtle.left(133)
    turtle.goto(-158,17)
    turtle.end_fill()
    #fuselage end
    turtle.penup()
    turtle.goto(133,28.5)
    turtle.pendown()
    turtle.right(-120)
    turtle.goto(140,26)
    turtle.goto(140,22)
    turtle.goto(133,18)
    #tyres
    turtle.penup()
    turtle.goto(10,-23)
    turtle.pendown()
    turtle.circle(5)
    turtle.goto(0,-23)
    turtle.circle(5)
    turtle.goto(-10,-23)
    turtle.circle(5)
    turtle.goto(-20,-23)
    turtle.circle(5)
    turtle.goto(20,-23)
    turtle.circle(5)
    turtle.penup()
    turtle.goto(-125,-23)
    turtle.pendown()
    turtle.circle(5)

    #runway line
    turtle.penup()
    turtle.goto(-200,-23)
    turtle.pendown()
    turtle.goto(300,-23)
    #door
    turtle.penup()
    turtle.goto(-100,13)
    turtle.pendown()
    turtle.goto(-100,-3)
    turtle.goto(-110,-3)
    turtle.goto(-110,13)
    turtle.goto(-100,13)
    #wing
    turtle.penup()
    turtle.goto(-80,32)
    turtle.pendown()
    turtle.goto(-10,0)
    turtle.goto(10,0)
    turtle.goto(-40,32)
    #engine
    turtle.penup()
    turtle.goto(-68,23)
    turtle.pendown()
    turtle.seth(-135)
    draw(9)
    turtle.penup()
    turtle.goto(-61,12)
    turtle.pendown()
    turtle.goto(-45,16)
    turtle.penup()
    turtle.goto(-45,13.5)
    turtle.pendown()
    turtle.seth(-135)
    draw(9)
    turtle.penup()
    turtle.goto(-39,2)
    turtle.pendown()
    turtle.goto(-28,7.5)

    # emphanage
    turtle.penup()
    turtle.goto(60,32)
    turtle.seth(0)
    turtle.pendown()
    turtle.goto(100,80)
    turtle.goto(120,80)
    turtle.goto(105,32)
    turtle.penup()
    turtle.seth(25)
    turtle.goto(60,22)
    turtle.pendown()
    for i in range (20):
      turtle.forward(2.5)
      turtle.right(2.5)
    turtle.right(130)  
    for i in range(20):
      turtle.forward(2.5)
      turtle.right(2.5)

    turtle.done()
'''
    
