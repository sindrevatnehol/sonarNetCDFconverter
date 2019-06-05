

#import stuff
from netCDF4 import Dataset
import dateutil.parser
import numpy as np





    
class mandotory_information(object):
    '''
    Defines the folder structure used in the project.
    the PySonar
    '''
    def __init__(self):
        self.Conventions = 'CF-1.7, SONAR-netCDF4-1.0, ACDD-1.3'
        self.date_created = 'YYYY-MM-DDThh:mm:ssZ'
        self.sonar_convention_authority = 'ICES'
        self.sonar_convention_name = "SONAR-netCDF4"




def TopLevel_test(fid): 
    '''
    TopLevel_test
    
    Test if the top level information is according to the definition
    
    '''
    
    #Grab any manditory info
    info = mandotory_information()
    
    
    #Test if the conventio info is avaliable
    try:
        fid.Conventions
        if not fid.Conventions==info.Conventions: 
            print('    ErrorMsg: fid.Conventions has wrong format name'+'\n')
            print('               :'+fid.Conventions)
            print('               :'+info.Conventions+'\n')
    except: 
        print('    ErrorMsg. fid.Conventions do not exist'+'\n')
    
        
    #Test if the time created is avaliable and in the right format   
    try:
        fid.date_created
        try: 
            dateutil.parser.parse(fid.date_created)
        except: 
            print('    ErrorMsg: fid.date_created has wrong format'+'\n')
    except: 
        print('    ErrorMsg: fid.date_created do not exist'+'\n')
    
    
    #Test if the keywords are avaliable
    try:
        fid.keywords
    except: 
        print('    ErrorMsg: fid.keywords do not exist'+'\n')
    
    
    #test the information of the convention authority
    try:
        fid.sonar_convention_authority
        if not fid.sonar_convention_authority == info.sonar_convention_authority: 
            print('    ErrorMsg: fid.sonar_convention_authority has wrong info'+'\n')
    except: 
        print('    ErrorMsg: fid.sonar_convention_authority do not exist'+'\n')
    
    
    #test the information of the convention name
    try:
        fid.sonar_convention_name
        if not fid.sonar_convention_name == info.sonar_convention_name: 
            print('    ErrorMsg: fid.sonar_convention_name has wrong info'+'\n')
    except: 
        print('    ErrorMsg: fid.sonar_convention_name do not exist'+'\n')
    
    
    #Test the license info
    try:
        fid.license
    except: 
        print('    WarningMsg: fid.license do not exist'+'\n')
    
    
    #Test the rights info
    try:
        fid.rights
    except: 
        print('    WarningMsg: fid.rights do not exist'+'\n')
    
    
    #Test the convention version
    try:
        fid.sonar_convention_version
        try: 
            if not isinstance(fid.sonar_convention_version, str): 
                print('    ErrorMsg: fid.sonar_convention_version has wrong format'+'\n')
        except: 
            print('    ErrorMsg: fid.sonar_convention_version info is wrong'+'\n')
    except: 
        print('    ErrorMsg: fid.sonar_convention_version do not exist'+'\n')
    
    
    #test the summary info
    try:
        fid.summary
    except: 
        print('    ErrorMsg: fid.summary do not exist'+'\n')
    
    
    #test the tidle ifo
    try:
        fid.title
    except: 
        print('    ErrorMsg: fid.title do not exist'+'\n')
        





