def includeme(config): # pragma: no cover
    config.include('pyramid_zodbconn')
    config.include('substanced.objectmap')
    config.include('substanced.catalog')
    config.include('substanced.content')
    config.include('substanced.models')
    config.include('substanced.evolution')
    config.include('substanced.sdi')
    config.include('substanced.principal')
