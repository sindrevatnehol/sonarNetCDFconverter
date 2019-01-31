"""


@author: Sindre Vatnehol


Kommentar for meg selv: 
    
    Hver transduser er en Beam_group
    Hver kvadrant i transducer er en Beam


Trenger beskrivelse av strukturen av output som kan kalles opp ved hjelp


"""

#Load the needed stuff
import numpy as np
import xml.etree.ElementTree as ET
from lxml import etree



def readEK80(file): 
    
    
    ''' readEK80 function 
    
    This fuction reads an simrad ek80 file and outputs the information as a structure. 
    
    usage:  filedata = readEK80(file)
    
    input: file - the filename (along with path if needed)
    
    output: filedata - structured data that follows the structure of the ICES sonar-netcdf format. 
    see detailed description underneat
    
    
    
    #Data format information
    FileData.Copyright 
    FileData.ApplicationName
    FileData.Version
    FileData.FileFormatVersion
    FileData.TimeBias
    
    
    
    #Environment group
    filedata.Environment
    FileData.Environment.Frequency          - array
    FileData.Environment.Depth              - array
    FileData.Environment.Acidity            - array
    FileData.Environment.Salinity           - array
    FileData.Environment.SoundSpeed         - array
    FileData.Environment.Temperature        - array
    FileData.Environment.Absorption         - array
    
    
    
    #Tranceiver, transducer information
    FileData.Tranceiver[ii] = structtype()      'ii' indicate iterable structure for several tranceivers
    FileData.Tranceiver[ii].TransceiverName
    FileData.Tranceiver[ii].EthernetAddress
    FileData.Tranceiver[ii].IPAddress
    FileData.Tranceiver[ii].Version
    FileData.Tranceiver[ii].TransceiverSoftwareVersion
    FileData.Tranceiver[ii].TransceiverNumber
    FileData.Tranceiver[ii].MarketSegment
    FileData.Tranceiver[ii].TransceiverType
    FileData.Tranceiver[ii].SerialNumber
    FileData.Tranceiver[ii].ChannelID
    FileData.Tranceiver[ii].ChannelIdShort
    FileData.Tranceiver[ii].ChannelNumber
    FileData.Tranceiver[ii].MaxTxPowerTransceiver
    FileData.Tranceiver[ii].PulseLength                -array
    FileData.Tranceiver[ii].HWChannelConfiguration
    FileData.Tranceiver[ii].TransducerName
    FileData.Tranceiver[ii].SerialNumbe
    FileData.Tranceiver[ii].Frequency
    FileData.Tranceiver[ii].FrequencyMinimum 
    FileData.Tranceiver[ii].FrequencyMaximum
    FileData.Tranceiver[ii].BeamType 
    FileData.Tranceiver[ii].EquivalentBeamAngle
    FileData.Tranceiver[ii].Gain                      -array
    FileData.Tranceiver[ii].SaCorrection
    FileData.Tranceiver[ii].MaxTxPowerTransducer
    FileData.Tranceiver[ii].BeamWidthAlongship
    FileData.Tranceiver[ii].BeamWidthAthwartship
    FileData.Tranceiver[ii].AngleSensitivityAlongship
    FileData.Tranceiver[ii].AngleSensitivityAthwartship
    FileData.Tranceiver[ii].AngleOffsetAlongship
    FileData.Tranceiver[ii].AngleOffsetAthwartship
    FileData.Tranceiver[ii].DirectivityDropAt2XBeamWidth
    
    
    #NMEA information
    FileData.NMEA
    FileData.NMEA.Telegram
    FileData.NMEA.Time
    
    
    
    #Sample data
    FileData.BeamGroup[beam_group_idx].ChannelID        - name of channel, used to identifiy
    FileData.BeamGroup[beam_group_idx] = structtype()
    FileData.BeamGroup[beam_group_idx].ChannelID= ChannelID
    FileData.BeamGroup[beam_group_idx].ChannelMode=dict()
    FileData.BeamGroup[beam_group_idx].PulseForm=dict()
    FileData.BeamGroup[beam_group_idx].FrequencyStart=dict()
    FileData.BeamGroup[beam_group_idx].FrequencyEnd=dict()
    FileData.BeamGroup[beam_group_idx].BandWidth=dict()
    FileData.BeamGroup[beam_group_idx].PulseLength=dict()
    FileData.BeamGroup[beam_group_idx].SampleInterval=dict()
    FileData.BeamGroup[beam_group_idx].TransducerDepth=dict()
    FileData.BeamGroup[beam_group_idx].TransmitPower=dict()
    FileData.BeamGroup[beam_group_idx].Slope=dict()
    FileData.BeamGroup[beam_group_idx].time = dict()
    FileData.BeamGroup[beam_group_idx].backscatter_r= dict()
    FileData.BeamGroup[beam_group_idx].backscatter_i= dict()
    FileData.BeamGroup[beam_group_idx].BeamMode= dict()     - temporary to identify how the transducer is organised, i.e. single bean, quadrants
    
    
    
    #MRU data
    FileData.MRU = structtype()
    FileData.MRU.Heave = dict()
    FileData.MRU.Time = dict()
    FileData.MRU.Pitch = dict()
    FileData.MRU.Roll = dict()
    FileData.MRU.Heading = dict()
    
    '''




    
    def fread(fid, nelements, dtype):
        #Small fuction to help to read the bite data    
        
        if dtype is np.str:
            dt = np.uint8
        else: 
            dt = dtype 
        if (isinstance( nelements, int )== True)or (isinstance( nelements, np.int32 )== True):
            data_array = np.fromfile(fid, dt, nelements)
        else:
            try:  
                data_array = np.fromfile(fid, dt, nelements[0])
            except IndexError: 
                data_array = np.fromfile(fid,dt,nelements)
        return data_array; 
        
    
    
    def StringArray(variabel): 
        #Instruction of how to read string from bites
        output = "" 
        for variabels in variabel:
            output = output+chr(variabels)
        return output; 

    
    
    
    #define structure type
    class structtype(): 
        pass
    
    
    #Make FileOutput data to structype
    FileData = structtype() 
    
    
    #Make environment group
    FileData.Environment = structtype()
    FileData.Environment.Depth=np.array([])
    FileData.Environment.Acidity=np.array([])
    FileData.Environment.Salinity=np.array([])
    FileData.Environment.SoundSpeed=np.array([])
    FileData.Environment.Temperature=np.array([])
    FileData.Environment.Frequency = np.array([])
    FileData.Environment.Absorption = np.array([])
    
    
    #NMEa stuff
    FileData.NMEA = structtype
    FileData.NMEA.Telegram = dict()
    FileData.NMEA.Time = dict()
    

    #Transceiver information
    FileData.Tranceiver = dict()    
    
    
    #Sample data
    FileData.BeamGroup = dict()
    
    
    #MRU data
    FileData.MRU = structtype()
    FileData.MRU.Heave = dict()
    FileData.MRU.Time = dict()
    FileData.MRU.Pitch = dict()
    FileData.MRU.Roll = dict()
    FileData.MRU.Heading = dict()
    
    
    def doXML0datagram(fid,FileData): 
    
       #Load the xml data 
       XML_text = (StringArray(fread(fid,Length-12,np.int8)))


       #Parse the xml
       parser = etree.XMLParser(recover=True)
       root = ET.fromstring(XML_text, parser = parser)
       
       
       
       #There are several of xml information. 
       #Test each of them
       if root.tag == 'Configuration':
           for i in range(len(root)): 
               
               
               #Read header information
               if root[i].tag == 'Header': 
                   FileData.Copyright = root[i].attrib.get('Copyright')
                   FileData.ApplicationName=root[i].attrib.get('ApplicationName')
                   FileData.Version=root[i].attrib.get('Version')
                   FileData.FileFormatVersion=root[i].attrib.get('FileFormatVersion')
                   FileData.TimeBias=root[i].attrib.get('TimeBias')
                   
                   
               elif root[i].tag == 'Transceivers': 
                   
                   MergeOperation=root[i].attrib.get('MergeOperation')
                   
                   #My own test
                   if MergeOperation!='AddNodeTree': 
                       print('Check the xml info!!!')
                   
                    
                    #Get information of each tranceiver
                   for ii in range(len(root[i])): 
                       FileData.Tranceiver[ii] = structtype()
                       
                       FileData.Tranceiver[ii].TransceiverName=root[i][ii].attrib.get('TransceiverName')
                       FileData.Tranceiver[ii].EthernetAddress=root[i][ii].attrib.get('EthernetAddress')
                       FileData.Tranceiver[ii].IPAddress=root[i][ii].attrib.get('IPAddress')
                       FileData.Tranceiver[ii].Version=root[i][ii].attrib.get('Version')
                       FileData.Tranceiver[ii].TransceiverSoftwareVersion=root[i][ii].attrib.get('TransceiverSoftwareVersion')
                       FileData.Tranceiver[ii].TransceiverNumber=root[i][ii].attrib.get('TransceiverNumber')
                       FileData.Tranceiver[ii].MarketSegment=root[i][ii].attrib.get('MarketSegment') 
                       FileData.Tranceiver[ii].TransceiverType=root[i][ii].attrib.get('TransceiverType') 
                       FileData.Tranceiver[ii].SerialNumber=root[i][ii].attrib.get('SerialNumber')


                        #get information of each transducer (chanel) 
                       if len(root[i][ii]) != 1: 
                           print('Check the xml info!!!')
                           
                       
                        #Chennel attributes
                       FileData.Tranceiver[ii].ChannelID=root[i][ii][0][0].attrib.get('ChannelID')
                       FileData.Tranceiver[ii].ChannelIdShort=root[i][ii][0][0].attrib.get('ChannelIdShort')
                       FileData.Tranceiver[ii].ChannelNumber=root[i][ii][0][0].attrib.get('ChannelNumber')
                       FileData.Tranceiver[ii].MaxTxPowerTransceiver=root[i][ii][0][0].attrib.get('MaxTxPowerTransceiver')
                       FileData.Tranceiver[ii].PulseLength=np.array(root[i][ii][0][0].attrib.get('PulseLength').split(';')).astype(np.float)
                       FileData.Tranceiver[ii].HWChannelConfiguration=root[i][ii][0][0].attrib.get('HWChannelConfiguration')
                          
                       
                       #Write transducer information
                       FileData.Tranceiver[ii].TransducerName=root[i][ii][0][0][0].attrib.get('TransducerName') 
                       FileData.Tranceiver[ii].SerialNumber=root[i][ii][0][0][0].attrib.get('SerialNumber')  
                       FileData.Tranceiver[ii].Frequency=root[i][ii][0][0][0].attrib.get('Frequency') 
                       FileData.Tranceiver[ii].FrequencyMinimum=root[i][ii][0][0][0].attrib.get('FrequencyMinimum') 
                       FileData.Tranceiver[ii].FrequencyMaximum=root[i][ii][0][0][0].attrib.get('FrequencyMaximum') 
                       FileData.Tranceiver[ii].BeamType=root[i][ii][0][0][0].attrib.get('BeamType') 
                       FileData.Tranceiver[ii].EquivalentBeamAngle=root[i][ii][0][0][0].attrib.get('EquivalentBeamAngle')  
                       FileData.Tranceiver[ii].Gain=np.array(root[i][ii][0][0][0].attrib.get('Gain').split(';')).astype(np.float)
                       FileData.Tranceiver[ii].SaCorrection=np.array(root[i][ii][0][0][0].attrib.get('SaCorrection').split(';')).astype(np.float) 
                       FileData.Tranceiver[ii].MaxTxPowerTransducer=root[i][ii][0][0][0].attrib.get('MaxTxPowerTransducer')  
                       FileData.Tranceiver[ii].BeamWidthAlongship=root[i][ii][0][0][0].attrib.get('BeamWidthAlongship')  
                       FileData.Tranceiver[ii].BeamWidthAthwartship=root[i][ii][0][0][0].attrib.get('BeamWidthAthwartship') 
                       FileData.Tranceiver[ii].AngleSensitivityAlongship=root[i][ii][0][0][0].attrib.get('AngleSensitivityAlongship') 
                       FileData.Tranceiver[ii].AngleSensitivityAthwartship=root[i][ii][0][0][0].attrib.get('AngleSensitivityAthwartship') 
                       FileData.Tranceiver[ii].AngleOffsetAlongship=root[i][ii][0][0][0].attrib.get('AngleOffsetAlongship')  
                       FileData.Tranceiver[ii].AngleOffsetAthwartship=root[i][ii][0][0][0].attrib.get('AngleOffsetAthwartship')  
                       FileData.Tranceiver[ii].DirectivityDropAt2XBeamWidth=root[i][ii][0][0][0].attrib.get('DirectivityDropAt2XBeamWidth')  
                       


                       #Add WB frequency information  if avaliable
                       if len(root[i][ii][0][0][0])>0: 
                           FileData.Tranceiver[ii].WBT_info = structtype
                           for iii in range(len(root[i][ii][0][0][0])): 
                               
                               if iii ==0: 
                                   FileData.Tranceiver[ii].WBT_info.Frequency = np.zeros((len(root[i][ii][0][0][0])))
                                   FileData.Tranceiver[ii].WBT_info.Gain = np.zeros((len(root[i][ii][0][0][0])))
                                   FileData.Tranceiver[ii].WBT_info.Impedance = np.zeros((len(root[i][ii][0][0][0])))
                                   FileData.Tranceiver[ii].WBT_info.Phase = np.zeros((len(root[i][ii][0][0][0])))
                                   FileData.Tranceiver[ii].WBT_info.BeamWidthAlongship = np.zeros((len(root[i][ii][0][0][0])))
                                   FileData.Tranceiver[ii].WBT_info.BeamWidthAthwartship = np.zeros((len(root[i][ii][0][0][0])))
                                   FileData.Tranceiver[ii].WBT_info.AngleOffsetAlongship = np.zeros((len(root[i][ii][0][0][0])))
                                   FileData.Tranceiver[ii].WBT_info.AngleOffsetAthwartship = np.zeros((len(root[i][ii][0][0][0])))
                               
                               
                               FileData.Tranceiver[ii].WBT_info.Frequency[iii]= root[i][ii][0][0][0][iii].attrib.get('Frequency')
                               FileData.Tranceiver[ii].WBT_info.Gain[iii]= root[i][ii][0][0][0][iii].attrib.get('Gain')
                               FileData.Tranceiver[ii].WBT_info.Impedance[iii]= root[i][ii][0][0][0][iii].attrib.get('Impedance')
                               FileData.Tranceiver[ii].WBT_info.Phase[iii]= root[i][ii][0][0][0][iii].attrib.get('Phase')
                               FileData.Tranceiver[ii].WBT_info.BeamWidthAlongship[iii]= root[i][ii][0][0][0][iii].attrib.get('BeamWidthAlongship')
                               FileData.Tranceiver[ii].WBT_info.BeamWidthAthwartship[iii]= root[i][ii][0][0][0][iii].attrib.get('BeamWidthAthwartship')
                               FileData.Tranceiver[ii].WBT_info.AngleOffsetAlongship[iii]= root[i][ii][0][0][0][iii].attrib.get('AngleOffsetAlongship')
                               FileData.Tranceiver[ii].WBT_info.AngleOffsetAthwartship[iii]= root[i][ii][0][0][0][iii].attrib.get('AngleOffsetAthwartship')
               
                   
                   
               else: 
                   print('bad xml')
                   
                   
                   
       elif root.tag == 'Environment': 
           
           #Add depth
           if len(FileData.Environment.Depth)==0: 
               FileData.Environment.Depth =np.int(root.attrib.get('Depth'))
           else:  
               FileData.Environment.Depth = np.array((FileData.Environment.Depth,np.int(root.attrib.get('Depth'))))
           
           #Add Acidity
           if len(FileData.Environment.Acidity)==0: 
               FileData.Environment.Acidity =np.int(root.attrib.get('Acidity'))
           else:  
               FileData.Environment.Acidity = np.array((FileData.Environment.Acidity,np.int(root.attrib.get('Acidity'))))
           
           #Add Salinity
           if len(FileData.Environment.Salinity)==0: 
               FileData.Environment.Salinity =np.int(root.attrib.get('Salinity'))
           else:  
               FileData.Environment.Salinity = np.array((FileData.Environment.Salinity,np.int(root.attrib.get('Salinity'))))
           
           #Add SoundSpeed
           if len(FileData.Environment.SoundSpeed)==0: 
               FileData.Environment.SoundSpeed =np.int(root.attrib.get('SoundSpeed'))
           else:  
               FileData.Environment.SoundSpeed = np.array((FileData.Environment.SoundSpeed,np.int(root.attrib.get('SoundSpeed'))))
           
           #Add SoundSpeed
           if len(FileData.Environment.Temperature)==0: 
               FileData.Environment.Temperature =np.int(root.attrib.get('Temperature'))
           else:  
               FileData.Environment.Temperature = np.array((FileData.Environment.Temperature,np.int(root.attrib.get('Temperature'))))
               
           
           # msg for user
           for trans_i in range(len(root)): 
               if root[trans_i].tag == 'Transducer': 
                   TransducerName=root[trans_i].attrib.get('TransducerName')
                   SoundSpeed=root[trans_i].attrib.get('SoundSpeed')
                   if TransducerName !='Unknown':
                       print()
                       print('netcdf requiere information of absorption and frequency. \nThis has not been included for ek80 at this stage')
                       print('If you see this msg, inform script author with a copy of the raw file')
                       print()
                       
