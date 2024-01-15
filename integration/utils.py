from .models import SearchData

def saveSearchData(user, locationKey, data):

    ''' Saves each search data if output is available with user_id, locationKey and weatherdata'''
    
    SearchData.objects.create(user_id=user.id, data=data, locationkey=locationKey)
