def is_client(user):
    return hasattr(user, 'clientprofile')

def is_physiotherapist(user):
    return hasattr(user, 'physiotherapist')