#                       #Add Frequency
#                       if len(FileData.Environment.Frequency)==0: 
#                           FileData.Environment.Frequency =np.nan
#                       else:  
#                           FileData.Environment.Frequency = np.array((FileData.Environment.Frequency,np.nan))
#                           
#                           
#                       #Add Absorption
#                       if len(FileData.Environment.Absorption)==0: 
#                           FileData.Environment.Absorption =np.nan
#                       else:  
#                           FileData.Environment.Absorption = np.array((FileData.Environment.Absorption,np.nan))
#               
#    
           
               else: 
                   print('Bad environment xml info')
               
            
            
            
       elif root.tag == 'Parameter': 
           #This telegram comes in front of the sample data
           
           
           if root[0].tag == 'Channel': 
#               FileData.BeamGroup[i]
               ChannelID=root[0].attrib.get('ChannelID')
               
               if len(FileData.BeamGroup) ==0: 
                   beam_group_idx = 0
                   FileData.BeamGroup[beam_group_idx] = structtype()
                   FileData.BeamGroup[beam_group_idx].ChannelID= ChannelID
                   FileData.BeamGroup[beam_group_idx].ChannelMode=dict()
                   FileData.BeamGroup[beam_group_idx].PulseForm=dict()
                   FileData.BeamGroup[beam_group_idx].FrequencyStart=dict()
                   FileData.BeamGroup[beam_group_idx].FrequencyEnd=dict()
                   FileData.BeamGroup[beam_group_idx].BandWidth=dict()
                   FileData.BeamGroup[beam_group_idx].PulseLength=dict()
                   FileData.BeamGroup[beam_group_idx].SampleInterval=dict()
                   FileData.BeamGroup[beam_group_idx].TransducerDepth=dict()
                   FileData.BeamGroup[beam_group_idx].TransmitPower=dict()
                   FileData.BeamGroup[beam_group_idx].Slope=dict()
                   FileData.BeamGroup[beam_group_idx].time = dict()
                   FileData.BeamGroup[beam_group_idx].backscatter_r= dict()
                   FileData.BeamGroup[beam_group_idx].backscatter_i= dict()
                   FileData.BeamGroup[beam_group_idx].BeamMode= dict()
               else: 
                   for beam_group_idx in range(len(FileData.BeamGroup)): 
                       if FileData.BeamGroup[beam_group_idx].ChannelID == ChannelID: 
                           break
                   if not FileData.BeamGroup[beam_group_idx].ChannelID == ChannelID: 
                       beam_group_idx = beam_group_idx+1
                       FileData.BeamGroup[beam_group_idx] = structtype()
                       FileData.BeamGroup[beam_group_idx].ChannelID= ChannelID
                       FileData.BeamGroup[beam_group_idx].ChannelMode=dict()
                       FileData.BeamGroup[beam_group_idx].PulseForm=dict()
                       FileData.BeamGroup[beam_group_idx].FrequencyStart=dict()
                       FileData.BeamGroup[beam_group_idx].FrequencyEnd=dict()
                       FileData.BeamGroup[beam_group_idx].BandWidth=dict()
                       FileData.BeamGroup[beam_group_idx].PulseLength=dict()
                       FileData.BeamGroup[beam_group_idx].SampleInterval=dict()
                       FileData.BeamGroup[beam_group_idx].TransducerDepth=dict()
                       FileData.BeamGroup[beam_group_idx].TransmitPower=dict()
                       FileData.BeamGroup[beam_group_idx].Slope=dict()
                       FileData.BeamGroup[beam_group_idx].time = dict()
                       FileData.BeamGroup[beam_group_idx].backscatter_r= dict()
                       FileData.BeamGroup[beam_group_idx].backscatter_i= dict()
                       FileData.BeamGroup[beam_group_idx].BeamMode= dict()
               
               
               FileData.BeamGroup[beam_group_idx].ChannelMode[len(FileData.BeamGroup[beam_group_idx].ChannelMode)]=np.int(root[0].attrib.get('ChannelMode') )
               FileData.BeamGroup[beam_group_idx].PulseForm[len(FileData.BeamGroup[beam_group_idx].PulseForm)]=np.int(root[0].attrib.get('PulseForm') )
               FileData.BeamGroup[beam_group_idx].FrequencyStart[len(FileData.BeamGroup[beam_group_idx].FrequencyStart)]=np.int(root[0].attrib.get('FrequencyStart'))
               FileData.BeamGroup[beam_group_idx].FrequencyEnd[len(FileData.BeamGroup[beam_group_idx].FrequencyEnd)]=np.int(root[0].attrib.get('FrequencyEnd') )
               FileData.BeamGroup[beam_group_idx].BandWidth[len(FileData.BeamGroup[beam_group_idx].BandWidth)]=np.float(root[0].attrib.get('BandWidth'))
               FileData.BeamGroup[beam_group_idx].PulseLength[len(FileData.BeamGroup[beam_group_idx].PulseLength)]=np.float(root[0].attrib.get('PulseLength'))
               FileData.BeamGroup[beam_group_idx].SampleInterval[len(FileData.BeamGroup[beam_group_idx].SampleInterval)]=np.float(root[0].attrib.get('SampleInterval'))
               FileData.BeamGroup[beam_group_idx].TransducerDepth[len(FileData.BeamGroup[beam_group_idx].TransducerDepth)]=np.int(root[0].attrib.get('TransducerDepth'))
               FileData.BeamGroup[beam_group_idx].TransmitPower[len(FileData.BeamGroup[beam_group_idx].TransmitPower)]=np.float(root[0].attrib.get('TransmitPower') )
               FileData.BeamGroup[beam_group_idx].Slope[len(FileData.BeamGroup[beam_group_idx].Slope)]=np.float(root[0].attrib.get('Slope') )
               
               
           else: 
               print('Bad parameter xml info')
           
           
       else: 
           print('bad xml root name')
       