def annotation_group_test(fid): 
    '''
    annotation_group_test
    
    Test of the annotation info
    '''
    
    
    #Check if dimesions are ok        
    try: 
        if not len(fid.dimensions)>=1: 
            print('    ErrorMsg: dataset.groups[\'Annotation\'].dimension has wrong dimension'+'\n')
    except: 
        print('    ErrorMsg:dataset.groups[\'Annotation\'].dimension do not exist'+'\n')
    
    
    
    
    #Check if all variables are there
    try: 
        fid.variables['time']
        do_time = True
    except: 
        do_time = False
        print('    ErrorMsg: dataset.groups[\'Annotation\'].variables[\'time\'] dont exist'+'\n')
    try: 
        do_text = True
        fid.variables['annotation_text']
    except: 
        do_text = False
        print('    ErrorMsg: dataset.groups[\'Annotation\'].variables[\'annotation_text\'] dont exist'+'\n')
    try: 
        do_annotgrp = True
    except: 
        print('    WarningMsg: dataset.groups[\'Annotation\'].variables[\'annotation_category\'] dont exist'+'\n')
        do_annotgrp = False
    
    
    
    if do_time == True: 
        if not len(fid.variables['time'].dimensions) == len(fid.dimensions): 
            print('    ErrorMsg: dataset.groups[\'Annotation\'].variables[\'time\'] has wrong dimension'+'\n')
        if not (fid.variables['time'].axis) == 'T':
            print('    ErrorMsg: dataset.groups[\'Annotation\'].variables[\'time\'].axis has wrong info'+'\n')
        if not (fid.variables['time'].calendar) == 'gregorian':
            print('    ErrorMsg: dataset.groups[\'Annotation\'].variables[\'time\'].calendar has wrong info'+'\n')
        if not (fid.variables['time'].long_name) == 'Timestamps of annotations':
            print('    ErrorMsg: dataset.groups[\'Annotation\'].variables[\'time\'].long_name has wrong info'+'\n')
        if not (fid.variables['time'].standard_name) == 'time':
            print('    ErrorMsg: dataset.groups[\'Annotation\'].variables[\'time\'].standard_name has wrong info'+'\n')
        if not (fid.variables['time'].units) == 'nanoseconds since 1601-01-01 00:00:00Z':
            print('    ErrorMsg: dataset.groups[\'Annotation\'].variables[\'time\'].units has wrong info'+'\n')
        
    
    
    
    if do_text == True: 
        if not len(fid.variables['annotation_text'].dimensions) == len(fid.dimensions): 
            print('    ErrorMsg: dataset.groups[\'Annotation\'].variables[\'annotation_text\'] has wrong dimension'+'\n')
        if not (fid.variables['annotation_text'].long_name) == "Annotation text":
            print('    ErrorMsg: dataset.groups[\'Annotation\'].variables[\'annotation_text\'].long_name has wrong info'+'\n')
        
    

    if do_annotgrp ==True: 
        if not len(fid.variables['annotation_category'].dimensions) == len(fid.dimensions): 
            print('    ErrorMsg: dataset.groups[\'Annotation\'].variables[\'annotation_category\'] has wrong dimension'+'\n')
         
        if not (fid.variables['annotation_category'].long_name) == "Annotation category":
            print('    ErrorMsg: dataset.groups[\'Annotation\'].variables[\'annotation_category\'].long_name has wrong info'+'\n')
        
    


def environment_group_test(fid): 

    #Check if dimesions are ok        
    try: 
        if not len(fid.dimensions)>=1: 
            print('    ErrorMsg: dataset.groups[\'Environment\'].dimension has wrong dimension'+'\n')
    except: 
        print('    ErrorMsg: dataset.groups[\'Environment\'].dimension do not exist'+'\n')
    
    
    
    #Test of dimesion name
    if not fid.variables['frequency'].dimensions[0] == 'frequency': 
        print('    ErrorMsg: dataset.groups[\'Environment\'].dimension has wrong dimension name'+'\n')


    
    #test if all variables exist        
    try: 
        fid.variables['frequency']
        do_frequecy = True
    except: 
        do_frequecy = False
        print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'Frequency\'] do not exist'+'\n')
    try: 
        fid.variables['sound_speed_indicative']
        do_soundspeed = True
    except: 
        do_soundspeed = False
        print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'sound_speed_indicative\'] do not exist'+'\n')
    try: 
        fid.variables['absorption_indicative']
        do_abs = True
    except: 
        do_abs = False
        print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'absorption_indicative\'] do not exist'+'\n')
    


    #test frequency variable
    if do_frequecy == True: 
        if not len(fid.variables['frequency'].dimensions) == len(fid.dimensions): 
            print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'frequency\'] has wrong dimension'+'\n')
        if not fid.variables['frequency'].long_name == 'Acoustic frequency': 
            print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'frequency\'].long_name has wrong info'+'\n')
        if not fid.variables['frequency'].units == 'Hz': 
            print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'frequency\'].units has wrong info'+'\n')

        if not fid.variables['frequency'].standard_name == 'sound_frequency': 
            print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'frequency\'].units has wrong info'+'\n')

            
    if do_soundspeed == True: 
        if not len(fid.variables['sound_speed_indicative'].dimensions) == len(fid.dimensions): 
            print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'sound_speed_indicative\'] has wrong dimension')
        if not fid.variables['sound_speed_indicative'].standard_name == 'speed_of_sound_in_sea_water': 
            print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'sound_speed_indicative\'].standard_name has wrong info'+'\n')
        if not fid.variables['sound_speed_indicative'].long_name == 'Indicative sound speed': 
            print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'sound_speed_indicative\'].long_name has wrong info'+'\n')
        if not fid.variables['sound_speed_indicative'].units == 'm/s': 
            print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'sound_speed_indicative\'].units has wrong info'+'\n')

            
    if do_abs == True: 
        if not len(fid.variables['absorption_indicative'].dimensions) == len(fid.dimensions): 
            print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'absorption_indicative\'] has wrong dimension'+'\n')
        if not fid.variables['absorption_indicative'].long_name == 'Indicative acoustic absorption': 
            print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'absorption_indicative\'].long_name has wrong info'+'\n')
        if not fid.variables['absorption_indicative'].units == 'dB/m': 
            print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'absorption_indicative\'].units has wrong info'+'\n')

        
            
        
        
