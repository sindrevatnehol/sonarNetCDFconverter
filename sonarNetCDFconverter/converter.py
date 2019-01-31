# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:05:47 2019

@author: Administrator
"""


    
#import stuff
from netCDF4 import Dataset
import numpy as np
import pytz, pynmea2, datetime


def makeSonarNetCDF(ncfilename,FileData): 
    ''' makeSonarNetCDF function
    
    Author: Sindre Vatnehol
    Institution: Institute of Marine Research, Norway
    
    
    Description: 
        
    
    Usage: 
        
        
        
    Output: 
    
    '''
    
        
    
    
    
    
        
    def addGlobalAttributes(f)   : 
        '''fuction to set the global variables for the netcdf file'''
        #Set the time of creation to the .nc file
        filetime=pytz.timezone('Europe/Oslo').localize(datetime.datetime.utcnow())
        
        
        #Write creation of file
        f.Conventions = 'CF-1.7, SONAR-netCDF4-1.0, ACDD-1.3'
        
        
        #f._NCProperties = 'version=1|netcdflibversion=4.6.1|hdf5libversion=1.8.20'
        f.date_created = str(filetime).replace(' ','T')
        f.keywords = 'Simrad '
        f.license = 'None'
        f.rights = 'Unrestricted rights'
        f.sonar_convention_authority  = 'ICES'
        f.sonar_convention_name = 'SONAR-netCDF4'
        f.sonar_convention_version  = '1.0'
        f.summary = 'Converted files from .raw format'
        f.title = 'raw to nc converted files'
        
        
    
    
    
        
        
    def addAnnotation(fid): 
        '''Function to create annotation'''
        #Create group
        fid.createGroup('Annotation')
        
        
        #Create time dimension
        fid.groups['Annotation'].createDimension('time',None)
        
        
        #Create annotaiton txt
        annotationTxt = fid.groups['Annotation'].createVariable('annotation_text',str,('time',), chunksizes = (512,))
        annotationTxt.long_name = "Annotation text"
    
        #Create annotation category    
        annotationTxt = fid.groups['Annotation'].createVariable('annotation_category',str,('time',), chunksizes = (512,))
        annotationTxt.long_name = "Annotation category"
        
        
        #Make time into variable and add attributes
        time = fid.groups['Annotation'].createVariable('time',np.uint64,('time',), chunksizes = (512,))
        time.axis = 'T'
        time.calendar = 'gregorian'
        time.long_name = 'Timestamps of annotations'
        time.standard_name = 'time'
        time.units = 'nanoseconds since 1601-01-01 00:00:00Z'
        
        
        
        
        
        
        
        
    
    def addAnnotationData(fid,FileData): 
        ''' Instructions of how to add annotation information '''
        
        
        annotation_category = []
        annotation_text = []
        time = []
        
        
        
        #read the information
        for i in range(len(FileData.Annotation.annotation_time)): 
            annotation_category = np.hstack((annotation_category,FileData.Annotation.annotation_category[i]))
            annotation_text = np.hstack((annotation_text,FileData.Annotation.annotation_text[i]))
            time = np.hstack((time,FileData.Annotation.annotation_time[i]))
        
        
        
        #Write Environment information
        for i in range(len(time)): 
            fid.groups['Annotation'].variables['annotation_category'][i]=annotation_category[i]
            fid.groups['Annotation'].variables['annotation_text'][i]=annotation_text[i]
            fid.groups['Annotation'].variables['time'][i]=time[i]
            
        
        
        
        
        
        
        
        
    def addEnvironment(fid): 
        '''Function to create environment group'''
        fid.createGroup('Environment')
        
        #create dimension frequency
        fid.groups['Environment'].createDimension('frequency',None)
    
        
        #Create absorption indicative variable with attributes
        abso = fid.groups['Environment'].createVariable('absorption_indicative',np.float32,('frequency',), chunksizes = (512,))
        abso.long_name = 'Indicative acoustic absorption'
        abso.units = 'dB/m'
        abso.valid_min = 0.0
    
        
        #Create sound_speed_indicative variable with attributes
        snd = fid.groups['Environment'].createVariable('sound_speed_indicative',np.float32,('frequency',), chunksizes = (512,))
        snd.long_name = 'Indicative sound speed'
        snd.standard_name = 'speed_of_sound_in_sea_water'
        snd.units = 'm/s'
        snd.valid_min = 0.0
        
        
        #Create frequency variable with attributes
        freq = fid.groups['Environment'].createVariable('frequency',np.float32,('frequency',),chunksizes = (512,))
        freq.long_name = 'Acoustic frequency'
        freq.standard_name = 'sound_frequency'
        freq.units = 'Hz'
        freq.valid_min = 0.0
        
    
    
    
    
        
        
    def addEnvironmentData(FileData, fid): 
        #Protocol to add environment data to netcdf
        
        Frequency_index = []
        Absorption_index = []
        SoundVelocity_index = []
        
        
        for i in range(len(FileData.Environment.Frequency)): 
            Frequency_index = np.hstack((Frequency_index,FileData.Environment.Frequency[i]))
            Absorption_index = np.hstack((Absorption_index,FileData.Environment.Absorption[i]))
            SoundVelocity_index = np.hstack((SoundVelocity_index,FileData.Environment.SoundSpeed[i]))
        
        #Write Environment information
        
        for i in range(len(Frequency_index)): 
            fid.groups['Environment'].variables['frequency'][i]=Frequency_index[i]
            fid.groups['Environment'].variables['absorption_indicative'][i]=Absorption_index[i]
            fid.groups['Environment'].variables['sound_speed_indicative'][i]=SoundVelocity_index[i]
    
        
    
    
    
        
        
    def addPlatform(fid,platform_code, platform_name, platform_type,FileData): 
        '''Function to create the platform group'''
        
        
        def addDistanceTraveled(grp, index): 
            '''Add the distance traveled variable '''
            grp.createDimension('time'+str(index),None)
            
            distance = grp.createVariable('distance',np.float,('time'+str(index),), chunksizes = (512,))
            distance.long_name = "Distance travelled by the platform"
            distance.units = 'm'
            distance.valid_min = 0.0
            
            time = grp.createVariable('time'+str(index),np.uint64,('time'+str(index),), chunksizes = (512,))
            time.axis = 'T'
            time.calendar = 'gregorian'
            time.long_name = 'Timestamps for NMEA datagrams'
            time.standard_name = 'time'
            time.units = 'nanoseconds since 1601-01-01 00:00:00Z'
            
            
            
        def addHeading(grp,index,fid):
            grp.createDimension('time'+str(index),None)
            
            if not fid.Time == []: 
                time = grp.createVariable('time'+str(index),np.uint64,('time'+str(index),), chunksizes = (512,))
                time.axis = 'T'
                time.calendar = 'gregorian'
                time.long_name = 'Timestamps for NMEA datagrams'
                time.standard_name = 'time'
                time.units = 'nanoseconds since 1601-01-01 00:00:00Z'
            
            if not fid.Heading == []: 
                heading = grp.createVariable('heading',np.float,('time'+str(index),), chunksizes = (512,))
                heading.long_name = "Platform heading (true)"
                heading.standard_name = "platform_orientation"
                heading.units = "degrees_north"
                heading.valid_range = [0.0, 360.0]
            
            
            if not fid.Pitch == []: 
                pitch = grp.createVariable('pitch',np.float,('time'+str(index),), chunksizes = (512,))
                pitch.long_name = "Platform pitch"
                pitch.standard_name = "platform_pitch_angle"
                pitch.units = "arc_degree"
                pitch.valid_range = [-90.0, 90.0]
            
            
            if not fid.Roll == []:
                roll = grp.createVariable('roll',np.float,('time'+str(index),), chunksizes = (512,))
                roll.long_name = "Platform roll"
                roll.standard_name = "platform_roll_angle"
                roll.units = "arc_degree"
                roll.valid_range = [-180.0, 180.0]
            
            
            if not fid.SpeedRelative == []:
                speed_relative = grp.createVariable('speed_relative',np.float,('time'+str(index),), chunksizes = (512,))
                speed_relative.long_name = "Platform speed relative to water"
                speed_relative.standard_name = "platform_speed_wrt_seawater"
                speed_relative.units = "m/s"
                speed_relative.valid_min = 0.0
            
            
            if not fid.Heave == []:
                vertical_offset = grp.createVariable('vertical_offset',np.float,('time'+str(index),), chunksizes = (512,))
                vertical_offset.long_name = "Platform vertical offset from nominal"
                vertical_offset.units = "m"
            
        
        
        def addNMEAtelegrams(grp): 
                
            #Create a sub-group named NMEA wiht attributes
            grp.createGroup('NMEA')
            
            grp2 = grp.groups['NMEA']
            grp2.description = 'All NMEA sensor datagrams'
            fid.groups['Platform'].groups['NMEA'].createDimension('time',None)
            
            
            #Create variable in subgroup
            grp2.createVariable('NMEA_datagram',np.str,('time',), chunksizes = (512,))
            grp2.variables['NMEA_datagram'].long_name = 'NMEA datagram'
        
                
            #create time variable in subgroup
            time = grp2.createVariable('time',np.uint64,('time',), chunksizes = (512,))
            time.axis = 'T'
            time.calendar = 'gregorian'
            time.long_name = 'Timestamps for NMEA datagrams'
            time.standard_name = 'time'
            time.units = 'nanoseconds since 1601-01-01 00:00:00Z'
        
        
        def addGPS(grp,index): 
            
            grp.createDimension('time'+str(index),None)
            
            
            latitude = grp.createVariable('latitude',np.float,('time'+str(index),), chunksizes = (512,))
            latitude.long_name = "Platform latitude"
            latitude.standard_name = "latitude"
            latitude.units = "degrees_north"
            latitude.valid_range = [-90.0, 90.0]
            
            longitude = grp.createVariable('longitude',np.float,('time'+str(index),), chunksizes = (512,))
            longitude.long_name = "Platform longitude"
            longitude.standard_name = "longitude"
            longitude.units = "degrees_east"
            longitude.valid_range = [-180.0, 180.0]
            
            speed_ground = grp.createVariable('speed_ground',np.float,('time'+str(index),), chunksizes = (512,))
            speed_ground.long_name = "Platform speed over ground"
            speed_ground.standard_name = "platform_speed_wrt_ground"
            speed_ground.units = "m/s"
            speed_ground.valid_min = 0.0

            
        def otherMRUstuff(grp): 
            MRU_offset_x = grp.createVariable('MRU_offset_x',np.float, chunksizes = (512,))
            MRU_offset_x.long_name = "Distance along the x-axis from the platform coordinate system origin to the motion reference unit sensor origin"
            MRU_offset_x.units = "m"
            
            
            MRU_offset_y = grp.createVariable('MRU_offset_y',np.float, chunksizes = (512,))
            MRU_offset_y.long_name = "Distance along the y-axis from the platform coordinate system origin to the motion reference unit sensor origin"
            MRU_offset_y.units = "m"
            
            
            MRU_offset_z = grp.createVariable('MRU_offset_z',np.float, chunksizes = (512,))
            MRU_offset_z.long_name = "Distance along the z-axis from the platform coordinate system origin to the motion reference unit sensor origin"
            MRU_offset_z.units = "m"
            
            MRU_rotation_x = grp.createVariable('MRU_rotation_x',np.float, chunksizes = (512,))
            MRU_rotation_x.long_name = "Extrinsic rotation about the x-axis from the platform to MRU coordinate systems"
            MRU_rotation_x.units = "arc_degree"
            MRU_rotation_x.valid_range = [-180,180]
            
            MRU_rotation_y = grp.createVariable('MRU_rotation_y',np.float, chunksizes = (512,))
            MRU_rotation_y.long_name = "Extrinsic rotation about the y-axis from the platform to MRU coordinate systems"
            MRU_rotation_y.units = "arc_degree"
            MRU_rotation_y.valid_range = [-180,180]
            
            MRU_rotation_z = grp.createVariable('MRU_rotation_z',np.float, chunksizes = (512,))
            MRU_rotation_z.long_name = "Extrinsic rotation about the z-axis from the platform to MRU coordinate systems"
            MRU_rotation_z.units = "arc_degree"
            MRU_rotation_z.valid_range = [-180,180]
            
            position_offset_x = grp.createVariable('position_offset_x',np.float, chunksizes = (512,))
            position_offset_x.long_name = "Distance along the x-axis from the platform coordinate system origin to the latitude/longitude sensor origin"
            position_offset_x.units = "m"
            
            position_offset_y = grp.createVariable('position_offset_y',np.float, chunksizes = (512,))
            position_offset_y.long_name = "Distance along the y-axis from the platform coordinate system origin to the latitude/longitude sensor origin"
            position_offset_y.units = "m"
            
            position_offset_z = grp.createVariable('position_offset_z',np.float, chunksizes = (512,))
            position_offset_z.long_name = "Distance along the z-axis from the platform coordinate system origin to the latitude/longitude sensor origin"
            position_offset_z.units = "m"
            
            transducer_offset_x = grp.createVariable('transducer_offset_x',np.float, chunksizes = (512,))
            transducer_offset_x.long_name = "x-axis distance from the platform coordinate system origin to the sonar transducer"
            transducer_offset_x.units = "m"
            
            transducer_offset_y = grp.createVariable('transducer_offset_y',np.float, chunksizes = (512,))
            transducer_offset_y.long_name = "y-axis distance from the platform coordinate system origin to the sonar transducer"
            transducer_offset_y.units = "m"
            
            transducer_offset_z = grp.createVariable('transducer_offset_z',np.float, chunksizes = (512,))
            transducer_offset_z.long_name = "z-axis distance from the platform coordinate system origin to the sonar transducer"
            transducer_offset_z.units = "m"
            
            water_level = grp.createVariable('water_level',np.float, chunksizes = (512,))
            water_level.long_name = "Distance from the platform coordinate system origin to the nominal water level along the z-axis"
            water_level.units = "m"
            
            
            
        #make group
        fid.createGroup('Platform')
        
        
        
        #add group information
        grp = fid.groups['Platform']
        grp.platform_code_ICES = platform_code
        grp.platform_name = platform_name
        grp.platform_type = platform_type
        
        
        #FileData.MRU.Distance = 5
        
        if not FileData.MRU.Distance == {}: 
            addDistanceTraveled(fid.groups['Platform'],1)
            
            #addDistanceTraveledData(fid.groups)
        
        #addHeading(fid.groups['Platform'],2,FileData.MRU)
        
        addGPS(grp,3)
        
        addNMEAtelegrams(grp)
        
        otherMRUstuff(grp)
        
        #MRU stuff
        
        
        
    
        
    def addNMEA_data(fid,FileData): 
        for i in range(len(FileData.NMEA.Telegram)): 
            fid.variables['NMEA_datagram'][i]=FileData.NMEA.Telegram[i]
            fid.variables['time'][i]=FileData.NMEA.Time[i]
        fid.variables['test']=1
    





    #open new .nc file
    fid = Dataset(ncfilename,'w')

    
    
    
    #Add global variables
    addGlobalAttributes(fid) 



    

    try: 
        FileData.Annotation
        go_annotation = True
    except: 
        go_annotation = False
        print('No annotation info avaliable')
    if go_annotation == True: 
        
        #Create annotation level
        addAnnotation(fid)
        
        addAnnotationData(fid,FileData)
        
        
    
    if FileData.Environment.Frequency != []: 
        #create environment level
        addEnvironment(fid)
            
        #add information into the environment group
        addEnvironmentData(FileData, fid)
        
        
    '''Dummy data'''
    
    
    #define structure type
    class structtype(): 
        pass
    
    #FileData.MRU.Distance = [5]
    
    
    #create platform level
    addPlatform(fid,'platform_code', 'vessel_name', 'platform_type',FileData)
    
    addNMEA_data(fid.groups['Platform'].groups['NMEA'],FileData)
    
    #print('\n\nClosing netcdf file')
    #Close File
    fid.close()