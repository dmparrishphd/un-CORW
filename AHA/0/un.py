def un ( function ) :
    def inverted ( * args , ** kwargs ) :
        return not function ( * args , ** kwargs )
    return inverted