def platform_group_test(fid): 


    #Test if attributes of the grupe are avaliable        
    try: 
        fid.platform_code_ICES
    except: 
        print('    - WarningMsg: dataset.groups[\'Platform\'].variables[\'platform_code_ICES\'] dont exist'+'\n')
    
    try: 
        fid.platform_name
    except: 
        print('    - Warning msg: dataset.groups[\'Platform\'].variables[\'platform_name\'] dont exist'+'\n')
        
    try: 
        fid.platform_type
    except: 
        print('    - Warning msg: dataset.groups[\'Platform\'].variables[\'platform_type\'] dont exist'+'\n')
        
        
        
    #check of dimensions and time is correct
    for dim in fid.dimensions: 
        if not dim[:4] == 'time': 
            print('    - ErrorMsg, dataset.groups[\'Platform\'].dimension name not valid'+'\n')
        else: 
            if not (fid.variables[dim].axis) == 'T':
                print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'time\'].axis has wrong info'+'\n')
            if not (fid.variables[dim].calendar) == 'gregorian':
                print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'time\'].calendar has wrong info'+'\n')
            if not (fid.variables[dim].long_name) == 'Timestamps of position data':
                print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'time\'].long_name has wrong info'+'\n')
            if not (fid.variables[dim].standard_name) == 'time':
                print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'time\'].standard_name has wrong info'+'\n')
            if not (fid.variables[dim].units) == 'nanoseconds since 1601-01-01 00:00:00Z':
                print('    ErrorMsg: dataset.groups[\'Annotation\'].variables[\'time\'].units has wrong info'+'\n')
            
        
        
        
    #Check distance variable
    #This one has been finished
    try: 
        fid.variables['distance']
        do_distance = True
    except: 
        print('    WarningMsg: dataset.groups[\'Platform\'].variables[\'distance\'] do not exist\n')
        do_distance=False
        
    if do_distance == True: 
        if not fid.variables['distance'].long_name == 'Distance travelled by the platform': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'distance\'] innvalid long name\n')
        if not fid.variables['distance'].units == 'm': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'distance\']  innvalid unit\n')
        if not fid.variables['distance'].valid_min == 0: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'distance\']  not valid valid min\n')
        if not (len(fid.dimensions[fid.variables['distance'].dimensions[0]])==len(fid.variables['distance'])): 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'distance\']inconsistent dimension length\n')
      
            
            
            
    #Test for the heading information
    #This one has been finnished
    try: 
        fid.variables['heading']
        do_heading = True
    except: 
        print('    WarningMsg: dataset.groups[\'Platform\'].variables[\'heading\'] do not exist\n')
        do_heading=False
    if do_heading == True: 
        if not fid.variables['heading'].long_name == 'Platform heading (true)': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'heading\'] wrong heading long name\n')
        if not fid.variables['heading'].standard_name == 'platform_orientation': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'heading\'] wrong heading standard name\n')
        if not fid.variables['heading'].units == 'degrees_north': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'heading\'] wrong heading unit\n')
        if not fid.variables['heading'].valid_range[0] == 0: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'heading\'] wrong heading unit\n')
        if not fid.variables['heading'].valid_range[1] == 360: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'heading\'] wrong heading unit\n')
        if not (len(fid.dimensions[fid.variables['heading'].dimensions[0]])==len(fid.variables['heading'])): 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'heading\']inconsistent dimension length\n')
            
            
    #Test of pitch information
    #This one has been finished
    try: 
        fid.variables['latitude']
        do_pitch = True
    except: 
        print('    WarningMsg: dataset.groups[\'Platform\'].variables[\'latitude\'] do not exist\n')
        do_pitch=False
    if do_pitch == True: 
        if not fid.variables['latitude'].long_name == 'Platform latitude': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'latitude\'] wrong long name\n')
        if not fid.variables['latitude'].standard_name == 'latitude': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'latitude\'] wrong standard name\n')
        if not fid.variables['latitude'].units == 'degrees_north': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'latitude\'] wrong units\n')
        if not fid.variables['latitude'].valid_range[0] == -90: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'latitude\'] wrong unit\n')
        if not fid.variables['latitude'].valid_range[1] == 90: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'latitude\'] wrong  unit\n')
        if not (len(fid.dimensions[fid.variables['latitude'].dimensions[0]])==len(fid.variables['latitude'])): 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'latitude\'] inconsistent dimension length\n')
    
        
    #Test of longitude information
    #This one has been finished
    try: 
        fid.variables['longitude']
        do_pitch = True
    except: 
        print('    WarningMsg: dataset.groups[\'Platform\'].variables[\'longitude\'] do not exist\n')
        do_pitch=False
    if do_pitch == True: 
        if not fid.variables['longitude'].long_name == 'Platform longitude': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'longitude\'] wrong long name\n')
        if not fid.variables['longitude'].standard_name == 'longitude': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'longitude\'] wrong standard name\n')
        if not fid.variables['longitude'].units == 'degrees_east': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'longitude\'] wrong units\n')
        if not fid.variables['longitude'].valid_range[0] == -180: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'longitude\'] wrong unit\n')
        if not fid.variables['longitude'].valid_range[1] == 180: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'latitlongitudeude\'] wrong  unit\n')
        if not (len(fid.dimensions[fid.variables['longitude'].dimensions[0]])==len(fid.variables['longitude'])): 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'longitude\'] inconsistent dimension length\n')
    
        
        
    try: 
        fid.variables['MRU_offset_x']
        do_pitch = True
    except: 
        print('    WarningMsg: dataset.groups[\'Platform\'].variables[\'MRU_offset_x\'] do not exist\n')
        do_pitch=False
    if do_pitch == True: 
        if not fid.variables['MRU_offset_x'].long_name == 'Distance along the x-axis from the platform coordinate system origin to the motion reference unit sensor origin': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_offset_x\'] wrong long name\n')
        if not fid.variables['MRU_offset_x'].units == 'm': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_offset_x\'] wrong units\n')
        try: 
            if not (len(fid.variables['MRU_offset_x']))== 1: 
                print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_offset_x\'] has wrong size of values\n')
        except: 
                print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_offset_x\'] value dont exist\n')
        
        
    try: 
        fid.variables['MRU_offset_y']
        do_pitch = True
    except: 
        print('    WarningMsg: dataset.groups[\'Platform\'].variables[\'MRU_offset_y\'] do not exist\n')
        do_pitch=False
    if do_pitch == True: 
        if not fid.variables['MRU_offset_y'].long_name == 'Distance along the y-axis from the platform coordinate system origin to the motion reference unit sensor origin': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_offset_y\'] wrong long name\n')
        if not fid.variables['MRU_offset_y'].units == 'm': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_offset_y\'] wrong units\n')
        try: 
            if not (len(fid.variables['MRU_offset_y']))== 1: 
                print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_offset_y\'] has wrong size of values\n')
        except: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_offset_y\'] value dont exist\n')
        
        
        
        
        
        
        
    try: 
        fid.variables['MRU_offset_z']
        do_pitch = True
    except: 
        print('    WarningMsg: dataset.groups[\'Platform\'].variables[\'MRU_offset_z\'] do not exist\n')
        do_pitch=False
    if do_pitch == True: 
        if not fid.variables['MRU_offset_z'].long_name == 'Distance along the z-axis from the platform coordinate system origin to the motion reference unit sensor origin': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_offset_z\'] wrong long name\n')
        if not fid.variables['MRU_offset_z'].units == 'm': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_offset_z\'] wrong units\n')
        try: 
            if not (len(fid.variables['MRU_offset_z']))== 1: 
                print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_offset_z\'] has wrong size of values\n')
        except: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_offset_z\'] value dont exist\n')
        
        
    try: 
        fid.variables['MRU_rotation_x']
        do_pitch = True
    except: 
        print('    WarningMsg: dataset.groups[\'Platform\'].variables[\'MRU_rotation_x\'] do not exist\n')
        do_pitch=False
    if do_pitch == True: 
        if not fid.variables['MRU_rotation_x'].long_name == 'Extrinsic rotation about the x-axis from the platform to MRU coordinate systems': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_rotation_x\'].long_name is wrong\n')
        if not fid.variables['MRU_rotation_x'].units == 'arc_degree': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_rotation_x\'].units is wrong\n')
        if not np.min(fid.variables['MRU_rotation_x'].valid_range) == -180: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_rotation_x\'].valid_range minimum is wrong\n')
        if not np.max(fid.variables['MRU_rotation_x'].valid_range) == 180: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_rotation_x\'].valid_range maximum is wrong\n')
        try: 
            if not (len(fid.variables['MRU_rotation_x']))== 1: 
                print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_rotation_x\'] has wrong size of values\n')
        except: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_rotation_x\'] value dont exist\n')
        
        
        
        
    try: 
        fid.variables['MRU_rotation_y']
        do_pitch = True
    except: 
        print('    WarningMsg: dataset.groups[\'Platform\'].variables[\'MRU_rotation_y\'] do not exist\n')
        do_pitch=False
    if do_pitch == True: 
        if not fid.variables['MRU_rotation_y'].long_name == 'Extrinsic rotation about the y-axis from the platform to MRU coordinate systems': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_rotation_y\'].long_name is wrong\n')
        if not fid.variables['MRU_rotation_y'].units == 'arc_degree': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_rotation_y\'].units is wrong\n')
        if not np.min(fid.variables['MRU_rotation_y'].valid_range) == -180: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_rotation_y\'].valid_range minimum is wrong\n')
        if not np.max(fid.variables['MRU_rotation_y'].valid_range) == 180: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_rotation_y\'].valid_range maximum is wrong\n')
        try: 
            if not (len(fid.variables['MRU_rotation_y']))== 1: 
                print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_rotation_y\'] has wrong size of values\n')
        except: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_rotation_y\'] value dont exist\n')
        
        
        
        
        
    try: 
        fid.variables['MRU_rotation_z']
        do_pitch = True
    except: 
        print('    WarningMsg: dataset.groups[\'Platform\'].variables[\'MRU_rotation_z\'] do not exist\n')
        do_pitch=False
    if do_pitch == True: 
        if not fid.variables['MRU_rotation_z'].long_name == 'Extrinsic rotation about the z-axis from the platform to MRU coordinate systems': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_rotation_z\'].long_name is wrong\n')
        if not fid.variables['MRU_rotation_z'].units == 'arc_degree': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_rotation_z\'].units is wrong\n')
        if not np.min(fid.variables['MRU_rotation_z'].valid_range) == -180: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_rotation_z\'].valid_range minimum is wrong\n')
        if not np.max(fid.variables['MRU_rotation_z'].valid_range) == 180: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_rotation_z\'].valid_range maximum is wrong\n')
        try: 
            if not (len(fid.variables['MRU_rotation_z']))== 1: 
                print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_rotation_z\'] has wrong size of values\n')
        except: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'MRU_rotation_z\'] value dont exist\n')
        
        
        
        
    try: 
        fid.variables['position_offset_x']
        do_pitch = True
    except: 
        print('    WarningMsg: dataset.groups[\'Platform\'].variables[\'position_offset_x\'] do not exist\n')
        do_pitch=False
    if do_pitch == True: 
        if not fid.variables['position_offset_x'].long_name == 'Distance along the x-axis from the platform coordinate system origin to the latitude/longitude sensor origin': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'position_offset_x\'].long_name is wrong\n')
        if not fid.variables['position_offset_x'].units == 'm': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'position_offset_x\'].units is wrong\n')
        try: 
            if not (len(fid.variables['position_offset_x']))== 1: 
                print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'position_offset_x\'] has wrong size of values\n')
        except: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'position_offset_x\'] value dont exist\n')
        
        
        
        
    try: 
        fid.variables['position_offset_y']
        do_pitch = True
    except: 
        print('    WarningMsg: dataset.groups[\'Platform\'].variables[\'position_offset_y\'] do not exist\n')
        do_pitch=False
    if do_pitch == True: 
        if not fid.variables['position_offset_y'].long_name == 'Distance along the y-axis from the platform coordinate system origin to the latitude/longitude sensor origin': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'position_offset_y\'].long_name is wrong\n')
        if not fid.variables['position_offset_y'].units == 'm': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'position_offset_y\'].units is wrong\n')
        try: 
            if not (len(fid.variables['position_offset_y']))== 1: 
                print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'position_offset_y\'] has wrong size of values\n')
        except: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'position_offset_y\'] value dont exist\n')
        
        
        
        
        
    try: 
        fid.variables['position_offset_z']
        do_pitch = True
    except: 
        print('    WarningMsg: dataset.groups[\'Platform\'].variables[\'position_offset_z\'] do not exist\n')
        do_pitch=False
    if do_pitch == True: 
        if not fid.variables['position_offset_z'].long_name == 'Distance along the z-axis from the platform coordinate system origin to the latitude/longitude sensor origin': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'position_offset_z\'].long_name is wrong\n')
        if not fid.variables['position_offset_z'].units == 'm': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'position_offset_z\'].units is wrong\n')
        try: 
            if not (len(fid.variables['position_offset_z']))== 1: 
                print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'position_offset_z\'] has wrong size of values\n')
        except: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'position_offset_z\'] value dont exist\n')
        
    
            
    #Test of pitch information
    #This one has been finished
    try: 
        fid.variables['pitch']
        do_pitch = True
    except: 
        print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'pitch\'] do not exist\n')
        do_pitch=False
    if do_pitch == True: 
        if not fid.variables['pitch'].long_name == 'Platform pitch': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'pitch\'] wrong pitch long name\n')
        if not fid.variables['pitch'].standard_name == 'platform_pitch_angle': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'pitch\'] wrong pitch standard name\n')
        if not fid.variables['pitch'].units == 'arc_degree': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'pitch\'] wrong pitch units\n')
        if not fid.variables['pitch'].valid_range[0] == -90: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'pitch\'] wrong pitch unit\n')
        if not fid.variables['pitch'].valid_range[1] == 90: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'pitch\'] wrong pitch unit\n')
        if not (len(fid.dimensions[fid.variables['pitch'].dimensions[0]])==len(fid.variables['pitch'])): 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'pitch\'] inconsistent dimension length\n')
    
    
    


    
    
    #test of roll information
    #This one has been finished
    try:
        fid.variables['roll']
        do_roll = True
    except: 
        print('    WarningMsg: dataset.groups[\'Platform\'].variables[\'roll\'] do not exist\n')
        do_roll = False
    if do_roll == True: 
        if not fid.variables['roll'].long_name == 'Platform roll': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'roll\'] wrong roll long name\n')
        if not fid.variables['roll'].standard_name == 'platform_roll_angle': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'roll\'] wrong roll standard name\n')
        if not fid.variables['roll'].units == 'arc_degree': 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'roll\'] rong roll units\n')
        if not fid.variables['roll'].valid_range[0] == -180: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'roll\'] wrong roll unit\n')
        if not fid.variables['roll'].valid_range[1] == 180: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'roll\'] wrong roll unit\n')
        if not (len(fid.dimensions[fid.variables['roll'].dimensions[0]])==len(fid.variables['roll'])): 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'roll\'] inconsistent dimension length\n')
        
        
        
        
    #Test of speed ground information   
    #This test has been finished
    try: 
        fid.variables['speed_ground']    
        do_speed_ground = True
    except: 
        print('    WarningMsg: dataset.groups[\'Platform\'].variables[\'speed_ground\'] do not exist\n')
        do_speed_ground =False
    if do_speed_ground == True: 
        if not fid.variables['speed_ground'].long_name =="Platform speed over ground": 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'speed_ground\'].long_name is wrong\n')
        if not fid.variables['speed_ground'].standard_name =="platform_speed_wrt_ground":
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'speed_ground\'].standard_name is wrong\n')
        if not fid.variables['speed_ground'].units == "m/s": 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'speed_ground\'].units is wrong\n')
        if not fid.variables['speed_ground'].valid_min == 0.0: 
            print('    error msg: wrong speed ground valid min') 
        if not (len(fid.dimensions[fid.variables['speed_ground'].dimensions[0]])==len(fid.variables['speed_ground'])): 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'speed_ground\'].long_name has wrong dimensions\n')
            
            
            
            
    #Test of speed relative information   
    #This test has been finished
    try: 
        fid.variables['speed_relative']    
        do_speed_ground = True
    except: 
        print('    WarningMsg: dataset.groups[\'Platform\'].variables[\'speed_relative\'] do not exist\n')
        do_speed_ground =False
    if do_speed_ground == True: 
        if not fid.variables['speed_relative'].long_name =="Platform speed relative to water": 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'speed_relative\'].long_name is wrong\n')
        if not fid.variables['speed_relative'].standard_name =="platform_speed_wrt_seawater": 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'speed_relative\'].standard_name is wrong\n')
        if not fid.variables['speed_relative'].units == "m/s": 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'speed_relative\'].units is wrong\n')
        if not fid.variables['speed_relative'].valid_min == 0.0: 
            print('    error msg: wrong speed ground valid min')
        if not (len(fid.dimensions[fid.variables['speed_relative'].dimensions[0]])==len(fid.variables['speed_relative'])): 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'speed_relative\'].long_name has wrong dimensions\n')
            
                            
            

    #This test has been finished
    try: 
        fid.variables['transducer_offset_x']    
        do_transducer_offset_x = True
    except: 
        print('    WarningMsg: dataset.groups[\'Platform\'].variables[\'transducer_offset_x\'] do not exist\n')
        do_transducer_offset_x =False
    if do_transducer_offset_x == True: 
        if not fid.variables['transducer_offset_x'].long_name =="x-axis distance from the platform coordinate system origin to the sonar transducer": 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'transducer_offset_x\'].long_name is wrong\n')
        if not fid.variables['transducer_offset_x'].units =="m": 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'transducer_offset_x\'].unit is wrong\n')
        try: 
            if not (len(fid.variables['transducer_offset_x']))== 1: 
                print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'transducer_offset_x\'] has wrong size of values\n')
        except: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'transducer_offset_x\'] value dont exist\n')
        
        
        
    #This test has been finished
    try: 
        fid.variables['transducer_offset_y']    
        do_transducer_offset_x = True
    except: 
        print('    WarningMsg: dataset.groups[\'Platform\'].variables[\'transducer_offset_y\'] do not exist\n')
        do_transducer_offset_x =False
    if do_transducer_offset_x == True: 
        if not fid.variables['transducer_offset_y'].long_name =="y-axis distance from the platform coordinate system origin to the sonar transducer": 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'transducer_offset_y\'].long_name is wrong\n')
        if not fid.variables['transducer_offset_y'].units =="m": 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'transducer_offset_y\'].unit is wrong\n')
        try: 
            if not (len(fid.variables['transducer_offset_y']))== 1: 
                print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'transducer_offset_y\'] has wrong size of values\n')
        except: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'transducer_offset_y\'] value dont exist\n')
        
        
        
    #This test has been finished
    try: 
        fid.variables['transducer_offset_z']    
        do_transducer_offset_x = True
    except: 
        print('    WarningMsg: dataset.groups[\'Platform\'].variables[\'transducer_offset_z\'] do not exist\n')
        do_transducer_offset_x =False
    if do_transducer_offset_x == True: 
        if not fid.variables['transducer_offset_z'].long_name =="z-axis distance from the platform coordinate system origin to the sonar transducer": 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'transducer_offset_z\'].long_name is wrong\n')
        if not fid.variables['transducer_offset_z'].units =="m": 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'transducer_offset_z\'].unit is wrong\n')
        try: 
            if not (len(fid.variables['transducer_offset_z']))== 1: 
                print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'transducer_offset_z\'] has wrong size of values\n')
        except: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'transducer_offset_z\'] value dont exist\n')
        
        
            
            
            
        
        
    #Test of heave information
    #This test has been finished
    try: 
        fid.variables['vertical_offset']    
        do_transducer_offset_x = True
    except: 
        print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'vertical_offset\'] do not exist\n')
        do_transducer_offset_x =False
    if do_transducer_offset_x == True: 
        if not fid.variables['vertical_offset'].long_name =="Platform vertical offset from nominal": 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'vertical_offset\'] wrong vertical offset long name')
        if not fid.variables['vertical_offset'].units =="m": 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'vertical_offset\'] wrong vertical offset unit name')
        if not (len(fid.dimensions[fid.variables['vertical_offset'].dimensions[0]])==len(fid.variables['vertical_offset'])): 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'vertical_offset\'] inconsistent dimension length')
            
            
            
        
    #This test has been finished    
    try: 
        fid.variables['water_level']    
        do_transducer_offset_x = True
    except: 
        print('   Warning msg: water_level not in file')
        do_transducer_offset_x =False
    if do_transducer_offset_x == True: 
        if not fid.variables['water_level'].long_name =="Distance from the platform coordinate system origin to the nominal water level along the z-axis": 
            print('    error msg: wrong water_level long name')

        
    #This test has been finished
    try: 
        fid.variables['water_level']    
        do_transducer_offset_x = True
    except: 
        print('    WarningMsg: dataset.groups[\'Platform\'].variables[\'water_level\'] do not exist\n')
        do_transducer_offset_x =False
    if do_transducer_offset_x == True: 
        if not fid.variables['water_level'].long_name =="Distance from the platform coordinate system origin to the nominal water level along the z-axis": 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'water_level\'].long_name is wrong\n')
        if not fid.variables['water_level'].units =="m": 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'water_level\'].unit is wrong\n')
        try: 
            if not (len(fid.variables['water_level']))== 1: 
                print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'water_level\'] has wrong size of values\n')
        except: 
            print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'water_level\'] value dont exist\n')
        
        