#    return FileData
        
        
    def doFIL1datagram(fid): 
        
        
        #Stage = 1,  datagram contains the filter parameters from the transceiver, 
        #Stage = 2, datagram contains the filterparameters from the Processor Unit software.
        Stage = fread(fid,1,np.int16)
        
        #Spare for the simrad to be used
        Spare = fread(fid,2,np.int8)
        
        #Identify the transceiver
        ChannelID = StringArray(fread(fid,128,np.int8))
        
        #umber of coefficients, only internal use
        NoOfCoefficients = fread(fid,1,np.int16)
        
        #Decimation Factor
        DecimationFactor = fread(fid,1,np.int16)
        
        #
        Coefficients = fread(fid,2*NoOfCoefficients,np.float32)
        
        #rearranged coefficients according to description of the data formmat
        Real_coefficient = Coefficients[np.arange((NoOfCoefficients))]
        Imag_coefficient = Coefficients[np.arange((NoOfCoefficients))+1]
        
    
    
        output = {'Stage' : Stage[0], 
                  'ChanelID' : ChannelID,
                  'DecimationFactor':DecimationFactor, 
                  'Coefficients(real)': Real_coefficient,
                  'Coefficients(imag)':Imag_coefficient}
        

        #Returns stuff
        return(output)    
    
    
    
    
    
    
    #Open files
    fid = open(file)
    
    
    
    
    #loop through the file
    while(fid): 
        
        
        
        
        #Get the legnth of the datagram
        Length = (fread(fid,1,np.int32) )
        
        
        
        
        #Check if this is end of file
        try: 
            Length[0]
        except IndexError: 
            break
        
        
        
        #get datagram type
        datagramtype=StringArray(fread(fid,4,np.int8) )
        
        
        #get time information
        LowDateTime = fread(fid,1,np.int32)
        HighDateTime = fread(fid,1,np.int32)
        
        
        
        #Convert this to 100 nanoseconds since 1/1 1601. 
        #!!! This has not been confirmed
        time =  (HighDateTime*2**32 + LowDateTime)/10000
        time = time[0]
        #This time will be used as ping-time
        
        
        
        #Do stuff to the different datatypes
        if datagramtype == 'XML0': 
            
            #Description
            doXML0datagram(fid,FileData)
           
           
            
                    
        elif datagramtype == 'FIL1': 
            #Description: 
            #There are two filter datagrams for each channel. The first datagram contains the
            #filter parameters from the transceiver, while the second datagram contains the filter
            #parameters from the Processor Unit software.
            FIL1_output = doFIL1datagram(fid)
            
            
            
            
            
            #Legg inn: Coefficients_real = Coefficients[1,3,5,...] 
            #Coefficients_imag = COefficients[2,4,6,...]
        elif datagramtype == 'NME0': 
            NMEA = StringArray(fread(fid,Length-12,np.int8)).replace('\x00','')
            
            FileData.NMEA.Telegram[len(FileData.NMEA.Telegram)] = NMEA
            FileData.NMEA.Time[len(FileData.NMEA.Time)] = time
            


            
        elif datagramtype == 'RAW3': 
            #CHannel ID, This is also the transducer name
            ChannelID = (StringArray(fread(fid,128,np.int8))).replace('\x00','')
            
            
            for beam_group_idx in range(len(FileData.BeamGroup)): 
                if FileData.BeamGroup[beam_group_idx].ChannelID[0:22]== ChannelID:
                    break
                
            if not FileData.BeamGroup[beam_group_idx].ChannelID[0:22]== ChannelID:
                print('Error in finding beam group')
                break
            
            #Datatype
            Datatype = fread(fid,1,np.int16)
            
            #Spare for simrad stuff
            Spare = fread(fid,2,np.int8)
            
            #Offset information
            Offset = fread(fid,1,np.int32)
            
            
            #Count is the length of the sample
            Count = fread(fid,1,np.int32)
            
            
            FileData.BeamGroup[beam_group_idx].time[len(FileData.BeamGroup[beam_group_idx].time)] = np.float(time)
            
            #Go for the datatypes
            if Datatype[0] == 1032: 
                
                #Get the samples of the data
                Samples = fread(fid,4*2*Count,np.float32)
                
                
                #Rearrange the data
                #Description: 
                #There is four quadrants, each a with a complexed value
                #The sequence is like
                    
                    
                Real_values = np.column_stack((Samples[np.arange(Count)*8],
                                                       Samples[np.arange(Count)*8+2],
                                                       Samples[np.arange(Count)*8+4],
                                                       Samples[np.arange(Count)*8+6]))


                Imag_values = np.column_stack((Samples[np.arange(Count)*8+1],
                                                       Samples[np.arange(Count)*8+3],
                                                       Samples[np.arange(Count)*8+5],
                                                       Samples[np.arange(Count)*8+7]))
                    
                FileData.BeamGroup[beam_group_idx].backscatter_r[len(FileData.BeamGroup[beam_group_idx].backscatter_r)] = Real_values
                FileData.BeamGroup[beam_group_idx].backscatter_i[len(FileData.BeamGroup[beam_group_idx].backscatter_i)] = Imag_values
                FileData.BeamGroup[beam_group_idx].BeamMode[len(FileData.BeamGroup[beam_group_idx].BeamMode)] = 'Quadrants'
                
            else: 
                print('There is information in the RAW3 format that has not been implemented here')
                print('If this error msg is showing, please revisit the code or notify the script\'s author')
                break
                
                
                
        elif datagramtype == 'MRU0': 
            #Stucture the mru datagram
            FileData.MRU.Heave[len(FileData.MRU.Heave)] = np.float(fread(fid,1,np.float32))
            FileData.MRU.Time[len(FileData.MRU.Time)] = time
            FileData.MRU.Roll[len(FileData.MRU.Roll)] = np.float(fread(fid,1,np.float32))
            FileData.MRU.Pitch[len(FileData.MRU.Pitch)] = np.float(fread(fid,1,np.float32))
            FileData.MRU.Heading[len(FileData.MRU.Heading)] = np.float(fread(fid,1,np.float32))
            





        else: 
            break
    
        LengthStopp = (fread(fid,1,np.int32) )
        
    fid.close()    
    
    return(FileData)
    