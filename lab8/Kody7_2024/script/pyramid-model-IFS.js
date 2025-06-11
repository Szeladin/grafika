/* Defines pyramidModel to be an IFS of the famous pyramid, about 20 units big.
 * Properties of the model are:
 *    pyramidModel.vertexPositions -- the vertex coordinates;
 *    pyramidModel.vertexNormals -- the normal vectors;
 *    pyramidModel.vertexTextureCoords -- the texture coordinates;
 *    pyramidModel.indices -- the face indices.
 * The first three properties are of type Float32Array, while pyramidModel.indices
 * is of type Uint16Array.
*/
var pyramidModel = {
    "vertexPositions": new Float32Array([
        // Base vertices (dodecagon) scaled 2x in width/depth and 4x in height
        8, 0, 0, 6.928, 0, 4, 4, 0, 6.928, 0, 0, 8, -4, 0, 6.928, -6.928, 0, 4,
        -8, 0, 0, -6.928, 0, -4, -4, 0, -6.928, 0, 0, -8, 4, 0, -6.928, 6.928, 0, -4,
        // Apex vertex scaled 4x in height
        0, 8, 0
    ]),
"vertexNormals": new Float32Array([
    // Normals for the base vertices (pointing downward)
    0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0,
    0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0,
    // Smooth normals for the side faces
    0.707, 0.447, 0,        // Vertex 0
    0.447, 0.447, 0.707,    // Vertex 1
    0, 0.447, 1,            // Vertex 2
    -0.447, 0.447, 0.707,   // Vertex 3
    -0.707, 0.447, 0,       // Vertex 4
    -0.447, 0.447, -0.707,  // Vertex 5
    0, 0.447, -1,           // Vertex 6
    0.447, 0.447, -0.707,   // Vertex 7
    0.707, 0.447, 0,        // Vertex 8
    // Normal for the apex (averaged from all side faces)
    0, 1, 0
]),
    "vertexTextureCoords": new Float32Array([
        // Texture coordinates remain unchanged
        1, 0.5, 0.933, 0.75, 0.75, 0.933, 0.5, 1, 0.25, 0.933, 0.067, 0.75,
        0, 0.5, 0.067, 0.25, 0.25, 0.067, 0.5, 0, 0.75, 0.067, 0.933, 0.25,
        0.933, 0.75,
        // Texture coordinate for the apex
        0.5, 0.5
    ]),
    "indices": new Uint16Array([
        // Indices remain unchanged
        0, 1, 2, 0, 2, 3, 0, 3, 4, 0, 4, 5, 0, 5, 6, 0, 6, 7,
        0, 7, 8, 0, 8, 9, 0, 9, 10, 0, 10, 11,
        0, 1, 12, 1, 2, 12, 2, 3, 12, 3, 4, 12, 4, 5, 12, 5, 6, 12,
        6, 7, 12, 7, 8, 12, 8, 9, 12, 9, 10, 12, 10, 11, 12, 11, 0, 12
    ])
};