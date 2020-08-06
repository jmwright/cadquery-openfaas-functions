def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    import io
    import sys
    from cadquery import cqgi
    from cadquery.occ_impl.exporters.json import JsonMesh

    # stdout redirect trap
    text_trap = io.StringIO()
    sys.stderr = text_trap

    mesher = JsonMesh()

    # Parse and build using the text
    cqModel = cqgi.parse(req)
    build_result = cqModel.build({})

    if build_result.success:
        # Display all the results that the caller
        for result in build_result.results:
            tess = result.shape.val().tessellate(0.001)

            # Add vertices
            for v in tess[0]:
                mesher.addVertex(v.x, v.y, v.z)

            # Add triangles
            for ixs in tess[1]:
                mesher.addTriangleFace(*ixs)

    return mesher.toJson()
