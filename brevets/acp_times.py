"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import math

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    
    km = control_dist_km
    if (km > brevet_dist_km * 1.2):
        return 'Wrong'
    if (km<= 200):
        max_time = km/34
        hours1 = max_time//1
        minutes1 = (max_time - hours1)*60
        if(math.floor(minutes1) < minutes1):
            minutes1 = math.floor(minutes1)+1

    elif(km<=400):
        max_time = (km-200)/32 +200/34
        hours1 = max_time//1
        minutes1 = (max_time - hours1)*60
        if(math.floor(minutes1) < minutes1):
            minutes1 = math.floor(minutes1)+1
        

    elif(km<=600):
        max_time = (km-400)/30 +200/34 + 200/32
        hours1 = max_time//1
        minutes1 = (max_time - hours1)*60
        if(math.floor(minutes1) < minutes1):
            minutes1 = math.floor(minutes1)+1
        
    elif(km<=1000):
        max_time = (km-600)/28 +200/34 + 200/32 + 200/30
        hours1 = max_time//1
        minutes1 = (max_time - hours1)*60
        if(math.floor(minutes1) < minutes1):
            minutes1 = math.floor(minutes1)+1
        
    else:
        max_time = (km-600)/26 +200/34 + 200/32 + 200/30 + 400/28
        hours1 = max_time//1
        minutes1 = (max_time - hours1)*60
        if(math.floor(minutes1) < minutes1):
            minutes1 = math.floor(minutes1)+1
  
    return brevet_start_time.shift(hours=+hours1, minutes=+minutes1).isoformat()


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
          brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    
    km = control_dist_km
    if(km<=600):
        min_time = km/15
        hours2 = min_time//1
        minutes2 = (min_time - hours2)*60
        if(math.floor(minutes2) < minutes2):
            minutes2 = math.floor(minutes2)+1
    elif(km<=1000):
        
        min_time = (km-600)/11.428 + 40
        hours2 = min_time//1
        minutes2 = (min_time - hours2)*60
        if(math.floor(minutes2) < minutes2):
            minutes2 = math.floor(minutes2)+1
    else:
       
        min_time = (km-1000)/13.333 + 40 + 400/11.428
        hours2 = min_time//1
        minutes2 = (min_time - hours2)*60
        if(math.floor(minutes2) < minutes2):
            minutes2 = math.floor(minutes2)+1
      
    return brevet_start_time.shift(hours=+hours2, minutes=+minutes2).isoformat()