def testNMEAgroup(fid): 

    if not fid.groups['Platform'].groups['NMEA'].description == 'All NMEA sensor datagrams': 
        print('    ErrorMsg: fid.groups[\'Platform\'].groups[\'NMEA\'].description is wrong ')
        
        
    #Test time
    
    if not (fid.groups['Platform'].groups['NMEA'].variables['time'].axis) == 'T':
        print('    ErrorMsg: dataset.groups[\'Platform\'].groups[\'NMEA\'].variables[\'time\'].axis has wrong info'+'\n')
    if not (fid.groups['Platform'].groups['NMEA'].variables['time'].calendar) == 'gregorian':
        print('    ErrorMsg: dataset.groups[\'Platform\'].groups[\'NMEA\'].variables[\'time\'].calendar has wrong info'+'\n')
    if not (fid.groups['Platform'].groups['NMEA'].variables['time'].long_name) == 'Timestamps for NMEA datagrams':
        print('    ErrorMsg: dataset.groups[\'Platform\'].groups[\'NMEA\'].variables[\'time\'].long_name has wrong info'+'\n')
    if not (fid.groups['Platform'].groups['NMEA'].variables['time'].standard_name) == 'time':
        print('    ErrorMsg: dataset.groups[\'Platform\'].groups[\'NMEA\'].variables[\'time\'].standard_name has wrong info'+'\n')
    if not (fid.groups['Platform'].groups['NMEA'].variables['time'].units) == 'nanoseconds since 1601-01-01 00:00:00Z':
        print('    ErrorMsg: dataset.groups[\'Platform\'].groups[\'NMEA\'].variables[\'time\'].units has wrong info'+'\n')
            
    if not (fid.groups['Platform'].groups['NMEA'].variables['NMEA_datagram'].dimensions[0]) == 'time': 
        print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'NMEA_datagram\'].dimensions has wrong info'+'\n')
    if not (fid.groups['Platform'].groups['NMEA'].variables['NMEA_datagram'].long_name) == 'NMEA datagram': 
        print('    ErrorMsg: dataset.groups[\'Platform\'].variables[\'NMEA_datagram\'].long_name has wrong info'+'\n')
    print((fid.groups['Platform'].groups['NMEA'].variables['NMEA_datagram'].long_name))







