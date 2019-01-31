

#import stuff
from netCDF4 import Dataset
import dateutil.parser
import numpy as np



def testNetCDF(ncfilename): 
    ''' testNetCDF function
    
    
    
    '''
    
    
        
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
#        print('Test of top level info:\n')
        try:
            fid.Conventions
            if not fid.Conventions==info.Conventions: 
                print('    ErrorMsg 1b: fid.Conventions has wrong format name')
                print('               :'+fid.Conventions)
                print('               :'+info.Conventions+'\n')
        except: 
            print('    ErrorMsg 1a. fid.Conventions do not exist'+'\n')
        
            
        
        
        try:
            fid.date_created
            try: 
                dateutil.parser.parse(fid.date_created)
            except: 
                print('    ErrorMsg 2b: fid.date_created has wrong format')
                print('               : '+fid.date_created+'\n')
        except: 
            print('    ErrorMsg 2a: fid.date_created do not exist'+'\n')
        
        
        try:
            fid.keywords
        except: 
            print('    ErrorMsg 3a: fid.keywords do not exist'+'\n')
        
        
        try:
            fid.sonar_convention_authority
            if not fid.sonar_convention_authority == info.sonar_convention_authority: 
                print('    ErrorMsg 4b: fid.sonar_convention_authority has wrong info')
                print('               : '+fid.sonar_convention_authority)
                print('               : '+info.sonar_convention_authority+'\n')
        except: 
            print('    ErrorMsg 4a: fid.sonar_convention_authority do not exist'+'\n')
        
        
        try:
            fid.sonar_convention_name
            if not fid.sonar_convention_name == info.sonar_convention_name: 
                print('    ErrorMsg 5b: fid.sonar_convention_name has wrong info')
                print('               : '+fid.sonar_convention_name)
                print('               : '+info.sonar_convention_name+'\n')
        except: 
            print('    ErrorMsg 5a: fid.sonar_convention_name do not exist'+'\n')
        
        
        try:
            fid.license
        except: 
            print('    WarningMsg 1a: fid.license do not exist'+'\n')
        
        
        try:
            fid.rights
        except: 
            print('    WarningMsg 2a: fid.rights do not exist'+'\n')
        
        
        try:
            fid.sonar_convention_version
            try: 
                if not isinstance(fid.sonar_convention_version, str): 
                    print('    ErrorMsg 6c: fid.sonar_convention_version has wrong format'+'\n')
            except: 
                print('    ErrorMsg 6b: fid.sonar_convention_version info is wrong')
                print('               : '+fid.sonar_convention_version)
                print('               : should be ISO8601:2004')
        except: 
            print('    ErrorMsg 6a: fid.sonar_convention_version do not exist'+'\n')
        
        
        try:
            fid.summary
        except: 
            print('    ErrorMsg 7a: fid.summary do not exist'+'\n')
        
        
        try:
            fid.title
        except: 
            print('    ErrorMsg 8a: fid.title do not exist'+'\n')
            

    
    
    
    
    def annotation_group_test(fid): 
        #Check if dimesions are ok        
        try: 
            if not len(fid.dimensions)>=1: 
                print('    ErrorMsg 15d:dataset.groups[\'Annotation\'].dimension has wrong dimension'+'\n')
        except: 
            print('    ErrorMsg 15a:dataset.groups[\'Annotation\'].dimension do not exist'+'\n')
        
        
        
        
        #Check if all variables are there
        try: 
            fid.variables['time']
            do_time = True
        except: 
            do_time = False
            print('    ErrorMsg: dataset.groups[\'Annotation\'].variables[\'time\'] dont exist')
        try: 
            do_text = True
            fid.variables['annotation_text']
        except: 
            do_text = False
            print('    ErrorMsg: dataset.groups[\'Annotation\'].variables[\'annotation_text\'] dont exist')
        try: 
            do_annotgrp = True
        except: 
            print('    WarningMsg: dataset.groups[\'Annotation\'].variables[\'annotation_category\'] dont exist')
            do_annotgrp = False
        
        
        
        if do_time == True: 
            if not len(fid.variables['time'].dimensions) == len(fid.dimensions): 
                print('    ErrorMsg: dataset.groups[\'Annotation\'].variables[\'time\'] has wrong dimension')
            if not (fid.variables['time'].axis) == 'T':
                print('    ErrorMsg: dataset.groups[\'Annotation\'].variables[\'time\'].axis has wrong info')
            if not (fid.variables['time'].calendar) == 'gregorian':
                print('    ErrorMsg: dataset.groups[\'Annotation\'].variables[\'time\'].calendar has wrong info')
            if not (fid.variables['time'].long_name) == 'Timestamps of annotations':
                print('    ErrorMsg: dataset.groups[\'Annotation\'].variables[\'time\'].long_name has wrong info')
            if not (fid.variables['time'].standard_name) == 'time':
                print('    ErrorMsg: dataset.groups[\'Annotation\'].variables[\'time\'].standard_name has wrong info')
            if not (fid.variables['time'].units) == 'nanoseconds since 1601-01-01 00:00:00Z':
                print('    ErrorMsg: dataset.groups[\'Annotation\'].variables[\'time\'].units has wrong info')
            
        
        
        
        if do_text == True: 
            if not len(fid.variables['annotation_text'].dimensions) == len(fid.dimensions): 
                print('    ErrorMsg: dataset.groups[\'Annotation\'].variables[\'annotation_text\'] has wrong dimension')
            if not (fid.variables['annotation_text'].long_name) == "Annotation text":
                print('    ErrorMsg: dataset.groups[\'Annotation\'].variables[\'annotation_text\'].long_name has wrong info')
            
        

        if do_annotgrp ==True: 
            if not len(fid.variables['annotation_category'].dimensions) == len(fid.dimensions): 
                print('    ErrorMsg: dataset.groups[\'Annotation\'].variables[\'annotation_category\'] has wrong dimension')
             
            if not (fid.variables['annotation_category'].long_name) == "Annotation category":
                print('    ErrorMsg: dataset.groups[\'Annotation\'].variables[\'annotation_category\'].long_name has wrong info')
            
        

    
    def environment_group_test(fid): 

        #Check if dimesions are ok        
        try: 
            if not len(fid.dimensions)>=1: 
                print('    ErrorMsg: dataset.groups[\'Environment\'].dimension has wrong dimension'+'\n')
        except: 
            print('    ErrorMsg: dataset.groups[\'Environment\'].dimension do not exist'+'\n')
        
        
        
        #Test of dimesion name
        if not fid.variables['frequency'].dimensions[0] == 'frequency': 
            print('    ErrorMsg: dataset.groups[\'Environment\'].dimension has wrong dimension name')


        
        #test if all variables exist        
        try: 
            fid.variables['frequency']
            do_frequecy = True
        except: 
            do_frequecy = False
            print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'Frequency\'] do not exist')
        try: 
            fid.variables['sound_speed_indicative']
            do_soundspeed = True
        except: 
            do_soundspeed = False
            print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'sound_speed_indicative\'] do not exist')
        try: 
            fid.variables['absorption_indicative']
            do_abs = True
        except: 
            do_abs = False
            print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'absorption_indicative\'] do not exist')
        


        #test frequency variable
        if do_frequecy == True: 
            if not len(fid.variables['frequency'].dimensions) == len(fid.dimensions): 
                print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'frequency\'] has wrong dimension')
            if not fid.variables['frequency'].long_name == 'Acoustic frequency': 
                print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'frequency\'].long_name has wrong info')
            if not fid.variables['frequency'].units == 'Hz': 
                print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'frequency\'].units has wrong info')

            if not fid.variables['frequency'].standard_name == 'sound_frequency': 
                print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'frequency\'].units has wrong info')

                
        if do_soundspeed == True: 
            if not len(fid.variables['sound_speed_indicative'].dimensions) == len(fid.dimensions): 
                print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'sound_speed_indicative\'] has wrong dimension')
            if not fid.variables['sound_speed_indicative'].standard_name == 'speed_of_sound_in_sea_water': 
                print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'sound_speed_indicative\'].standard_name has wrong info')
            if not fid.variables['sound_speed_indicative'].long_name == 'Indicative sound speed': 
                print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'sound_speed_indicative\'].long_name has wrong info')
            if not fid.variables['sound_speed_indicative'].units == 'm/s': 
                print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'sound_speed_indicative\'].units has wrong info')

                
        if do_abs == True: 
            if not len(fid.variables['absorption_indicative'].dimensions) == len(fid.dimensions): 
                print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'absorption_indicative\'] has wrong dimension')
            if not fid.variables['absorption_indicative'].long_name == 'Indicative acoustic absorption': 
                print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'absorption_indicative\'].long_name has wrong info')
            if not fid.variables['absorption_indicative'].units == 'dB/m': 
                print('    ErrorMsg: dataset.groups[\'Environment\'].variables[\'absorption_indicative\'].units has wrong info')

            
                
            
            
    def platform_group_test(fid): 


        #Test if attributes of the grupe are avaliable        
        try: 
            fid.platform_code_ICES
        except: 
            print('    - WarningMsg: platform code not specifed')
        
        try: 
            fid.platform_name
        except: 
            print('    - Warning msg xxx: platform name dont exist')
            
        try: 
            fid.platform_type
        except: 
            print('    - Warning msg xxx: platform type dont exist')
            
            
            
        #check of dimensions
        for dim in fid.dimensions: 
            if not dim[:4] == 'time': 
                print('    - error msg xxx, not a valid dimesion name')
            
            
            
            
        #Check distance variable
        try: 
            fid.variables['distance']
            do_distance = True
        except: 
            print('    WarningMsg: dataset.groups[\'Platform\'].variables[\'distance\'] do not exist')
            do_distance=False
            
        if do_distance == True: 
            if not fid.variables['distance'].long_name == 'Distance travelled by the platform': 
                print('    Error Msg: innvalid long name')
            if not fid.variables['distance'].units == 'm': 
                print('    Error Msg: innvalid unit')
            if not fid.variables['distance'].valid_min == 0: 
                print('    error msg: not valid valid min')
                
        
        try: 
            fid.variables['heading']
            do_heading = True
        except: 
            print('    warning: heading not in file')
            do_heading=False
        if do_heading == True: 
            if not fid.variables['heading'].long_name == 'Platform heading (true)': 
                print('    error msg: wrong heading long name')
            if not fid.variables['heading'].standard_name == 'platform_orientation': 
                print('    error msg: wrong heading standard name')
            if not fid.variables['heading'].units == 'degrees_north': 
                print('    error msg: wrong heading unit')
            if not fid.variables['heading'].valid_range[0] == 0: 
                print('    error msg: wrong heading unit')
            if not fid.variables['heading'].valid_range[1] == 360: 
                print('    error msg: wrong heading unit')
                
                
        try: 
            fid.variables['pitch']
            do_pitch = True
        except: 
            print('    warning: heading not in file')
            do_pitch=False
        if do_pitch == True: 
            if not fid.variables['pitch'].long_name == 'Platform pitch': 
                print('    error msg: wrong pitch long name')
            if not fid.variables['pitch'].standard_name == 'platform_pitch_angle': 
                print('    error msg: wrong pitch standard name')
            if not fid.variables['pitch'].units == 'arc_degree': 
                print('    error msg: wrong pitch units')
            if not fid.variables['pitch'].valid_range[0] == -90: 
                print('    error msg: wrong pitch unit')
            if not fid.variables['pitch'].valid_range[1] == 90: 
                print('    error msg: wrong pitch unit')
        
        
        try:
            fid.variables['roll']
            do_roll = True
        except: 
            print('    Error: no roll information')
            do_roll = False
        if do_roll == True: 
            if not fid.variables['roll'].long_name == 'Platform roll': 
                print('    error msg: wrong roll long name')
            if not fid.variables['roll'].standard_name == 'platform_roll_angle': 
                print('    error msg: wrong roll standard name')
            if not fid.variables['roll'].units == 'arc_degree': 
                print('    error msg: wrong roll units')
            if not fid.variables['roll'].valid_range[0] == -180: 
                print('    error msg: wrong roll unit')
            if not fid.variables['roll'].valid_range[1] == 180: 
                print('    error msg: wrong roll unit')
            
            
        
        try: 
            fid.variables['position_offset_x']
            do_position_offset_x = True
        except: 
            print(' Error msg. position_offset_x not in data')
            do_position_offset_x = False
        if do_position_offset_x == True: 
            if not fid.variables['position_offset_x'].long_name == "Distance along the x-axis from the platform coordinate system origin to the latitude/longitude sensor origin": 
                print('          Erro msg. wrong long name')
            if not fid.variables['position_offset_x'].units == 'm': 
                print('          Erro msg. wrong unit value')
        
        
        try: 
            fid.variables['position_offset_y']
            do_position_offset_y = True
        except: 
            print(' Error msg. position_offset_y not in data')
            do_position_offset_y = False
        if do_position_offset_y == True: 
            if not fid.variables['position_offset_y'].long_name == "Distance along the y-axis from the platform coordinate system origin to the latitude/longitude sensor origin": 
                print('          Erro msg. wrong long name')
            if not fid.variables['position_offset_y'].units == 'm': 
                print('          Erro msg. wrong unit value')
        
        
        try: 
            fid.variables['position_offset_z']
            do_position_offset_z = True
        except: 
            print(' Error msg. position_offset_x not in data')
            do_position_offset_z = False
        if do_position_offset_z == True: 
            if not fid.variables['position_offset_z'].long_name == "Distance along the z-axis from the platform coordinate system origin to the latitude/longitude sensor origin": 
                print('          Erro msg. wrong long name')
            if not fid.variables['position_offset_z'].units == 'm': 
                print('          Erro msg. wrong unit value')
                
                
        try: 
            fid.variables['speed_ground']    
            do_speed_ground = True
        except: 
            print('   Warning msg: speed_ground not in file')
            do_speed_ground =False
        if do_speed_ground == True: 
            if not fid.variables['speed_ground'].long_name =="Platform speed over ground": 
                print('    error msg: wrong speed ground long name')
            if not fid.variables['speed_ground'].standard_name =="platform_speed_wrt_ground": 
                print('    error msg: wrong speed ground standard name')
            if not fid.variables['speed_ground'].units == "m/s": 
                print('    error msg: wrong speed ground unit name')
            if not fid.variables['speed_ground'].valid_min == 0.0: 
                print('    error msg: wrong speed ground valid min')
                
                
        try: 
            fid.variables['speed_relative']    
            do_speed_ground = True
        except: 
            print('   Warning msg: speed_relative not in file')
            do_speed_ground =False
        if do_speed_ground == True: 
            if not fid.variables['speed_relative'].long_name =="Platform speed relative to water": 
                print('    error msg: wrong speed ground long name')
            if not fid.variables['speed_relative'].standard_name =="platform_speed_wrt_seawater": 
                print('    error msg: wrong speed ground standard name')
            if not fid.variables['speed_relative'].units == "m/s": 
                print('    error msg: wrong speed ground unit name')
            if not fid.variables['speed_relative'].valid_min == 0.0: 
                print('    error msg: wrong speed ground valid min')
                


        try: 
            fid.variables['transducer_offset_x']    
            do_transducer_offset_x = True
        except: 
            print('   Warning msg: transducer_offset_x not in file')
            do_transducer_offset_x =False
        if do_transducer_offset_x == True: 
            if not fid.variables['transducer_offset_x'].long_name =="x-axis distance from the platform coordinate system origin to the sonar transducer": 
                print('    error msg: wrong speed seawater long name')
            if not fid.variables['transducer_offset_x'].units =="m": 
                print('    error msg: wrong speed seawater unit name')
                
                
        try: 
            fid.variables['transducer_offset_y']    
            do_transducer_offset_x = True
        except: 
            print('   Warning msg: transducer_offset_y not in file')
            do_transducer_offset_x =False
        if do_transducer_offset_x == True: 
            if not fid.variables['transducer_offset_y'].long_name =="y-axis distance from the platform coordinate system origin to the sonar transducer": 
                print('    error msg: wrong speed seawater long name')
            if not fid.variables['transducer_offset_y'].units =="m": 
                print('    error msg: wrong speed seawater unit name')
                
                
                
        try: 
            fid.variables['transducer_offset_z']    
            do_transducer_offset_x = True
        except: 
            print('   Warning msg: transducer_offset_z not in file')
            do_transducer_offset_x =False
        if do_transducer_offset_x == True: 
            if not fid.variables['transducer_offset_z'].long_name =="z-axis distance from the platform coordinate system origin to the sonar transducer": 
                print('    error msg: wrong speed seawater long name')
            if not fid.variables['transducer_offset_z'].units =="m": 
                print('    error msg: wrong speed seawater unit name')
                
                
                
        try: 
            fid.variables['vertical_offset']    
            do_transducer_offset_x = True
        except: 
            print('   Warning msg: vertical_offset not in file')
            do_transducer_offset_x =False
        if do_transducer_offset_x == True: 
            if not fid.variables['vertical_offset'].long_name =="Platform vertical offset from nominal": 
                print('    error msg: wrong vertical offset long name')
            if not fid.variables['vertical_offset'].units =="m": 
                print('    error msg: wrong vertical offset unit name')
                
                
                
        try: 
            fid.variables['water_level']    
            do_transducer_offset_x = True
        except: 
            print('   Warning msg: water_level not in file')
            do_transducer_offset_x =False
        if do_transducer_offset_x == True: 
            if not fid.variables['water_level'].long_name =="Distance from the platform coordinate system origin to the nominal water level along the z-axis": 
                print('    error msg: wrong water_level long name')
            if not fid.variables['vertical_offset'].units =="m": 
                print('    error msg: wrong  water_level unit name')



            
    info = mandotory_information()
    
    
    
    #open new .nc file
    fid = Dataset(ncfilename,'r')
    

    #Test of top level information
    TopLevel_test(fid)
    
    
    #Test of annotation information
    try: 
        fid.groups['Annotation']
        test_annotation = True
    except: 
        test_annotation = False
        print('No annotation information to test')
        
    if test_annotation == True: 
        annotation_group_test(fid.groups['Annotation'])
    
    
    
    try: 
        fid.groups['Environment']
        test_environment = True
    except KeyError: 
        print('   Warning: Environment group don\'t exist')
        test_environment = False
    if test_environment == True: 
        environment_group_test(fid.groups['Environment'])
        
        
    platform_group_test(fid.groups['Platform'])
    
        
        
    fid.close()