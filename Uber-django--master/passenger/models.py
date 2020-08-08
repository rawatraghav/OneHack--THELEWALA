from django.db import models
from uber.models import Location

#Import User method for django
from django.contrib.auth.models import User
'''End Of Import'''
#---------------------------------------------------------------------#



# MODELS CREATED HERE!

#################################################################################################################################################################################
# MODEL FOR PASSENGERS!
#################################################################################################################################################################################

#...Class DRIVER added here...
class Passenger(models.Model):
#Attribute Variables for Driver class to represent different columns in database
    '''
    name-: This is the name of the passenger
    avatar-: A picture of the rider
    pickup_location-: Connected to the Location class using a FOREIGN_KEY
    '''
    name = models.OneToOneField(User, related_name='rider_profile',on_delete=models.CASCADE)
    bio = models.CharField(max_length=60)
    avatar = models.ImageField(upload_to='ProfilePicture/')
    current_location = models.ForeignKey('uber.Location', related_name='current_location', on_delete=models.CASCADE, null=True)
    pickup_location = models.ForeignKey('uber.Location',related_name='rider_pickup', on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=50)

    
    '''Method to filter database results'''
    def __str__(self):
        return str(self.name)

#################################################################################################################################################################################
