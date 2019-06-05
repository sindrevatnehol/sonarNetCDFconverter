# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:05:47 2019

@author: Administrator
"""


    
#import stuff
from netCDF4 import Dataset
import numpy as np
import pytz, datetime






    
def addGlobalAttributes(f,sonartype, licens = False, rights = False): 
    ''' addGlobalAttributes
    
    A fuction to add iformation to the top-level group in the ICES sonar-netcdf
    data format. 
    
    '''
    
    
    #Write the versio of the netcdf and the sonar-netcdf
    f.Conventions = 'CF-1.7, SONAR-netCDF4-1.0, ACDD-1.3'
    
    #Write time created
    f.date_created = str(pytz.timezone('Europe/Oslo').localize(datetime.datetime.utcnow())).replace(' ','T')
    
    #Write the type of the sonar
    f.keywords = sonartype
    
    #Write licens if avaliable (this is optional)
    if not licens == False: 
        f.license = licens
        
    
    #Write rights if avaliable (this is optional)
    if not rights == False: 
        f.rights = rights #'Unrestricted rights'
        
    #write sonar-netcdf spesific information
    f.sonar_convention_authority  = 'ICES'
    f.sonar_convention_name = 'SONAR-netCDF4'
    f.sonar_convention_version  = '1.0'
    f.summary = 'Converted files from .raw format'
    f.title = 'raw to nc converted files'
    
    



    
    
def addAnnotation(fid): 
    '''
    addAnnotation
    
    Function to create annotation and add info'''
    
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
    '''
    addAnnotationData
    
    Instructions of how to add annotation information 
    '''
    
    
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
    '''
    Function to create environment group
    
    '''
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
    '''
    addEnvironmentData
    
    Add data to environment
    
    '''
    
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

    


def addDistanceTraveled(grp, index): 
    '''
    addDistanceTraveled
    
    Add the distance traveled variable 
    
    '''
    grp.createDimension('time'+str(index),None)
    
    distance = grp.createVariable('distance',np.float,('time'+str(index),), chunksizes = (512,))
    distance.long_name = "Distance travelled by the platform"
    distance.units = 'm'
    distance.valid_min = 0.0
    
    time = grp.createVariable('time'+str(index),np.uint64,('time'+str(index),), chunksizes = (512,))
    time.axis = 'T'
    time.calendar = 'gregorian'
    time.long_name = 'Timestamps for gyrocompass data'
    time.standard_name = 'time'
    time.units = 'nanoseconds since 1601-01-01 00:00:00Z'
    
    
    
    
def addVesselMotion(grp,index,fid):
    
    '''
    addVesselMotion
    
    Add information regarding vessel motion
    
    '''
    
    
    grp.createDimension('time'+str(index),None)
    
    if not fid.Time == {}: 
        time = grp.createVariable('time'+str(index),np.uint64,('time'+str(index),), chunksizes = (512,))
        time.axis = 'T'
        time.calendar = 'gregorian'
        time.long_name = 'Timestamps for gyrocompass data'
        time.standard_name = 'time'
        time.units = 'nanoseconds since 1601-01-01 00:00:00Z'
    
    if not fid.Heading == {}: 
        heading = grp.createVariable('heading',np.float,('time'+str(index),), chunksizes = (512,))
        heading.long_name = "Platform heading (true)"
        heading.standard_name = "platform_orientation"
        heading.units = "degrees_north"
        heading.valid_range = [0.0, 360.0]
    
    
    if not fid.Pitch == {}: 
        pitch = grp.createVariable('pitch',np.float,('time'+str(index),), chunksizes = (512,))
        pitch.long_name = "Platform pitch"
        pitch.standard_name = "platform_pitch_angle"
        pitch.units = "arc_degree"
        pitch.valid_range = [-90.0, 90.0]
    
    
    if not fid.Roll == {}:
        roll = grp.createVariable('roll',np.float,('time'+str(index),), chunksizes = (512,))
        roll.long_name = "Platform roll"
        roll.standard_name = "platform_roll_angle"
        roll.units = "arc_degree"
        roll.valid_range = [-180.0, 180.0]
    
    if not fid.SpeedRelative == {}:
        speed_relative = grp.createVariable('speed_relative',np.float,('time'+str(index),), chunksizes = (512,))
        speed_relative.long_name = "Platform speed relative to water"
        speed_relative.standard_name = "platform_speed_wrt_seawater"
        speed_relative.units = "m/s"
        speed_relative.valid_min = 0.0
    
    
    if not fid.Heave == {}:
        vertical_offset = grp.createVariable('vertical_offset',np.float,('time'+str(index),), chunksizes = (512,))
        vertical_offset.long_name = "Platform vertical offset from nominal"
        vertical_offset.units = "m"
    


def addNMEAtelegrams(grp,fid): 
        
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


def addGPS(grp,index, FileData): 
    
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
    
#            #create time variable in subgroup
    time = grp.createVariable('time'+str(index),np.uint64,('time'+str(index),), chunksizes = (512,))
    time.axis = 'T'
    time.calendar = 'gregorian'
    time.long_name = 'Timestamps for position data'
    time.standard_name = 'time'
    time.units = 'nanoseconds since 1601-01-01 00:00:00Z'
    
    
    for i in range(len(FileData.Platform.GPS.Latitude)): 
        grp.variables['latitude'][i] = FileData.Platform.GPS.Latitude[i]
        grp.variables['longitude'][i] = FileData.Platform.GPS.Longitude[i]
        grp.variables['time'+str(index)][i] = FileData.Platform.GPS.Time[i]
#            
#            speed_ground = grp.createVariable('speed_ground',np.float,('time'+str(index),), chunksizes = (512,))
#            speed_ground.long_name = "Platform speed over ground"
#            speed_ground.standard_name = "platform_speed_wrt_ground"
#            speed_ground.units = "m/s"
#            speed_ground.valid_min = 0.0

    
def otherMRUstuff(grp): 
#    grp.createDimension('MRUdim',1)
    
    MRU_offset_x = grp.createVariable('MRU_offset_x',np.float, chunksizes = (1,))
    MRU_offset_x.long_name = "Distance along the x-axis from the platform coordinate system origin to the motion reference unit sensor origin"
    MRU_offset_x.units = "m"

    
    MRU_offset_y = grp.createVariable('MRU_offset_y',np.float, chunksizes = (1,))
    MRU_offset_y.long_name = "Distance along the y-axis from the platform coordinate system origin to the motion reference unit sensor origin"
    MRU_offset_y.units = "m"
    
    
    MRU_offset_z = grp.createVariable('MRU_offset_z',np.float, chunksizes = (1,))
    MRU_offset_z.long_name = "Distance along the z-axis from the platform coordinate system origin to the motion reference unit sensor origin"
    MRU_offset_z.units = "m"
    
    MRU_rotation_x = grp.createVariable('MRU_rotation_x',np.float, chunksizes = (1,))
    MRU_rotation_x.long_name = "Extrinsic rotation about the x-axis from the platform to MRU coordinate systems"
    MRU_rotation_x.units = "arc_degree"
    MRU_rotation_x.valid_range = [-180,180]
    
    MRU_rotation_y = grp.createVariable('MRU_rotation_y',np.float, chunksizes = (1,))
    MRU_rotation_y.long_name = "Extrinsic rotation about the y-axis from the platform to MRU coordinate systems"
    MRU_rotation_y.units = "arc_degree"
    MRU_rotation_y.valid_range = [-180,180]
    
    MRU_rotation_z = grp.createVariable('MRU_rotation_z',np.float, chunksizes = (1,))
    MRU_rotation_z.long_name = "Extrinsic rotation about the z-axis from the platform to MRU coordinate systems"
    MRU_rotation_z.units = "arc_degree"
    MRU_rotation_z.valid_range = [-180,180]
    
    position_offset_x = grp.createVariable('position_offset_x',np.float, chunksizes = (1,))
    position_offset_x.long_name = "Distance along the x-axis from the platform coordinate system origin to the latitude/longitude sensor origin"
    position_offset_x.units = "m"
    
    position_offset_y = grp.createVariable('position_offset_y',np.float, chunksizes = (1,))
    position_offset_y.long_name = "Distance along the y-axis from the platform coordinate system origin to the latitude/longitude sensor origin"
    position_offset_y.units = "m"
    
    position_offset_z = grp.createVariable('position_offset_z',np.float, chunksizes = (1,))
    position_offset_z.long_name = "Distance along the z-axis from the platform coordinate system origin to the latitude/longitude sensor origin"
    position_offset_z.units = "m"
    
    transducer_offset_x = grp.createVariable('transducer_offset_x',np.float, chunksizes = (1,))
    transducer_offset_x.long_name = "x-axis distance from the platform coordinate system origin to the sonar transducer"
    transducer_offset_x.units = "m"
    
    transducer_offset_y = grp.createVariable('transducer_offset_y',np.float, chunksizes = (1,))
    transducer_offset_y.long_name = "y-axis distance from the platform coordinate system origin to the sonar transducer"
    transducer_offset_y.units = "m"
    
    transducer_offset_z = grp.createVariable('transducer_offset_z',np.float, chunksizes = (1,))
    transducer_offset_z.long_name = "z-axis distance from the platform coordinate system origin to the sonar transducer"
    transducer_offset_z.units = "m"
    
    water_level = grp.createVariable('water_level',np.float, chunksizes = (1,))
    water_level.long_name = "Distance from the platform coordinate system origin to the nominal water level along the z-axis"
    water_level.units = "m"
    
    
    
def addVesselMotionInfo(fid,data): 
    for i in range(len(data.Heading)): 
        fid.variables['heading'][i]= data.Heading[i]
    
    for i in range(len(data.Roll)): 
        fid.variables['roll'][i]= data.Roll[i]
    
    for i in range(len(data.Pitch)): 
        fid.variables['pitch'][i]= data.Pitch[i]
        
    for i in range(len(data.Heave)): 
        fid.variables['vertical_offset'] = data.Heave[i]
        
        


    
    
    
    
def addPlatform(fid,platform_code, platform_name, platform_type,FileData): 
    '''Function to create the platform group'''
    
    
    
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
    
    addVesselMotion(fid.groups['Platform'],2,FileData.MRU)
    
    addVesselMotionInfo(fid.groups['Platform'],FileData.MRU)
    
    if not FileData.Platform.GPS.Latitude==[]: 
        addGPS(grp,3,FileData)
    
    addNMEAtelegrams(grp,fid)
    
    otherMRUstuff(grp)
    
    #MRU stuff
    
    
    

    
def addNMEA_data(fid,FileData): 
    for i in range(len(FileData.NMEA.Telegram)): 
        fid.groups['NMEA'].variables['NMEA_datagram'][i]=FileData.NMEA.Telegram[i]
        fid.groups['NMEA'].variables['time'][i]=FileData.NMEA.Time[i]






def addProvenanceGroup(fid,FileData): 
    fid.createGroup('Provenance')
    
    fid.groups['Provenance'].conversion_software_name = 'sonarNetCDFconverter.py - python'
    fid.groups['Provenance'].conversion_software_version = 'v 1.0'
    fid.groups['Provenance'].conversion_time = str(pytz.timezone('Europe/Oslo').localize(datetime.datetime.utcnow())).replace(' ','T')
    
    fid.groups['Provenance'].createDimension('filenames',len(FileData.OriginalFileName))
    fid.groups['Provenance'].createVariable('source_filenames',str,('filenames',),chunksizes = (len(FileData.OriginalFileName),))


    fid.groups['Provenance'].variables['source_filenames'].long_name = 'Source filenames'


    for i in range(len(FileData.OriginalFileName)): 
        fid.groups['Provenance'].variables['source_filenames'][i] = FileData.OriginalFileName[i]

    



def addSonarGroup(fid,FileData): 
    fid.createGroup('Sonar')


    fid.groups['Sonar'].sonar_manufacturer = FileData.Copyright
    fid.groups['Sonar'].sonar_model = FileData.SounderName
    
    
    fid.groups['Sonar'].sonar_type = FileData.SonarType
    
    sonar = fid.groups['Sonar']
    
    enum_dict_stab = {u'not_stabilised': 0, u'stabilised': 1}
    beam_stabilisation_t=sonar.createEnumType(np.uint8,'beam_stabilisation_t',enum_dict_stab)
    
    enum_dict = {u'single': 0, u'split_aperture': 1}
    beam_t=sonar.createEnumType(np.uint8,'beam_t',enum_dict)
    
    enum_dict = {u'type_1': 1, u'type_2': 2}
    conversion_equation_t=sonar.createEnumType(np.uint8,'conversion_equation_t',enum_dict)
    
    sample_t = sonar.createVLType(np.float32,'sample_t')
    
    enum_dict = {u'CW': 0, u'LFM': 1,u'HFM' :2}
    transmit_t=sonar.createEnumType(np.uint8,'transmit_t',enum_dict)
    
    
    
    for i in range(len(FileData.BeamGroup)): 
        sonar.createGroup('Beam_group'+str(i+1))
        
        sgrp = sonar.groups['Beam_group'+str(i+1)]
        
        sgrp.createDimension('beam',FileData.BeamGroup[i].NumberOfBeams)
        sgrp.createDimension('ping_time',None)
        
        
        #Create beam dimension
        sgrp.createVariable('beam',str,('beam',),chunksizes = (FileData.BeamGroup[i].NumberOfBeams,))
        beam = sgrp.variables['beam']
        beam.long_name = 'Beam Name'
    
    
        #create time variation
        time = sgrp.createVariable('ping_time',np.uint64,('ping_time',),chunksizes = (512,))
        time.axis = 'T'
        time.calendar = 'gregorian'
        time.long_name = 'Timestamp of each ping'
        time.standard_name = 'time'
        time.units = 'nanoseconds since 1601-01-01 00:00:00Z'
    
        sgrp.createVariable('backscatter_i',sample_t,('ping_time','beam'))
        back = sgrp.variables['backscatter_i']
        back.long_name = 'Raw backscatter measurements (imaginary part)'
        back.units = 'VA'
    
        sgrp.createVariable('backscatter_r',sample_t,('ping_time','beam'))
        back = sgrp.variables['backscatter_r']
        back.long_name = 'Raw backscatter measurements (real part)'
        back.units = 'VA'
    
        sgrp.createVariable('beamwidth_receive_major',np.float32,('ping_time','beam'))
        back = sgrp.variables['beamwidth_receive_major']
        back.long_name = 'Half power one-way receive beam width along major (horizontal) axis of beam'
        back.units='arc_degree'
        back.valid_range = np.array((0.0,360.0))
    
        sgrp.createVariable('beamwidth_receive_minor',np.float32,('ping_time','beam'))
        back = sgrp.variables['beamwidth_receive_minor']
        back.long_name = 'Half power one-way receive beam width along minor (vertical) axis of beam'
        back.units='arc_degree'
        back.valid_range = np.array((0.0,360.0))
        
        sgrp.createVariable('beamwidth_transmit_major',np.float32,('ping_time','beam'))
        back = sgrp.variables['beamwidth_transmit_major']
        back.long_name = 'Half power one-way transmit beam width along major (horizontal) axis of beam'
        back.units='arc_degree'
        back.valid_range = np.array((0.0,360.0))
    
        sgrp.createVariable('beamwidth_transmit_minor',np.float32,('ping_time','beam'))
        back = sgrp.variables['beamwidth_transmit_minor']
        back.long_name = 'Half power one-way transmit beam width along minor (vertical) axis of beam'
        back.units='arc_degree'
        back.valid_range = np.array((0.0,360.0))
        
        sgrp.createVariable('beam_direction_x',np.float32,('ping_time','beam'))
        back = sgrp.variables['beam_direction_x']
        back.long_name = 'x-component of the vector that gives the pointing direction of the beam, in sonar beam coordinate system'
        back.units = '1'
        back.valid_range = np.array((-1.0,1.0))
        
        sgrp.createVariable('beam_direction_y',np.float32,('ping_time','beam'))
        back = sgrp.variables['beam_direction_y']
        back.long_name = 'y-component of the vector that gives the pointing direction of the beam, in sonar beam coordinate system'
        back.units = '1'
        back.valid_range = np.array((-1.0,1.0))
    
        sgrp.createVariable('beam_direction_z',np.float32,('ping_time','beam'))
        back = sgrp.variables['beam_direction_z']
        back.long_name = 'z-component of the vector that gives the pointing direction of the beam, in sonar beam coordinate system'
        back.units = '1'
        back.valid_range = np.array((-1.0,1.0))
    
        sgrp.createVariable('beam_stabilisation',beam_stabilisation_t,('ping_time',),chunksizes = (512,))
        back = sgrp.variables['beam_stabilisation']
        back.long_name = 'Beam stabilisation applied (or not)'
    
        sgrp.createVariable('beam_type',beam_t,('ping_time',),chunksizes = (512,))
        back = sgrp.variables['beam_stabilisation']
        back.long_name = 'Type of beam'
          
        sgrp.createVariable('equivalent_beam_angle',np.float32,('ping_time','beam'))
        back = sgrp.variables['equivalent_beam_angle']
        back.long_name = 'Equivalent beam angle'
        back.units='sr'
        back.valid_range = np.array((0.0,12.56637061435917295385))
    
        sgrp.createVariable('gain_correction',np.float32,('ping_time','beam'))
        back = sgrp.variables['gain_correction']
        back.long_name = 'Gain correction'
        back.units='dB'
    
        sgrp.createVariable('non_quantitative_processing',np.int16,('ping_time',),chunksizes = (512,))
        back = sgrp.variables['non_quantitative_processing']
        back.flag_meanings = 'no_non_quantitative_processing simrad_weak_noise_filter simrad_medium_noise_filter simrad_strong_noise_filter'
        back.flag_values = '0, 1, 2, 3'
        back.long_name = 'Presence or not of non-quantitative processing applied to the backscattering data (sonar specific)'
    
        sgrp.createVariable('receiver_sensitivity',np.float32,('ping_time','beam'))
        back = sgrp.variables['receiver_sensitivity']
        back.long_name = 'Receiver sensitivity'
        back.units = 'dB re 1/uPa'

        sgrp.createVariable('sample_interval',np.float32,('ping_time',),chunksizes = (512,))
        back = sgrp.variables['sample_interval']
        back.long_name = ' Interval between recorded raw data samples'
        back.units = 's'
        back.valid_min = '0.0'
    
        sgrp.createVariable('sample_time_offset',np.float32,('ping_time',),chunksizes = (512,))
        back = sgrp.variables['sample_time_offset']
        back.long_name = 'Time offset that is subtracted from the timestamp of each sample'
        back.units = 's'
    
        sgrp.createVariable('time_varied_gain',sample_t,('ping_time',),chunksizes = (512,))
        back = sgrp.variables['time_varied_gain']
        back.long_name = 'Time-varied-gain coefficients'
        back.units = 'dB'
    
        sgrp.createVariable('transducer_gain',np.float32,('ping_time','beam'))
        back = sgrp.variables['transducer_gain']
        back.long_name = 'Gain of transducer'
        back.units = 'dB'
    
        sgrp.createVariable('transmit_bandwidth',np.float32,('ping_time'),chunksizes = (512,))
        back = sgrp.variables['transmit_bandwidth']
        back.long_name = 'Nominal bandwidth of transmitted pulse'
        back.units = 'Hz'
        back.valid_min = '0.0'
    
        sgrp.createVariable('transmit_duration_equivalent',np.float32,('ping_time'),chunksizes = (512,))
        back = sgrp.variables['transmit_duration_equivalent']
        back.long_name = 'Equivalent duration of transmitted pulse'
        back.units = 's'
        back.valid_min = '0.0'
    
        sgrp.createVariable('transmit_duration_nominal',np.float32,('ping_time'),chunksizes = (512,))
        back = sgrp.variables['transmit_duration_nominal']
        back.long_name = 'Nominal duration of transmitted pulse'
        back.units = 's'
        back.valid_min = '0.0'
    
        sgrp.createVariable('transmit_frequency_start',np.float32,('ping_time'),chunksizes = (512,))
        back = sgrp.variables['transmit_frequency_start']
        back.long_name = ' Start frequency in transmitted pulse'
        back.standard_name = 'sound_frequency'
        back.units = 'Hz'
        back.valid_min = '0.0'
    
        sgrp.createVariable('transmit_frequency_stop',np.float32,('ping_time'),chunksizes = (512,))
        back = sgrp.variables['transmit_frequency_stop']
        back.long_name = 'Stop frequency in transmitted pulse'
        back.standard_name = 'sound_frequency'
        back.units = 'Hz'
        back.valid_min = '0.0'
    
        sgrp.createVariable('transmit_power',np.float32,('ping_time'),chunksizes = (512,))
        back = sgrp.variables['transmit_power']
        back.long_name = 'Nominal transmit power'
        back.units = 'W'
        back.valid_min = '0.0'
    
        sgrp.createVariable('transmit_source_level',np.float32,('ping_time'),chunksizes = (512,))
        back = sgrp.variables['transmit_source_level']
        back.long_name = 'Transmit source level'
        back.units = 'dB re 1 uPa at 1m'
    
        sgrp.createVariable('transmit_type',transmit_t,('ping_time'),chunksizes = (512,))
        back = sgrp.variables['transmit_type']
        back.long_name = 'Type of transmitted pulse'

        sgrp.conversion_equation_type = FileData.SonarConversionEquation 
        
        sgrp.beam_mode = FileData.BeamGroup[i].beam_mode
        
    
        
        
def addSonarGroupData(fid,FileData): 
    
    for i in range(len(FileData.BeamGroup)):
        
        for ii in range(len(FileData.BeamGroup[i].TransmitPower)): 
            fid.groups['Sonar'].groups['Beam_group'+str(i)].variables['transmit_power'][ii] = FileData.BeamGroup[i].TransmitPower[ii]
    



def makeSonarNetCDF(ncfilename,FileData,sonartype): 
    ''' makeSonarNetCDF function
    
    Author: Sindre Vatnehol
    Institution: Institute of Marine Research, Norway
    
    
    Description: 
        
    
    Usage: 
        
        
        
    Output: 
    
    '''
    
        
    
    



    #open new .nc file
    fid = Dataset(ncfilename,'w')

    
    
    
    #Add global variables
    addGlobalAttributes(fid,sonartype=sonartype) 



    
    #Protocol to add annotation
    try: 
        FileData.Annotation
        go_annotation = True
    except: 
        go_annotation = False
    if go_annotation == True: 
        addAnnotation(fid)
        addAnnotationData(fid,FileData)
        
        
    
    #Protocol to add environment
    if FileData.Environment.Frequency != []: 
        addEnvironment(fid)
        addEnvironmentData(FileData, fid)
        
    
    
    #define structure type
    class structtype(): 
        pass
    
    
    
    
    #create platform level
    addPlatform(fid,'platform_code', 'vessel_name', 'platform_type',FileData)
    
    
    addNMEA_data(fid.groups['Platform'],FileData)
    
    
    addProvenanceGroup(fid,FileData)
    
    
    addSonarGroup(fid,FileData)
    
    addSonarGroupData(fid,FileData)
    
    
    fid.close()