# test_random


test random to explain branches

descargar repo
```console
git clone [link]
```


cargar cosas al repo
```console
git add -A
git commit -m "mensaje"
git push
```
## comandos branches

Listar branches
```console
git branch
```

Crear branch
```console
git branch [name_new_branch]
git checkout [name_new_branch]
```
la branch que se Crear es un copia de la branch en que te encuentras


change to branches
```console
git checkout [name_branch]
```

fist commit from a branch
```console
git push --set-upstream origin nico
```


#  Generador de colores hex

## Requerimientos

Ruby 2.7 o posterior
rubygems #gem install rubygems
httparty #gem install httparty


## Como correr codigo

ruby main.rb

## Herrramientas usadas

Atom

## Breve explicación codigo

La aplicación solicita al usaurio a ingresar un número entre 1 y 10 y luego genera 2 paletas de colores y muestra en consola las 3 paletas en el hex, rgb, hsl y cymk de cada color en las paletas.

Para hacer esto la primero se pide al usuario que ingrese por consola la cantidad de paletas que se desean obtener.\n
Entonces, se generan codigos Hex de colores al azar de acuerdo al número ingresado por el usuario.\n
Luego, para cada uno de los colores, se hace una consulta a la API de ​"The Color Api"​ para genera las paletas de 3 colores.\n
Por ultimo, se filtar la información importante y se muestran en consola las paletas al usaurio.
