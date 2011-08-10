// the texture
uniform sampler2D image;

const vec3 unity = vec3(1,1,1);

void main (void)
{
    vec3 texColor = vec3(texture2D(image, gl_TexCoord[0].st));
    
    vec3 result = unity - texColor;
    result.r = 0.0;

    gl_FragColor = vec4(result, 1);
}