def testNetCDF(ncfilename): 
    ''' testNetCDF function
    
    
    
    '''
    
    
    #open new .nc file
    fid = Dataset(ncfilename,'r')
    

    #Test of top level information
    #Status: this test is finnished
    TopLevel_test(fid)
    
    
    
    #Test of annotation information
    #Status this test is finished
    try: 
        fid.groups['Annotation']
        test_annotation = True
    except: 
        test_annotation = False
        print('No annotation information to test')
        
    if test_annotation == True: 
        annotation_group_test(fid.groups['Annotation'])
    
    
    
    #Test of environment group
    #This one has not been properly tested
    try: 
        fid.groups['Environment']
        test_environment = True
    except KeyError: 
        print('Warning: Environment group don\'t exist')
        test_environment = False
    if test_environment == True: 
        environment_group_test(fid.groups['Environment'])
        
        
        
    #Test of platform group
    platform_group_test(fid.groups['Platform'])
    
    
    try: 
        fid.groups['Platform'].groups['NMEA']
        test = True
    except: 
        print('    WarningMsg. fid.groups[\'Platform\'].groups[\'NMEA\'] do not exist')
        test = False
    if test == True: 
        testNMEAgroup(fid)
        
        
    try: 
        fid.groups['Provenance']
        test = True
    except: 
        print('    WarningMsg:  fid.groups[\'Provenance\'] do not exist')
        test = False






    print(fid.groups['Sonar'])
    print(fid.groups['Sonar'].groups['Beam_group1'])
            
            
#        
#    print('add nmea info test')
#    
#    
#    print('add provenance group test here')
#    
#        
    fid.close()