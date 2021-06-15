# Proyecto Grupal 1

## Diseño e Implementación de un ASIP vectorial para composición alfa

Through the development of this project, the student will apply the concepts of parallelism at the data level, specifically Single Instruction Multiple Data (SIMD) processors of the vector type. An Application Specific Instruction Set Processor (ASIP) will be carried out by means of a composition of the alpha channel.

### Required
```python
# Pillow
https://pillow.readthedocs.io/en/stable/installation.html
# VsCode
https://code.visualstudio.com/download
```

### Run Code
```python
cd Compiler
python3 .\main.py
```



## Example
```sh
Color#1 : (0, 255, 0)
Color#2 : (0, 255, 255)
Opacity : 0.25
Orientation : vertical
```

### Origin image
![Screenshot](.ReadMeImages/example.jpg)

### Gradient image
![Screenshot](.ReadMeImages/vertical.png)

### Image with alpha composition
![Screenshot](.ReadMeImages/alfa_0.png) ![Screenshot](.ReadMeImages/alfa_25.png) ![Screenshot](.ReadMeImages/alfa_75.png) ![Screenshot](.ReadMeImages/alfa_100.png)

Opacity> ---- 0% ---- 25% ---- 75% ---- 100% ----