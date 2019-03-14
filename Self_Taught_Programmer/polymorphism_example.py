#polymorphism example, DO NOT RUN

#drawing shapes without polymorphism
shapes=[tri,sql,crl]
for a_shape in shapes:
    if type(a_shape)== "Triangle":
        a_shape.draw_triangle()
    if type(a_shape)=="Square":
        a_shape.draw_square()
    if type(a_shae)=="Circle":
        a_shape.draw_circle()

#^for every data type we have to do a specific method draw_data type, as opposed to:
#drawing shapes wih polymorphism
shapes=[trl,
        swl,
        crl]
for a_shape in shapes:
    a_shapes.draw()



    
